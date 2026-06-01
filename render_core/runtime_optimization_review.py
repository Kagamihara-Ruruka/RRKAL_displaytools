"""Runtime optimization metadata packets for reviewer-facing evidence."""

from __future__ import annotations


def build_runtime_optimization_module_boundary_packet(source: str) -> dict[str, object]:
    helper_exports = [
        "build_runtime_pressure_snapshot_packet",
        "build_layer_render_state_packet",
        "build_lod_counter_packet",
        "build_heavy_overlay_defer_cache_packet",
        "build_runtime_optimization_review_summary_packet",
    ]
    metadata_fields = [
        "renderer_output_metadata.policies.runtime_pressure_snapshot",
        "renderer_output_metadata.policies.layer_render_state",
        "renderer_output_metadata.policies.lod_counters",
        "renderer_output_metadata.policies.heavy_overlay_defer_cache",
        "renderer_output_metadata.policies.runtime_optimization_review_summary",
    ]
    return {
        "schema": "rrkal_displaytools.runtime_optimization_module_boundary.v1",
        "source": source,
        "status": "helper_module_split_contract_module_unchanged",
        "helper_module": "render_core.runtime_optimization_review",
        "contract_module": "render_core.render_plan_performance",
        "helper_exports": helper_exports,
        "helper_export_count": len(helper_exports),
        "metadata_fields": metadata_fields,
        "metadata_field_count": len(metadata_fields),
        "runtime_entrypoint": "HybridRenderController.project_handoff_snapshot",
        "review_entrypoint": "scripts/inspect_layer_render_plan_performance.ps1",
        "runtime_optimization_applied": False,
        "boundary": "Module boundary evidence only; helper extraction does not change render order, worker scheduling, cache governance or compose merging.",
    }


def build_runtime_pressure_snapshot_packet(
    source: str,
    width: int,
    height: int,
    last_render_ms: float | None,
    target_fps: float,
    interaction_active: bool,
    visible_layer_count: int,
    vector_record_count: int,
    lod: str,
    cache_hit_count: int = 0,
    cache_miss_count: int = 0,
    deferred_overlay_count: int = 0,
    budget_decision: dict[str, object] | None = None,
) -> dict[str, object]:
    budget = budget_decision if isinstance(budget_decision, dict) else {}
    target_fps_value = max(1.0, float(target_fps))
    target_frame_budget_ms = 1000.0 / target_fps_value
    render_ms = float(last_render_ms or 0.0)
    pressure = render_ms / max(target_frame_budget_ms, 1e-6) if render_ms > 0.0 else 0.0
    return {
        "schema": "rrkal_displaytools.runtime_pressure_snapshot.v1",
        "source": source,
        "status": "observed_no_runtime_mutation",
        "width": max(1, int(width)),
        "height": max(1, int(height)),
        "last_render_ms": render_ms,
        "target_fps": target_fps_value,
        "target_frame_budget_ms": target_frame_budget_ms,
        "pressure": pressure,
        "pressure_state": str(budget.get("state", "warming-up" if render_ms <= 0.0 else "observed")),
        "interaction_active": bool(interaction_active),
        "visible_layer_count": max(0, int(visible_layer_count)),
        "vector_record_count": max(0, int(vector_record_count)),
        "lod": str(lod),
        "defer_vector_overlays": bool(budget.get("defer_vector_overlays", False)),
        "prefer_static_cache": bool(budget.get("prefer_static_cache", False)),
        "vector_cache_degrees": float(budget.get("vector_cache_degrees", 0.0) or 0.0),
        "vector_cache_zoom_step": float(budget.get("vector_cache_zoom_step", 0.0) or 0.0),
        "vector_point_stride": int(budget.get("vector_point_stride", 1) or 1),
        "cache_hit_count": max(0, int(cache_hit_count)),
        "cache_miss_count": max(0, int(cache_miss_count)),
        "deferred_overlay_count": max(0, int(deferred_overlay_count)),
        "runtime_optimization_applied": False,
        "boundary": "Snapshot reports renderer pressure and defer/cache policy only; it does not change target FPS, LOD, cache governance or render order.",
    }


