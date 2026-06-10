from __future__ import annotations

import unittest

from tests import test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_contract_planning as reduction_planning


FUTURE_HELPER_TARGET = "render_core/dynamic_point_presentation_reduction_boundary.py"
FUTURE_CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py"
RECOMMENDED_NEXT_GATE = "dynamic_point_lod_view_frame_presentation_reduction_import_boundary_checker_gate"

AST_NODE_COVERAGE = [
    "Import",
    "ImportFrom",
    "Name",
    "Attribute",
    "Call",
    "FunctionDef",
    "AsyncFunctionDef",
    "ClassDef",
]

ALLOWED_STRING_LABELS = [
    "rendered_lower_than_visible",
    "presentation_or_sampling_reduction_candidate",
    "visible_count_observation",
    "rendered_count_observation",
    "source_loss_not_inferred",
    "frame_truth_not_claimed",
    "frame_visible_not_observed",
    "transparent_globe_leak_not_inferred",
    "visual_correctness_not_claimed",
    "readiness_not_claimed",
    "source_lineage_guarded_by_source_lineage_guard_boundary",
    "presentation_count_boundary_reference",
    "sampling_visibility_boundary_reference",
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
    "source_lineage_mutation",
    "source_loss_interpretation",
    "frame_truth_claim",
    "transparent_globe_leak_inference",
    "correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "performance_claim",
    "transparent_globe_leak_fix_claim",
    "c4_odoriba_bypass",
    "label_executable_reference",
]

CHECKER_EXPECTATION = {
    "dedicated_checker_required": True,
    "existing_checker_reusable": False,
    "existing_checkers_pattern_reference_only": True,
    "ast_only": True,
    "target_imported": False,
    "target_executed": False,
    "missing_target_status": "not_applicable_candidate_missing",
    "missing_target_boundary_passed": True,
    "syntax_error_json_fail": True,
    "syntax_error_nonzero_exit": True,
    "ast_node_coverage": AST_NODE_COVERAGE,
    "allowed_string_labels": ALLOWED_STRING_LABELS,
    "forbidden_families": FORBIDDEN_FAMILIES,
    "allowed_labels_pass_as_string_data_only": True,
    "allowed_labels_fail_as_executable_reference": True,
    "negative_self_test_must_cover_all_forbidden_families": True,
}

CHECKER_PLANNING_MATRIX = [
    {
        "surface": "rendered_lower_than_visible",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["source_loss_interpretation", "frame_truth_claim"],
        "checker_family": "presentation_reduction_contract",
    },
    {
        "surface": "presentation_or_sampling_reduction_candidate",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["runtime_probe", "sampling_formula_movement"],
        "checker_family": "presentation_reduction_contract",
    },
    {
        "surface": "source_loss_not_inferred",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["source_loss_interpretation", "source_lineage_mutation"],
        "checker_family": "source_guard",
    },
    {
        "surface": "frame_truth_not_claimed",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["frame_truth_claim", "frame_buffer", "renderer_runtime"],
        "checker_family": "frame_stop_line",
    },
    {
        "surface": "transparent_globe_leak_not_inferred",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["transparent_globe_leak_inference", "transparent_globe_leak_fix_claim"],
        "checker_family": "leak_stop_line",
    },
    {
        "surface": "presentation_count_boundary_reference",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["render_core_change", "helper_creation"],
        "checker_family": "evidence_reference_only",
    },
    {
        "surface": "sampling_visibility_boundary_reference",
        "allowed_as_string_label": True,
        "forbidden_as_executable_reference": True,
        "forbidden_drift": ["runtime_probe", "formula_movement"],
        "checker_family": "evidence_reference_only",
    },
]

DECISION_OUTPUT = {
    "presentation_reduction_checker_planning_passed": True,
    "dedicated_checker_required": True,
    "existing_checker_reusable": False,
    "checker_creation_authorized": False,
    "helper_creation_authorized": False,
    "checker_modification_authorized": False,
    "render_core_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "real_source_read_authorized": False,
    "source_lineage_mutation_authorized": False,
    "raw_row_seam_runtime_authorized": False,
    "direct_c3_to_c1_integration_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "source_loss_interpretation_authorized": False,
    "frame_truth_claim_authorized": False,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "performance_claimed": False,
    "rrkal_wide_methodology_claimed": False,
    "recommended_next_gate": RECOMMENDED_NEXT_GATE,
}

PRESENTATION_REDUCTION_CHECKER_PLANNING_PACKET = {
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "checker_expectation": CHECKER_EXPECTATION,
    "planning_matrix": CHECKER_PLANNING_MATRIX,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": (
        "Docs/test-only dynamic point LOD view-frame presentation reduction import-boundary checker planning gate. "
        "No checker creation, no helper creation, no checker modification, no render_core change, "
        "no runtime/probe/renderer/frame/formula/source behavior change, no source-loss/frame-truth/"
        "leak/correctness/readiness/performance claim, no c_4/Odoriba bypass, and no push."
    ),
}


def _matrix_by_surface() -> dict[str, dict[str, object]]:
    return {row["surface"]: row for row in CHECKER_PLANNING_MATRIX}


