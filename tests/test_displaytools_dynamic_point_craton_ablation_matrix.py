import unittest


MATRIX_FIELDS = {
    "craton_surface",
    "ablation_mode",
    "consumer_surface",
    "expected_effect",
    "risk_level",
    "rollback_method",
    "evidence_level",
    "forbidden_next_action",
}

ALLOWED_ABLATION_MODES = {"null_mode", "tripwire_mode", "trace_mode", "substitute_mode"}
ALLOWED_EFFECTS = {
    "no_effect",
    "degraded_descriptor",
    "hidden_dependency_discovered",
    "blocked_runtime_dependency",
    "extraction_stop_condition",
}
ALLOWED_RISK_LEVELS = {"low", "medium", "high", "blocked"}
ALLOWED_EVIDENCE_LEVELS = {"historically_grounded", "structurally_inferred", "exploratory"}


def build_dynamic_point_craton_ablation_matrix():
    return [
        {
            "craton_surface": "source_descriptor",
            "ablation_mode": "null_mode",
            "consumer_surface": "descriptor_bundle",
            "expected_effect": "degraded_descriptor",
            "risk_level": "low",
            "rollback_method": "remove_fake_descriptor",
            "evidence_level": "historically_grounded",
            "forbidden_next_action": "do_not_execute_sql_websocket_or_live_source",
        },
        {
            "craton_surface": "payload_shape_descriptor",
            "ablation_mode": "substitute_mode",
            "consumer_surface": "future_helper_candidate",
            "expected_effect": "no_effect",
            "risk_level": "low",
            "rollback_method": "restore_descriptor_bundle",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_parse_real_ais_adsb_or_dataframe_payload",
        },
        {
            "craton_surface": "replay_live_lineage_descriptor",
            "ablation_mode": "tripwire_mode",
            "consumer_surface": "safety_checker",
            "expected_effect": "hidden_dependency_discovered",
            "risk_level": "medium",
            "rollback_method": "reset_test_local_recorder",
            "evidence_level": "historically_grounded",
            "forbidden_next_action": "do_not_execute_replay_query_websocket_or_real_clock",
        },
        {
            "craton_surface": "selection_descriptor",
            "ablation_mode": "trace_mode",
            "consumer_surface": "selection_panel",
            "expected_effect": "hidden_dependency_discovered",
            "risk_level": "medium",
            "rollback_method": "reset_test_local_recorder",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_mutate_controller_selection_picker_or_hit_test",
        },
        {
            "craton_surface": "render_policy_descriptor",
            "ablation_mode": "null_mode",
            "consumer_surface": "render_policy_consumer",
            "expected_effect": "degraded_descriptor",
            "risk_level": "medium",
            "rollback_method": "restore_descriptor_bundle",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_execute_datashader_or_renderer_runtime",
        },
        {
            "craton_surface": "safety_ledger",
            "ablation_mode": "tripwire_mode",
            "consumer_surface": "safety_checker",
            "expected_effect": "extraction_stop_condition",
            "risk_level": "blocked",
            "rollback_method": "reset_test_local_recorder",
            "evidence_level": "historically_grounded",
            "forbidden_next_action": "do_not_weaken_sql_websocket_datashader_runtime_stop_lines",
        },
        {
            "craton_surface": "known_fault_ledger",
            "ablation_mode": "substitute_mode",
            "consumer_surface": "planning_bundle",
            "expected_effect": "degraded_descriptor",
            "risk_level": "low",
            "rollback_method": "restore_descriptor_bundle",
            "evidence_level": "exploratory",
            "forbidden_next_action": "do_not_claim_live_restored_bug_fix_or_readiness",
        },
        {
            "craton_surface": "projection_peer_sync_candidate",
            "ablation_mode": "trace_mode",
            "consumer_surface": "projection_peer",
            "expected_effect": "hidden_dependency_discovered",
            "risk_level": "high",
            "rollback_method": "reset_test_local_recorder",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_change_projection_flip_or_mask_formula",
        },
        {
            "craton_surface": "selection_panel_dependency",
            "ablation_mode": "trace_mode",
            "consumer_surface": "selection_panel",
            "expected_effect": "hidden_dependency_discovered",
            "risk_level": "high",
            "rollback_method": "reset_test_local_recorder",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_touch_controller_selection_runtime",
        },
        {
            "craton_surface": "render_policy_consumer_dependency",
            "ablation_mode": "null_mode",
            "consumer_surface": "render_policy_consumer",
            "expected_effect": "degraded_descriptor",
            "risk_level": "medium",
            "rollback_method": "restore_descriptor_bundle",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_execute_renderer_qt_vispy_taichi_or_datashader",
        },
        {
            "craton_surface": "sql_websocket_datashader_runtime_dependency",
            "ablation_mode": "tripwire_mode",
            "consumer_surface": "safety_checker",
            "expected_effect": "blocked_runtime_dependency",
            "risk_level": "blocked",
            "rollback_method": "not_applicable_because_no_runtime_patch",
            "evidence_level": "historically_grounded",
            "forbidden_next_action": "do_not_execute_sql_websocket_live_source_datashader_or_dataframe_runtime",
        },
        {
            "craton_surface": "runtime_dependency_required_stop_condition",
            "ablation_mode": "tripwire_mode",
            "consumer_surface": "future_helper_candidate",
            "expected_effect": "extraction_stop_condition",
            "risk_level": "blocked",
            "rollback_method": "not_applicable_because_no_runtime_patch",
            "evidence_level": "structurally_inferred",
            "forbidden_next_action": "do_not_extract_if_runtime_dependency_is_required",
        },
    ]