def build_layer_render_state_packet(
    source: str,
    layer_visible: dict[str, object] | None,
    layer_opacity: dict[str, object] | None = None,
    layer_blend_mode: dict[str, object] | None = None,
    selected_layer_semantic_target: str | None = None,
    dirty_flags: dict[str, object] | None = None,
    renderer_targets: dict[str, object] | None = None,
    lod_bucket: str = "",
    cache_key: str | None = None,
    defer_reason: str | None = None,
) -> dict[str, object]:
    visible = layer_visible if isinstance(layer_visible, dict) else {}
    opacity = layer_opacity if isinstance(layer_opacity, dict) else {}
    blend = layer_blend_mode if isinstance(layer_blend_mode, dict) else {}
    targets = renderer_targets if isinstance(renderer_targets, dict) else {}
    dirty = dirty_flags if isinstance(dirty_flags, dict) else {}
    active_dirty_flags = [str(key) for key, value in dirty.items() if bool(value)]
    layers = []
    for layer_id in sorted(str(key) for key in visible.keys()):
        layers.append(
            {
                "layer_id": layer_id,
                "visible": bool(visible.get(layer_id, False)),
                "opacity": float(opacity.get(layer_id, 1.0) or 0.0),
                "blend_mode": str(blend.get(layer_id, "normal") or "normal"),
                "dirty_flags": list(active_dirty_flags),
                "renderer_target": str(targets.get(layer_id, layer_id) or layer_id),
                "cache_key": "" if cache_key is None else str(cache_key),
                "lod_bucket": str(lod_bucket or "unknown"),
                "defer_reason": str(defer_reason or "none"),
            }
        )
    return {
        "schema": "rrkal_displaytools.layer_render_state_packet.v1",
        "source": source,
        "status": "observed_no_runtime_mutation",
        "contract_schema": "rrkal_displaytools.layer_render_state_contract.v1",
        "layer_count": len(layers),
        "visible_layer_count": sum(1 for layer in layers if bool(layer.get("visible"))),
        "selected_layer_semantic_target": selected_layer_semantic_target,
        "active_dirty_flags": active_dirty_flags,
        "lod_bucket": str(lod_bucket or "unknown"),
        "layers": layers,
        "runtime_optimization_applied": False,
        "boundary": "LayerRenderState packet freezes existing layer UI/runtime facts for metadata review only; it does not reorder rendering or enable collapsed compose runs.",
    }


def build_lod_counter_packet(
    source: str,
    lod_bucket: str,
    visible_layer_count: int,
    visible_vector_records: int,
    deferred_overlay_count: int,
    cache_hit_count: int,
    cache_miss_count: int,
    target_fps: float,
    last_render_ms: float | None,
) -> dict[str, object]:
    target_fps_value = max(1.0, float(target_fps))
    target_frame_budget_ms = 1000.0 / target_fps_value
    render_ms = float(last_render_ms or 0.0)
    pressure = render_ms / max(target_frame_budget_ms, 1e-6) if render_ms > 0.0 else 0.0
    return {
        "schema": "rrkal_displaytools.lod_counter_packet.v1",
        "source": source,
        "status": "observed_no_runtime_mutation",
        "contract_schema": "rrkal_displaytools.lod_counter_contract.v1",
        "lod_bucket": str(lod_bucket or "unknown"),
        "visible_layer_count": max(0, int(visible_layer_count)),
        "visible_vector_records": max(0, int(visible_vector_records)),
        "deferred_overlay_count": max(0, int(deferred_overlay_count)),
        "cache_hit_count": max(0, int(cache_hit_count)),
        "cache_miss_count": max(0, int(cache_miss_count)),
        "target_fps": target_fps_value,
        "target_frame_budget_ms": target_frame_budget_ms,
        "last_render_ms": render_ms,
        "pressure": pressure,
        "runtime_optimization_applied": False,
        "boundary": "LOD counters are renderer metadata evidence only; they do not change LOD selection, cache lifecycle or render order.",
    }


def build_heavy_overlay_defer_cache_packet(
    source: str,
    budget_decision: dict[str, object] | None,
    interaction_active: bool,
    visible_vector_records: int,
    deferred_overlay_count: int,
    cache_hit_count: int,
    cache_miss_count: int,
    lod_bucket: str,
    target_fps: float,
    last_render_ms: float | None,
) -> dict[str, object]:
    budget = budget_decision if isinstance(budget_decision, dict) else {}
    target_fps_value = max(1.0, float(target_fps))
    target_frame_budget_ms = 1000.0 / target_fps_value
    render_ms = float(last_render_ms or 0.0)
    pressure = render_ms / max(target_frame_budget_ms, 1e-6) if render_ms > 0.0 else 0.0
    defer_vector_overlays = bool(budget.get("defer_vector_overlays", False))
    prefer_static_cache = bool(budget.get("prefer_static_cache", False))
    if defer_vector_overlays:
        defer_reason = "interaction_over_budget_vector_overlay"
    elif prefer_static_cache:
        defer_reason = "prefer_static_cache_for_heavy_overlay"
    else:
        defer_reason = "none"
    return {
        "schema": "rrkal_displaytools.heavy_overlay_defer_cache_snapshot.v1",
        "source": source,
        "status": "observed_no_runtime_mutation",
        "policy_schema": "rrkal_displaytools.heavy_overlay_defer_cache_policy.v1",
        "lod_bucket": str(lod_bucket or "unknown"),
        "interaction_active": bool(interaction_active),
        "visible_vector_records": max(0, int(visible_vector_records)),
        "defer_vector_overlays": defer_vector_overlays,
        "prefer_static_cache": prefer_static_cache,
        "vector_cache_degrees": float(budget.get("vector_cache_degrees", 0.0) or 0.0),
        "vector_cache_zoom_step": float(budget.get("vector_cache_zoom_step", 0.0) or 0.0),
        "vector_point_stride": int(budget.get("vector_point_stride", 1) or 1),
        "defer_reason": defer_reason,
        "deferred_overlay_count": max(0, int(deferred_overlay_count)),
        "cache_hit_count": max(0, int(cache_hit_count)),
        "cache_miss_count": max(0, int(cache_miss_count)),
        "target_fps": target_fps_value,
        "target_frame_budget_ms": target_frame_budget_ms,
        "last_render_ms": render_ms,
        "pressure": pressure,
        "runtime_optimization_applied": False,
        "boundary": "Heavy overlay defer/cache snapshot reports current policy decisions only; it does not create worker threads, change cache governance or merge render passes.",
    }


