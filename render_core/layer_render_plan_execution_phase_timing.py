"""Pure execution phase timing packet helpers for layer render plans."""

from __future__ import annotations


def build_layer_render_plan_execution_summary(
    apply_path: list[dict[str, object]],
    batch_decisions: list[dict[str, object]],
    *,
    source: str = "render_core.render_plan.build_layer_render_plan_execution_summary",
) -> dict[str, object]:
    helper_counts: dict[str, int] = {}
    decision_counts: dict[str, int] = {}
    single_pass_candidate_count = 0
    single_pass_blockers: list[str] = []
    for item in apply_path:
        if not isinstance(item, dict):
            continue
        helper = str(item.get("apply_helper") or "unknown_apply_helper")
        helper_counts[helper] = helper_counts.get(helper, 0) + 1
        decision = str(item.get("decision") or "unknown_decision")
        decision_counts[decision] = decision_counts.get(decision, 0) + 1
        if item.get("single_pass_candidate"):
            single_pass_candidate_count += 1
        else:
            single_pass_blockers.append(str(item.get("id") or "unknown_step"))
    batch_decision_counts: dict[str, int] = {}
    for item in batch_decisions:
        if not isinstance(item, dict):
            continue
        decision = str(item.get("decision") or "unknown_decision")
        batch_decision_counts[decision] = batch_decision_counts.get(decision, 0) + 1
    return {
        "schema": "rrkal_displaytools.layer_render_plan_execution_summary.v1",
        "source": source,
        "current_execution_mode": "centralized_overlay_composition",
        "current_apply_helper": "HybridRenderController.apply_layer_render_plan_composition",
        "runtime_optimization_applied": False,
        "apply_path_count": len(apply_path),
        "batch_decision_count": len(batch_decisions),
        "single_pass_candidate_count": single_pass_candidate_count,
        "single_pass_blockers": single_pass_blockers,
        "helper_counts": helper_counts,
        "decision_counts": decision_counts,
        "batch_decision_counts": batch_decision_counts,
        "next_refactor_target": "replace per-step overlay helpers with a unified Taichi render/composite pass",
    }


def build_layer_render_plan_execution_phases(
    apply_path: list[dict[str, object]],
    batch_decisions: list[dict[str, object]],
    execution_summary: dict[str, object],
) -> list[dict[str, object]]:
    def phase_decisions(items: list[dict[str, object]]) -> list[str]:
        values = sorted(
            {
                str(item.get("decision") or "unknown_decision")
                for item in items
                if isinstance(item, dict)
            }
        )
        return values or ["none"]

    batch_items = [
        item
        for item in batch_decisions
        if isinstance(item, dict) and item.get("scope") == "batch"
    ]
    layer_items = [
        item
        for item in batch_decisions
        if isinstance(item, dict) and item.get("scope") == "layer"
    ]
    single_pass_items = [
        item
        for item in apply_path
        if isinstance(item, dict) and item.get("single_pass_candidate")
    ]
    blockers_value = execution_summary.get("single_pass_blockers")
    blockers = blockers_value if isinstance(blockers_value, list) else []
    postprocess_count = sum(
        1
        for item in apply_path
        if isinstance(item, dict) and item.get("kind") == "style_profile_postprocess"
    )
    return [
        {
            "id": "prepare_batches",
            "order": 0,
            "status": "planned_runtime_metadata",
            "item_count": len(batch_items),
            "decisions": phase_decisions(batch_items),
            "current_runtime_path": "precomputed_overlay_buffers",
            "future_single_pass_role": "prepare GPU-ready batch inputs",
        },
        {
            "id": "compose_overlays",
            "order": 1,
            "status": "current_runtime_path",
            "item_count": len(layer_items),
            "decisions": phase_decisions(layer_items),
            "current_runtime_path": "HybridRenderController.apply_layer_render_plan_composition",
            "future_single_pass_role": "replace per-layer overlay composition with one Taichi composite pass",
        },
        {
            "id": "postprocess",
            "order": 2,
            "status": "current_runtime_path",
            "item_count": postprocess_count,
            "decisions": ["postprocess_each_frame"],
            "current_runtime_path": "apply_style_profile",
            "future_single_pass_role": "remain final style pass unless folded into shader",
        },
        {
            "id": "future_single_pass_candidate",
            "order": 3,
            "status": "queued_after_module_decoupling",
            "item_count": len(single_pass_items),
            "decisions": ["single_pass_candidate"],
            "current_runtime_path": "metadata_only",
            "future_single_pass_role": "candidate steps for unified Taichi render/composite pass",
            "blockers": blockers,
        },
    ]


def build_layer_render_plan_phase_timing_contract(
    execution_phases: list[dict[str, object]],
) -> dict[str, object]:
    phase_probe_points = []
    for phase in execution_phases:
        if not isinstance(phase, dict):
            continue
        phase_id = str(phase.get("id") or "unknown_phase")
        phase_probe_points.append(
            {
                "phase_id": phase_id,
                "order": phase.get("order"),
                "probe_key": f"phase_ms.{phase_id}",
                "recommended_start": f"{phase_id}.perf_counter_start",
                "recommended_end": f"{phase_id}.perf_counter_end",
                "metadata_field": f"phase_timing_ms.{phase_id}",
            }
        )
    return {
        "schema": "rrkal_displaytools.layer_render_plan_phase_timing_contract.v1",
        "source": "render_core.render_plan.build_layer_render_plan_phase_timing_contract",
        "status": "probe_contract_ready",
        "runtime_measurements_available": False,
        "timing_unit": "milliseconds",
        "slow_frame_threshold_ms": 33.3,
        "phase_probe_count": len(phase_probe_points),
        "phase_probe_points": phase_probe_points,
        "summary_fields": ["total_ms", "phase_timing_ms", "slowest_phase_id", "frame_index"],
        "next_runtime_step": "wrap phase boundaries with perf_counter and write measured phase_timing_ms into renderer metadata",
    }


