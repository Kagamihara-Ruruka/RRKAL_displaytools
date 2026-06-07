"""Pure adapter/preflight packet helpers for layer render plans."""

from __future__ import annotations


def _render_plan_count(value: object) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def build_layer_render_plan_single_pass_preflight_contract(
    compose_runs: list[dict[str, object]],
    execution_summary: dict[str, object],
    phase_timing_runtime: dict[str, object],
) -> dict[str, object]:
    merge_candidates = [
        run
        for run in compose_runs
        if isinstance(run, dict) and run.get("merge_safe") is True
    ]
    measured = bool(phase_timing_runtime.get("runtime_measurements_available")) if isinstance(phase_timing_runtime, dict) else False
    single_pass_candidate_count = _render_plan_count(execution_summary.get("single_pass_candidate_count"))
    candidate_count = len(merge_candidates) + single_pass_candidate_count
    if candidate_count <= 0:
        status = "no_candidates"
    elif measured:
        status = "ready_for_parity_smoke"
    else:
        status = "waiting_for_runtime_timing"
    return {
        "schema": "rrkal_displaytools.layer_render_plan_single_pass_preflight_contract.v1",
        "source": "render_core.render_plan.build_layer_render_plan_single_pass_preflight_contract",
        "status": status,
        "runtime_single_pass_enabled": False,
        "runtime_path_unchanged": True,
        "merge_candidate_run_count": len(merge_candidates),
        "candidate_run_ids": [str(run.get("id")) for run in merge_candidates],
        "single_pass_candidate_count": single_pass_candidate_count,
        "runtime_measurements_available": measured,
        "required_before_enable": [
            "compose_run_parity_smoke",
            "phase_timing_runtime_metadata",
            "manual_visual_review",
        ],
        "parity_gate": "zero_diff_against_sequential_compose_queue",
        "timing_gate": "measured_compose_overlays_bottleneck_before_runtime_replacement",
        "review_gate": "manual_qt_or_renderer_output_review_before_default_enable",
        "next_runtime_step": "prototype opt-in single-pass composition only after parity and timing gates pass",
    }


def build_layer_render_plan_adapter_boundary_contract(
    runtime_snapshot: dict[str, object],
    composition_steps: list[dict[str, object]],
) -> dict[str, object]:
    visible_layers = runtime_snapshot.get("visible_layers") if isinstance(runtime_snapshot.get("visible_layers"), list) else []
    dirty_flags = runtime_snapshot.get("dirty_flags") if isinstance(runtime_snapshot.get("dirty_flags"), dict) else {}
    return {
        "schema": "rrkal_displaytools.layer_render_plan_adapter_boundary.v1",
        "source": "render_core.render_plan.build_layer_render_plan_adapter_boundary_contract",
        "status": "documented_boundary",
        "runtime_path_unchanged": True,
        "controller_owned_inputs": [
            "frame_index",
            "visible_layers",
            "selected_layer_semantic_target",
            "dirty_flags",
            "step_runtime_states",
            "overlay_array_lookup",
            "transparent_overlay_checks",
        ],
        "core_owned_decisions": [
            "composition_steps",
            "compose_queue_classification",
            "compose_runs",
            "cache_key",
            "cache_invalidation_scope",
            "batch_decisions",
            "execution_summary",
            "single_pass_preflight_contract",
        ],
        "forbidden_in_render_core": [
            "Qt widgets",
            "np.ndarray overlay object ownership",
            "Taichi kernel/frame mutation",
            "metadata file writes",
            "RRKAL provider discovery/download/cache governance",
        ],
        "adapter_payload_fields": [
            "runtime_snapshot",
            "composition_steps",
            "step_runtime_states",
            "compose_queue_packet",
            "compiled_layer_render_plan",
        ],
        "visible_layer_count": len(visible_layers),
        "dirty_flag_count": len(dirty_flags),
        "composition_step_count": len(composition_steps),
        "next_extraction_target": "normalize controller-to-core adapter payload before moving overlay runtime state out of HybridRenderController",
    }


def build_layer_render_plan_adapter_payload_summary(
    runtime_snapshot: dict[str, object],
    composition_steps: list[dict[str, object]],
    compose_queue_packet: dict[str, object],
) -> dict[str, object]:
    visible_layers = runtime_snapshot.get("visible_layers") if isinstance(runtime_snapshot.get("visible_layers"), list) else []
    dirty_flags = runtime_snapshot.get("dirty_flags") if isinstance(runtime_snapshot.get("dirty_flags"), dict) else {}
    compose_queue = compose_queue_packet.get("queue") if isinstance(compose_queue_packet.get("queue"), list) else []
    skipped_steps = compose_queue_packet.get("skipped_steps") if isinstance(compose_queue_packet.get("skipped_steps"), list) else []
    compose_runs = compose_queue_packet.get("compose_runs") if isinstance(compose_queue_packet.get("compose_runs"), list) else []
    return {
        "schema": "rrkal_displaytools.layer_render_plan_adapter_payload_summary.v1",
        "source": "render_core.render_plan.build_layer_render_plan_adapter_payload_summary",
        "status": "normalized_summary",
        "runtime_path_unchanged": True,
        "payload_boundary": "serializable_summary_only_no_overlay_arrays",
        "visible_layer_ids": [str(layer_id) for layer_id in visible_layers],
        "dirty_flag_ids": sorted(str(key) for key in dirty_flags.keys()),
        "composition_step_ids": [
            str(step.get("id") or step.get("layer_id") or "unknown_step")
            for step in composition_steps
            if isinstance(step, dict)
        ],
        "compose_queue_ids": [
            str(step.get("id") or step.get("layer_id") or "unknown_step")
            for step in compose_queue
            if isinstance(step, dict)
        ],
        "skipped_step_ids": [
            str(step.get("id") or step.get("layer_id") or "unknown_step")
            for step in skipped_steps
            if isinstance(step, dict)
        ],
        "compose_run_ids": [
            str(run.get("id") or "unknown_run")
            for run in compose_runs
            if isinstance(run, dict)
        ],
        "visible_layer_count": len(visible_layers),
        "dirty_flag_count": len(dirty_flags),
        "composition_step_count": len(composition_steps),
        "compose_queue_count": len(compose_queue),
        "skipped_step_count": len(skipped_steps),
        "compose_run_count": len(compose_runs),
        "next_extraction_target": "replace ad-hoc controller method arguments with this normalized serializable adapter payload shape",
    }


