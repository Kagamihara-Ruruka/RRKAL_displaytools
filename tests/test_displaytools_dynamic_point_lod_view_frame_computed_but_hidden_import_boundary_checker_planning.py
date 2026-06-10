"""Planning gate for computed-but-hidden import-boundary checker."""

from __future__ import annotations

import unittest


FUTURE_HELPER_TARGET = "render_core/dynamic_point_computed_but_hidden_boundary.py"
FUTURE_CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py"

ALLOWED_LABELS = [
    "source_present_token",
    "computed_point_token",
    "hidden_visibility_token",
    "frame_visible_not_observed",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "computed_but_hidden_contract",
    "transparent_globe_leak_not_inferred",
    "source_loss_not_inferred",
    "frame_buffer_read_blocked",
    "renderer_execution_blocked",
    "readiness_not_claimed",
]

FORBIDDEN_FAMILIES = [
    "monolith",
    "runtime_probe",
    "render_if_needed",
    "controller_runtime",
    "renderer_runtime",
    "frame_buffer",
    "artifact_writer",
    "projection_formula",
    "mask_formula",
    "sampling_formula_movement",
    "alpha_compose_formula",
    "dataframe_runtime",
    "live_source",
    "cache_database_io",
    "hidden_as_missing_interpretation",
    "source_lineage_loss_interpretation",
    "transparent_globe_leak_inference",
    "correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "transparent_globe_leak_fix_claim",
    "label_executable_reference",
]

AST_NODE_COVERAGE = [
    "ast.Import",
    "ast.ImportFrom",
    "ast.Name",
    "ast.Attribute",
    "ast.Call",
    "ast.FunctionDef",
    "ast.AsyncFunctionDef",
    "ast.ClassDef",
]

NEGATIVE_SELF_TEST_EXPECTATIONS = [
    {
        "family": "monolith",
        "example": "import taichi_global_bathymetry",
        "expected_status": "fail",
    },
    {
        "family": "runtime_probe",
        "example": "run_probe()",
        "expected_status": "fail",
    },
    {
        "family": "render_if_needed",
        "example": "from taichi_global_bathymetry import render_if_needed",
        "expected_status": "fail",
    },
    {
        "family": "controller_runtime",
        "example": "HybridRenderController",
        "expected_status": "fail",
    },
    {
        "family": "renderer_runtime",
        "example": "renderer.render(None)",
        "expected_status": "fail",
    },
    {
        "family": "frame_buffer",
        "example": "frame_rgba",
        "expected_status": "fail",
    },
    {
        "family": "artifact_writer",
        "example": "Image.fromarray(None).save('x.png')",
        "expected_status": "fail",
    },
    {
        "family": "projection_formula",
        "example": "project_ais_to_screen(None)",
        "expected_status": "fail",
    },
    {
        "family": "mask_formula",
        "example": "mask_overlay_to_globe(None, None)",
        "expected_status": "fail",
    },
    {
        "family": "sampling_formula_movement",
        "example": "_sample_projected_frame(None, 'ais')",
        "expected_status": "fail",
    },
    {
        "family": "alpha_compose_formula",
        "example": "alpha_compose(None, None)",
        "expected_status": "fail",
    },
    {
        "family": "dataframe_runtime",
        "example": "pd.DataFrame(np.asarray([]))",
        "expected_status": "fail",
    },
    {
        "family": "live_source",
        "example": "AISSource()",
        "expected_status": "fail",
    },
    {
        "family": "cache_database_io",
        "example": "sqlite3.connect('x.db')",
        "expected_status": "fail",
    },
    {
        "family": "hidden_as_missing_interpretation",
        "example": "hidden_as_missing = True",
        "expected_status": "fail",
    },
    {
        "family": "source_lineage_loss_interpretation",
        "example": "source_lineage_loss_claimed = True",
        "expected_status": "fail",
    },
    {
        "family": "transparent_globe_leak_inference",
        "example": "transparent_globe_leak_inferred = True",
        "expected_status": "fail",
    },
    {
        "family": "correctness_claim",
        "example": "visual_correctness_claimed = True",
        "expected_status": "fail",
    },
    {
        "family": "visual_parity_claim",
        "example": "visual_parity_claimed = True",
        "expected_status": "fail",
    },
    {
        "family": "readiness_claim",
        "example": "readiness_claimed = True",
        "expected_status": "fail",
    },
    {
        "family": "transparent_globe_leak_fix_claim",
        "example": "transparent_globe_leak_fix_claimed = True",
        "expected_status": "fail",
    },
    {
        "family": "label_executable_reference",
        "example": "return hidden_is_not_missing",
        "expected_status": "fail",
    },
]

