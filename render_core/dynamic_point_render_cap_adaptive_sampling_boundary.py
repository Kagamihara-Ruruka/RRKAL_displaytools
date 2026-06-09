from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "runtime_sampling_allowed": False,
    "dataframe_runtime_allowed": False,
    "renderer_runtime_allowed": False,
    "projection_formula_allowed": False,
    "controller_selection_runtime_allowed": False,
    "sql_live_source_execution_allowed": False,
    "cache_database_io_allowed": False,
    "metadata_artifact_writer_allowed": False,
}

VISIBLE_COUNT_LABELS = ["visible_count", "below_cap", "equals_cap", "exceeds_cap", "unknown"]
RENDERED_COUNT_LABELS = ["rendered_count", "lower_than_visible", "equals_visible", "unknown"]
RENDER_CAP_LABELS = ["render_cap", "cap_enabled", "cap_disabled", "cap_unknown"]
ADAPTIVE_SAMPLING_LABELS = ["adaptive_sampling", "enabled", "disabled", "degraded"]
SAMPLING_DEPENDENCY_LABELS = [
    "datashader_runtime_dependency",
    "pandas_numpy_runtime_dependency",
    "renderer_runtime_dependency",
    "selection_policy_dependency",
    "payload_quality_dependency",
]
KNOWN_FAULTS = [
    "cap_exceeded_without_runtime_count_parity",
    "adaptive_sampling_degraded_without_datashader_runtime",
    "selection_payload_dependency_unproven",
]
BLOCKED_SURFACES = [
    "datashader_runtime_dependency",
    "pandas_numpy_runtime_dependency",
    "renderer_runtime_dependency",
    "projection_flip_mask_formula",
    "controller_selection_picker_hit_test_mutation",
    "sql_websocket_live_source",
    "metadata_artifact_writer",
    "alpha_apply_composition_hot_path",
]


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def _normalize(label: str, allowed: list[str], fallback: str) -> str:
    return label if label in allowed else fallback


def build_dynamic_point_visible_count_descriptor(visible_count: str = "visible_count") -> dict[str, object]:
    label = _normalize(visible_count, VISIBLE_COUNT_LABELS, "visible_count")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.visible_count_descriptor.v1",
            "descriptor_kind": "dynamic_point_visible_count_descriptor",
            "visible_count": label,
            "available_count_labels": list(VISIBLE_COUNT_LABELS),
            "runtime_count_query_used": False,
            "allowed_content_kind": "dict_list_scalar_descriptor_only",
            "forbidden_next_action": "do_not_query_renderer_visible_count",
        }
    )


def build_dynamic_point_rendered_count_descriptor(rendered_count: str = "rendered_count") -> dict[str, object]:
    label = _normalize(rendered_count, RENDERED_COUNT_LABELS, "rendered_count")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.rendered_count_descriptor.v1",
            "descriptor_kind": "dynamic_point_rendered_count_descriptor",
            "rendered_count": label,
            "available_count_labels": list(RENDERED_COUNT_LABELS),
            "runtime_count_query_used": False,
            "allowed_content_kind": "dict_list_scalar_descriptor_only",
            "forbidden_next_action": "do_not_query_renderer_rendered_count",
        }
    )


def build_dynamic_point_render_cap_policy_descriptor(render_cap: str = "render_cap") -> dict[str, object]:
    label = _normalize(render_cap, RENDER_CAP_LABELS, "render_cap")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.render_cap_policy_descriptor.v1",
            "descriptor_kind": "dynamic_point_render_cap_policy_descriptor",
            "render_cap": label,
            "cap_policy_labels": list(RENDER_CAP_LABELS),
            "runtime_cap_execution_used": False,
            "allowed_content_kind": "dict_list_scalar_policy_label_only",
            "forbidden_next_action": "do_not_execute_render_cap_runtime",
        }
    )