def build_layer_render_plan_bottleneck_recommendation(
    phase_timing_runtime: dict[str, object],
) -> dict[str, object]:
    timing = phase_timing_runtime if isinstance(phase_timing_runtime, dict) else {}
    slowest_phase_id = str(timing.get("slowest_phase_id") or "unavailable")
    measured = bool(timing.get("runtime_measurements_available"))
    phase_plan = {
        "prepare_batches": {
            "recommended_next_action": "reuse_static_geometry_batches",
            "target_helper": "HybridRenderController.compile_layer_render_plan",
            "optimization_boundary": "cache renderer-ready hydrology, boundary, traffic and pin batches before composition",
        },
        "compose_overlays": {
            "recommended_next_action": "collapse_overlay_composition_passes",
            "target_helper": "HybridRenderController.apply_layer_render_plan_composition",
            "optimization_boundary": "replace per-layer alpha/runtime helper sequence with fewer unified composite passes",
        },
        "postprocess": {
            "recommended_next_action": "fold_or_defer_style_profile_postprocess",
            "target_helper": "apply_style_profile",
            "optimization_boundary": "avoid repeated full-frame tone/style work when style profile is unchanged",
        },
        "future_single_pass_candidate": {
            "recommended_next_action": "prototype_single_taichi_composite_pass",
            "target_helper": "HybridRenderController.apply_layer_render_plan_composition",
            "optimization_boundary": "consume compiled layer state in one Taichi render/composite path",
        },
    }
    selected = phase_plan.get(
        slowest_phase_id,
        {
            "recommended_next_action": "collect_more_runtime_phase_timing",
            "target_helper": "render_core.render_plan.build_layer_render_plan_phase_timing_runtime_packet",
            "optimization_boundary": "wait for measured phase_timing_ms before changing render behavior",
        },
    )
    return {
        "schema": "rrkal_displaytools.layer_render_plan_bottleneck_recommendation.v1",
        "source": "render_core.render_plan.build_layer_render_plan_bottleneck_recommendation",
        "status": "ready" if measured else "waiting_for_runtime_metadata",
        "basis_schema": timing.get("schema", "rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1"),
        "slowest_phase_id": slowest_phase_id,
        "slowest_phase_ms": timing.get("slowest_phase_ms", 0.0),
        "total_ms": timing.get("total_ms", 0.0),
        "slow_frame": bool(timing.get("slow_frame", False)),
        "recommended_next_action": selected["recommended_next_action"],
        "target_helper": selected["target_helper"],
        "optimization_boundary": selected["optimization_boundary"],
        "runtime_optimization_applied": False,
        "next_commit_scope": "implement the recommended action only after smoke-gated phase timing confirms the bottleneck",
    }


def _normalize_phase_timing_ms(phase_timing_ms: dict[str, float]) -> dict[str, float]:
    return {
        str(phase_id): round(float(elapsed_ms), 3)
        for phase_id, elapsed_ms in phase_timing_ms.items()
        if isinstance(phase_id, str)
    }


def _select_slowest_phase(measured: dict[str, float]) -> tuple[str | None, float]:
    if not measured:
        return None, 0.0
    slowest_phase_id = max(measured, key=lambda key: measured[key])
    return slowest_phase_id, measured.get(slowest_phase_id, 0.0)


def build_layer_render_plan_phase_timing_runtime_packet(
    phase_timing_ms: dict[str, float],
    frame_index: int,
    total_ms: float,
) -> dict[str, object]:
    measured = _normalize_phase_timing_ms(phase_timing_ms)
    slowest_phase_id, slowest_phase_ms = _select_slowest_phase(measured)
    threshold_ms = 33.3
    packet = {
        "schema": "rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1",
        "source": "render_core.render_plan.build_layer_render_plan_phase_timing_runtime_packet",
        "status": "measured" if measured else "unavailable",
        "runtime_measurements_available": bool(measured),
        "timing_unit": "milliseconds",
        "total_ms": round(float(total_ms), 3),
        "phase_timing_ms": measured,
        "measured_phase_ids": list(measured.keys()),
        "slowest_phase_id": slowest_phase_id,
        "slowest_phase_ms": round(float(slowest_phase_ms), 3),
        "slow_frame": float(total_ms) > threshold_ms,
        "slow_frame_threshold_ms": threshold_ms,
        "frame_index": int(frame_index),
        "next_optimization_use": "identify whether prepare_batches, compose_overlays or postprocess dominates before replacing the render loop",
    }
    packet["bottleneck_recommendation_schema"] = "rrkal_displaytools.layer_render_plan_bottleneck_recommendation.v1"
    packet["bottleneck_recommendation"] = build_layer_render_plan_bottleneck_recommendation(packet)
    return packet
