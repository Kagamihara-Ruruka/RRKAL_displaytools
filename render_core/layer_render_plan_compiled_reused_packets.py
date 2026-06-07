"""Compiled/reused layer render-plan packet helpers."""

from __future__ import annotations

from render_core.layer_render_plan_adapter_preflight import (
    build_layer_render_plan_adapter_boundary_contract,
    build_layer_render_plan_adapter_payload,
    build_layer_render_plan_adapter_payload_contract,
    build_layer_render_plan_adapter_payload_summary,
    build_layer_render_plan_single_pass_preflight_contract,
)


def _payload_list(adapter_payload: dict[str, object], key: str) -> list[dict[str, object]]:
    value = adapter_payload.get(key)
    return value if isinstance(value, list) else []


def _payload_dict(adapter_payload: dict[str, object], key: str) -> dict[str, object]:
    value = adapter_payload.get(key)
    return value if isinstance(value, dict) else {}


def build_compiled_layer_render_plan_packet_from_adapter_payload(
    adapter_payload: dict[str, object],
    frame_index: int,
    *,
    source: str,
) -> dict[str, object]:
    payload = adapter_payload if isinstance(adapter_payload, dict) else {}
    return build_compiled_layer_render_plan_packet(
        str(payload.get("cache_key") or ""),
        _payload_list(payload, "invalidation_reasons"),
        _payload_list(payload, "invalidation_scope"),
        _payload_list(payload, "batch_decisions"),
        _payload_list(payload, "apply_path"),
        _payload_dict(payload, "execution_summary"),
        _payload_list(payload, "execution_phases"),
        _payload_dict(payload, "phase_timing_contract"),
        _payload_dict(payload, "phase_timing_runtime"),
        _payload_dict(payload, "bottleneck_recommendation"),
        frame_index,
        _payload_dict(payload, "runtime_snapshot"),
        _payload_list(payload, "composition_steps"),
        _payload_dict(payload, "compose_queue_packet"),
        payload,
        source=source,
    )


def build_reused_compiled_layer_render_plan_packet_from_adapter_payload(
    cached_plan: dict[str, object],
    adapter_payload: dict[str, object],
    frame_index: int,
) -> dict[str, object]:
    payload = adapter_payload if isinstance(adapter_payload, dict) else {}
    return build_reused_compiled_layer_render_plan_packet(
        cached_plan,
        _payload_list(payload, "invalidation_reasons"),
        _payload_list(payload, "invalidation_scope"),
        _payload_list(payload, "batch_decisions"),
        _payload_list(payload, "apply_path"),
        _payload_dict(payload, "execution_summary"),
        _payload_list(payload, "execution_phases"),
        _payload_dict(payload, "phase_timing_contract"),
        _payload_dict(payload, "phase_timing_runtime"),
        _payload_dict(payload, "bottleneck_recommendation"),
        frame_index,
        _payload_dict(payload, "runtime_snapshot"),
        _payload_dict(payload, "compose_queue_packet"),
        payload,
    )