CHECKER_EXPECTATION = {
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "ast_only": True,
    "target_imported": False,
    "target_executed": False,
    "missing_target_status": "not_applicable_candidate_missing",
    "missing_target_boundary_passed": True,
    "syntax_error_status": "syntax_error_json_fail_nonzero_exit",
    "ast_node_coverage": AST_NODE_COVERAGE,
    "allowed_labels_pass_as_string_data_only": True,
    "allowed_labels_fail_as_executable_reference": True,
    "negative_self_test_covers_all_forbidden_families": True,
}

DECISION_OUTPUT = {
    "computed_but_hidden_import_boundary_checker_planning_gate_passed": True,
    "future_helper_target_defined": True,
    "future_checker_target_defined": True,
    "allowed_labels_defined": True,
    "forbidden_families_defined": True,
    "checker_expectation_defined": True,
    "missing_target_behavior_defined": True,
    "negative_self_test_expectation_defined": True,
    "checker_creation_authorized": False,
    "helper_creation_authorized": False,
    "render_core_change_authorized": False,
    "existing_checker_modification_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "hidden_as_missing_authorized": False,
    "source_lineage_loss_interpretation_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_gate",
}

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_planning.v1",
    "evidence_sources": {
        "computed_but_hidden_contract_planning": "3c86eea",
        "post_presentation_count_next_bridge_selection": "d25e94c",
        "presentation_count_cartography_update": "a5fe556",
        "sampling_visibility_minimal_boundary": "76abda8",
        "occlusion_responsibility_boundary": "44356e9",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "presentation_count_checker_pattern_reference": "31b0e18",
        "runtime_executed_by_this_gate": False,
    },
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "allowed_labels": ALLOWED_LABELS,
    "forbidden_families": FORBIDDEN_FAMILIES,
    "checker_expectation": CHECKER_EXPECTATION,
    "negative_self_test_expectations": NEGATIVE_SELF_TEST_EXPECTATIONS,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": (
        "Docs/test-only dynamic point LOD view-frame computed-but-hidden import-boundary checker planning gate. "
        "No checker creation, no helper creation, no render_core change, no existing checker modification, "
        "no runtime probe change, no taichi_global_bathymetry change, no render_if_needed, no controller, "
        "no renderer, no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing "
        "interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, "
        "no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push."
    ),
}


