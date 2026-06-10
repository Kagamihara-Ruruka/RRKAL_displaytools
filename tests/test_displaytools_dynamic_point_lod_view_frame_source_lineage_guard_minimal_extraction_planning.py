"""Planning gate for dynamic point source-lineage guard minimal extraction."""

from __future__ import annotations

from pathlib import Path
import unittest

from scripts import validate_displaytools_dynamic_point_source_lineage_guard_import_boundary as checker
from tests import test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning as contract_planning
from tests import test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning as checker_planning


FUTURE_HELPER_TARGET = "render_core/dynamic_point_source_lineage_guard_boundary.py"
REQUIRED_CHECKER = "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py"

PLANNED_HELPER_FAMILIES = [
    "build_dynamic_point_source_identity_contract_descriptor",
    "build_dynamic_point_source_lineage_integrity_descriptor",
    "build_dynamic_point_payload_identity_guard_descriptor",
    "build_dynamic_point_sampling_source_guard_descriptor",
    "build_dynamic_point_presentation_count_source_guard_descriptor",
    "build_dynamic_point_hidden_visibility_source_guard_descriptor",
    "build_dynamic_point_mask_occlusion_source_guard_descriptor",
    "build_dynamic_point_raw_row_compatibility_seam_descriptor",
    "build_dynamic_point_source_lineage_guard_stop_line_ledger",
    "dynamic_point_source_lineage_guard_boundary_descriptor",
    "dynamic_point_source_lineage_guard_planning_bundle",
]

ALLOWED_OUTPUT_SHAPE = ["dict", "list", "scalar"]
FORBIDDEN_OUTPUT_SHAPE = [
    "callable",
    "runtime_object",
    "dataframe",
    "renderer_buffer",
    "file_handle",
    "network_object",
    "sql_cache_object",
    "live_source_object",
    "c1_object",
    "c4_odoriba_object",
]

ALLOWED_LABELS = [
    "source_present_token",
    "source_label",
    "point_id",
    "source_lineage_integrity_token",
    "payload_identity_guard",
    "sampling_does_not_mutate_source",
    "presentation_count_does_not_mutate_source",
    "hidden_visibility_does_not_mutate_source",
    "mask_visibility_does_not_mutate_source",
    "occlusion_visibility_does_not_mutate_source",
    "reduced_count_is_not_source_loss",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "controlled_raw_row_compatibility_seam",
    "developmental_compensation_surface",
    "future_c4_odoriba_handoff_material",
    "direct_c1_integration_not_authorized",
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
    "alpha_compose_formula",
    "dataframe_runtime",
    "live_source",
    "cache_database_io",
    "real_ais_adsb_source",
    "source_lineage_mutation",
    "hidden_as_missing_interpretation",
    "reduced_count_as_source_loss_interpretation",
    "occluded_as_source_loss_interpretation",
    "raw_row_seam_runtime_authorization",
    "direct_c1_integration",
    "c4_odoriba_bypass",
    "transparent_globe_leak_inference",
    "correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "transparent_globe_leak_fix_claim",
]

PROTECTED_ANDESITE_HELPERS = [
    "sampling_visibility_boundary",
    "presentation_count_boundary",
    "computed_but_hidden_boundary",
]

RAW_ROW_SEAM_TREATMENT = {
    "controlled_raw_row_compatibility_seam_label_allowed": True,
    "controlled_raw_row_compatibility_seam_runtime_authorized": False,
    "developmental_compensation_surface_recognized": True,
    "mature_c1_integration": False,
    "future_c4_odoriba_handoff_material": True,
}

C4_ODORIBA_MEDIATION_BOUNDARY = {
    "future_cross_organ_integration_requires_c4_odoriba_mediation": True,
    "direct_c3_to_c1_dependency_authorized": False,
    "c4_odoriba_bypass_authorized": False,
}


