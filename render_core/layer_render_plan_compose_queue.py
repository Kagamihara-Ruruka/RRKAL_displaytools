"""Pure compose queue packet helpers for layer render plans."""

from __future__ import annotations


def build_layer_render_plan_compose_queue_packet(
    input_step_count: int,
    queue: list[dict[str, object]],
    skipped_steps: list[dict[str, object]],
    compose_runs_packet: dict[str, object],
    compose_run_parity_contract: dict[str, object],
    *,
    source: str,
) -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.layer_render_plan_compose_queue.v1",
        "source": source,
        "status": "runtime_optimized",
        "optimization_applied": True,
        "optimization": "skip_hidden_missing_or_transparent_overlays_before_composition",
        "input_step_count": input_step_count,
        "executable_step_count": len(queue),
        "skipped_step_count": len(skipped_steps),
        "queue": queue,
        "skipped_steps": skipped_steps,
        "compose_runs_schema": "rrkal_displaytools.layer_render_plan_compose_runs.v1",
        "compose_runs": compose_runs_packet.get("runs", []),
        "compose_run_count": compose_runs_packet.get("run_count", 0),
        "compose_merge_candidate_run_count": compose_runs_packet.get("merge_candidate_run_count", 0),
        "compose_run_parity_contract_schema": "rrkal_displaytools.layer_render_plan_compose_run_parity_contract.v1",
        "compose_run_parity_contract": compose_run_parity_contract,
        "next_optimization_target": "collapse executable queue into fewer overlay composition passes",
    }


