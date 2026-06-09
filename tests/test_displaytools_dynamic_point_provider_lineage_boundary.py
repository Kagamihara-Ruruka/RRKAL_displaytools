import unittest


DESCRIPTOR_FIELDS = {
    "surface_name",
    "source_kind",
    "lineage_kind",
    "payload_status",
    "timestamp_status",
    "coordinate_status",
    "provider_policy",
    "blocked_surfaces",
    "fixture_status",
    "forbidden_next_action",
}

DECISION_FIELDS = {
    "provider_lineage_fixture_gate_passed",
    "source_lineage_planning_candidate",
    "selection_render_policy_planning_candidate",
    "source_lineage_extraction_candidate",
    "selection_render_policy_extraction_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "recommended_next_gate",
    "decision_reason",
}

REQUIRED_SURFACES = {
    "ais_source",
    "adsb_source",
    "sql_replay_lineage",
    "websocket_live_lineage",
    "synthetic_source",
    "unavailable_source",
    "stale_timestamp",
    "missing_timestamp",
    "missing_lat_lon",
    "invalid_lat_lon",
    "source_id_label",
    "lineage_status_label",
    "provider_blocked_surface",
    "database_blocked_surface",
    "live_stream_blocked_surface",
    "cache_read_blocked_surface",
}

ALLOWED_FIXTURE_STATUS = {"pinned", "unresolved_static_only", "blocked_runtime_only"}