def _matrix_row(helper_family: str, protected_surface: str, protected_helper: str) -> dict[str, object]:
    return {
        "helper_family": helper_family,
        "intended_output_keys": [
            "surface",
            "allowed_labels",
            "source_identity_guard",
            "forbidden_interpretations",
            "stop_line_ledger",
        ],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_fields": FORBIDDEN_FIELDS,
        "protected_source_identity_surface": protected_surface,
        "protected_existing_andesite_helper": protected_helper,
        "raw_row_seam_treatment": "label_ledger_handoff_only_no_runtime",
        "c4_odoriba_mediation_boundary": "future_cross_organ_integration_requires_c4_odoriba_mediation",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "real_source_dependency": False,
        "output_shape": ALLOWED_OUTPUT_SHAPE,
        "forbidden_output_shape": FORBIDDEN_OUTPUT_SHAPE,
        "checker_coverage_expectation": REQUIRED_CHECKER,
        "helper_creation_authorization": False,
    }


PLANNED_HELPER_MATRIX = [
    _matrix_row(
        "build_dynamic_point_source_identity_contract_descriptor",
        "source_label_and_point_id_identity",
        "sampling_visibility_boundary,presentation_count_boundary,computed_but_hidden_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_source_lineage_integrity_descriptor",
        "source_lineage_integrity_token",
        "sampling_visibility_boundary,presentation_count_boundary,computed_but_hidden_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_payload_identity_guard_descriptor",
        "payload_identity_guard",
        "sampling_visibility_boundary,presentation_count_boundary,computed_but_hidden_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_sampling_source_guard_descriptor",
        "sampling_does_not_mutate_source",
        "sampling_visibility_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_presentation_count_source_guard_descriptor",
        "presentation_count_does_not_mutate_source",
        "presentation_count_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_hidden_visibility_source_guard_descriptor",
        "hidden_visibility_does_not_mutate_source",
        "computed_but_hidden_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_mask_occlusion_source_guard_descriptor",
        "mask_visibility_and_occlusion_do_not_mutate_source",
        "sampling_visibility_boundary,computed_but_hidden_boundary",
    ),
    _matrix_row(
        "build_dynamic_point_raw_row_compatibility_seam_descriptor",
        "controlled_raw_row_compatibility_seam",
        "future_c4_odoriba_handoff_material",
    ),
    _matrix_row(
        "build_dynamic_point_source_lineage_guard_stop_line_ledger",
        "source_lineage_guard_stop_line_ledger",
        "sampling_visibility_boundary,presentation_count_boundary,computed_but_hidden_boundary",
    ),
    _matrix_row(
        "dynamic_point_source_lineage_guard_boundary_descriptor",
        "source_lineage_guard_boundary_descriptor",
        "sampling_visibility_boundary,presentation_count_boundary,computed_but_hidden_boundary",
    ),
    _matrix_row(
        "dynamic_point_source_lineage_guard_planning_bundle",
        "source_lineage_guard_planning_bundle",
        "sampling_visibility_boundary,presentation_count_boundary,computed_but_hidden_boundary",
    ),
]

DECISION_OUTPUT = {
    "source_lineage_guard_minimal_extraction_planning_passed": True,
    "required_checker_available": True,
    "source_lineage_guard_helper_candidate_supported": True,
    "descriptor_contract_ledger_candidate": True,
    "helper_creation_authorized": False,
    "checker_modification_authorized": False,
    "runtime_execution_authorized": False,
    "source_lineage_mutation_authorized": False,
    "controlled_raw_row_compatibility_seam_label_allowed": True,
    "controlled_raw_row_compatibility_seam_runtime_authorized": False,
    "direct_c1_integration_authorized": False,
    "c4_odoriba_mediation_required": True,
    "dependency_cycle_watch_enabled": True,
    "render_core_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "real_source_read_authorized": False,
    "hidden_as_missing_interpretation_authorized": False,
    "reduced_count_as_source_loss_interpretation_authorized": False,
    "occluded_as_source_loss_interpretation_authorized": False,
    "raw_row_seam_promoted_to_mature_c1_integration": False,
    "direct_c3_to_c1_dependency_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "transparent_globe_leak_inferred": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_source_lineage_guard_minimal_extraction_gate",
}

