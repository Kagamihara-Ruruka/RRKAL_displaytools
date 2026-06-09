import unittest


PIN_FIELDS = {
    "pin_name",
    "ablation_modes",
    "consumer_expectation",
    "rollback_method",
    "dependency_classification",
    "fixture_status",
    "forbidden_next_action",
}

BOUNDARY_FILL_KEYS = {
    "future_helper_target",
    "descriptor_candidate_families",
    "blocked_runtime_surfaces",
    "import_boundary_checker_needed",
    "existing_checker_reusable",
    "new_checker_required",
    "source_lineage_planning_candidate",
    "source_lineage_extraction_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "checker_decision_reason",
}

REQUIRED_PINS = {
    "ais_source_label",
    "adsb_source_label",
    "sql_replay_lineage_label",
    "websocket_live_lineage_label",
    "synthetic_source_label",
    "unavailable_source_label",
    "timestamp_quality_label",
    "coordinate_payload_quality_label",
    "source_id_label",
    "lineage_status_label",
    "provider_runtime_dependency",
    "database_runtime_dependency",
    "live_stream_runtime_dependency",
    "cache_io_runtime_dependency",
    "dataframe_projection_runtime_dependency",
}

REQUIRED_ABLATION_MODES = {"null_mode", "tripwire_mode", "trace_mode", "substitute_mode"}

REQUIRED_CANDIDATE_FAMILIES = [
    "build_dynamic_point_source_lineage_descriptor",
    "build_dynamic_point_replay_lineage_label_descriptor",
    "build_dynamic_point_live_lineage_label_descriptor",
    "build_dynamic_point_source_availability_descriptor",
    "build_dynamic_point_timestamp_quality_descriptor",
    "build_dynamic_point_coordinate_payload_quality_descriptor",
    "build_dynamic_point_source_lineage_known_fault_ledger",
    "dynamic_point_source_lineage_boundary_descriptor",
    "dynamic_point_source_lineage_planning_bundle",
]

REQUIRED_BLOCKED_SURFACES = [
    "SQL / MySQL / pymysql / sqlalchemy / DB URL / replay query execution",
    "WebSocket / live AIS / live ADS-B stream execution",
    "real AIS / ADS-B / cache / database read",
    "pandas / datashader / numpy runtime",
    "projection / flip / mask formula",
    "controller selection / picker / hit-test mutation",
    "renderer / Qt / VisPy / Taichi runtime",
    "metadata / artifact writer",
    "alpha / apply / composition hot path",
    "readiness / performance / visual parity / bug-fix / live-data claims",
]