def build_compiled_layer_render_plan_packet(
    cache_key: str,
    invalidation_reasons: list[str],
    invalidation_scope: list[dict[str, object]],
    batch_decisions: list[dict[str, object]],
    apply_path: list[dict[str, object]],
    execution_summary: dict[str, object],
    execution_phases: list[dict[str, object]],
    phase_timing_contract: dict[str, object],
    phase_timing_runtime: dict[str, object],
    bottleneck_recommendation: dict[str, object],
    frame_index: int,
    runtime_snapshot: dict[str, object],
    composition_steps: list[dict[str, object]],
    compose_queue_packet: dict[str, object],
    adapter_payload: dict[str, object] | None = None,
    *,
    source: str,
) -> dict[str, object]:
    if not isinstance(adapter_payload, dict):
        adapter_payload = build_layer_render_plan_adapter_payload(
            runtime_snapshot,
            composition_steps,
            compose_queue_packet,
            cache_key,
            invalidation_reasons,
            invalidation_scope,
            batch_decisions,
            apply_path,
            execution_summary,
            execution_phases,
            phase_timing_contract,
            phase_timing_runtime,
            bottleneck_recommendation,
        )
    adapter_payload_contract = build_layer_render_plan_adapter_payload_contract(adapter_payload)
    single_pass_preflight_contract = build_layer_render_plan_single_pass_preflight_contract(
        compose_queue_packet.get("compose_runs", []),
        execution_summary,
        phase_timing_runtime,
    )
    adapter_boundary_contract = build_layer_render_plan_adapter_boundary_contract(
        runtime_snapshot,
        composition_steps,
    )
    adapter_payload_summary = adapter_payload.get("summary")
    if not isinstance(adapter_payload_summary, dict):
        adapter_payload_summary = build_layer_render_plan_adapter_payload_summary(
            runtime_snapshot,
            composition_steps,
            compose_queue_packet,
        )
    return {
        "schema": "rrkal_displaytools.compiled_layer_render_plan.v1",
        "source": source,
        "status": "compiled_snapshot",
        "cache_status": "compiled",
        "cache_reuse_decision": "compiled",
        "cache_key": cache_key,
        "cache_invalidation_reasons": invalidation_reasons,
        "cache_invalidation_reason_schema": "rrkal_displaytools.layer_render_plan_cache_invalidation_reasons.v1",
        "cache_invalidation_scope": invalidation_scope,
        "cache_invalidation_scope_schema": "rrkal_displaytools.layer_render_plan_cache_invalidation_scope.v1",
        "batch_decisions": batch_decisions,
        "batch_decision_schema": "rrkal_displaytools.layer_render_plan_batch_decisions.v1",
        "batch_decision_count": len(batch_decisions),
        "apply_path": apply_path,
        "apply_path_schema": "rrkal_displaytools.layer_render_plan_apply_path.v1",
        "apply_path_count": len(apply_path),
        "execution_summary": execution_summary,
        "execution_summary_schema": "rrkal_displaytools.layer_render_plan_execution_summary.v1",
        "execution_phases": execution_phases,
        "execution_phases_schema": "rrkal_displaytools.layer_render_plan_execution_phases.v1",
        "execution_phase_count": len(execution_phases),
        "phase_timing_contract": phase_timing_contract,
        "phase_timing_contract_schema": "rrkal_displaytools.layer_render_plan_phase_timing_contract.v1",
        "phase_timing_runtime": phase_timing_runtime,
        "phase_timing_runtime_schema": "rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1",
        "bottleneck_recommendation": bottleneck_recommendation,
        "bottleneck_recommendation_schema": "rrkal_displaytools.layer_render_plan_bottleneck_recommendation.v1",
        "single_pass_preflight_contract": single_pass_preflight_contract,
        "single_pass_preflight_contract_schema": "rrkal_displaytools.layer_render_plan_single_pass_preflight_contract.v1",
        "adapter_boundary_contract": adapter_boundary_contract,
        "adapter_boundary_contract_schema": "rrkal_displaytools.layer_render_plan_adapter_boundary.v1",
        "adapter_payload": adapter_payload,
        "adapter_payload_schema": "rrkal_displaytools.layer_render_plan_adapter_payload.v1",
        "adapter_payload_contract": adapter_payload_contract,
        "adapter_payload_contract_schema": "rrkal_displaytools.layer_render_plan_adapter_payload_contract.v1",
        "adapter_payload_summary": adapter_payload_summary,
        "adapter_payload_summary_schema": "rrkal_displaytools.layer_render_plan_adapter_payload_summary.v1",
        "reuse_policy": "reuse_when_cache_key_matches_previous_compiled_plan",
        "reuse_status_values": ["compiled", "reused"],
        "runtime_optimization_applied": False,
        "optimization_target": "precompute_layer_state_then_single_render_pass",
        "frame_index": int(frame_index),
        "runtime_snapshot": runtime_snapshot,
        "dirty_flags": runtime_snapshot.get("dirty_flags", {}),
        "batch_targets": runtime_snapshot.get("batch_targets", []),
        "composition_steps": composition_steps,
        "composition_step_count": len(composition_steps),
        "compose_queue": compose_queue_packet.get("queue", []),
        "compose_queue_schema": "rrkal_displaytools.layer_render_plan_compose_queue.v1",
        "compose_queue_packet": compose_queue_packet,
        "compose_queue_count": compose_queue_packet.get("executable_step_count", 0),
        "compose_queue_skipped_count": compose_queue_packet.get("skipped_step_count", 0),
        "compose_runs": compose_queue_packet.get("compose_runs", []),
        "compose_runs_schema": "rrkal_displaytools.layer_render_plan_compose_runs.v1",
        "compose_run_count": compose_queue_packet.get("compose_run_count", 0),
        "compose_merge_candidate_run_count": compose_queue_packet.get("compose_merge_candidate_run_count", 0),
        "compose_run_parity_contract": compose_queue_packet.get("compose_run_parity_contract", {}),
        "compose_run_parity_contract_schema": "rrkal_displaytools.layer_render_plan_compose_run_parity_contract.v1",
        "compose_order": runtime_snapshot.get("compose_order", []),
        "apply_helper": "HybridRenderController.apply_layer_render_plan_composition",
        "single_pass_ready": False,
        "reuse_boundary": "valid_until_dirty_flags_or_camera_change",
    }