def build_runtime_optimization_review_summary_packet(
    source: str,
    runtime_pressure_snapshot: dict[str, object] | None,
    layer_render_state: dict[str, object] | None,
    lod_counters: dict[str, object] | None,
    heavy_overlay_defer_cache: dict[str, object] | None,
) -> dict[str, object]:
    pressure = runtime_pressure_snapshot if isinstance(runtime_pressure_snapshot, dict) else {}
    layer_state = layer_render_state if isinstance(layer_render_state, dict) else {}
    lod = lod_counters if isinstance(lod_counters, dict) else {}
    overlay = heavy_overlay_defer_cache if isinstance(heavy_overlay_defer_cache, dict) else {}
    pressure_value = float(pressure.get("pressure", 0.0) or 0.0)
    defer_vector_overlays = bool(overlay.get("defer_vector_overlays", False))
    prefer_static_cache = bool(overlay.get("prefer_static_cache", False))
    if defer_vector_overlays:
        reviewer_status = "defer_heavy_overlay_during_interaction"
    elif prefer_static_cache:
        reviewer_status = "prefer_static_cache"
    elif pressure_value > 1.08:
        reviewer_status = "over_budget_observed"
    else:
        reviewer_status = "within_budget_or_warming_up"
    return {
        "schema": "rrkal_displaytools.runtime_optimization_review_summary.v1",
        "source": source,
        "status": "observed_no_runtime_mutation",
        "reviewer_status": reviewer_status,
        "pressure": pressure_value,
        "target_fps": float(pressure.get("target_fps", 0.0) or 0.0),
        "last_render_ms": float(pressure.get("last_render_ms", 0.0) or 0.0),
        "lod_bucket": str(lod.get("lod_bucket", pressure.get("lod", "unknown")) or "unknown"),
        "visible_layer_count": int(layer_state.get("visible_layer_count", pressure.get("visible_layer_count", 0)) or 0),
        "visible_vector_records": int(lod.get("visible_vector_records", pressure.get("vector_record_count", 0)) or 0),
        "layer_state_count": int(layer_state.get("layer_count", 0) or 0),
        "defer_vector_overlays": defer_vector_overlays,
        "prefer_static_cache": prefer_static_cache,
        "deferred_overlay_count": int(overlay.get("deferred_overlay_count", lod.get("deferred_overlay_count", 0)) or 0),
        "cache_hit_count": int(overlay.get("cache_hit_count", lod.get("cache_hit_count", 0)) or 0),
        "cache_miss_count": int(overlay.get("cache_miss_count", lod.get("cache_miss_count", 0)) or 0),
        "source_packets": [
            "runtime_pressure_snapshot",
            "layer_render_state",
            "lod_counters",
            "heavy_overlay_defer_cache",
        ],
        "summary_text": "Runtime optimization review: pressure={pressure:.2f}x; lod={lod}; layers={layers}; vectors={vectors}; defer={defer}; static_cache={static_cache}; cache={hits}/{misses}; runtime_mutation=false".format(
            pressure=pressure_value,
            lod=str(lod.get("lod_bucket", pressure.get("lod", "unknown")) or "unknown"),
            layers=int(layer_state.get("visible_layer_count", pressure.get("visible_layer_count", 0)) or 0),
            vectors=int(lod.get("visible_vector_records", pressure.get("vector_record_count", 0)) or 0),
            defer=defer_vector_overlays,
            static_cache=prefer_static_cache,
            hits=int(overlay.get("cache_hit_count", lod.get("cache_hit_count", 0)) or 0),
            misses=int(overlay.get("cache_miss_count", lod.get("cache_miss_count", 0)) or 0),
        ),
        "runtime_optimization_applied": False,
        "boundary": "Reviewer summary aggregates existing runtime metadata only; it does not mutate render order, worker scheduling, cache governance or compose merging.",
    }