def build_layer_render_plan_compose_queue_entries(
    composition_steps: list[dict[str, object]],
    step_runtime_states: list[dict[str, object]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    queue: list[dict[str, object]] = []
    skipped_steps: list[dict[str, object]] = []
    for index, step in enumerate(composition_steps):
        state = step_runtime_states[index] if index < len(step_runtime_states) and isinstance(step_runtime_states[index], dict) else {}
        if not isinstance(step, dict):
            skipped_steps.append({"source_order": index, "id": "unknown_step", "reason": "malformed_step"})
            continue
        step_id = str(step.get("id") or step.get("layer_id") or f"step_{index}")
        kind = str(step.get("kind") or "")
        if kind == "style_profile_postprocess":
            queued = dict(step)
            queued["source_order"] = index
            queued["queue_order"] = len(queue)
            queued["compose_queue_reason"] = "postprocess_required"
            queue.append(queued)
            continue
        if state.get("visible") is False:
            skipped_steps.append({"source_order": index, "id": step_id, "kind": kind, "reason": "hidden_layer"})
            continue
        if state.get("overlay_present") is not True:
            skipped_steps.append({"source_order": index, "id": step_id, "kind": kind, "reason": "missing_overlay"})
            continue
        if state.get("overlay_transparent") is True:
            skipped_steps.append({"source_order": index, "id": step_id, "kind": kind, "reason": "transparent_overlay"})
            continue
        queued = dict(step)
        queued["source_order"] = index
        queued["queue_order"] = len(queue)
        queued["compose_queue_reason"] = "executable_overlay"
        queue.append(queued)
    return queue, skipped_steps


def build_layer_render_plan_step_runtime_state(
    source_order: int,
    step: dict[str, object] | object,
    *,
    visible: bool | None = True,
    overlay_present: bool | None = None,
    overlay_transparent: bool | None = False,
) -> dict[str, object]:
    if not isinstance(step, dict):
        return {"source_order": source_order, "malformed": True}
    kind = str(step.get("kind") or "")
    if kind == "style_profile_postprocess":
        return {"source_order": source_order, "kind": kind}
    if visible is False:
        return {"source_order": source_order, "kind": kind, "visible": False}
    if overlay_present is not True:
        return {
            "source_order": source_order,
            "kind": kind,
            "visible": True,
            "overlay_present": False,
        }
    return {
        "source_order": source_order,
        "kind": kind,
        "visible": True,
        "overlay_present": True,
        "overlay_transparent": bool(overlay_transparent),
    }


def build_layer_render_plan_compose_queue_packet_from_states(
    composition_steps: list[dict[str, object]],
    step_runtime_states: list[dict[str, object]],
    *,
    source: str = "render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states",
) -> dict[str, object]:
    queue, skipped_steps = build_layer_render_plan_compose_queue_entries(
        composition_steps,
        step_runtime_states,
    )
    compose_runs_packet = build_layer_render_plan_compose_runs(queue)
    runs = compose_runs_packet.get("runs", [])
    compose_run_parity_contract = build_layer_render_plan_compose_run_parity_contract(
        runs if isinstance(runs, list) else []
    )
    return build_layer_render_plan_compose_queue_packet(
        len(composition_steps),
        queue,
        skipped_steps,
        compose_runs_packet,
        compose_run_parity_contract,
        source=source,
    )


def build_layer_render_plan_compose_runs(
    compose_queue: list[dict[str, object]],
    *,
    source: str = "render_core.render_plan.build_layer_render_plan_compose_runs",
) -> dict[str, object]:
    runs: list[dict[str, object]] = []
    current_run: dict[str, object] | None = None
    for step in compose_queue:
        if not isinstance(step, dict):
            continue
        kind = str(step.get("kind") or "unknown")
        step_id = str(step.get("id") or step.get("layer_id") or "unknown_step")
        queue_order = int(step.get("queue_order", len(runs)))
        if kind == "style_profile_postprocess":
            run_kind = "postprocess"
            merge_safe = False
            merge_reason = "full_frame_style_profile_boundary"
        elif kind == "alpha_compose":
            run_kind = "alpha_compose_overlays"
            merge_safe = True
            merge_reason = "adjacent_alpha_compose_overlays_can_be_collapsed_after_visual_parity_check"
        elif kind == "alpha_blend":
            run_kind = "alpha_blend_overlay"
            merge_safe = False
            merge_reason = "blend_mode_specific_overlay_boundary"
        elif kind in {"runtime_blend", "runtime_overlay"}:
            run_kind = "runtime_layer_overlay"
            merge_safe = False
            merge_reason = "preserve_per_layer_visibility_opacity_blend_semantics"
        else:
            run_kind = "unknown_overlay"
            merge_safe = False
            merge_reason = "unknown_runtime_semantics"
        can_extend = (
            current_run is not None
            and current_run.get("run_kind") == run_kind
            and current_run.get("merge_safe") is True
            and merge_safe
        )
        if not can_extend:
            current_run = {
                "id": f"compose_run_{len(runs)}",
                "run_kind": run_kind,
                "merge_safe": merge_safe,
                "merge_reason": merge_reason,
                "start_queue_order": queue_order,
                "end_queue_order": queue_order,
                "step_ids": [],
                "step_count": 0,
                "current_runtime_path": "sequential_compose_queue_execution",
                "next_runtime_path": "merged_overlay_pass" if merge_safe else "preserve_ordered_step_execution",
            }
            runs.append(current_run)
        current_run["end_queue_order"] = queue_order
        step_ids = current_run.get("step_ids")
        if isinstance(step_ids, list):
            step_ids.append(step_id)
        current_run["step_count"] = int(current_run.get("step_count", 0)) + 1
    return {
        "schema": "rrkal_displaytools.layer_render_plan_compose_runs.v1",
        "source": source,
        "status": "ready",
        "run_count": len(runs),
        "merge_candidate_run_count": sum(1 for run in runs if run.get("merge_safe") is True),
        "runs": runs,
        "next_optimization_target": "merge safe adjacent alpha_compose overlays after visual parity smoke is available",
    }


def build_layer_render_plan_compose_run_parity_contract(
    compose_runs: list[dict[str, object]],
    *,
    source: str = "render_core.render_plan.build_layer_render_plan_compose_run_parity_contract",
) -> dict[str, object]:
    merge_candidates = [
        run
        for run in compose_runs
        if isinstance(run, dict) and run.get("merge_safe") is True
    ]
    return {
        "schema": "rrkal_displaytools.layer_render_plan_compose_run_parity_contract.v1",
        "source": source,
        "status": "required_before_runtime_merge" if merge_candidates else "no_merge_candidates",
        "runtime_merge_enabled": False,
        "merge_candidate_run_count": len(merge_candidates),
        "candidate_run_ids": [str(run.get("id")) for run in merge_candidates],
        "compare_method": "sequential_compose_queue_vs_merged_candidate_rgba_diff",
        "required_artifacts": [
            "baseline_sequential_frame_rgba",
            "merged_candidate_frame_rgba",
            "max_abs_diff",
            "changed_pixel_count",
            "renderer_output_metadata",
        ],
        "tolerance": {
            "max_abs_diff": 0,
            "changed_pixel_count": 0,
        },
        "gate": "block_compose_run_merge_until_visual_parity_passes",
        "parity_smoke_schema": "rrkal_displaytools.render_compose_parity_smoke.v1",
        "parity_smoke_script": "scripts\\render_compose_parity_smoke.ps1",
        "parity_smoke_manifest": "state/render_compose_parity_smoke_manifest.json",
        "parity_smoke_default_mode": "contract_only_until_artifacts_then_rgba_diff",
        "parity_smoke_precommit_command": "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\\render_compose_parity_smoke.ps1 -ContractOnly",
        "parity_smoke_validates": ["png_dimensions_match", "max_abs_diff", "changed_pixel_count"],
        "parity_smoke_pass_fields": ["passed", "max_abs_diff", "changed_pixel_count", "diff_status"],
        "recommended_command": "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\\render_compose_parity_smoke.ps1",
        "next_runtime_step": "add an opt-in merged alpha compose path and compare it against the sequential compose queue before enabling it by default",
    }