def descriptor(surface_name, source_kind, lineage_kind, payload_status, timestamp_status, coordinate_status, provider_policy, blocked_surfaces, fixture_status, forbidden_next_action):
    return {
        "surface_name": surface_name,
        "source_kind": source_kind,
        "lineage_kind": lineage_kind,
        "payload_status": payload_status,
        "timestamp_status": timestamp_status,
        "coordinate_status": coordinate_status,
        "provider_policy": provider_policy,
        "blocked_surfaces": list(blocked_surfaces),
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_dynamic_point_provider_lineage_matrix():
    return [
        descriptor(
            "ais_source",
            "AIS",
            "source_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "provider_descriptor_only",
            [],
            "pinned",
            "do_not_execute_ais_provider_or_database_source",
        ),
        descriptor(
            "adsb_source",
            "ADS-B",
            "source_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "provider_descriptor_only",
            [],
            "pinned",
            "do_not_execute_adsb_provider_or_live_source",
        ),
        descriptor(
            "sql_replay_lineage",
            "replay",
            "sql_replay_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "blocked_provider_runtime",
            ["SQL", "MySQL", "pymysql", "sqlalchemy", "replay_query"],
            "blocked_runtime_only",
            "do_not_execute_sql_mysql_pymysql_sqlalchemy_or_replay_query",
        ),
        descriptor(
            "websocket_live_lineage",
            "live_lineage_unresolved",
            "websocket_live_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "blocked_provider_runtime",
            ["WebSocket", "live_AIS", "live_ADSB"],
            "blocked_runtime_only",
            "do_not_open_websocket_live_ais_or_live_adsb",
        ),
        descriptor(
            "synthetic_source",
            "synthetic",
            "synthetic_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "synthetic_descriptor_only",
            [],
            "pinned",
            "do_not_generate_runtime_points_or_render_buffers",
        ),
        descriptor(
            "unavailable_source",
            "unavailable",
            "unavailable_label_only",
            "payload_unavailable",
            "timestamp_unavailable",
            "lat_lon_unavailable",
            "provider_descriptor_only",
            [],
            "pinned",
            "do_not_probe_real_provider_or_cache",
        ),
        descriptor(
            "stale_timestamp",
            "AIS",
            "timestamp_staleness_label_only",
            "payload_shape_label_only",
            "stale_timestamp",
            "lat_lon_label_only",
            "provider_descriptor_only",
            [],
            "unresolved_static_only",
            "do_not_execute_real_clock_or_replay_clock",
        ),
        descriptor(
            "missing_timestamp",
            "AIS",
            "timestamp_missing_label_only",
            "payload_shape_label_only",
            "missing_timestamp",
            "lat_lon_label_only",
            "provider_descriptor_only",
            [],
            "unresolved_static_only",
            "do_not_parse_real_payload_or_query_database",
        ),
        descriptor(
            "missing_lat_lon",
            "AIS",
            "coordinate_missing_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "missing_lat_lon",
            "provider_descriptor_only",
            [],
            "unresolved_static_only",
            "do_not_invoke_projection_or_mask_formula",
        ),
        descriptor(
            "invalid_lat_lon",
            "ADS-B",
            "coordinate_invalid_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "invalid_lat_lon",
            "provider_descriptor_only",
            [],
            "unresolved_static_only",
            "do_not_normalize_real_coordinates_or_invoke_projection",
        ),
        descriptor(
            "source_id_label",
            "AIS",
            "source_id_label_only",
            "id_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "provider_descriptor_only",
            [],
            "pinned",
            "do_not_resolve_real_source_identity_or_database_handle",
        ),
        descriptor(
            "lineage_status_label",
            "AIS",
            "lineage_status_label_only",
            "payload_shape_label_only",
            "timestamp_label_only",
            "lat_lon_label_only",
            "provider_descriptor_only",
            [],
            "pinned",
            "do_not_convert_lineage_label_into_runtime_source",
        ),
        descriptor(
            "provider_blocked_surface",
            "unavailable",
            "provider_blocked_label_only",
            "payload_unavailable",
            "timestamp_unavailable",
            "lat_lon_unavailable",
            "blocked_provider_runtime",
            ["provider_execution"],
            "blocked_runtime_only",
            "do_not_execute_provider_loader_or_source_runtime",
        ),
        descriptor(
            "database_blocked_surface",
            "replay",
            "database_blocked_label_only",
            "payload_unavailable",
            "timestamp_unavailable",
            "lat_lon_unavailable",
            "blocked_provider_runtime",
            ["database_read", "DB_handle", "replay_query"],
            "blocked_runtime_only",
            "do_not_open_database_or_create_db_handle",
        ),
        descriptor(
            "live_stream_blocked_surface",
            "live_lineage_unresolved",
            "live_stream_blocked_label_only",
            "payload_unavailable",
            "timestamp_unavailable",
            "lat_lon_unavailable",
            "blocked_provider_runtime",
            ["websocket", "live_stream_socket"],
            "blocked_runtime_only",
            "do_not_open_socket_or_live_stream",
        ),
        descriptor(
            "cache_read_blocked_surface",
            "unavailable",
            "cache_read_blocked_label_only",
            "payload_unavailable",
            "timestamp_unavailable",
            "lat_lon_unavailable",
            "blocked_provider_runtime",
            ["cache_read", "real_AIS_cache", "real_ADSB_cache"],
            "blocked_runtime_only",
            "do_not_read_real_ais_adsb_cache_or_database",
        ),
    ]


def build_dynamic_point_provider_lineage_decision_output():
    return {
        "provider_lineage_fixture_gate_passed": True,
        "source_lineage_planning_candidate": True,
        "selection_render_policy_planning_candidate": False,
        "source_lineage_extraction_candidate": False,
        "selection_render_policy_extraction_candidate": False,
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "recommended_next_gate": "dynamic_point_source_lineage_source_surface_movement_preimplementation_gate",
        "decision_reason": "provider lineage surfaces have clear descriptor stop lines while selection render policy can wait",
    }


def is_scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def is_packet_data(value):
    if is_scalar(value):
        return True
    if isinstance(value, list):
        return all(is_packet_data(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_packet_data(item) for key, item in value.items())
    return False


class DynamicPointProviderLineageBoundaryFixtureTests(unittest.TestCase):
    def test_fixture_matrix_has_required_surfaces_and_exact_fields(self):
        matrix = build_dynamic_point_provider_lineage_matrix()
        self.assertEqual({entry["surface_name"] for entry in matrix}, REQUIRED_SURFACES)
        for entry in matrix:
            self.assertEqual(set(entry), DESCRIPTOR_FIELDS)
            self.assertIn(entry["fixture_status"], ALLOWED_FIXTURE_STATUS)

    def test_matrix_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_dynamic_point_provider_lineage_matrix()))
        self.assertTrue(is_packet_data(build_dynamic_point_provider_lineage_decision_output()))

    def test_runtime_blocked_surfaces_are_explicitly_blocked(self):
        matrix = build_dynamic_point_provider_lineage_matrix()
        blocked = {entry["surface_name"]: entry for entry in matrix if entry["fixture_status"] == "blocked_runtime_only"}
        for surface in [
            "sql_replay_lineage",
            "websocket_live_lineage",
            "provider_blocked_surface",
            "database_blocked_surface",
            "live_stream_blocked_surface",
            "cache_read_blocked_surface",
        ]:
            self.assertIn(surface, blocked)
            self.assertTrue(blocked[surface]["blocked_surfaces"])
            self.assertIn("do_not", blocked[surface]["forbidden_next_action"])

    def test_timestamp_and_coordinate_faults_remain_static_only(self):
        matrix = {entry["surface_name"]: entry for entry in build_dynamic_point_provider_lineage_matrix()}
        for surface in ["stale_timestamp", "missing_timestamp", "missing_lat_lon", "invalid_lat_lon"]:
            self.assertEqual(matrix[surface]["fixture_status"], "unresolved_static_only")
        self.assertEqual(matrix["stale_timestamp"]["timestamp_status"], "stale_timestamp")
        self.assertEqual(matrix["missing_lat_lon"]["coordinate_status"], "missing_lat_lon")
        self.assertEqual(matrix["invalid_lat_lon"]["coordinate_status"], "invalid_lat_lon")

    def test_decision_output_is_pinned(self):
        decision = build_dynamic_point_provider_lineage_decision_output()
        self.assertEqual(set(decision), DECISION_FIELDS)
        self.assertTrue(decision["provider_lineage_fixture_gate_passed"])
        self.assertTrue(decision["source_lineage_planning_candidate"])
        self.assertFalse(decision["selection_render_policy_planning_candidate"])
        self.assertFalse(decision["source_lineage_extraction_candidate"])
        self.assertFalse(decision["selection_render_policy_extraction_candidate"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_source_lineage_source_surface_movement_preimplementation_gate",
        )

    def test_no_monolith_runtime_or_readiness_claims(self):
        packet_text = repr(build_dynamic_point_provider_lineage_matrix()) + repr(build_dynamic_point_provider_lineage_decision_output())
        for marker in [
            "taichi_global_bathymetry",
            "datashader_runtime_imported",
            "bug_fixed",
            "readiness_claimed",
            "live_data_restored",
            "safe_to_extract",
            "visual_parity_ready",
            "performance_ready",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
