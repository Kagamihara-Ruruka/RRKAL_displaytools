import unittest


PIN_KEYS = {
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
    "new_checker_required",
    "existing_checker_reusable",
    "payload_coordinate_quality_planning_candidate",
    "payload_coordinate_quality_extraction_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "candidate_helper_families",
    "blocked_runtime_surfaces",
    "required_checker_gate",
    "deterministic_fill_reason",
}

REQUIRED_ABLATION_MODES = ["null_mode", "tripwire_mode", "trace_mode", "substitute_mode"]

REQUIRED_PINS = [
    "payload_shape_pin",
    "coordinate_quality_pin",
    "timestamp_quality_pin",
    "source_id_quality_pin",
    "speed_heading_quality_pin",
    "point_vector_sync_fault_pin",
    "projection_dependency_stop_pin",
    "live_source_dependency_stop_pin",
    "controller_selection_dependency_stop_pin",
    "renderer_runtime_dependency_stop_pin",
]

CANDIDATE_HELPER_FAMILIES = [
    "build_dynamic_point_payload_shape_descriptor",
    "build_dynamic_point_coordinate_quality_descriptor",
    "build_dynamic_point_timestamp_quality_descriptor",
    "build_dynamic_point_source_id_quality_descriptor",
    "build_dynamic_point_speed_heading_quality_descriptor",
    "build_dynamic_point_payload_coordinate_quality_known_fault_ledger",
    "dynamic_point_payload_coordinate_quality_boundary_descriptor",
    "dynamic_point_payload_coordinate_quality_planning_bundle",
]

BLOCKED_RUNTIME_SURFACES = [
    "projection_flip_mask_formula",
    "sql_websocket_live_source",
    "real_ais_adsb_cache_database_read",
    "pandas_datashader_numpy_runtime",
    "controller_selection_picker_hit_test_runtime",
    "renderer_qt_vispy_taichi_runtime",
    "metadata_artifact_writer",
    "alpha_apply_composition_hot_path",
]


