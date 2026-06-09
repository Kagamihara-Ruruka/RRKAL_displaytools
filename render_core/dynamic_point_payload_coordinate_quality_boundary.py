from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "sql_live_source_execution_allowed": False,
    "cache_database_io_allowed": False,
    "dataframe_runtime_allowed": False,
    "projection_formula_allowed": False,
    "controller_selection_runtime_allowed": False,
    "renderer_runtime_allowed": False,
    "metadata_artifact_writer_allowed": False,
}

PAYLOAD_FIELDS = ["lat", "lon", "timestamp", "source_id", "speed", "heading"]
QUALITY_LABELS = ["valid", "missing", "invalid", "stale", "unknown"]
COORDINATE_LABELS = ["coordinate_quality", "missing_lat_lon", "invalid_lat_lon", "out_of_range_lat_lon", "zero_coordinate_candidate", "anti_meridian_candidate"]
TIMESTAMP_LABELS = ["timestamp_quality", "missing_timestamp", "stale_timestamp", "future_timestamp_candidate", "timezone_ambiguity"]
SOURCE_ID_LABELS = ["source_id_quality", "missing_id", "synthetic_id", "AIS_id", "ADS-B_id"]
SPEED_HEADING_LABELS = ["speed_heading_quality", "missing_speed", "missing_heading", "invalid_speed", "invalid_heading", "unknown"]
KNOWN_FAULTS = ["timestamp_staleness", "coordinate_payload_ambiguity", "point_vector_sync_dependency"]
BLOCKED_SURFACES = [
    "projection_dependency",
    "live_source_dependency",
    "controller_selection_dependency",
    "renderer_runtime_dependency",
    "pandas_datashader_numpy_runtime",
    "metadata_artifact_writer",
    "alpha_apply_composition_hot_path",
]


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def _normalize(label: str, allowed: list[str], fallback: str) -> str:
    return label if label in allowed else fallback


def build_dynamic_point_payload_shape_descriptor(payload_shape: str = "payload_shape") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.payload_shape_descriptor.v1",
            "descriptor_kind": "dynamic_point_payload_shape_descriptor",
            "payload_shape": "payload_shape" if payload_shape != "unknown" else "unknown",
            "payload_fields": list(PAYLOAD_FIELDS),
            "quality_labels": list(QUALITY_LABELS),
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_read_real_ais_adsb_database_cache_or_dataframe_payload",
        }
    )


def build_dynamic_point_coordinate_quality_descriptor(coordinate_quality: str = "coordinate_quality") -> dict[str, object]:
    normalized = _normalize(coordinate_quality, COORDINATE_LABELS, "coordinate_quality")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.coordinate_quality_descriptor.v1",
            "descriptor_kind": "dynamic_point_coordinate_quality_descriptor",
            "coordinate_quality": normalized,
            "quality_branches": list(COORDINATE_LABELS),
            "known_fault_refs": ["coordinate_payload_ambiguity", "point_vector_sync_dependency"],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_projection_flip_mask_or_point_vector_sync_runtime",
        }
    )


def build_dynamic_point_timestamp_quality_descriptor(timestamp_quality: str = "timestamp_quality") -> dict[str, object]:
    normalized = _normalize(timestamp_quality, TIMESTAMP_LABELS, "timestamp_quality")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.timestamp_quality_descriptor.v1",
            "descriptor_kind": "dynamic_point_timestamp_quality_descriptor",
            "timestamp_quality": normalized,
            "quality_branches": list(TIMESTAMP_LABELS),
            "real_clock_execution_used": False,
            "known_fault_refs": ["timestamp_staleness"],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_live_clock_replay_clock_database_or_timezone_runtime",
        }
    )


def build_dynamic_point_source_id_quality_descriptor(source_id_quality: str = "source_id_quality") -> dict[str, object]:
    normalized = _normalize(source_id_quality, SOURCE_ID_LABELS, "source_id_quality")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.source_id_quality_descriptor.v1",
            "descriptor_kind": "dynamic_point_source_id_quality_descriptor",
            "source_id_quality": normalized,
            "quality_branches": list(SOURCE_ID_LABELS),
            "source_lookup_performed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_probe_live_source_database_cache_or_identity_runtime",
        }
    )


def build_dynamic_point_speed_heading_quality_descriptor(speed_heading_quality: str = "speed_heading_quality") -> dict[str, object]:
    normalized = _normalize(speed_heading_quality, SPEED_HEADING_LABELS, "speed_heading_quality")
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.speed_heading_quality_descriptor.v1",
            "descriptor_kind": "dynamic_point_speed_heading_quality_descriptor",
            "speed_heading_quality": normalized,
            "quality_branches": list(SPEED_HEADING_LABELS),
            "runtime_sampling_used": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_datashader_renderer_speed_or_heading_runtime",
        }
    )


def build_dynamic_point_payload_coordinate_quality_known_fault_ledger() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.known_fault_ledger.v1",
            "descriptor_kind": "dynamic_point_payload_coordinate_quality_known_fault_ledger",
            "fixture_status": "unresolved_static_only",
            "known_faults": list(KNOWN_FAULTS),
            "blocked_surfaces": list(BLOCKED_SURFACES),
            "payload_coordinate_quality_extraction_candidate": False,
            "live_data_restored": False,
            "bug_fixed": False,
            "safe_to_extract_claimed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_claim_projection_live_data_readiness_bug_fix_or_safe_to_extract",
        }
    )


def dynamic_point_payload_coordinate_quality_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.boundary_descriptor.v1",
        "descriptor_kind": "dynamic_point_payload_coordinate_quality_boundary_descriptor",
        "payload_shape_descriptor": build_dynamic_point_payload_shape_descriptor(),
        "coordinate_quality_descriptor": build_dynamic_point_coordinate_quality_descriptor(),
        "timestamp_quality_descriptor": build_dynamic_point_timestamp_quality_descriptor(),
        "source_id_quality_descriptor": build_dynamic_point_source_id_quality_descriptor(),
        "speed_heading_quality_descriptor": build_dynamic_point_speed_heading_quality_descriptor(),
        "known_fault_ledger": build_dynamic_point_payload_coordinate_quality_known_fault_ledger(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "readiness_claimed": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_include_projection_live_source_database_dataframe_controller_renderer_or_runtime_behavior",
    }


def dynamic_point_payload_coordinate_quality_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality.planning_bundle.v1",
        "descriptor_kind": "dynamic_point_payload_coordinate_quality_planning_bundle",
        "target_candidate": "render_core/dynamic_point_payload_coordinate_quality_boundary.py",
        "boundary_descriptor": dynamic_point_payload_coordinate_quality_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "helper_module_creation_authorized": True,
        "payload_coordinate_quality_extraction_candidate": False,
        "required_checker": "scripts/validate_displaytools_dynamic_point_payload_coordinate_quality_import_boundary.py",
        "blocked_surfaces": list(BLOCKED_SURFACES),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "readiness_claimed": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "live_data_restored": False,
        "safe_to_extract_claimed": False,
        "forbidden_next_action": "do_not_authorize_runtime_source_movement_or_big_A_extraction_inside_bundle",
    }