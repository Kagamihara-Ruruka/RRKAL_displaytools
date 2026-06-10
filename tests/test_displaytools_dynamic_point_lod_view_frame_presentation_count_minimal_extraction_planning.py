"""Minimal extraction planning for future presentation count boundary helpers."""

from __future__ import annotations

import unittest
from pathlib import Path


FUTURE_HELPER_TARGET = "render_core/dynamic_point_presentation_count_boundary.py"
CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py"

ALLOWED_LABELS = [
    "visible_count",
    "rendered_count",
    "visible_count_observation",
    "rendered_count_observation",
    "rendered_lower_than_visible",
    "sampling_or_presentation_reduction_candidate",
    "presentation_count_contract",
    "source_lineage_integrity_token",
    "frame_visible_not_observed",
    "transparent_globe_leak_not_inferred",
    "source_loss_not_inferred",
    "visual_correctness_not_claimed",
    "readiness_not_claimed",
]

FORBIDDEN_FIELDS = [
    "runtime_probe",
    "render_if_needed",
    "controller_runtime",
    "renderer_runtime",
    "frame_buffer",
    "artifact_writer",
    "projection_formula",
    "mask_formula",
    "sampling_formula_movement",
    "dataframe_runtime",
    "live_source",
    "cache_database_io",
    "source_loss_interpretation",
    "transparent_globe_leak_inference",
    "coordinate_correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "transparent_globe_leak_fix_claim",
]

HELPER_FAMILY_MATRIX = [
    {
        "helper_family": "build_dynamic_point_visible_count_contract_descriptor",
        "intended_output_keys": ["visible_count", "visible_count_observation", "presentation_count_contract"],
        "allowed_labels": ["visible_count", "visible_count_observation", "presentation_count_contract"],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "read_only_no_mutation",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "readiness_level": "minimal_extraction_candidate",
        "checker_coverage_expectation": "presentation_count_checker_required",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_rendered_count_contract_descriptor",
        "intended_output_keys": ["rendered_count", "rendered_count_observation", "presentation_count_contract"],
        "allowed_labels": ["rendered_count", "rendered_count_observation", "presentation_count_contract"],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "read_only_no_mutation",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "readiness_level": "minimal_extraction_candidate",
        "checker_coverage_expectation": "presentation_count_checker_required",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_presentation_reduction_candidate_descriptor",
        "intended_output_keys": ["rendered_lower_than_visible", "sampling_or_presentation_reduction_candidate"],
        "allowed_labels": ["rendered_lower_than_visible", "sampling_or_presentation_reduction_candidate"],
        "forbidden_fields": FORBIDDEN_FIELDS + ["source_loss_claimed"],
        "source_lineage_impact": "source_loss_not_inferred",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "readiness_level": "minimal_extraction_candidate",
        "checker_coverage_expectation": "source_loss_interpretation_must_fail",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_presentation_count_source_lineage_guard_descriptor",
        "intended_output_keys": ["source_lineage_integrity_token", "source_loss_not_inferred"],
        "allowed_labels": ["source_lineage_integrity_token", "source_loss_not_inferred"],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "guard_only_no_source_loss",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "readiness_level": "minimal_extraction_candidate",
        "checker_coverage_expectation": "source_loss_interpretation_must_fail",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_presentation_count_stop_line_ledger",
        "intended_output_keys": [
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
        ],
        "allowed_labels": [
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
        ],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "none",
        "renderer_frame_dependency": "blocked_stop_line_only",
        "formula_dependency": "none",
        "readiness_level": "stop_line_ledger_candidate",
        "checker_coverage_expectation": "frame_buffer_and_leak_claim_must_fail",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "dynamic_point_presentation_count_boundary_descriptor",
        "intended_output_keys": ["allowed_outputs", "owned_semantics", "blocked_actions"],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "descriptor_only",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "readiness_level": "minimal_extraction_candidate",
        "checker_coverage_expectation": "full_forbidden_family_coverage_required",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "dynamic_point_presentation_count_planning_bundle",
        "intended_output_keys": ["minimal_extraction_planning_passed", "checker_protected", "helper_creation_authorized"],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "bundle_only_no_mutation",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "readiness_level": "planning_bundle_candidate",
        "checker_coverage_expectation": "checker_must_pass_before_helper_creation",
        "helper_creation_authorized": False,
    },
]

DECISION_OUTPUT = {
    "minimal_extraction_planning_passed": True,
    "future_helper_target": FUTURE_HELPER_TARGET,
    "checker_available_for_future_helper": True,
    "checker_target": CHECKER_TARGET,
    "dict_list_scalar_output_only": True,
    "visible_count_contract_field_allowed": True,
    "rendered_count_contract_field_allowed": True,
    "rendered_lower_than_visible_reduction_candidate_only": True,
    "source_loss_interpretation_authorized": False,
    "frame_truth_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "helper_creation_authorized": False,
    "checker_modification_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_presentation_count_minimal_extraction_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame presentation count minimal extraction planning gate. "
    "No helper creation, no render_core/dynamic_point_presentation_count_boundary.py creation, "
    "no checker modification, no runtime probe change, no taichi_global_bathymetry change, "
    "no render_if_needed, no controller, no renderer, no frame buffer read, no artifact generation, "
    "no projection/mask/sampling formula movement, no source-loss interpretation, no transparent-globe "
    "leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology "
    "promotion, and no push."
)