def build_dynamic_point_adaptive_sampling_policy_descriptor(adaptive_sampling: str = "adaptive_sampling") -> dict[str, object]:
    label = _normalize(adaptive_sampling, ADAPTIVE_SAMPLING_LABELS, "adaptive_sampling")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.adaptive_sampling_policy_descriptor.v1",
            "descriptor_kind": "dynamic_point_adaptive_sampling_policy_descriptor",
            "adaptive_sampling": label,
            "sampling_policy_labels": list(ADAPTIVE_SAMPLING_LABELS),
            "runtime_sampling_used": False,
            "allowed_content_kind": "dict_list_scalar_policy_label_only",
            "forbidden_next_action": "do_not_execute_adaptive_sampling_runtime",
        }
    )


def build_dynamic_point_sampling_dependency_descriptor(sampling_dependency: str = "datashader_runtime_dependency") -> dict[str, object]:
    label = _normalize(sampling_dependency, SAMPLING_DEPENDENCY_LABELS, "datashader_runtime_dependency")
    classification = "adjacent_descriptor_dependency" if label in {"selection_policy_dependency", "payload_quality_dependency"} else "blocked_runtime_only"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.sampling_dependency_descriptor.v1",
            "descriptor_kind": "dynamic_point_sampling_dependency_descriptor",
            "sampling_dependency": label,
            "dependency_classification": classification,
            "dependency_labels": list(SAMPLING_DEPENDENCY_LABELS),
            "runtime_dependency_executed": False,
            "allowed_content_kind": "dict_list_scalar_dependency_label_only",
            "forbidden_next_action": "do_not_execute_datashader_dataframe_renderer_or_adjacent_runtime",
        }
    )


def build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.known_fault_ledger.v1",
            "descriptor_kind": "dynamic_point_render_cap_adaptive_sampling_known_fault_ledger",
            "fixture_status": "unresolved_static_only",
            "known_faults": list(KNOWN_FAULTS),
            "blocked_surfaces": list(BLOCKED_SURFACES),
            "render_cap_adaptive_sampling_extraction_candidate": False,
            "live_data_restored": False,
            "bug_fixed": False,
            "safe_to_extract_claimed": False,
            "allowed_content_kind": "dict_list_scalar_fault_ledger_only",
            "forbidden_next_action": "do_not_claim_runtime_sampling_renderer_or_count_behavior_fixed",
        }
    )


def dynamic_point_render_cap_adaptive_sampling_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.boundary_descriptor.v1",
        "descriptor_kind": "dynamic_point_render_cap_adaptive_sampling_boundary_descriptor",
        "visible_count_descriptor": build_dynamic_point_visible_count_descriptor(),
        "rendered_count_descriptor": build_dynamic_point_rendered_count_descriptor(),
        "render_cap_policy_descriptor": build_dynamic_point_render_cap_policy_descriptor(),
        "adaptive_sampling_policy_descriptor": build_dynamic_point_adaptive_sampling_policy_descriptor(),
        "sampling_dependency_descriptor": build_dynamic_point_sampling_dependency_descriptor(),
        "known_fault_ledger": build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "readiness_claimed": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_execute_runtime_sampling_renderer_controller_or_projection",
    }


def dynamic_point_render_cap_adaptive_sampling_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling.planning_bundle.v1",
        "descriptor_kind": "dynamic_point_render_cap_adaptive_sampling_planning_bundle",
        "target_candidate": "render_core/dynamic_point_render_cap_adaptive_sampling_boundary.py",
        "boundary_descriptor": dynamic_point_render_cap_adaptive_sampling_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "helper_module_creation_authorized": True,
        "render_cap_adaptive_sampling_extraction_candidate": False,
        "required_checker": "scripts/validate_displaytools_dynamic_point_render_cap_adaptive_sampling_import_boundary.py",
        "blocked_surfaces": list(BLOCKED_SURFACES),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "readiness_claimed": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_move_runtime_sampling_datashader_dataframe_renderer_or_projection",
    }
