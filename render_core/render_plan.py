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


def build_layer_render_plan_runtime_snapshot(
    frame_index: int,
    visible_layers: list[object],
    selected_layer_semantic_target: object,
    dirty_flags: dict[str, object],
    defer_vector_overlays: object,
    composition_steps: list[dict[str, object]],
    *,
    source: str,
) -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.layer_render_plan_runtime_snapshot.v1",
        "source": source,
        "frame_index": int(frame_index),
        "status": "snapshot_only",
        "runtime_optimization_applied": False,
        "optimization_target": "precompute_layer_state_then_single_render_pass",
        "visible_layers": visible_layers,
        "visible_layer_count": len(visible_layers),
        "selected_layer_semantic_target": selected_layer_semantic_target,
        "dirty_flags": dirty_flags,
        "defer_vector_overlays": defer_vector_overlays,
        "batch_targets": [
            {"id": "globe_material", "source": "TaichiGlobe.render", "dirty_flag": "globe_dirty"},
            {"id": "hydrology_polylines", "source": "lake_overlay_rgba/river_overlay_rgba", "dirty_flag": "hydrology_dirty"},
            {"id": "boundary_and_maritime_lines", "source": "boundary_layer_rgba/boundary_overlay_rgba", "dirty_flag": "boundary_dirty"},
            {"id": "traffic_points", "source": "overlay_rgba/aircraft_overlay_rgba", "dirty_flag": "overlay_dirty"},
            {"id": "research_pins", "source": "pin_overlay_rgba", "dirty_flag": "overlay_dirty"},
            {"id": "vehicle_icons", "source": "vehicle_icon_overlay_rgba", "dirty_flag": "overlay_dirty"},
        ],
        "compose_order": ["globe_rgba", *[str(step.get("id")) for step in composition_steps]],
        "composition_step_count": len(composition_steps),
        "composition_helper": "HybridRenderController.apply_layer_render_plan_composition",
        "single_pass_target": "future_unified_taichi_render_plan",
        "current_path": "centralized_plan_helper_with_existing_overlay_composition",
    }


def select_layer_render_plan_composition_input(
    compiled_plan: dict[str, object] | None,
) -> tuple[list[dict[str, object]] | None, str]:
    plan = compiled_plan if isinstance(compiled_plan, dict) else {}
    compose_queue = plan.get("compose_queue")
    if isinstance(compose_queue, list):
        return compose_queue, "compose_queue"
    composition_steps = plan.get("composition_steps")
    if isinstance(composition_steps, list):
        return composition_steps, "composition_steps"
    return None, "missing_composition_input"


def build_layer_render_plan_style_postprocess_packet(
    style_profile: object,
) -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.layer_render_plan_style_postprocess.v1",
        "source": "render_core.render_plan.build_layer_render_plan_style_postprocess_packet",
        "style_profile": style_profile,
        "apply_helper": "apply_style_profile",
        "phase_id": "postprocess",
        "runtime_optimization_applied": False,
        "boundary": "Style profile value is captured as runtime input; pixel postprocess remains in the renderer helper.",
    }


def build_layer_render_plan_composition_timing_packet(
    step_timing_ms: dict[str, object],
) -> dict[str, object]:
    phase_timing_ms: dict[str, float] = {}
    source_timings = step_timing_ms if isinstance(step_timing_ms, dict) else {}
    for phase_id, elapsed_ms in source_timings.items():
        try:
            phase_timing_ms[str(phase_id)] = round(float(elapsed_ms), 3)
        except (TypeError, ValueError):
            continue
    return {
        "schema": "rrkal_displaytools.layer_render_plan_composition_timing.v1",
        "source": "render_core.render_plan.build_layer_render_plan_composition_timing_packet",
        "phase_timing_ms": phase_timing_ms,
        "phase_ids": list(phase_timing_ms.keys()),
        "measured_phase_count": len(phase_timing_ms),
        "compose_overlays_ms": phase_timing_ms.get("compose_overlays", 0.0),
        "postprocess_ms": phase_timing_ms.get("postprocess", 0.0),
        "runtime_optimization_applied": False,
        "boundary": "Controller measures perf_counter deltas; render_core only normalizes composition phase timing metadata.",
    }