def build_layer_render_plan_adapter_payload(
    runtime_snapshot: dict[str, object],
    composition_steps: list[dict[str, object]],
    compose_queue_packet: dict[str, object],
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
) -> dict[str, object]:
    summary = build_layer_render_plan_adapter_payload_summary(
        runtime_snapshot,
        composition_steps,
        compose_queue_packet,
    )
    return {
        "schema": "rrkal_displaytools.layer_render_plan_adapter_payload.v1",
        "source": "render_core.render_plan.build_layer_render_plan_adapter_payload",
        "status": "normalized_payload",
        "contract_role": "primary_payload_contract",
        "runtime_path_unchanged": True,
        "payload_boundary": "serializable_controller_to_core_payload_no_overlay_arrays",
        "summary_schema": "rrkal_displaytools.layer_render_plan_adapter_payload_summary.v1",
        "summary": summary,
        "cache_key": cache_key,
        "invalidation_reasons": invalidation_reasons,
        "invalidation_scope": invalidation_scope,
        "batch_decisions": batch_decisions,
        "apply_path": apply_path,
        "execution_summary": execution_summary,
        "execution_phases": execution_phases,
        "phase_timing_contract": phase_timing_contract,
        "phase_timing_runtime": phase_timing_runtime,
        "bottleneck_recommendation": bottleneck_recommendation,
        "runtime_snapshot": runtime_snapshot,
        "composition_steps": composition_steps,
        "compose_queue_packet": compose_queue_packet,
        "next_extraction_target": "make compiled/reused plan builders consume this payload as the primary contract",
    }


def build_layer_render_plan_compile_input(
    *,
    composition_steps: list[dict[str, object]],
    runtime_snapshot: dict[str, object],
    compose_queue_packet: dict[str, object],
    style_profile: object,
    boundary_layer_ids: list[str],
    layer_opacity: dict[str, object],
    layer_blend: dict[str, object],
    phase_timing_runtime: dict[str, object],
    cached_plan_available: bool,
    previous_cache_key: object,
    frame_index: int,
) -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.layer_render_plan_compile_input.v1",
        "source": "render_core.render_plan.build_layer_render_plan_compile_input",
        "status": "packaged",
        "runtime_path_unchanged": True,
        "composition_steps": composition_steps,
        "runtime_snapshot": runtime_snapshot,
        "compose_queue_packet": compose_queue_packet,
        "style_profile": style_profile,
        "boundary_layer_ids": boundary_layer_ids,
        "layer_opacity": layer_opacity,
        "layer_blend": layer_blend,
        "phase_timing_runtime": phase_timing_runtime,
        "cached_plan_available": bool(cached_plan_available),
        "previous_cache_key": previous_cache_key,
        "frame_index": int(frame_index),
        "boundary": "Controller-collected compile inputs only; no cache decision, overlay lookup, rendering, metadata schema change, or runtime merge enablement.",
    }


def build_layer_render_plan_adapter_payload_contract(
    adapter_payload: dict[str, object],
) -> dict[str, object]:
    payload = adapter_payload if isinstance(adapter_payload, dict) else {}
    required_fields = [
        "schema",
        "status",
        "contract_role",
        "payload_boundary",
        "cache_key",
        "runtime_snapshot",
        "composition_steps",
        "compose_queue_packet",
        "invalidation_reasons",
        "invalidation_scope",
        "batch_decisions",
        "apply_path",
        "execution_summary",
        "execution_phases",
        "phase_timing_contract",
        "phase_timing_runtime",
        "bottleneck_recommendation",
        "summary",
    ]
    present_fields = [field for field in required_fields if field in payload]
    missing_fields = [field for field in required_fields if field not in payload]
    return {
        "schema": "rrkal_displaytools.layer_render_plan_adapter_payload_contract.v1",
        "source": "render_core.render_plan.build_layer_render_plan_adapter_payload_contract",
        "status": "ready" if not missing_fields else "incomplete",
        "required_field_count": len(required_fields),
        "present_field_count": len(present_fields),
        "missing_field_count": len(missing_fields),
        "required_fields": required_fields,
        "missing_fields": missing_fields,
        "payload_schema": payload.get("schema", "unavailable"),
        "payload_status": payload.get("status", "unavailable"),
        "payload_contract_role": payload.get("contract_role", "unavailable"),
        "payload_boundary": payload.get("payload_boundary", "unavailable"),
        "runtime_path_unchanged": bool(payload.get("runtime_path_unchanged", False)),
        "next_extraction_gate": "do_not_make_payload_primary_implementation_until_status_ready",
    }