def build_reused_compiled_layer_render_plan_packet(
    cached_plan: dict[str, object],
    invalidation_reasons: list[str],
    invalidation_scope: list[dict[str, object]],
    batch_decisions: list[dict[str, object]],
    apply_path: list[dict[str, object]],
    execution_summary: dict[str, object],
    execution_phases: list[dict[str, object]],
    phase_timing_contract: dict[str, object],
    phase_timing_runtime: dict[str, object],
    bottleneck_recommendation: dict[str, object],
    frame_index: int,
    runtime_snapshot: dict[str, object],
    compose_queue_packet: dict[str, object],
    adapter_payload: dict[str, object] | None = None,
) -> dict[str, object]:
    plan = dict(cached_plan)
    plan["cache_status"] = "reused"
    plan["cache_reuse_decision"] = "reused"
    plan["cache_invalidation_reasons"] = invalidation_reasons
    plan["cache_invalidation_scope"] = invalidation_scope
    plan["batch_decisions"] = batch_decisions
    plan["batch_decision_count"] = len(batch_decisions)
    plan["apply_path"] = apply_path
    plan["apply_path_count"] = len(apply_path)
    plan["execution_summary"] = execution_summary
    plan["execution_phases"] = execution_phases
    plan["execution_phases_schema"] = plan.get("execution_phases_schema", "rrkal_displaytools.layer_render_plan_execution_phases.v1")
    plan["execution_phase_count"] = len(execution_phases)
    plan["phase_timing_contract"] = phase_timing_contract
    plan["phase_timing_contract_schema"] = "rrkal_displaytools.layer_render_plan_phase_timing_contract.v1"
    plan["phase_timing_runtime"] = phase_timing_runtime
    plan["phase_timing_runtime_schema"] = "rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1"
    plan["bottleneck_recommendation"] = bottleneck_recommendation
    plan["bottleneck_recommendation_schema"] = "rrkal_displaytools.layer_render_plan_bottleneck_recommendation.v1"
    plan["single_pass_preflight_contract"] = build_layer_render_plan_single_pass_preflight_contract(
        compose_queue_packet.get("compose_runs", []),
        execution_summary,
        phase_timing_runtime,
    )
    plan["single_pass_preflight_contract_schema"] = "rrkal_displaytools.layer_render_plan_single_pass_preflight_contract.v1"
    composition_steps = plan.get("composition_steps")
    if not isinstance(composition_steps, list):
        composition_steps = []
    if not isinstance(adapter_payload, dict):
        adapter_payload = build_layer_render_plan_adapter_payload(
            runtime_snapshot,
            composition_steps,
            compose_queue_packet,
            str(plan.get("cache_key") or ""),
            invalidation_reasons,
            invalidation_scope,
            batch_decisions,
            apply_path,
            execution_summary,
            execution_phases,
            phase_timing_contract,
            phase_timing_runtime,
            bottleneck_recommendation,
        )
    adapter_payload_contract = build_layer_render_plan_adapter_payload_contract(adapter_payload)
    plan["adapter_boundary_contract"] = build_layer_render_plan_adapter_boundary_contract(
        runtime_snapshot,
        composition_steps,
    )
    plan["adapter_boundary_contract_schema"] = "rrkal_displaytools.layer_render_plan_adapter_boundary.v1"
    adapter_payload_summary = adapter_payload.get("summary")
    if not isinstance(adapter_payload_summary, dict):
        adapter_payload_summary = build_layer_render_plan_adapter_payload_summary(
            runtime_snapshot,
            composition_steps,
            compose_queue_packet,
        )
    plan["adapter_payload"] = adapter_payload
    plan["adapter_payload_schema"] = "rrkal_displaytools.layer_render_plan_adapter_payload.v1"
    plan["adapter_payload_contract"] = adapter_payload_contract
    plan["adapter_payload_contract_schema"] = "rrkal_displaytools.layer_render_plan_adapter_payload_contract.v1"
    plan["adapter_payload_summary"] = adapter_payload_summary
    plan["adapter_payload_summary_schema"] = "rrkal_displaytools.layer_render_plan_adapter_payload_summary.v1"
    plan["reuse_policy"] = "reuse_when_cache_key_matches_previous_compiled_plan"
    plan["reuse_boundary"] = plan.get("reuse_boundary", "valid_until_dirty_flags_or_camera_change")
    plan["frame_index"] = int(frame_index)
    plan["runtime_snapshot"] = runtime_snapshot
    plan["dirty_flags"] = runtime_snapshot.get("dirty_flags", {})
    plan["compose_queue"] = compose_queue_packet.get("queue", [])
    plan["compose_queue_schema"] = "rrkal_displaytools.layer_render_plan_compose_queue.v1"
    plan["compose_queue_packet"] = compose_queue_packet
    plan["compose_queue_count"] = compose_queue_packet.get("executable_step_count", 0)
    plan["compose_queue_skipped_count"] = compose_queue_packet.get("skipped_step_count", 0)
    plan["compose_runs"] = compose_queue_packet.get("compose_runs", [])
    plan["compose_runs_schema"] = "rrkal_displaytools.layer_render_plan_compose_runs.v1"
    plan["compose_run_count"] = compose_queue_packet.get("compose_run_count", 0)
    plan["compose_merge_candidate_run_count"] = compose_queue_packet.get("compose_merge_candidate_run_count", 0)
    plan["compose_run_parity_contract"] = compose_queue_packet.get("compose_run_parity_contract", {})
    plan["compose_run_parity_contract_schema"] = "rrkal_displaytools.layer_render_plan_compose_run_parity_contract.v1"
    return plan
