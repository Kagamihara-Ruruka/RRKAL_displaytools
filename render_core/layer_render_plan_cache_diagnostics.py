"""Pure cache diagnostics helpers for layer render plans."""

from __future__ import annotations

import json


def _render_plan_count(value: object) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def build_layer_render_plan_metadata_summary(plan: dict[str, object]) -> dict[str, object]:
    compiled_plan = plan if isinstance(plan, dict) else {}
    runtime_snapshot = compiled_plan.get("runtime_snapshot")
    if not isinstance(runtime_snapshot, dict):
        runtime_snapshot = {}
    execution_summary = compiled_plan.get("execution_summary")
    if not isinstance(execution_summary, dict):
        execution_summary = {}
    phase_timing_runtime = compiled_plan.get("phase_timing_runtime")
    if not isinstance(phase_timing_runtime, dict):
        phase_timing_runtime = {}
    single_pass_preflight = compiled_plan.get("single_pass_preflight_contract")
    if not isinstance(single_pass_preflight, dict):
        single_pass_preflight = {}
    adapter_payload = compiled_plan.get("adapter_payload_summary")
    if not isinstance(adapter_payload, dict):
        adapter_payload = {}
    adapter_payload_contract = compiled_plan.get("adapter_payload_contract")
    if not isinstance(adapter_payload_contract, dict):
        adapter_payload_contract = {}
    available = bool(compiled_plan)
    return {
        "schema": "rrkal_displaytools.layer_render_plan_metadata_summary.v1",
        "source": "render_core.render_plan.build_layer_render_plan_metadata_summary",
        "status": "ready" if available else "unavailable",
        "full_plan_field": "layer_render_plan",
        "full_plan_schema": compiled_plan.get("schema") if available else None,
        "cache_status": compiled_plan.get("cache_status", "unavailable") if available else "unavailable",
        "cache_reuse_decision": compiled_plan.get("cache_reuse_decision", "unavailable") if available else "unavailable",
        "frame_index": compiled_plan.get("frame_index"),
        "visible_layer_count": _render_plan_count(runtime_snapshot.get("visible_layer_count")),
        "composition_step_count": _render_plan_count(compiled_plan.get("composition_step_count")),
        "compose_queue_count": _render_plan_count(compiled_plan.get("compose_queue_count")),
        "compose_queue_skipped_count": _render_plan_count(compiled_plan.get("compose_queue_skipped_count")),
        "compose_run_count": _render_plan_count(compiled_plan.get("compose_run_count")),
        "compose_merge_candidate_run_count": _render_plan_count(compiled_plan.get("compose_merge_candidate_run_count")),
        "execution_phase_count": _render_plan_count(compiled_plan.get("execution_phase_count")),
        "single_pass_ready": bool(compiled_plan.get("single_pass_ready", False)) if available else False,
        "single_pass_preflight_status": single_pass_preflight.get("status", "unavailable"),
        "adapter_payload_status": adapter_payload.get("status", "unavailable"),
        "adapter_payload_contract_status": adapter_payload_contract.get("status", "unavailable"),
        "runtime_optimization_applied": bool(compiled_plan.get("runtime_optimization_applied", False)) if available else False,
        "current_execution_mode": execution_summary.get("current_execution_mode", "unavailable"),
        "phase_timing_status": phase_timing_runtime.get("status", "unavailable"),
        "slowest_phase_id": phase_timing_runtime.get("slowest_phase_id"),
        "slow_frame": bool(phase_timing_runtime.get("slow_frame", False)),
        "reuse_policy": compiled_plan.get("reuse_policy", "unavailable") if available else "unavailable",
        "reuse_boundary": compiled_plan.get("reuse_boundary", "unavailable") if available else "unavailable",
        "boundary": "Summary only; full layer_render_plan remains the renderer parity/debugging contract.",
    }


def build_layer_render_plan_cache_key(
    runtime_snapshot: dict[str, object],
    composition_steps: list[dict[str, object]],
    style_profile: object,
    boundary_layer_ids: list[str],
    layer_opacity: dict[str, object],
    layer_blend: dict[str, object],
) -> str:
    visible_layers = runtime_snapshot.get("visible_layers") if isinstance(runtime_snapshot.get("visible_layers"), list) else []
    visible_layer_ids = [str(layer_id) for layer_id in visible_layers]
    payload = {
        "style_profile": style_profile,
        "visible_layers": visible_layer_ids,
        "selected_layer_semantic_target": runtime_snapshot.get("selected_layer_semantic_target"),
        "dirty_flags": runtime_snapshot.get("dirty_flags"),
        "defer_vector_overlays": runtime_snapshot.get("defer_vector_overlays"),
        "composition_ids": [str(step.get("id")) for step in composition_steps],
        "boundary_layer_ids": sorted(str(layer_id) for layer_id in boundary_layer_ids),
        "layer_opacity": {str(layer_id): layer_opacity.get(layer_id) for layer_id in visible_layer_ids},
        "layer_blend": {str(layer_id): layer_blend.get(layer_id) for layer_id in visible_layer_ids},
    }
    return json.dumps(payload, sort_keys=True, default=str)


def build_layer_render_plan_cache_invalidation_reasons(
    runtime_snapshot: dict[str, object],
    cache_key: str,
    cached_plan: object,
    previous_key: object,
) -> list[str]:
    reasons: list[str] = []
    dirty_flags = runtime_snapshot.get("dirty_flags") if isinstance(runtime_snapshot.get("dirty_flags"), dict) else {}
    for flag, value in dirty_flags.items():
        if value is True:
            reasons.append(f"dirty_flag:{flag}")
    if not isinstance(cached_plan, dict):
        reasons.append("no_previous_compiled_plan")
    elif previous_key != cache_key:
        reasons.append("cache_key_changed")
    if not reasons:
        reasons.append("cache_key_match")
    return reasons


def build_layer_render_plan_cache_invalidation_scope(
    runtime_snapshot: dict[str, object],
    invalidation_reasons: list[str],
) -> list[dict[str, object]]:
    dirty_flags = runtime_snapshot.get("dirty_flags") if isinstance(runtime_snapshot.get("dirty_flags"), dict) else {}
    batch_targets = runtime_snapshot.get("batch_targets") if isinstance(runtime_snapshot.get("batch_targets"), list) else []
    scopes: list[dict[str, object]] = []
    for batch in batch_targets:
        if not isinstance(batch, dict):
            continue
        dirty_flag = str(batch.get("dirty_flag") or "")
        if dirty_flag and dirty_flags.get(dirty_flag) is True:
            scopes.append(
                {
                    "scope": "batch",
                    "id": str(batch.get("id") or dirty_flag),
                    "dirty_flag": dirty_flag,
                    "source": batch.get("source"),
                }
            )
    for global_flag in ("force", "changed"):
        if dirty_flags.get(global_flag) is True:
            scopes.append({"scope": "global", "id": global_flag, "dirty_flag": global_flag})
    if "cache_key_changed" in invalidation_reasons or "no_previous_compiled_plan" in invalidation_reasons:
        scopes.append({"scope": "plan", "id": "compiled_layer_render_plan", "dirty_flag": "cache_key"})
    if not scopes and "cache_key_match" in invalidation_reasons:
        scopes.append({"scope": "reuse", "id": "compiled_layer_render_plan", "dirty_flag": None})
    return scopes