class DynamicPointPresentationReductionImportBoundaryCheckerPlanningTest(unittest.TestCase):
    def test_previous_contract_planning_authorized_checker_planning_only(self) -> None:
        self.assertEqual(
            reduction_planning.DECISION_OUTPUT["recommended_next_gate"],
            "dynamic_point_lod_view_frame_presentation_reduction_import_boundary_checker_planning_gate",
        )
        self.assertFalse(reduction_planning.DECISION_OUTPUT["helper_creation_authorized"])
        self.assertFalse(reduction_planning.DECISION_OUTPUT["checker_creation_authorized"])
        self.assertFalse(reduction_planning.DECISION_OUTPUT["source_loss_interpretation_authorized"])
        self.assertFalse(reduction_planning.DECISION_OUTPUT["frame_truth_claim_authorized"])

    def test_future_targets_are_planning_targets_only(self) -> None:
        self.assertEqual(FUTURE_HELPER_TARGET, "render_core/dynamic_point_presentation_reduction_boundary.py")
        self.assertEqual(
            FUTURE_CHECKER_TARGET,
            "scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py",
        )
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])
        self.assertFalse(DECISION_OUTPUT["checker_creation_authorized"])
        self.assertFalse(DECISION_OUTPUT["render_core_change_authorized"])

    def test_checker_expectation_requires_dedicated_ast_only_checker(self) -> None:
        self.assertTrue(CHECKER_EXPECTATION["dedicated_checker_required"])
        self.assertFalse(CHECKER_EXPECTATION["existing_checker_reusable"])
        self.assertTrue(CHECKER_EXPECTATION["existing_checkers_pattern_reference_only"])
        self.assertTrue(CHECKER_EXPECTATION["ast_only"])
        self.assertFalse(CHECKER_EXPECTATION["target_imported"])
        self.assertFalse(CHECKER_EXPECTATION["target_executed"])
        self.assertEqual(CHECKER_EXPECTATION["missing_target_status"], "not_applicable_candidate_missing")
        self.assertTrue(CHECKER_EXPECTATION["missing_target_boundary_passed"])
        self.assertTrue(CHECKER_EXPECTATION["syntax_error_json_fail"])
        self.assertTrue(CHECKER_EXPECTATION["syntax_error_nonzero_exit"])

    def test_ast_node_coverage_is_complete_for_planned_checker(self) -> None:
        self.assertEqual(
            AST_NODE_COVERAGE,
            ["Import", "ImportFrom", "Name", "Attribute", "Call", "FunctionDef", "AsyncFunctionDef", "ClassDef"],
        )

    def test_allowed_string_labels_are_data_only(self) -> None:
        self.assertEqual(
            ALLOWED_STRING_LABELS,
            [
                "rendered_lower_than_visible",
                "presentation_or_sampling_reduction_candidate",
                "visible_count_observation",
                "rendered_count_observation",
                "source_loss_not_inferred",
                "frame_truth_not_claimed",
                "frame_visible_not_observed",
                "transparent_globe_leak_not_inferred",
                "visual_correctness_not_claimed",
                "readiness_not_claimed",
                "source_lineage_guarded_by_source_lineage_guard_boundary",
                "presentation_count_boundary_reference",
                "sampling_visibility_boundary_reference",
            ],
        )
        self.assertTrue(CHECKER_EXPECTATION["allowed_labels_pass_as_string_data_only"])
        self.assertTrue(CHECKER_EXPECTATION["allowed_labels_fail_as_executable_reference"])
        for row in CHECKER_PLANNING_MATRIX:
            self.assertTrue(row["allowed_as_string_label"], row["surface"])
            self.assertTrue(row["forbidden_as_executable_reference"], row["surface"])

    def test_forbidden_family_plan_covers_required_drifts(self) -> None:
        required = {
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
            "source_lineage_mutation",
            "source_loss_interpretation",
            "frame_truth_claim",
            "transparent_globe_leak_inference",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "performance_claim",
            "transparent_globe_leak_fix_claim",
            "c4_odoriba_bypass",
            "label_executable_reference",
        }
        self.assertEqual(set(FORBIDDEN_FAMILIES), required)
        self.assertTrue(CHECKER_EXPECTATION["negative_self_test_must_cover_all_forbidden_families"])

    def test_planning_matrix_blocks_source_loss_frame_truth_and_leak_drift(self) -> None:
        matrix = _matrix_by_surface()
        self.assertIn("source_loss_interpretation", matrix["rendered_lower_than_visible"]["forbidden_drift"])
        self.assertIn("frame_truth_claim", matrix["rendered_lower_than_visible"]["forbidden_drift"])
        self.assertIn("transparent_globe_leak_inference", matrix["transparent_globe_leak_not_inferred"]["forbidden_drift"])
        self.assertIn("transparent_globe_leak_fix_claim", matrix["transparent_globe_leak_not_inferred"]["forbidden_drift"])
        self.assertIn("source_lineage_mutation", matrix["source_loss_not_inferred"]["forbidden_drift"])
        self.assertIn("runtime_probe", matrix["sampling_visibility_boundary_reference"]["forbidden_drift"])

    def test_decision_output_keeps_all_creation_and_runtime_authorizations_closed(self) -> None:
        required_true = [
            "presentation_reduction_checker_planning_passed",
            "dedicated_checker_required",
        ]
        for key in required_true:
            self.assertTrue(DECISION_OUTPUT[key], key)
        self.assertFalse(DECISION_OUTPUT["existing_checker_reusable"])

        required_false = [
            "checker_creation_authorized",
            "helper_creation_authorized",
            "checker_modification_authorized",
            "render_core_change_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "real_source_read_authorized",
            "source_lineage_mutation_authorized",
            "raw_row_seam_runtime_authorized",
            "direct_c3_to_c1_integration_authorized",
            "c4_odoriba_bypass_authorized",
            "source_loss_interpretation_authorized",
            "frame_truth_claim_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "performance_claimed",
            "rrkal_wide_methodology_claimed",
        ]
        for key in required_false:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_recommended_next_gate_is_checker_creation(self) -> None:
        self.assertEqual(DECISION_OUTPUT["recommended_next_gate"], RECOMMENDED_NEXT_GATE)


if __name__ == "__main__":
    unittest.main()