def pin(pin_name, consumer_expectation, rollback_method, dependency_classification, fixture_status, forbidden_next_action):
    return {
        "pin_name": pin_name,
        "ablation_modes": ["null_mode", "tripwire_mode", "trace_mode", "substitute_mode"],
        "consumer_expectation": consumer_expectation,
        "rollback_method": rollback_method,
        "dependency_classification": dependency_classification,
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_source_lineage_ablation_matrix():
    return [
        pin(
            "ais_source_label",
            "descriptor consumers degrade to unavailable source label only",
            "restore AIS descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_execute_ais_provider_or_database_source",
        ),
        pin(
            "adsb_source_label",
            "descriptor consumers degrade to unavailable source label only",
            "restore ADS-B descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_execute_adsb_provider_or_live_source",
        ),
        pin(
            "sql_replay_lineage_label",
            "tripwire marks SQL replay as blocked runtime dependency",
            "restore replay lineage label descriptor",
            "descriptor_label_with_blocked_runtime_peer",
            "pinned",
            "do_not_execute_sql_replay_runtime",
        ),
        pin(
            "websocket_live_lineage_label",
            "tripwire marks live lineage as blocked runtime dependency",
            "restore live lineage unresolved label descriptor",
            "descriptor_label_with_blocked_runtime_peer",
            "pinned",
            "do_not_open_websocket_or_live_stream",
        ),
        pin(
            "synthetic_source_label",
            "substitute descriptor remains local fixture data",
            "restore synthetic source descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_generate_runtime_points_or_render_buffers",
        ),
        pin(
            "unavailable_source_label",
            "null mode keeps provider unavailable branch deterministic",
            "restore unavailable source descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_probe_real_provider_cache_or_database",
        ),
        pin(
            "timestamp_quality_label",
            "trace mode records stale and missing timestamp labels only",
            "reset test-local timestamp quality descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_execute_real_clock_replay_clock_or_database_query",
        ),
        pin(
            "coordinate_payload_quality_label",
            "trace mode records missing and invalid lat/lon labels only",
            "reset test-local coordinate payload descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_invoke_projection_flip_or_mask_formula",
        ),
        pin(
            "source_id_label",
            "substitute mode keeps source id as scalar label",
            "restore source id descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_resolve_real_source_identity_or_database_handle",
        ),
        pin(
            "lineage_status_label",
            "null mode keeps lineage status label unresolved without runtime source",
            "restore lineage status descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_convert_lineage_label_into_runtime_source",
        ),
        pin(
            "provider_runtime_dependency",
            "tripwire must stop extraction if provider execution is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_provider_loader_or_source_runtime",
        ),
        pin(
            "database_runtime_dependency",
            "tripwire must stop extraction if database runtime is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_open_database_or_create_db_handle",
        ),
        pin(
            "live_stream_runtime_dependency",
            "tripwire must stop extraction if live stream runtime is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_open_socket_or_live_stream",
        ),
        pin(
            "cache_io_runtime_dependency",
            "tripwire must stop extraction if cache IO is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_read_real_ais_adsb_cache_or_database",
        ),
        pin(
            "dataframe_projection_runtime_dependency",
            "tripwire must stop extraction if dataframe or projection runtime is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_import_dataframe_runtime_or_change_projection_formula",
        ),
    ]


def build_deterministic_boundary_fill():
    return {
        "future_helper_target": "render_core\\dynamic_point_source_lineage_boundary.py",
        "descriptor_candidate_families": list(REQUIRED_CANDIDATE_FAMILIES),
        "blocked_runtime_surfaces": list(REQUIRED_BLOCKED_SURFACES),
        "import_boundary_checker_needed": True,
        "existing_checker_reusable": False,
        "new_checker_required": True,
        "source_lineage_planning_candidate": True,
        "source_lineage_extraction_candidate": False,
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "checker_decision_reason": "future target is narrower than aggregate dynamic_point_boundary and needs dedicated source-lineage checker before extraction",
    }


def build_next_gate_decision():
    return {
        "recommended_next_gate": "dynamic_point_source_lineage_import_boundary_checker_gate",
        "reason": "new second-layer helper target needs independent checker before planning can advance",
        "runtime_risk_excluded_by_matrix": True,
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "safe_to_extract_claimed": False,
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


class DynamicPointSourceLineageCratonAblationMatrixTests(unittest.TestCase):
    def test_phase_a_matrix_has_required_pins_and_fields(self):
        matrix = build_source_lineage_ablation_matrix()
        self.assertEqual({entry["pin_name"] for entry in matrix}, REQUIRED_PINS)
        for entry in matrix:
            self.assertEqual(set(entry), PIN_FIELDS)
            self.assertEqual(set(entry["ablation_modes"]), REQUIRED_ABLATION_MODES)
            self.assertIn(entry["fixture_status"], {"pinned", "unresolved_static_only", "blocked_runtime_only"})
            self.assertIn("do_not", entry["forbidden_next_action"])

    def test_runtime_dependency_pins_are_blocked(self):
        blocked = [entry for entry in build_source_lineage_ablation_matrix() if entry["fixture_status"] == "blocked_runtime_only"]
        self.assertEqual(
            {entry["pin_name"] for entry in blocked},
            {
                "provider_runtime_dependency",
                "database_runtime_dependency",
                "live_stream_runtime_dependency",
                "cache_io_runtime_dependency",
                "dataframe_projection_runtime_dependency",
            },
        )
        for entry in blocked:
            self.assertEqual(entry["dependency_classification"], "blocked_runtime_dependency")

    def test_descriptor_pins_remain_planning_only(self):
        descriptor_entries = [entry for entry in build_source_lineage_ablation_matrix() if entry["dependency_classification"].startswith("descriptor")]
        self.assertGreaterEqual(len(descriptor_entries), 10)
        for entry in descriptor_entries:
            self.assertNotEqual(entry["fixture_status"], "blocked_runtime_only")

    def test_phase_b_deterministic_boundary_fill_is_pinned(self):
        fill = build_deterministic_boundary_fill()
        self.assertEqual(set(fill), BOUNDARY_FILL_KEYS)
        self.assertEqual(fill["future_helper_target"], "render_core\\dynamic_point_source_lineage_boundary.py")
        self.assertEqual(fill["descriptor_candidate_families"], REQUIRED_CANDIDATE_FAMILIES)
        self.assertEqual(fill["blocked_runtime_surfaces"], REQUIRED_BLOCKED_SURFACES)
        self.assertTrue(fill["import_boundary_checker_needed"])
        self.assertFalse(fill["existing_checker_reusable"])
        self.assertTrue(fill["new_checker_required"])
        self.assertTrue(fill["source_lineage_planning_candidate"])
        self.assertFalse(fill["source_lineage_extraction_candidate"])
        self.assertFalse(fill["helper_module_creation_authorized"])
        self.assertFalse(fill["source_movement_authorized"])

    def test_phase_c_recommends_new_import_boundary_checker_gate(self):
        decision = build_next_gate_decision()
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_source_lineage_import_boundary_checker_gate")
        self.assertTrue(decision["runtime_risk_excluded_by_matrix"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["safe_to_extract_claimed"])

    def test_packets_are_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_source_lineage_ablation_matrix()))
        self.assertTrue(is_packet_data(build_deterministic_boundary_fill()))
        self.assertTrue(is_packet_data(build_next_gate_decision()))

    def test_no_forbidden_claim_markers(self):
        packet_text = repr(build_source_lineage_ablation_matrix()) + repr(build_deterministic_boundary_fill()) + repr(build_next_gate_decision())
        for marker in [
            "taichi_global_bathymetry",
            "source_movement_authorized_true",
            "helper_module_creation_authorized_true",
            "source_lineage_extraction_candidate_true",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "readiness_claimed",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
