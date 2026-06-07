"""Residual render-plan packet surface helpers."""

from __future__ import annotations


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
