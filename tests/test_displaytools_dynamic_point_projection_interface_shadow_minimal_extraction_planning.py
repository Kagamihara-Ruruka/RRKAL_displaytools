import unittest


FUTURE_HELPER_TARGET = "render_core\\dynamic_point_projection_interface_shadow_boundary.py"
REQUIRED_CHECKER = "scripts\\validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py"

REQUIRED_CANDIDATE_FAMILIES = {
    "build_dynamic_point_projection_policy_ref_descriptor",
    "build_dynamic_point_flip_policy_ref_descriptor",
    "build_dynamic_point_mask_policy_ref_descriptor",
    "build_dynamic_point_frame_sync_ref_descriptor",
    "build_dynamic_point_projection_consumer_surface_descriptor",
    "build_dynamic_point_projection_shadow_uncertainty_ledger",
    "dynamic_point_projection_interface_shadow_boundary_descriptor",
    "dynamic_point_projection_interface_shadow_planning_bundle",
}

REQUIRED_BLOCKED_SURFACES = {
    "projection_formula",
    "longitude_flip_formula",
    "latitude_flip_formula",
    "mask_formula",
    "renderer_frame_transform",
    "runtime_renderer_host",
    "dynamic_point_screen_projection_execution",
    "hot_path_alpha_apply_composition",
    "controller_selection",
    "dataframe_runtime",
    "live_source",
    "artifact_metadata",
    "coordinate_correctness_claim",
    "visual_correctness_claim",
}

HELPER_PLAN_KEYS = {
    "helper_name",
    "candidate_for_minimal_extraction",
    "allowed_surface_kind",
    "expected_output_shape",
    "required_checker",
    "blocked_surface_refs",
    "forbidden_runtime_dependency",
    "fixture_parity_required",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "projection_shadow_source",
    "planning_source",
    "checker_source",
    "creation_order_counterexample_source",
    "future_helper_target",
    "required_checker",
    "candidate_helper_families",
    "candidate_helper_plan",
    "blocked_surfaces",
    "checker_expectation",
    "planning_decisions",
    "boundary_statement",
}


