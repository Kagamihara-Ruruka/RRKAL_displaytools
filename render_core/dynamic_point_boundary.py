from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "sql_live_source_execution_allowed": False,
    "dataframe_runtime_allowed": False,
    "projection_formula_allowed": False,
    "controller_selection_runtime_allowed": False,
    "renderer_runtime_allowed": False,
}


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def build_dynamic_point_source_descriptor(source_kind: str = "AIS") -> dict[str, object]:
    normalized = source_kind if source_kind in {"AIS", "ADS-B", "replay", "synthetic", "unavailable"} else "unavailable"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.source_descriptor.v1",
            "descriptor_kind": "dynamic_point_source_descriptor",
            "source_kind": normalized,
            "source_evidence": [
                "AIS source label",
                "ADS-B source label",
                "replay source label",
                "synthetic source label",
                "unavailable source label",
            ],
            "lineage_policy": "descriptor_label_only",
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_sql_websocket_live_source_or_cache_read",
        }
    )


def build_dynamic_point_payload_shape_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.payload_shape_descriptor.v1",
            "descriptor_kind": "dynamic_point_payload_shape_descriptor",
            "payload_fields": [
                "lat",
                "lon",
                "speed",
                "heading",
                "timestamp",
                "id",
            ],
            "coordinate_payload_kind": "raw_lon_lat_label_only",
            "payload_runtime_parsed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_parse_real_ais_adsb_or_dataframe_payload",
        }
    )


def build_dynamic_point_replay_live_lineage_descriptor(lineage: str = "live_lineage_unresolved") -> dict[str, object]:
    normalized = lineage if lineage in {"replay", "live_lineage_unresolved", "synthetic", "unavailable"} else "unavailable"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.replay_live_lineage_descriptor.v1",
            "descriptor_kind": "dynamic_point_replay_live_lineage_descriptor",
            "lineage_label": normalized,
            "lineage_status": "unresolved_static_only",
            "real_clock_execution_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_replay_query_websocket_or_real_clock",
        }
    )


def build_dynamic_point_selection_label_descriptor(selection_label: str = "selected_vehicle") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.selection_label_descriptor.v1",
            "descriptor_kind": "dynamic_point_selection_label_descriptor",
            "selection_label": selection_label,
            "selection_policy": "label_only",
            "selection_runtime_mutated": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_mutate_controller_selection_picker_or_hit_test",
        }
    )


def build_dynamic_point_render_policy_label_descriptor(policy_label: str = "visible_count_cap") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.render_policy_label_descriptor.v1",
            "descriptor_kind": "dynamic_point_render_policy_label_descriptor",
            "policy_label": policy_label,
            "render_policy_labels": [
                "visible_count",
                "rendered_count",
                "cap",
                "adaptive_sampling_label",
            ],
            "render_runtime_invoked": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_datashader_or_renderer_runtime",
        }
    )


def build_dynamic_point_safety_ledger_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.safety_ledger_descriptor.v1",
            "descriptor_kind": "dynamic_point_safety_ledger_descriptor",
            "fixture_status": "blocked_runtime_only",
            "blocked_surfaces": [
                "SQL replay database",
                "WebSocket live source",
                "pandas datashader numpy runtime",
                "projection flip mask formula",
                "controller selection runtime",
                "renderer host runtime",
                "metadata artifact writer",
            ],
            "runtime_dependency_allowed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_weaken_sql_websocket_datashader_runtime_stop_lines",
        }
    )


def build_dynamic_point_known_fault_ledger_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point.known_fault_ledger_descriptor.v1",
            "descriptor_kind": "dynamic_point_known_fault_ledger_descriptor",
            "fixture_status": "unresolved_static_only",
            "known_faults": [
                "live_vs_replay_ambiguity",
                "timestamp_staleness",
                "point_vector_sync_dependency",
                "selection_runtime_boundary_unresolved",
            ],
            "live_data_restored": False,
            "bug_fixed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_claim_live_data_bug_fix_or_visual_parity",
        }
    )


def dynamic_point_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point.boundary_descriptor.v1",
        "descriptor_kind": "dynamic_point_boundary_descriptor",
        "source_descriptor": build_dynamic_point_source_descriptor(),
        "payload_shape_descriptor": build_dynamic_point_payload_shape_descriptor(),
        "replay_live_lineage_descriptor": build_dynamic_point_replay_live_lineage_descriptor(),
        "selection_label_descriptor": build_dynamic_point_selection_label_descriptor(),
        "render_policy_label_descriptor": build_dynamic_point_render_policy_label_descriptor(),
        "safety_ledger_descriptor": build_dynamic_point_safety_ledger_descriptor(),
        "known_fault_ledger_descriptor": build_dynamic_point_known_fault_ledger_descriptor(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "live_data_restored": False,
        "forbidden_next_action": "do_not_include_sql_live_dataframe_projection_controller_or_runtime_behavior",
    }


def dynamic_point_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point.planning_bundle.v1",
        "descriptor_kind": "dynamic_point_planning_bundle",
        "target_candidate": "render_core/dynamic_point_boundary.py",
        "boundary_descriptor": dynamic_point_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "blocked_surfaces": [
            "sql_replay_database",
            "live_stream",
            "runtime_dataframe_projection",
            "controller_selection_runtime",
            "renderer_host",
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
        "forbidden_next_action": "do_not_authorize_source_movement_inside_bundle",
    }
