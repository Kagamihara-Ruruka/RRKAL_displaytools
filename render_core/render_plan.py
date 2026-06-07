"""Render-plan composition helpers.

This module is the first post-07 extraction seam from
``taichi_global_bathymetry.py``. It intentionally keeps the existing
sequential compose behavior and does not enable runtime compose-run merging.
"""

from __future__ import annotations

import numpy as np

from render_core.layer_render_plan_cache_diagnostics import (
    build_layer_render_plan_cache_invalidation_reasons,
    build_layer_render_plan_cache_invalidation_scope,
    build_layer_render_plan_cache_key,
    build_layer_render_plan_metadata_summary,
)
from render_core.layer_render_plan_adapter_preflight import (
    build_layer_render_plan_adapter_boundary_contract,
    build_layer_render_plan_adapter_payload,
    build_layer_render_plan_adapter_payload_contract,
    build_layer_render_plan_adapter_payload_summary,
    build_layer_render_plan_compile_input,
    build_layer_render_plan_single_pass_preflight_contract,
)
from render_core.layer_render_plan_composition_dispatch import (
    build_layer_render_plan_composition_apply_action,
    build_layer_render_plan_composition_dispatch_packet,
)
from render_core.layer_render_plan_compose_queue import (
    build_layer_render_plan_compose_queue_entries,
    build_layer_render_plan_compose_queue_packet,
    build_layer_render_plan_compose_queue_packet_from_states,
    build_layer_render_plan_compose_run_parity_contract,
    build_layer_render_plan_compose_runs,
    build_layer_render_plan_step_runtime_state,
)
from render_core.layer_render_plan_execution_phase_timing import (
    build_layer_render_plan_bottleneck_recommendation,
    build_layer_render_plan_execution_phases,
    build_layer_render_plan_execution_summary,
    build_layer_render_plan_phase_timing_contract,
    build_layer_render_plan_phase_timing_runtime_packet,
)
from render_core.layer_render_plan_compiled_reused_packets import (
    build_compiled_layer_render_plan_packet,
    build_compiled_layer_render_plan_packet_from_adapter_payload,
    build_reused_compiled_layer_render_plan_packet,
    build_reused_compiled_layer_render_plan_packet_from_adapter_payload,
)
from render_core.layer_render_plan_residual_packet_surfaces import (
    build_layer_render_plan_batch_decisions,
    build_layer_render_plan_composition_steps,
    build_layer_render_plan_composition_timing_packet,
    build_layer_render_plan_runtime_snapshot,
    build_layer_render_plan_style_postprocess_packet,
    select_layer_render_plan_composition_input,
)


def alpha_compose(background: np.ndarray, overlay: np.ndarray) -> np.ndarray:
    if overlay.shape != background.shape:
        raise ValueError(f"Overlay shape {overlay.shape} does not match background {background.shape}")

    out = background.copy()
    alpha = overlay[..., 3:4].astype(np.float32) / 255.0
    out[..., :3] = (
        overlay[..., :3].astype(np.float32) * alpha
        + out[..., :3].astype(np.float32) * (1.0 - alpha)
    ).astype(np.uint8)
    out[..., 3] = 255
    return out


def alpha_blend_compose(background: np.ndarray, overlay: np.ndarray, blend_mode: str) -> np.ndarray:
    if blend_mode == "Normal":
        return alpha_compose(background, overlay)
    if overlay.shape != background.shape:
        raise ValueError(f"Overlay shape {overlay.shape} does not match background {background.shape}")

    base_rgb = background[..., :3].astype(np.float32) / 255.0
    overlay_rgb = overlay[..., :3].astype(np.float32) / 255.0
    alpha = overlay[..., 3:4].astype(np.float32) / 255.0
    if blend_mode == "Screen":
        blended = 1.0 - (1.0 - base_rgb) * (1.0 - overlay_rgb)
    elif blend_mode == "Multiply":
        blended = base_rgb * overlay_rgb
    elif blend_mode == "Overlay":
        blended = np.where(
            base_rgb <= 0.5,
            2.0 * base_rgb * overlay_rgb,
            1.0 - 2.0 * (1.0 - base_rgb) * (1.0 - overlay_rgb),
        )
    elif blend_mode == "Soft Light":
        blended = (1.0 - 2.0 * overlay_rgb) * base_rgb * base_rgb + 2.0 * overlay_rgb * base_rgb
    else:
        return alpha_compose(background, overlay)

    out = background.copy()
    out[..., :3] = np.clip((blended * alpha + base_rgb * (1.0 - alpha)) * 255.0, 0.0, 255.0).astype(np.uint8)
    out[..., 3] = 255
    return out


def alpha_compose_transparent(background: np.ndarray, overlay: np.ndarray) -> np.ndarray:
    if overlay.shape != background.shape:
        raise ValueError(f"Overlay shape {overlay.shape} does not match background {background.shape}")
    bg = background.astype(np.float32) / 255.0
    fg = overlay.astype(np.float32) / 255.0
    fg_a = fg[..., 3:4]
    bg_a = bg[..., 3:4]
    out_a = fg_a + bg_a * (1.0 - fg_a)
    safe_a = np.maximum(out_a, 1e-6)
    out_rgb = (fg[..., :3] * fg_a + bg[..., :3] * bg_a * (1.0 - fg_a)) / safe_a
    out = np.zeros_like(background)
    out[..., :3] = np.clip(out_rgb * 255.0, 0.0, 255.0).astype(np.uint8)
    out[..., 3:4] = np.clip(out_a * 255.0, 0.0, 255.0).astype(np.uint8)
    return out


def build_layer_render_plan_apply_path(
    composition_steps: list[dict[str, object]],
    batch_decisions: list[dict[str, object]],
) -> list[dict[str, object]]:
    decisions_by_id = {
        str(decision.get("id")): decision
        for decision in batch_decisions
        if isinstance(decision, dict) and decision.get("scope") == "layer"
    }
    path: list[dict[str, object]] = []
    for index, step in enumerate(composition_steps):
        if not isinstance(step, dict):
            continue
        action = build_layer_render_plan_composition_apply_action(step)
        step_id = str(step.get("id") or step.get("layer_id") or "")
        decision = decisions_by_id.get(step_id, {})
        path.append(
            {
                "order": index,
                "id": step_id,
                "layer_id": step.get("layer_id"),
                "kind": action.get("kind"),
                "decision": decision.get("decision", "compose_cached_overlay"),
                "apply_helper": action.get("apply_helper"),
                "overlay_attr": step.get("overlay_attr"),
                "overlay_source": step.get("overlay_source"),
                "current_runtime_path": "HybridRenderController.apply_layer_render_plan_composition",
                "single_pass_candidate": action.get("single_pass_candidate"),
            }
        )
    return path