class DynamicPointComputedButHiddenImportBoundaryCheckerPlanningTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "future_helper_target",
                "future_checker_target",
                "allowed_labels",
                "forbidden_families",
                "checker_expectation",
                "negative_self_test_expectations",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_future_targets_are_planned_only(self) -> None:
        self.assertEqual(PACKET["future_helper_target"], FUTURE_HELPER_TARGET)
        self.assertEqual(PACKET["future_checker_target"], FUTURE_CHECKER_TARGET)
        decision = PACKET["decision_output"]
        self.assertFalse(decision["checker_creation_authorized"])
        self.assertFalse(decision["helper_creation_authorized"])
        self.assertFalse(decision["render_core_change_authorized"])

    def test_allowed_labels_are_exact(self) -> None:
        self.assertEqual(
            set(PACKET["allowed_labels"]),
            {
                "source_present_token",
                "computed_point_token",
                "hidden_visibility_token",
                "frame_visible_not_observed",
                "hidden_is_not_missing",
                "occluded_is_not_source_lineage_loss",
                "computed_but_hidden_contract",
                "transparent_globe_leak_not_inferred",
                "source_loss_not_inferred",
                "frame_buffer_read_blocked",
                "renderer_execution_blocked",
                "readiness_not_claimed",
            },
        )

    def test_forbidden_families_are_exact(self) -> None:
        self.assertEqual(
            set(PACKET["forbidden_families"]),
            {
                "monolith",
                "runtime_probe",
                "render_if_needed",
                "controller_runtime",
                "renderer_runtime",
                "frame_buffer",
                "artifact_writer",
                "projection_formula",
                "mask_formula",
                "sampling_formula_movement",
                "alpha_compose_formula",
                "dataframe_runtime",
                "live_source",
                "cache_database_io",
                "hidden_as_missing_interpretation",
                "source_lineage_loss_interpretation",
                "transparent_globe_leak_inference",
                "correctness_claim",
                "visual_parity_claim",
                "readiness_claim",
                "transparent_globe_leak_fix_claim",
                "label_executable_reference",
            },
        )

    def test_checker_expectation_matches_ast_only_pattern(self) -> None:
        expectation = PACKET["checker_expectation"]
        self.assertTrue(expectation["ast_only"])
        self.assertFalse(expectation["target_imported"])
        self.assertFalse(expectation["target_executed"])
        self.assertEqual(expectation["missing_target_status"], "not_applicable_candidate_missing")
        self.assertTrue(expectation["missing_target_boundary_passed"])
        self.assertEqual(expectation["syntax_error_status"], "syntax_error_json_fail_nonzero_exit")
        self.assertEqual(set(expectation["ast_node_coverage"]), set(AST_NODE_COVERAGE))
        self.assertTrue(expectation["allowed_labels_pass_as_string_data_only"])
        self.assertTrue(expectation["allowed_labels_fail_as_executable_reference"])
        self.assertTrue(expectation["negative_self_test_covers_all_forbidden_families"])

    def test_negative_self_test_expectations_cover_all_forbidden_families(self) -> None:
        rows = {row["family"]: row for row in PACKET["negative_self_test_expectations"]}
        self.assertEqual(set(rows), set(PACKET["forbidden_families"]))
        for row in rows.values():
            self.assertTrue(row["example"])
            self.assertEqual(row["expected_status"], "fail")

    def test_label_distinction_is_required(self) -> None:
        expectation = PACKET["checker_expectation"]
        self.assertTrue(expectation["allowed_labels_pass_as_string_data_only"])
        self.assertTrue(expectation["allowed_labels_fail_as_executable_reference"])
        self.assertIn("label_executable_reference", PACKET["forbidden_families"])

    def test_hidden_missing_and_source_lineage_loss_are_forbidden(self) -> None:
        families = set(PACKET["forbidden_families"])
        self.assertIn("hidden_as_missing_interpretation", families)
        self.assertIn("source_lineage_loss_interpretation", families)
        self.assertIn("transparent_globe_leak_inference", families)
        self.assertIn("transparent_globe_leak_fix_claim", families)
        decision = PACKET["decision_output"]
        self.assertFalse(decision["hidden_as_missing_authorized"])
        self.assertFalse(decision["source_lineage_loss_interpretation_authorized"])
        self.assertFalse(decision["transparent_globe_leak_inference_authorized"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["computed_but_hidden_import_boundary_checker_planning_gate_passed"])
        self.assertTrue(decision["allowed_labels_defined"])
        self.assertTrue(decision["forbidden_families_defined"])
        self.assertTrue(decision["checker_expectation_defined"])
        for key in (
            "checker_creation_authorized",
            "helper_creation_authorized",
            "render_core_change_authorized",
            "existing_checker_modification_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "hidden_as_missing_authorized",
            "source_lineage_loss_interpretation_authorized",
            "transparent_globe_leak_inference_authorized",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_recommended_next_gate_is_checker_creation(self) -> None:
        self.assertEqual(
            PACKET["decision_output"]["recommended_next_gate"],
            "dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_gate",
        )

    def test_boundary_statement(self) -> None:
        statement = PACKET["boundary_statement"]
        self.assertIn("No checker creation", statement)
        self.assertIn("no helper creation", statement)
        self.assertIn("no render_core change", statement)
        self.assertIn("no existing checker modification", statement)
        self.assertIn("no frame buffer read", statement)
        self.assertIn("no hidden-as-missing interpretation", statement)
        self.assertIn("no source-lineage-loss interpretation", statement)
        self.assertIn("no transparent-globe leak inference", statement)
        self.assertIn("no RRKAL-wide methodology promotion", statement)
        self.assertIn("no push", statement)


if __name__ == "__main__":
    unittest.main()