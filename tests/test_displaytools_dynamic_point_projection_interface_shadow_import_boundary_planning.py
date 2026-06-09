import unittest


REQUIRED_FORBIDDEN_FAMILIES = {
    "monolith",
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

REQUIRED_ALLOWED_STRING_LABELS = {
    "source_coordinate_space",
    "target_coordinate_space",
    "projection_policy_ref",
    "flip_policy_ref",
    "mask_policy_ref",
    "frame_sync_ref",
    "consumer_surface",
    "uncertainty_label",
    "evidence_refs",
    "formula_behavior_not_executed",
    "coordinate_correctness_not_claimed",
    "visual_correctness_not_claimed",
}

REQUIRED_ALLOWED_DATA_SURFACES = {
    "label_only_policy_refs",
    "static_evidence_refs",
    "interface_field_names",
    "uncertainty_labels",
    "consumer_expectation_descriptors",
    "stop_condition_ledger",
    "no_callable_formula_refs",
    "no_renderer_buffer_refs",
}

REQUIRED_AST_NODES = {
    "ast.Import",
    "ast.ImportFrom",
    "ast.Name",
    "ast.Attribute",
    "ast.Call",
    "ast.FunctionDef",
    "ast.AsyncFunctionDef",
    "ast.ClassDef",
}


def build_dynamic_point_projection_interface_shadow_import_boundary_planning_packet():
    return {
        "schema": "rrkal.displaytools.dynamic_point_projection_interface_shadow_import_boundary_planning.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "local_pattern_source": "60cded8",
        "shadow_source": "6289c60",
        "future_helper_target": "render_core\\dynamic_point_projection_interface_shadow_boundary.py",
        "future_checker_script": "scripts\\validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py",
        "checker_creation_authorized": False,
        "helper_creation_authorized": False,
        "forbidden_families": {
            "monolith": ["taichi_global_bathymetry"],
            "projection_formula": ["projection formula", "project_point", "lon_lat_to_screen"],
            "longitude_flip_formula": ["flip_longitude", "longitude flip formula"],
            "latitude_flip_formula": ["flip_latitude", "latitude flip formula"],
            "mask_formula": ["mask formula", "globe_mask", "mask_overlay_to_globe"],
            "renderer_frame_transform": ["renderer frame transform", "rotate_view_to_world"],
            "runtime_renderer_host": ["TaichiGlobeRenderer", "taichi", "PyQt6", "PySide6", "vispy", "Qt", "VisPy"],
            "dynamic_point_screen_projection_execution": ["project_ais_to_screen", "project_aircraft_to_screen", "screen projection execution"],
            "hot_path_alpha_apply_composition": ["alpha_compose", "apply path", "composition apply"],
            "controller_selection": ["selected vehicle runtime", "picker", "hit-test", "controller mutation"],
            "dataframe_runtime": ["pandas", "datashader", "numpy"],
            "live_source": ["pymysql", "sqlalchemy", "websocket", "AISStream", "ADSBStream"],
            "artifact_metadata": ["metadata sidecar writer", "artifact writer", "state writer", "runtime JSON writer"],
            "coordinate_correctness_claim": ["coordinate correctness", "projection correctness"],
            "visual_correctness_claim": ["visual correctness", "visual parity"],
        },
        "allowed_string_labels": sorted(REQUIRED_ALLOWED_STRING_LABELS),
        "allowed_data_surfaces": sorted(REQUIRED_ALLOWED_DATA_SURFACES),
        "checked_ast_nodes_planned": sorted(REQUIRED_AST_NODES),
        "missing_target_behavior": {
            "candidate_exists": False,
            "status": "not_applicable_candidate_missing",
            "boundary_passed": True,
            "exit_code": 0,
            "json_output_required": True,
        },
        "negative_self_test_expectation": {
            "required": True,
            "must_detect_all_forbidden_families": True,
            "covered_forbidden_families": sorted(REQUIRED_FORBIDDEN_FAMILIES),
        },
        "generic_checker_status": {
            "trust_level": "L1_shadow",
            "blocking": False,
            "replacement_authorized": False,
            "profile_change_authorized": False,
        },
        "decision_output": {
            "planning_gate_passed": True,
            "checker_creation_authorized": False,
            "helper_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "generic_checker_blocking": False,
            "generic_checker_replacement_authorized": False,
            "runtime_merge_enabled": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "readiness_claimed": False,
            "recommended_next_gate": "dynamic_point_projection_interface_shadow_import_boundary_checker_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point projection interface shadow import-boundary planning gate. "
            "No helper module creation, no source movement, no production source change, "
            "no checker script creation, no checker script change, no generic checker trust-level change, "
            "no generic checker blocking behavior change, no generic profile change, no monolith import, "
            "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no controller selection/picker/hit-test mutation, "
            "no metadata/output schema change, no cross-organ integration implementation, "
            "no runtime merge enablement, no coordinate/visual correctness claim, "
            "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointProjectionInterfaceShadowImportBoundaryPlanningTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_projection_interface_shadow_import_boundary_planning_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "base_camp_rollback_anchor",
                "local_pattern_source",
                "shadow_source",
                "future_helper_target",
                "future_checker_script",
                "checker_creation_authorized",
                "helper_creation_authorized",
                "forbidden_families",
                "allowed_string_labels",
                "allowed_data_surfaces",
                "checked_ast_nodes_planned",
                "missing_target_behavior",
                "negative_self_test_expectation",
                "generic_checker_status",
                "decision_output",
                "boundary_statement",
            },
        )

    def test_anchor_and_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["shadow_source"], "6289c60")

    def test_future_paths_exact(self):
        self.assertEqual(
            self.packet["future_helper_target"],
            "render_core\\dynamic_point_projection_interface_shadow_boundary.py",
        )
        self.assertEqual(
            self.packet["future_checker_script"],
            "scripts\\validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py",
        )

    def test_checker_and_helper_creation_not_authorized(self):
        self.assertIs(self.packet["checker_creation_authorized"], False)
        self.assertIs(self.packet["helper_creation_authorized"], False)
        self.assertIs(self.packet["decision_output"]["checker_creation_authorized"], False)
        self.assertIs(self.packet["decision_output"]["helper_creation_authorized"], False)

    def test_all_required_forbidden_families_present(self):
        self.assertEqual(set(self.packet["forbidden_families"]), REQUIRED_FORBIDDEN_FAMILIES)
        for family, terms in self.packet["forbidden_families"].items():
            self.assertTrue(terms, family)

    def test_all_required_allowed_labels_present(self):
        self.assertEqual(set(self.packet["allowed_string_labels"]), REQUIRED_ALLOWED_STRING_LABELS)

    def test_all_required_allowed_data_surfaces_present(self):
        self.assertEqual(set(self.packet["allowed_data_surfaces"]), REQUIRED_ALLOWED_DATA_SURFACES)
        self.assertIn("no_callable_formula_refs", self.packet["allowed_data_surfaces"])
        self.assertIn("no_renderer_buffer_refs", self.packet["allowed_data_surfaces"])

    def test_all_required_ast_nodes_planned(self):
        self.assertEqual(set(self.packet["checked_ast_nodes_planned"]), REQUIRED_AST_NODES)

    def test_missing_target_behavior_is_pass(self):
        behavior = self.packet["missing_target_behavior"]
        self.assertIs(behavior["candidate_exists"], False)
        self.assertEqual(behavior["status"], "not_applicable_candidate_missing")
        self.assertIs(behavior["boundary_passed"], True)
        self.assertEqual(behavior["exit_code"], 0)
        self.assertIs(behavior["json_output_required"], True)

    def test_negative_self_test_covers_all_forbidden_families(self):
        expectation = self.packet["negative_self_test_expectation"]
        self.assertIs(expectation["required"], True)
        self.assertIs(expectation["must_detect_all_forbidden_families"], True)
        self.assertEqual(set(expectation["covered_forbidden_families"]), REQUIRED_FORBIDDEN_FAMILIES)

    def test_generic_checker_remains_non_blocking_and_not_replacement(self):
        status = self.packet["generic_checker_status"]
        self.assertEqual(status["trust_level"], "L1_shadow")
        self.assertIs(status["blocking"], False)
        self.assertIs(status["replacement_authorized"], False)
        self.assertIs(status["profile_change_authorized"], False)

    def test_no_formula_movement_or_correctness_claims(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["formula_movement_authorized"], False)
        self.assertIs(decision["coordinate_correctness_claimed"], False)
        self.assertIs(decision["visual_correctness_claimed"], False)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", self.packet["boundary_statement"])
        self.assertIn("no coordinate/visual correctness claim", self.packet["boundary_statement"])

    def test_no_readiness_or_source_movement(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["source_movement_authorized"], False)
        self.assertIs(decision["runtime_merge_enabled"], False)
        self.assertIs(decision["generic_checker_blocking"], False)
        self.assertIs(decision["generic_checker_replacement_authorized"], False)
        self.assertIs(decision["readiness_claimed"], False)

    def test_recommended_next_gate_is_checker_gate(self):
        self.assertEqual(
            self.packet["decision_output"]["recommended_next_gate"],
            "dynamic_point_projection_interface_shadow_import_boundary_checker_gate",
        )


if __name__ == "__main__":
    unittest.main()