def build_layer_render_plan_composition_steps(
    boundary_layers_available: bool,
    boundary_layer_ids: list[str],
    boundary_aggregate_blend_mode: object,
) -> list[dict[str, object]]:
    steps: list[dict[str, object]] = [
        {"id": "lakes", "kind": "runtime_blend", "layer_id": "lakes", "overlay_attr": "lake_overlay_rgba"},
        {"id": "rivers", "kind": "runtime_blend", "layer_id": "rivers", "overlay_attr": "river_overlay_rgba"},
    ]
    if boundary_layers_available:
        for layer_id in ("borders", "territorial_sea", "eez", "high_seas"):
            if layer_id in boundary_layer_ids:
                steps.append({"id": layer_id, "kind": "runtime_blend", "layer_id": layer_id, "overlay_source": "boundary_layer_rgba"})
    else:
        steps.append(
            {
                "id": "boundary_aggregate",
                "kind": "alpha_blend",
                "overlay_attr": "boundary_overlay_rgba",
                "blend_mode": boundary_aggregate_blend_mode,
            }
        )
    steps.extend(
        [
            {"id": "ais_overlay", "kind": "alpha_compose", "overlay_attr": "overlay_rgba"},
            {"id": "aircraft", "kind": "runtime_overlay", "layer_id": "aircraft", "overlay_attr": "aircraft_overlay_rgba"},
            {"id": "vehicle_icons", "kind": "runtime_overlay", "layer_id": "vehicle_icons", "overlay_attr": "vehicle_icon_overlay_rgba"},
            {"id": "pins", "kind": "runtime_overlay", "layer_id": "pins", "overlay_attr": "pin_overlay_rgba"},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
        ]
    )
    return steps


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


def build_layer_render_plan_batch_decisions(
    runtime_snapshot: dict[str, object],
    composition_steps: list[dict[str, object]],
    invalidation_scope: list[dict[str, object]],
) -> list[dict[str, object]]:
    dirty_flags = runtime_snapshot.get("dirty_flags") if isinstance(runtime_snapshot.get("dirty_flags"), dict) else {}
    batch_targets = runtime_snapshot.get("batch_targets") if isinstance(runtime_snapshot.get("batch_targets"), list) else []
    global_dirty = bool(dirty_flags.get("force") or dirty_flags.get("changed"))
    dirty_scope_ids = {
        str(scope.get("id"))
        for scope in invalidation_scope
        if isinstance(scope, dict) and scope.get("scope") in {"batch", "global", "plan"}
    }
    decisions: list[dict[str, object]] = []
    for batch in batch_targets:
        if not isinstance(batch, dict):
            continue
        batch_id = str(batch.get("id") or "")
        dirty_flag = str(batch.get("dirty_flag") or "")
        dirty = global_dirty or bool(dirty_flag and dirty_flags.get(dirty_flag)) or batch_id in dirty_scope_ids
        decisions.append(
            {
                "scope": "batch",
                "id": batch_id,
                "dirty_flag": dirty_flag,
                "source": batch.get("source"),
                "decision": "rebuild_batch" if dirty else "reuse_batch",
                "reason": f"dirty_flag:{dirty_flag}" if dirty and dirty_flag else ("global_dirty" if dirty else "cache_key_match"),
            }
        )

    layer_dirty_map = {
        "lakes": "hydrology_dirty",
        "rivers": "hydrology_dirty",
        "borders": "boundary_dirty",
        "territorial_sea": "boundary_dirty",
        "eez": "boundary_dirty",
        "high_seas": "boundary_dirty",
        "boundary_aggregate": "boundary_dirty",
        "ais_overlay": "overlay_dirty",
        "aircraft": "overlay_dirty",
        "vehicle_icons": "overlay_dirty",
        "pins": "overlay_dirty",
        "style_profile_postprocess": "globe_dirty",
    }
    for step in composition_steps:
        if not isinstance(step, dict):
            continue
        step_id = str(step.get("id") or step.get("layer_id") or "")
        dirty_flag = layer_dirty_map.get(step_id)
        dirty = global_dirty or bool(dirty_flag and dirty_flags.get(dirty_flag))
        kind = str(step.get("kind") or "")
        if kind == "style_profile_postprocess":
            decision = "postprocess_each_frame"
        else:
            decision = "compose_dirty_overlay" if dirty else "compose_cached_overlay"
        decisions.append(
            {
                "scope": "layer",
                "id": step_id,
                "layer_id": step.get("layer_id"),
                "kind": kind,
                "dirty_flag": dirty_flag,
                "decision": decision,
                "reason": f"dirty_flag:{dirty_flag}" if dirty and dirty_flag else ("global_dirty" if dirty else "cache_key_match"),
            }
        )
    return decisions