def build_deterministic_boundary_fill():
    return {
        "future_helper_target": "render_core\\dynamic_point_boundary.py",
        "candidate_scope": "descriptor_policy_ledger_only",
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "dynamic_point_extraction_candidate": False,
        "dynamic_point_planning_candidate": True,
        "a1_macro_observer_required_before_source_movement": True,
        "import_boundary_checker_already_available": True,
        "checker_script": "scripts\\validate_displaytools_dynamic_point_import_boundary.py",
        "runtime_dependency_allowed": False,
        "sql_replay_database_surface": "blocked",
        "live_stream_surface": "blocked",
        "dataframe_projection_runtime_surface": "blocked",
        "controller_selection_runtime_surface": "blocked",
        "renderer_host_surface": "blocked",
        "metadata_artifact_writer_surface": "blocked",
    }


def build_next_slice_refinement():
    return {
        "ablation_matrix_methodology_trial": True,
        "production_monkey_patch_used": False,
        "runtime_import_used": False,
        "source_movement_authorized": False,
        "dynamic_point_extraction_candidate": False,
        "matrix_improves_next_gate_precision": True,
        "matrix_precision_reason": "matrix fills deterministic descriptor stop lines before source movement",
        "recommended_next_gate": "dynamic_point_boundary_minimal_extraction_gate_after_a1_macro_review",
        "helper_module_created": False,
        "runtime_execution_used": False,
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


class DisplaytoolsDynamicPointCratonAblationMatrixTests(unittest.TestCase):
    def test_matrix_entries_pin_exact_fields_and_allowed_values(self):
        matrix = build_dynamic_point_craton_ablation_matrix()

        self.assertGreaterEqual(len(matrix), 12)
        for entry in matrix:
            self.assertEqual(set(entry), MATRIX_FIELDS)
            self.assertIn(entry["ablation_mode"], ALLOWED_ABLATION_MODES)
            self.assertIn(entry["expected_effect"], ALLOWED_EFFECTS)
            self.assertIn(entry["risk_level"], ALLOWED_RISK_LEVELS)
            self.assertIn(entry["evidence_level"], ALLOWED_EVIDENCE_LEVELS)

    def test_required_craton_surface_cases_are_present(self):
        surfaces = {entry["craton_surface"] for entry in build_dynamic_point_craton_ablation_matrix()}

        self.assertEqual(
            surfaces,
            {
                "source_descriptor",
                "payload_shape_descriptor",
                "replay_live_lineage_descriptor",
                "selection_descriptor",
                "render_policy_descriptor",
                "safety_ledger",
                "known_fault_ledger",
                "projection_peer_sync_candidate",
                "selection_panel_dependency",
                "render_policy_consumer_dependency",
                "sql_websocket_datashader_runtime_dependency",
                "runtime_dependency_required_stop_condition",
            },
        )

    def test_required_ablation_modes_are_covered(self):
        modes = {entry["ablation_mode"] for entry in build_dynamic_point_craton_ablation_matrix()}

        self.assertEqual(modes, ALLOWED_ABLATION_MODES)

    def test_runtime_dependencies_are_blocked_stop_conditions(self):
        blocked_entries = [
            entry
            for entry in build_dynamic_point_craton_ablation_matrix()
            if entry["risk_level"] == "blocked"
        ]

        self.assertGreaterEqual(len(blocked_entries), 2)
        for entry in blocked_entries:
            self.assertIn(entry["expected_effect"], {"blocked_runtime_dependency", "extraction_stop_condition"})
            self.assertIn("do_not", entry["forbidden_next_action"])

    def test_deterministic_boundary_fill_pins_required_cells(self):
        fill = build_deterministic_boundary_fill()

        self.assertEqual(fill["future_helper_target"], "render_core\\dynamic_point_boundary.py")
        self.assertEqual(fill["candidate_scope"], "descriptor_policy_ledger_only")
        self.assertFalse(fill["source_movement_authorized"])
        self.assertFalse(fill["helper_module_creation_authorized"])
        self.assertFalse(fill["dynamic_point_extraction_candidate"])
        self.assertTrue(fill["dynamic_point_planning_candidate"])
        self.assertTrue(fill["a1_macro_observer_required_before_source_movement"])
        self.assertTrue(fill["import_boundary_checker_already_available"])
        self.assertEqual(fill["checker_script"], "scripts\\validate_displaytools_dynamic_point_import_boundary.py")
        self.assertFalse(fill["runtime_dependency_allowed"])
        self.assertEqual(fill["sql_replay_database_surface"], "blocked")
        self.assertEqual(fill["live_stream_surface"], "blocked")
        self.assertEqual(fill["dataframe_projection_runtime_surface"], "blocked")
        self.assertEqual(fill["controller_selection_runtime_surface"], "blocked")
        self.assertEqual(fill["renderer_host_surface"], "blocked")
        self.assertEqual(fill["metadata_artifact_writer_surface"], "blocked")

    def test_next_slice_refinement_recommends_after_macro_review(self):
        refinement = build_next_slice_refinement()

        self.assertTrue(refinement["ablation_matrix_methodology_trial"])
        self.assertFalse(refinement["production_monkey_patch_used"])
        self.assertFalse(refinement["runtime_import_used"])
        self.assertFalse(refinement["source_movement_authorized"])
        self.assertFalse(refinement["dynamic_point_extraction_candidate"])
        self.assertTrue(refinement["matrix_improves_next_gate_precision"])
        self.assertEqual(
            refinement["recommended_next_gate"],
            "dynamic_point_boundary_minimal_extraction_gate_after_a1_macro_review",
        )
        self.assertFalse(refinement["helper_module_created"])
        self.assertFalse(refinement["runtime_execution_used"])
        self.assertFalse(refinement["safe_to_extract_claimed"])

    def test_all_packets_are_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_dynamic_point_craton_ablation_matrix()))
        self.assertTrue(is_packet_data(build_deterministic_boundary_fill()))
        self.assertTrue(is_packet_data(build_next_slice_refinement()))

    def test_test_module_imports_no_monolith_or_runtime_dependency(self):
        import_names = {name for name, _value in globals().items() if name.startswith("test_displaytools")}

        self.assertEqual(import_names, set())
        self.assertNotIn("taichi_global_bathymetry", globals())
        self.assertNotIn("pandas", globals())
        self.assertNotIn("datashader", globals())
        self.assertNotIn("numpy", globals())


if __name__ == "__main__":
    unittest.main()
