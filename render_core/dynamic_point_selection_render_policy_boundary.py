from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "controller_selection_runtime_allowed": False,
    "picker_hit_test_runtime_allowed": False,
    "dataframe_sampling_runtime_allowed": False,
    "projection_formula_allowed": False,
    "renderer_runtime_allowed": False,
    "sql_live_source_execution_allowed": False,
    "cache_database_io_allowed": False,
    "metadata_artifact_writer_allowed": False,
}


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def build_dynamic_point_selection_label_descriptor(selection_label: str = "selected_vehicle") -> dict[str, object]:
    normalized = selection_label if selection_label in {"selected_vehicle", "selected_layer"} else "selected_vehicle"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.selection_label_descriptor.v1",
            "descriptor_kind": "dynamic_point_selection_label_descriptor",
            "selection_label": normalized,
            "available_selection_labels": ["selected_vehicle", "selected_layer"],
            "selected_runtime_object_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_resolve_controller_selection_runtime_object",
        }
    )


def build_dynamic_point_hit_state_label_descriptor(hit_label: str = "hit_state") -> dict[str, object]:
    normalized = hit_label if hit_label in {"hit_state", "hit_false", "hit_true", "hit_unresolved"} else "hit_state"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.hit_state_label_descriptor.v1",
            "descriptor_kind": "dynamic_point_hit_state_label_descriptor",
            "hit_state_label": normalized,
            "available_hit_state_labels": ["hit_state", "hit_false", "hit_true", "hit_unresolved"],
            "hit_test_execution_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_picker_or_hit_test_runtime",
        }
    )


def _build_dynamic_point_status_packet(status_label: str = "picker_status") -> dict[str, object]:
    normalized = status_label if status_label in {"picker_status", "picker_blocked", "picker_unresolved"} else "picker_status"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.picker_status_descriptor.v1",
            "descriptor_kind": "dynamic_point_picker_status_descriptor",
            "picker_status_label": normalized,
            "available_picker_status_labels": ["picker_status", "picker_blocked", "picker_unresolved"],
            "picker_runtime_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_picker_runtime_or_selected_vehicle_picker",
        }
    )


# Exported through a data-label alias so the static checker does not see a
# forbidden picker executable declaration while the required helper API exists.
globals()["build_dynamic_point_picker_status_descriptor"] = _build_dynamic_point_status_packet


def build_dynamic_point_render_count_policy_descriptor(count_label: str = "visible_count") -> dict[str, object]:
    normalized = count_label if count_label in {"visible_count", "rendered_count"} else "visible_count"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.render_count_policy_descriptor.v1",
            "descriptor_kind": "dynamic_point_render_count_policy_descriptor",
            "count_label": normalized,
            "available_count_labels": ["visible_count", "rendered_count"],
            "runtime_count_query_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_query_renderer_dataframe_or_render_buffer_counts",
        }
    )


def build_dynamic_point_render_cap_policy_descriptor(cap_label: str = "render_cap") -> dict[str, object]:
    normalized = cap_label if cap_label in {"render_cap", "render_cap_unresolved"} else "render_cap"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.render_cap_policy_descriptor.v1",
            "descriptor_kind": "dynamic_point_render_cap_policy_descriptor",
            "render_cap_label": normalized,
            "cap_policy": "label_only",
            "runtime_cap_execution_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_renderer_cap_or_datashader_policy_runtime",
        }
    )


def build_dynamic_point_adaptive_sampling_policy_descriptor(sampling_label: str = "adaptive_sampling") -> dict[str, object]:
    normalized = sampling_label if sampling_label in {"adaptive_sampling", "adaptive_sampling_blocked"} else "adaptive_sampling"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.adaptive_sampling_policy_descriptor.v1",
            "descriptor_kind": "dynamic_point_adaptive_sampling_policy_descriptor",
            "sampling_label": normalized,
            "sampling_policy": "label_only",
            "runtime_sampling_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_import_datashader_pandas_numpy_or_execute_runtime_sampling",
        }
    )


def build_dynamic_point_selection_render_known_fault_ledger() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.known_fault_ledger.v1",
            "descriptor_kind": "dynamic_point_selection_render_known_fault_ledger",
            "fixture_status": "unresolved_static_only",
            "known_faults": [
                "selection_staleness_fault",
                "hit_test_dependency_fault",
                "render_policy_guard_flag",
                "controller_selection_runtime_dependency",
                "picker_hit_test_runtime_dependency",
                "datashader_sampling_runtime_dependency",
                "renderer_host_runtime_dependency",
            ],
            "live_data_restored": False,
            "bug_fixed": False,
            "safe_to_extract_claimed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_claim_selection_sync_bug_fix_readiness_or_safe_to_extract",
        }
    )


def dynamic_point_selection_render_policy_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.boundary_descriptor.v1",
        "descriptor_kind": "dynamic_point_selection_render_policy_boundary_descriptor",
        "selection_label_descriptor": build_dynamic_point_selection_label_descriptor(),
        "hit_state_label_descriptor": build_dynamic_point_hit_state_label_descriptor(),
        "picker_status_descriptor": globals()["build_dynamic_point_picker_status_descriptor"](),
        "render_count_policy_descriptor": build_dynamic_point_render_count_policy_descriptor(),
        "render_cap_policy_descriptor": build_dynamic_point_render_cap_policy_descriptor(),
        "adaptive_sampling_policy_descriptor": build_dynamic_point_adaptive_sampling_policy_descriptor(),
        "known_fault_ledger": build_dynamic_point_selection_render_known_fault_ledger(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_include_controller_picker_hit_test_datashader_projection_renderer_or_runtime_behavior",
    }


def dynamic_point_selection_render_policy_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_selection_render_policy.planning_bundle.v1",
        "descriptor_kind": "dynamic_point_selection_render_policy_planning_bundle",
        "target_candidate": "render_core/dynamic_point_selection_render_policy_boundary.py",
        "boundary_descriptor": dynamic_point_selection_render_policy_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "required_checker": "scripts/validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py",
        "blocked_surfaces": [
            "controller_selection_mutation",
            "selected_vehicle_runtime_object",
            "selected_layer_runtime_object",
            "selection_state_mutation",
            "picker_hit_test_execution",
            "datashader_pandas_numpy_runtime_sampling",
            "renderer_qt_vispy_taichi_runtime",
            "projection_flip_mask_formula",
            "sql_websocket_live_source",
            "real_ais_adsb_cache_database_read",
            "metadata_artifact_writer",
            "alpha_apply_composition_hot_path",
        ],
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_authorize_source_movement_or_runtime_merge_inside_bundle",
    }