class DynamicPointPresentationCountMinimalExtractionPlanningTest(unittest.TestCase):
    def test_future_helper_target_is_planned_without_authorizing_creation(self) -> None:
        self.assertEqual(FUTURE_HELPER_TARGET, "render_core/dynamic_point_presentation_count_boundary.py")
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])

    def test_expected_helper_families_are_planned(self) -> None:
        self.assertEqual(
            {row["helper_family"] for row in HELPER_FAMILY_MATRIX},
            {
                "build_dynamic_point_visible_count_contract_descriptor",
                "build_dynamic_point_rendered_count_contract_descriptor",
                "build_dynamic_point_presentation_reduction_candidate_descriptor",
                "build_dynamic_point_presentation_count_source_lineage_guard_descriptor",
                "build_dynamic_point_presentation_count_stop_line_ledger",
                "dynamic_point_presentation_count_boundary_descriptor",
                "dynamic_point_presentation_count_planning_bundle",
            },
        )

    def test_each_helper_family_has_required_planning_fields(self) -> None:
        required = {
            "helper_family",
            "intended_output_keys",
            "allowed_labels",
            "forbidden_fields",
            "source_lineage_impact",
            "renderer_frame_dependency",
            "formula_dependency",
            "readiness_level",
            "checker_coverage_expectation",
            "helper_creation_authorized",
        }
        for row in HELPER_FAMILY_MATRIX:
            self.assertEqual(set(row), required)
            self.assertTrue(row["intended_output_keys"])
            self.assertTrue(row["allowed_labels"])
            self.assertTrue(row["forbidden_fields"])
            self.assertFalse(row["helper_creation_authorized"])

    def test_all_outputs_are_planned_as_dict_list_scalar_only(self) -> None:
        self.assertTrue(DECISION_OUTPUT["dict_list_scalar_output_only"])
        for row in HELPER_FAMILY_MATRIX:
            self.assertNotIn("callable", row["intended_output_keys"])
            self.assertNotIn("runtime_object", row["intended_output_keys"])

    def test_checker_can_protect_future_helper(self) -> None:
        self.assertTrue(Path(CHECKER_TARGET).exists())
        self.assertTrue(DECISION_OUTPUT["checker_available_for_future_helper"])
        for row in HELPER_FAMILY_MATRIX:
            self.assertTrue(row["checker_coverage_expectation"])

    def test_visible_and_rendered_count_fields_remain_contract_safe(self) -> None:
        self.assertTrue(DECISION_OUTPUT["visible_count_contract_field_allowed"])
        self.assertTrue(DECISION_OUTPUT["rendered_count_contract_field_allowed"])
        rows = {row["helper_family"]: row for row in HELPER_FAMILY_MATRIX}
        self.assertIn("visible_count", rows["build_dynamic_point_visible_count_contract_descriptor"]["allowed_labels"])
        self.assertIn("rendered_count", rows["build_dynamic_point_rendered_count_contract_descriptor"]["allowed_labels"])

    def test_reduction_candidate_is_not_source_loss(self) -> None:
        self.assertTrue(DECISION_OUTPUT["rendered_lower_than_visible_reduction_candidate_only"])
        self.assertFalse(DECISION_OUTPUT["source_loss_interpretation_authorized"])
        row = next(
            item
            for item in HELPER_FAMILY_MATRIX
            if item["helper_family"] == "build_dynamic_point_presentation_reduction_candidate_descriptor"
        )
        self.assertEqual(row["source_lineage_impact"], "source_loss_not_inferred")
        self.assertIn("source_loss_claimed", row["forbidden_fields"])

    def test_frame_truth_and_leak_inference_remain_forbidden(self) -> None:
        self.assertFalse(DECISION_OUTPUT["frame_truth_authorized"])
        self.assertFalse(DECISION_OUTPUT["transparent_globe_leak_inference_authorized"])
        row = next(
            item
            for item in HELPER_FAMILY_MATRIX
            if item["helper_family"] == "build_dynamic_point_presentation_count_stop_line_ledger"
        )
        self.assertEqual(row["renderer_frame_dependency"], "blocked_stop_line_only")
        self.assertIn("transparent_globe_leak_not_inferred", row["allowed_labels"])

    def test_all_forbidden_surfaces_remain_closed(self) -> None:
        for key in (
            "checker_modification_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(DECISION_OUTPUT[key], False, key)

    def test_next_gate_is_minimal_extraction(self) -> None:
        self.assertEqual(
            DECISION_OUTPUT["recommended_next_gate"],
            "dynamic_point_lod_view_frame_presentation_count_minimal_extraction_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker modification", BOUNDARY_STATEMENT)
        self.assertIn("no source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no transparent-globe leak inference", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()