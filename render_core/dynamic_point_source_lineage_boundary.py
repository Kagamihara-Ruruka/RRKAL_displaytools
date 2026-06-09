from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "sql_live_source_execution_allowed": False,
    "cache_database_io_allowed": False,
    "dataframe_runtime_allowed": False,
    "projection_formula_allowed": False,
    "controller_selection_runtime_allowed": False,
    "renderer_runtime_allowed": False,
}


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def build_dynamic_point_source_lineage_descriptor(source_label: str = "ais_source") -> dict[str, object]:
    normalized = source_label if source_label in {"ais_source", "adsb_source", "synthetic_source", "unavailable_source"} else "unavailable_source"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.source_lineage_descriptor.v1",
            "descriptor_kind": "dynamic_point_source_lineage_descriptor",
            "source_label": normalized,
            "lineage_label": "lineage_status",
            "available_source_labels": [
                "ais_source",
                "adsb_source",
                "synthetic_source",
                "unavailable_source",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_sql_websocket_cache_database_or_live_source",
        }
    )


def build_dynamic_point_replay_lineage_label_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.replay_lineage_label_descriptor.v1",
            "descriptor_kind": "dynamic_point_replay_lineage_label_descriptor",
            "lineage_label": "sql_replay_lineage",
            "lineage_status": "blocked_runtime_peer",
            "provider_execution_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_database_replay_or_query_runtime",
        }
    )


def build_dynamic_point_live_lineage_label_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.live_lineage_label_descriptor.v1",
            "descriptor_kind": "dynamic_point_live_lineage_label_descriptor",
            "lineage_label": "websocket_live_lineage",
            "lineage_status": "unresolved_static_only",
            "provider_execution_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_open_live_stream_or_socket_runtime",
        }
    )


def build_dynamic_point_source_availability_descriptor(availability_label: str = "unavailable_source") -> dict[str, object]:
    normalized = availability_label if availability_label in {"ais_source", "adsb_source", "synthetic_source", "unavailable_source"} else "unavailable_source"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.source_availability_descriptor.v1",
            "descriptor_kind": "dynamic_point_source_availability_descriptor",
            "availability_label": normalized,
            "availability_policy": "label_only",
            "source_probe_performed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_probe_real_provider_cache_database_or_network",
        }
    )


def build_dynamic_point_timestamp_quality_descriptor(timestamp_quality: str = "timestamp_quality") -> dict[str, object]:
    normalized = timestamp_quality if timestamp_quality in {"timestamp_quality", "stale_timestamp", "missing_timestamp"} else "timestamp_quality"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.timestamp_quality_descriptor.v1",
            "descriptor_kind": "dynamic_point_timestamp_quality_descriptor",
            "timestamp_quality": normalized,
            "quality_branches": ["timestamp_quality", "stale_timestamp", "missing_timestamp"],
            "real_clock_execution_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_real_clock_replay_clock_or_database_runtime",
        }
    )


def build_dynamic_point_coordinate_payload_quality_descriptor(coordinate_quality: str = "coordinate_payload_quality") -> dict[str, object]:
    normalized = coordinate_quality if coordinate_quality in {"coordinate_payload_quality", "missing_lat_lon", "invalid_lat_lon"} else "coordinate_payload_quality"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.coordinate_payload_quality_descriptor.v1",
            "descriptor_kind": "dynamic_point_coordinate_payload_quality_descriptor",
            "coordinate_payload_quality": normalized,
            "quality_branches": ["coordinate_payload_quality", "missing_lat_lon", "invalid_lat_lon"],
            "projection_runtime_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_invoke_projection_flip_mask_or_dataframe_runtime",
        }
    )


def build_dynamic_point_source_lineage_known_fault_ledger() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_source_lineage.known_fault_ledger.v1",
            "descriptor_kind": "dynamic_point_source_lineage_known_fault_ledger",
            "fixture_status": "unresolved_static_only",
            "known_faults": [
                "live_vs_replay_ambiguity",
                "timestamp_staleness",
                "source_identity_unresolved",
                "coordinate_payload_quality_unresolved",
            ],
            "live_data_restored": False,
            "bug_fixed": False,
            "safe_to_extract_claimed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_claim_live_data_bug_fix_readiness_or_safe_to_extract",
        }
    )


def dynamic_point_source_lineage_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_source_lineage.boundary_descriptor.v1",
        "descriptor_kind": "dynamic_point_source_lineage_boundary_descriptor",
        "source_lineage_descriptor": build_dynamic_point_source_lineage_descriptor(),
        "replay_lineage_label_descriptor": build_dynamic_point_replay_lineage_label_descriptor(),
        "live_lineage_label_descriptor": build_dynamic_point_live_lineage_label_descriptor(),
        "source_availability_descriptor": build_dynamic_point_source_availability_descriptor(),
        "timestamp_quality_descriptor": build_dynamic_point_timestamp_quality_descriptor(),
        "coordinate_payload_quality_descriptor": build_dynamic_point_coordinate_payload_quality_descriptor(),
        "known_fault_ledger": build_dynamic_point_source_lineage_known_fault_ledger(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_include_sql_live_cache_database_dataframe_projection_controller_or_runtime_behavior",
    }


def dynamic_point_source_lineage_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_source_lineage.planning_bundle.v1",
        "descriptor_kind": "dynamic_point_source_lineage_planning_bundle",
        "target_candidate": "render_core/dynamic_point_source_lineage_boundary.py",
        "boundary_descriptor": dynamic_point_source_lineage_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "required_checker": "scripts/validate_displaytools_dynamic_point_source_lineage_import_boundary.py",
        "blocked_surfaces": [
            "sql_replay_database",
            "live_stream",
            "cache_database_io",
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
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_authorize_source_movement_inside_bundle",
    }