PLANNING_PACKET = {
    "schema": "rrkal_displaytools.dynamic_point_source_lineage_guard_minimal_extraction_planning.v1",
    "future_helper_target": FUTURE_HELPER_TARGET,
    "required_checker": REQUIRED_CHECKER,
    "planned_helper_families": PLANNED_HELPER_FAMILIES,
    "planned_helper_matrix": PLANNED_HELPER_MATRIX,
    "allowed_output_shape": ALLOWED_OUTPUT_SHAPE,
    "forbidden_output_shape": FORBIDDEN_OUTPUT_SHAPE,
    "protected_existing_andesite_helpers": PROTECTED_ANDESITE_HELPERS,
    "raw_row_seam_treatment": RAW_ROW_SEAM_TREATMENT,
    "c4_odoriba_mediation_boundary": C4_ODORIBA_MEDIATION_BOUNDARY,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": "Docs/test-only dynamic point LOD view-frame source-lineage guard minimal extraction planning gate.",
}


class DynamicPointSourceLineageGuardMinimalExtractionPlanningTest(unittest.TestCase):
    def test_future_targets_and_checker_are_declared_without_creation_authorization(self) -> None:
        self.assertEqual(FUTURE_HELPER_TARGET, "render_core/dynamic_point_source_lineage_guard_boundary.py")
        self.assertEqual(REQUIRED_CHECKER, "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py")
        self.assertEqual(Path(checker.DEFAULT_TARGET).as_posix(), FUTURE_HELPER_TARGET)
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])
        self.assertFalse(DECISION_OUTPUT["checker_modification_authorized"])
        self.assertEqual(contract_planning.FUTURE_HELPER_TARGET, FUTURE_HELPER_TARGET)
        self.assertEqual(checker_planning.FUTURE_HELPER_TARGET, FUTURE_HELPER_TARGET)

    def test_required_checker_protection_is_available_and_static(self) -> None:
        self.assertTrue(DECISION_OUTPUT["required_checker_available"])
        clean_packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertTrue(clean_packet["boundary_passed"])
        self.assertFalse(clean_packet["target_imported"])
        self.assertFalse(clean_packet["target_executed"])
        missing_packet = checker.validate_target(Path("render_core/__missing_source_lineage_guard_candidate__.py"))
        self.assertEqual(missing_packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(missing_packet["boundary_passed"])
        self.assertFalse(missing_packet["candidate_exists"])

    def test_planned_helper_families_are_complete(self) -> None:
        self.assertEqual(PLANNED_HELPER_FAMILIES, [row["helper_family"] for row in PLANNED_HELPER_MATRIX])
        for helper in (
            "build_dynamic_point_source_identity_contract_descriptor",
            "build_dynamic_point_source_lineage_integrity_descriptor",
            "build_dynamic_point_payload_identity_guard_descriptor",
            "build_dynamic_point_sampling_source_guard_descriptor",
            "build_dynamic_point_presentation_count_source_guard_descriptor",
            "build_dynamic_point_hidden_visibility_source_guard_descriptor",
            "build_dynamic_point_mask_occlusion_source_guard_descriptor",
            "build_dynamic_point_raw_row_compatibility_seam_descriptor",
            "build_dynamic_point_source_lineage_guard_stop_line_ledger",
            "dynamic_point_source_lineage_guard_boundary_descriptor",
            "dynamic_point_source_lineage_guard_planning_bundle",
        ):
            self.assertIn(helper, PLANNED_HELPER_FAMILIES)

    def test_each_helper_family_is_descriptor_contract_ledger_only(self) -> None:
        for row in PLANNED_HELPER_MATRIX:
            self.assertFalse(row["runtime_dependency"], row["helper_family"])
            self.assertFalse(row["frame_renderer_dependency"], row["helper_family"])
            self.assertFalse(row["formula_dependency"], row["helper_family"])
            self.assertFalse(row["real_source_dependency"], row["helper_family"])
            self.assertEqual(row["output_shape"], ["dict", "list", "scalar"])
            self.assertFalse(row["helper_creation_authorization"], row["helper_family"])
            self.assertEqual(row["checker_coverage_expectation"], REQUIRED_CHECKER)
            self.assertEqual(row["raw_row_seam_treatment"], "label_ledger_handoff_only_no_runtime")
            self.assertEqual(row["c4_odoriba_mediation_boundary"], "future_cross_organ_integration_requires_c4_odoriba_mediation")

    def test_output_shape_policy_excludes_runtime_and_cross_organ_objects(self) -> None:
        self.assertEqual(PLANNING_PACKET["allowed_output_shape"], ["dict", "list", "scalar"])
        for forbidden_shape in (
            "callable",
            "runtime_object",
            "dataframe",
            "renderer_buffer",
            "file_handle",
            "network_object",
            "sql_cache_object",
            "live_source_object",
            "c1_object",
            "c4_odoriba_object",
        ):
            self.assertIn(forbidden_shape, PLANNING_PACKET["forbidden_output_shape"])

    def test_raw_row_seam_is_label_and_handoff_only(self) -> None:
        treatment = PLANNING_PACKET["raw_row_seam_treatment"]
        self.assertTrue(treatment["controlled_raw_row_compatibility_seam_label_allowed"])
        self.assertTrue(treatment["developmental_compensation_surface_recognized"])
        self.assertTrue(treatment["future_c4_odoriba_handoff_material"])
        self.assertFalse(treatment["controlled_raw_row_compatibility_seam_runtime_authorized"])
        self.assertFalse(treatment["mature_c1_integration"])

    def test_c4_odoriba_boundary_blocks_direct_c1_and_bypass(self) -> None:
        boundary = PLANNING_PACKET["c4_odoriba_mediation_boundary"]
        self.assertTrue(boundary["future_cross_organ_integration_requires_c4_odoriba_mediation"])
        self.assertFalse(boundary["direct_c3_to_c1_dependency_authorized"])
        self.assertFalse(boundary["c4_odoriba_bypass_authorized"])

    def test_decision_output_is_non_authorizing_except_planning(self) -> None:
        self.assertTrue(DECISION_OUTPUT["source_lineage_guard_minimal_extraction_planning_passed"])
        self.assertTrue(DECISION_OUTPUT["source_lineage_guard_helper_candidate_supported"])
        self.assertTrue(DECISION_OUTPUT["descriptor_contract_ledger_candidate"])
        self.assertTrue(DECISION_OUTPUT["dependency_cycle_watch_enabled"])
        for key in (
            "helper_creation_authorized",
            "checker_modification_authorized",
            "runtime_execution_authorized",
            "source_lineage_mutation_authorized",
            "controlled_raw_row_compatibility_seam_runtime_authorized",
            "direct_c1_integration_authorized",
            "render_core_change_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "real_source_read_authorized",
            "hidden_as_missing_interpretation_authorized",
            "reduced_count_as_source_loss_interpretation_authorized",
            "occluded_as_source_loss_interpretation_authorized",
            "raw_row_seam_promoted_to_mature_c1_integration",
            "direct_c3_to_c1_dependency_authorized",
            "c4_odoriba_bypass_authorized",
            "transparent_globe_leak_inferred",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_forbidden_interpretations_are_explicitly_listed(self) -> None:
        forbidden = set(FORBIDDEN_FIELDS)
        for field in (
            "source_lineage_mutation",
            "hidden_as_missing_interpretation",
            "reduced_count_as_source_loss_interpretation",
            "occluded_as_source_loss_interpretation",
            "raw_row_seam_runtime_authorization",
            "direct_c1_integration",
            "c4_odoriba_bypass",
            "transparent_globe_leak_inference",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "transparent_globe_leak_fix_claim",
        ):
            self.assertIn(field, forbidden)

    def test_recommended_next_gate_is_minimal_extraction(self) -> None:
        self.assertEqual(
            DECISION_OUTPUT["recommended_next_gate"],
            "dynamic_point_lod_view_frame_source_lineage_guard_minimal_extraction_gate",
        )


if __name__ == "__main__":
    unittest.main()