def build_dynamic_point_projection_interface_shadow_minimal_extraction_planning_packet():
    candidate_helper_plan = [
        {
            "helper_name": helper_name,
            "candidate_for_minimal_extraction": True,
            "allowed_surface_kind": "label_reference_ledger_only",
            "expected_output_shape": "dict_list_scalar_only",
            "required_checker": REQUIRED_CHECKER,
            "blocked_surface_refs": sorted(REQUIRED_BLOCKED_SURFACES),
            "forbidden_runtime_dependency": True,
            "fixture_parity_required": [
                "safe_import_future_helper",
                "exact_key_set_parity",
                "deterministic_repeat_call_parity",
                "dict_list_scalar_only_output",
                "no_callable_formula_refs",
                "no_renderer_buffer_refs",
                "no_coordinate_transform_implementation",
                "checker_candidate_pass",
                "checker_negative_forbidden_dependency_fail",
            ],
        }
        for helper_name in sorted(REQUIRED_CANDIDATE_FAMILIES)
    ]

    return {
        "schema": "rrkal.displaytools.dynamic_point_projection_interface_shadow_minimal_extraction_planning.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "projection_shadow_source": "6289c60",
        "planning_source": "a72d141",
        "checker_source": "827440c",
        "creation_order_counterexample_source": "53afb98",
        "future_helper_target": FUTURE_HELPER_TARGET,
        "required_checker": REQUIRED_CHECKER,
        "candidate_helper_families": sorted(REQUIRED_CANDIDATE_FAMILIES),
        "candidate_helper_plan": candidate_helper_plan,
        "blocked_surfaces": sorted(REQUIRED_BLOCKED_SURFACES),
        "checker_expectation": {
            "checker_is_ast_only": True,
            "target_imported": False,
            "target_executed": False,
            "current_missing_target_behavior": "pass",
            "expected_clean_candidate_behavior": "pass",
            "expected_runtime_dependency_behavior": "fail",
            "string_labels_allowed_as_data": True,
            "forbidden_executable_references_fail": True,
            "forbidden_declaration_names_fail": True,
            "syntax_error_json_fail": True,
            "negative_self_test_required": True,
        },
        "planning_decisions": {
            "planning_gate_passed": True,
            "projection_shadow_planning_candidate": True,
            "projection_shadow_extraction_candidate": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "runtime_merge_enabled": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "generic_checker_blocking": False,
            "generic_checker_replacement_authorized": False,
            "required_checker": REQUIRED_CHECKER,
            "future_helper_target": FUTURE_HELPER_TARGET,
            "recommended_next_gate": "dynamic_point_projection_interface_shadow_minimal_extraction_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point projection interface shadow minimal extraction planning gate. "
            "No helper module creation, no source movement, no production source change, no checker script change, "
            "no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, "
            "no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no controller selection/picker/hit-test mutation, "
            "no metadata/output schema change, no cross-organ integration implementation, "
            "no coordinate/visual correctness claim, no runtime merge enablement, "
            "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointProjectionInterfaceShadowMinimalExtractionPlanningTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_projection_interface_shadow_minimal_extraction_planning_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_projection_interface_shadow_minimal_extraction_planning.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["projection_shadow_source"], "6289c60")
        self.assertEqual(self.packet["planning_source"], "a72d141")
        self.assertEqual(self.packet["checker_source"], "827440c")
        self.assertEqual(self.packet["creation_order_counterexample_source"], "53afb98")

    def test_future_target_and_checker_are_fixed(self):
        self.assertEqual(self.packet["future_helper_target"], FUTURE_HELPER_TARGET)
        self.assertEqual(self.packet["required_checker"], REQUIRED_CHECKER)
        self.assertEqual(self.packet["planning_decisions"]["future_helper_target"], FUTURE_HELPER_TARGET)
        self.assertEqual(self.packet["planning_decisions"]["required_checker"], REQUIRED_CHECKER)

    def test_candidate_helper_families_are_planning_only(self):
        self.assertEqual(set(self.packet["candidate_helper_families"]), REQUIRED_CANDIDATE_FAMILIES)
        for plan in self.packet["candidate_helper_plan"]:
            self.assertEqual(set(plan), HELPER_PLAN_KEYS)
            self.assertIn(plan["helper_name"], REQUIRED_CANDIDATE_FAMILIES)
            self.assertTrue(plan["candidate_for_minimal_extraction"])
            self.assertEqual(plan["allowed_surface_kind"], "label_reference_ledger_only")
            self.assertEqual(plan["expected_output_shape"], "dict_list_scalar_only")
            self.assertTrue(plan["forbidden_runtime_dependency"])
            self.assertIn("no_callable_formula_refs", plan["fixture_parity_required"])
            self.assertIn("no_renderer_buffer_refs", plan["fixture_parity_required"])
            self.assertIn("no_coordinate_transform_implementation", plan["fixture_parity_required"])

    def test_blocked_surfaces_are_complete(self):
        self.assertEqual(set(self.packet["blocked_surfaces"]), REQUIRED_BLOCKED_SURFACES)
        for plan in self.packet["candidate_helper_plan"]:
            self.assertEqual(set(plan["blocked_surface_refs"]), REQUIRED_BLOCKED_SURFACES)

    def test_checker_expectation_matches_checker_gate(self):
        expectation = self.packet["checker_expectation"]
        self.assertTrue(expectation["checker_is_ast_only"])
        self.assertFalse(expectation["target_imported"])
        self.assertFalse(expectation["target_executed"])
        self.assertEqual(expectation["current_missing_target_behavior"], "pass")
        self.assertEqual(expectation["expected_clean_candidate_behavior"], "pass")
        self.assertEqual(expectation["expected_runtime_dependency_behavior"], "fail")
        self.assertTrue(expectation["string_labels_allowed_as_data"])
        self.assertTrue(expectation["forbidden_executable_references_fail"])
        self.assertTrue(expectation["forbidden_declaration_names_fail"])
        self.assertTrue(expectation["syntax_error_json_fail"])
        self.assertTrue(expectation["negative_self_test_required"])

    def test_planning_decisions_do_not_authorize_extraction_or_runtime(self):
        decisions = self.packet["planning_decisions"]
        self.assertTrue(decisions["planning_gate_passed"])
        self.assertTrue(decisions["projection_shadow_planning_candidate"])
        self.assertFalse(decisions["projection_shadow_extraction_candidate"])
        self.assertFalse(decisions["helper_module_creation_authorized"])
        self.assertFalse(decisions["source_movement_authorized"])
        self.assertFalse(decisions["formula_movement_authorized"])
        self.assertFalse(decisions["runtime_merge_enabled"])
        self.assertFalse(decisions["coordinate_correctness_claimed"])
        self.assertFalse(decisions["visual_correctness_claimed"])
        self.assertFalse(decisions["generic_checker_blocking"])
        self.assertFalse(decisions["generic_checker_replacement_authorized"])

    def test_recommended_next_gate_is_minimal_extraction_gate(self):
        self.assertEqual(
            self.packet["planning_decisions"]["recommended_next_gate"],
            "dynamic_point_projection_interface_shadow_minimal_extraction_gate",
        )

    def test_boundary_statement_contains_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no readiness/performance/visual parity/bug-fix/safe-to-extract claim", boundary)


if __name__ == "__main__":
    unittest.main()