def pin(pin_name, consumer_expectation, rollback_method, dependency_classification, fixture_status, forbidden_next_action):
    return {
        "pin_name": pin_name,
        "ablation_modes": list(REQUIRED_ABLATION_MODES),
        "consumer_expectation": consumer_expectation,
        "rollback_method": rollback_method,
        "dependency_classification": dependency_classification,
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_payload_coordinate_quality_ablation_matrix():
    return [
        pin(
            "payload_shape_pin",
            "null mode degrades descriptor bundle when lat lon timestamp source_id speed or heading labels are absent",
            "restore payload shape descriptor",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_read_real_ais_adsb_database_or_dataframe_payload",
        ),
        pin(
            "coordinate_quality_pin",
            "substitute mode replaces missing invalid out-of-range zero and anti-meridian coordinate labels as data only",
            "restore coordinate quality descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_invoke_projection_flip_mask_formula",
        ),
        pin(
            "timestamp_quality_pin",
            "trace mode records missing stale future and timezone ambiguity labels without real clock execution",
            "reset timestamp quality recorder descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_execute_replay_clock_live_clock_or_database_timestamp_query",
        ),
        pin(
            "source_id_quality_pin",
            "substitute mode swaps missing synthetic AIS and ADS-B id labels without source lookup",
            "restore source id quality descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_probe_live_source_database_or_cache_identity",
        ),
        pin(
            "speed_heading_quality_pin",
            "null mode removes speed heading labels while keeping render policy consumers descriptor-only",
            "restore speed heading quality descriptor",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_execute_datashader_or_renderer_speed_heading_runtime",
        ),
        pin(
            "point_vector_sync_fault_pin",
            "tripwire records point/vector sync dependency as unresolved ledger only",
            "reset known fault ledger descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_claim_projection_or_vector_sync_correctness",
        ),
        pin(
            "projection_dependency_stop_pin",
            "tripwire stops if coordinate quality needs projection flip or mask formula execution",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_projection_flip_or_mask_formula",
        ),
        pin(
            "live_source_dependency_stop_pin",
            "tripwire stops if payload quality requires SQL WebSocket live AIS ADS-B cache or database read",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_sql_websocket_live_cache_or_database_runtime",
        ),
        pin(
            "controller_selection_dependency_stop_pin",
            "tripwire stops if source id or coordinate quality requires controller selection picker or hit-test runtime",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_controller_selection_picker_or_hit_test_runtime",
        ),
        pin(
            "renderer_runtime_dependency_stop_pin",
            "tripwire stops if payload quality requires renderer Qt VisPy Taichi or Datashader runtime",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_renderer_qt_vispy_taichi_or_datashader_runtime",
        ),
    ]


def build_deterministic_boundary_fill():
    return {
        "future_helper_target": "render_core\\dynamic_point_payload_coordinate_quality_boundary.py",
        "new_checker_required": True,
        "existing_checker_reusable": False,
        "payload_coordinate_quality_planning_candidate": True,
        "payload_coordinate_quality_extraction_candidate": False,
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "candidate_helper_families": list(CANDIDATE_HELPER_FAMILIES),
        "blocked_runtime_surfaces": list(BLOCKED_RUNTIME_SURFACES),
        "required_checker_gate": "dynamic_point_payload_coordinate_quality_import_boundary_checker_gate",
        "deterministic_fill_reason": "payload coordinate quality has distinct projection live source dataframe controller and renderer stop lines, so a dedicated checker is required before planning or extraction",
    }


def build_next_gate_decision():
    return {
        "recommended_next_gate": "dynamic_point_payload_coordinate_quality_import_boundary_checker_gate",
        "matrix_gate_passed": True,
        "matrix_improves_next_gate_precision": True,
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "runtime_execution_used": False,
        "safe_to_extract_claimed": False,
    }


def build_payload_coordinate_quality_ablation_packet():
    return {
        "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality_craton_ablation_matrix.v1",
        "phase_a_matrix": build_payload_coordinate_quality_ablation_matrix(),
        "phase_b_deterministic_boundary_fill": build_deterministic_boundary_fill(),
        "phase_c_next_gate_decision": build_next_gate_decision(),
        "boundary_statement": "Docs/test-only dynamic point payload/coordinate quality craton ablation capability matrix and deterministic boundary fill gate.",
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


class DynamicPointPayloadCoordinateQualityCratonAblationMatrixTests(unittest.TestCase):
    def test_phase_a_matrix_has_required_pins_and_modes(self):
        matrix = build_payload_coordinate_quality_ablation_matrix()
        self.assertEqual([entry["pin_name"] for entry in matrix], REQUIRED_PINS)
        for entry in matrix:
            self.assertEqual(set(entry), PIN_KEYS)
            self.assertEqual(entry["ablation_modes"], REQUIRED_ABLATION_MODES)
            self.assertIn(entry["fixture_status"], {"pinned", "unresolved_static_only", "blocked_runtime_only"})
            self.assertIn("do_not", entry["forbidden_next_action"])

    def test_descriptor_pins_are_not_runtime_extraction_claims(self):
        descriptor_entries = [entry for entry in build_payload_coordinate_quality_ablation_matrix() if entry["dependency_classification"] == "descriptor_policy_ledger"]
        self.assertEqual(
            [entry["pin_name"] for entry in descriptor_entries],
            [
                "payload_shape_pin",
                "coordinate_quality_pin",
                "timestamp_quality_pin",
                "source_id_quality_pin",
                "speed_heading_quality_pin",
                "point_vector_sync_fault_pin",
            ],
        )
        for entry in descriptor_entries:
            self.assertNotEqual(entry["fixture_status"], "blocked_runtime_only")

    def test_runtime_dependency_pins_are_blocked_runtime_only(self):
        blocked = [entry for entry in build_payload_coordinate_quality_ablation_matrix() if entry["dependency_classification"] == "blocked_runtime_dependency"]
        self.assertEqual(
            [entry["pin_name"] for entry in blocked],
            [
                "projection_dependency_stop_pin",
                "live_source_dependency_stop_pin",
                "controller_selection_dependency_stop_pin",
                "renderer_runtime_dependency_stop_pin",
            ],
        )
        for entry in blocked:
            self.assertEqual(entry["fixture_status"], "blocked_runtime_only")

    def test_phase_b_deterministic_boundary_fill_is_pinned(self):
        fill = build_deterministic_boundary_fill()
        self.assertEqual(set(fill), BOUNDARY_FILL_KEYS)
        self.assertEqual(fill["future_helper_target"], "render_core\\dynamic_point_payload_coordinate_quality_boundary.py")
        self.assertTrue(fill["new_checker_required"])
        self.assertFalse(fill["existing_checker_reusable"])
        self.assertTrue(fill["payload_coordinate_quality_planning_candidate"])
        self.assertFalse(fill["payload_coordinate_quality_extraction_candidate"])
        self.assertFalse(fill["helper_module_creation_authorized"])
        self.assertFalse(fill["source_movement_authorized"])
        self.assertEqual(fill["candidate_helper_families"], CANDIDATE_HELPER_FAMILIES)
        self.assertEqual(fill["blocked_runtime_surfaces"], BLOCKED_RUNTIME_SURFACES)

    def test_candidate_helper_families_are_planning_only(self):
        fill = build_deterministic_boundary_fill()
        for helper in fill["candidate_helper_families"]:
            self.assertTrue(helper.startswith("build_dynamic_point_") or helper.startswith("dynamic_point_"))
        self.assertFalse(fill["payload_coordinate_quality_extraction_candidate"])
        self.assertFalse(fill["helper_module_creation_authorized"])

    def test_phase_c_recommends_import_boundary_checker_gate(self):
        decision = build_next_gate_decision()
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_payload_coordinate_quality_import_boundary_checker_gate")
        self.assertTrue(decision["matrix_gate_passed"])
        self.assertTrue(decision["matrix_improves_next_gate_precision"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["runtime_execution_used"])
        self.assertFalse(decision["safe_to_extract_claimed"])

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_payload_coordinate_quality_ablation_packet()))

    def test_no_runtime_readiness_bug_fix_or_safe_to_extract_claims(self):
        packet_text = repr(build_payload_coordinate_quality_ablation_packet())
        for marker in [
            "source_movement_authorized': True",
            "helper_module_creation_authorized': True",
            "payload_coordinate_quality_extraction_candidate': True",
            "runtime_execution_used': True",
            "safe_to_extract_claimed': True",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "readiness_claimed",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()