from __future__ import annotations

import unittest
from pathlib import Path

from render_core import dynamic_point_presentation_count_boundary as presentation_count_boundary
from render_core import dynamic_point_sampling_visibility_boundary as sampling_visibility_boundary
from render_core import dynamic_point_source_lineage_guard_boundary as source_lineage_guard_boundary
from scripts import validate_displaytools_dynamic_point_presentation_reduction_import_boundary as reduction_checker
from tests import test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_contract_planning as contract_planning


FUTURE_HELPER_TARGET = "render_core/dynamic_point_presentation_reduction_boundary.py"
REQUIRED_CHECKER = "scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py"
RECOMMENDED_NEXT_GATE = "dynamic_point_lod_view_frame_presentation_reduction_minimal_extraction_gate"

ALLOWED_OUTPUT_SHAPE = {
    "nested_dict": True,
    "list": True,
    "scalar": True,
    "callable": False,
    "runtime_object": False,
    "dataframe": False,
    "renderer_buffer": False,
    "file_handle": False,
    "network_object": False,
    "sql_cache_object": False,
    "live_source_object": False,
    "c1_object": False,
    "c4_odoriba_object": False,
}

ALLOWED_LABELS = [
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

FORBIDDEN_INTERPRETATIONS = [
    "source_loss_interpretation",
    "frame_truth_claim",
    "transparent_globe_leak_inference",
    "transparent_globe_leak_fix_claim",
    "visual_correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "performance_claim",
    "runtime_execution",
    "renderer_frame_buffer_access",
    "projection_formula_movement",
    "mask_formula_movement",
    "sampling_formula_movement",
    "alpha_compose_formula_movement",
    "source_lineage_mutation",
    "c4_odoriba_bypass",
]

PLANNED_HELPER_FAMILIES = [
    {
        "helper_family": "build_dynamic_point_presentation_reduction_candidate_descriptor",
        "intended_output_keys": [
            "rendered_lower_than_visible",
            "presentation_or_sampling_reduction_candidate",
            "source_loss_not_inferred",
        ],
        "allowed_labels": [
            "rendered_lower_than_visible",
            "presentation_or_sampling_reduction_candidate",
            "source_loss_not_inferred",
        ],
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "does_not_mutate_source_identity",
        "presentation_count_boundary_dependency": "evidence_reference_only",
        "sampling_visibility_boundary_dependency": "evidence_reference_only",
        "source_lineage_guard_boundary_dependency": "guard_reference_only",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
        "intended_output_keys": [
            "visible_count_observation",
            "rendered_count_observation",
            "rendered_lower_than_visible",
            "frame_truth_not_claimed",
        ],
        "allowed_labels": [
            "visible_count_observation",
            "rendered_count_observation",
            "rendered_lower_than_visible",
            "frame_truth_not_claimed",
        ],
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "count_relation_does_not_rewrite_source_lineage",
        "presentation_count_boundary_dependency": "count_contract_reference_only",
        "sampling_visibility_boundary_dependency": "count_observation_reference_only",
        "source_lineage_guard_boundary_dependency": "reduced_count_is_not_source_loss_guard",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_presentation_reduction_sampling_reference_descriptor",
        "intended_output_keys": [
            "sampling_visibility_boundary_reference",
            "presentation_or_sampling_reduction_candidate",
        ],
        "allowed_labels": [
            "sampling_visibility_boundary_reference",
            "presentation_or_sampling_reduction_candidate",
        ],
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "sampling_reference_does_not_mutate_source_identity",
        "presentation_count_boundary_dependency": "none",
        "sampling_visibility_boundary_dependency": "descriptor_reference_only",
        "source_lineage_guard_boundary_dependency": "guard_reference_only",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_presentation_reduction_source_guard_descriptor",
        "intended_output_keys": [
            "source_lineage_guarded_by_source_lineage_guard_boundary",
            "source_loss_not_inferred",
        ],
        "allowed_labels": [
            "source_lineage_guarded_by_source_lineage_guard_boundary",
            "source_loss_not_inferred",
        ],
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "source_lineage_guard_boundary_protects_reduction_semantics",
        "presentation_count_boundary_dependency": "protected_surface_reference",
        "sampling_visibility_boundary_dependency": "protected_surface_reference",
        "source_lineage_guard_boundary_dependency": "required_guard_reference",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_presentation_reduction_stop_line_ledger",
        "intended_output_keys": [
            "frame_visible_not_observed",
            "frame_truth_not_claimed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
        ],
        "allowed_labels": [
            "frame_visible_not_observed",
            "frame_truth_not_claimed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
        ],
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "stop_line_ledger_does_not_mutate_source_identity",
        "presentation_count_boundary_dependency": "none",
        "sampling_visibility_boundary_dependency": "none",
        "source_lineage_guard_boundary_dependency": "guard_reference_only",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "dynamic_point_presentation_reduction_boundary_descriptor",
        "intended_output_keys": [
            "schema",
            "boundary_id",
            "allowed_output_shape",
            "allowed_labels",
            "helper_families",
            "guard_flags",
        ],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "descriptor_only_no_mutation",
        "presentation_count_boundary_dependency": "descriptor_reference_only",
        "sampling_visibility_boundary_dependency": "descriptor_reference_only",
        "source_lineage_guard_boundary_dependency": "guard_reference_only",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "dynamic_point_presentation_reduction_planning_bundle",
        "intended_output_keys": [
            "planning_passed",
            "future_helper_target",
            "required_checker",
            "helper_creation_authorized",
            "recommended_next_gate",
        ],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_interpretations": FORBIDDEN_INTERPRETATIONS,
        "source_lineage_impact": "planning_bundle_only_no_mutation",
        "presentation_count_boundary_dependency": "evidence_reference_only",
        "sampling_visibility_boundary_dependency": "evidence_reference_only",
        "source_lineage_guard_boundary_dependency": "guard_reference_only",
        "renderer_frame_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "presentation_reduction_import_boundary_checker",
        "helper_creation_authorized": False,
    },
]

DECISION_OUTPUT = {
    "presentation_reduction_minimal_extraction_planning_passed": True,
    "future_helper_target": FUTURE_HELPER_TARGET,
    "required_checker": REQUIRED_CHECKER,
    "required_checker_available": True,
    "required_checker_passes_missing_target": True,
    "presentation_reduction_helper_candidate_supported": True,
    "descriptor_contract_ledger_candidate": True,
    "dict_list_scalar_output_only": True,
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
    "source_loss_interpretation_authorized": False,
    "frame_truth_claim_authorized": False,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "performance_claimed": False,
    "c4_odoriba_bypass_authorized": False,
    "recommended_next_gate": RECOMMENDED_NEXT_GATE,
}

PRESENTATION_REDUCTION_MINIMAL_EXTRACTION_PLANNING_PACKET = {
    "future_helper_target": FUTURE_HELPER_TARGET,
    "required_checker": REQUIRED_CHECKER,
    "allowed_output_shape": ALLOWED_OUTPUT_SHAPE,
    "allowed_labels": ALLOWED_LABELS,
    "planned_helper_families": PLANNED_HELPER_FAMILIES,
    "decision_output": DECISION_OUTPUT,
    "lifecycle_tolerant_future_target_assertion": True,
    "boundary_statement": (
        "Docs/test-only dynamic point LOD view-frame presentation reduction minimal extraction planning gate. "
        "No helper creation, no render_core/dynamic_point_presentation_reduction_boundary.py creation, "
        "no checker modification, no runtime probe change, no taichi_global_bathymetry.py change, "
        "no existing render_core helper change, no render_if_needed, no controller, no renderer, "
        "no frame buffer read, no artifact generation, no formula movement, no source-loss interpretation, "
        "no frame-truth claim, no transparent-globe leak inference or fix claim, no correctness/visual "
        "parity/readiness/performance claim, no c_4/Odoriba bypass, and no push."
    ),
}


class DynamicPointPresentationReductionMinimalExtractionPlanningTest(unittest.TestCase):
    def test_future_helper_target_is_lifecycle_tolerant_planning_target(self) -> None:
        self.assertEqual(FUTURE_HELPER_TARGET, "render_core/dynamic_point_presentation_reduction_boundary.py")
        self.assertEqual(Path(FUTURE_HELPER_TARGET), reduction_checker.DEFAULT_TARGET)
        self.assertTrue(PRESENTATION_REDUCTION_MINIMAL_EXTRACTION_PLANNING_PACKET["lifecycle_tolerant_future_target_assertion"])
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])

    def test_required_checker_available_and_missing_target_passes(self) -> None:
        packet = reduction_checker.validate_target(Path(FUTURE_HELPER_TARGET))
        self.assertTrue(DECISION_OUTPUT["required_checker_available"])
        self.assertTrue(packet["boundary_passed"])
        self.assertFalse(packet["target_imported"])
        self.assertFalse(packet["target_executed"])
        if packet["candidate_exists"]:
            self.assertEqual(packet["status"], "pass")
        else:
            self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])

    def test_planned_helper_families_match_minimal_extraction_surface(self) -> None:
        self.assertEqual(
            [row["helper_family"] for row in PLANNED_HELPER_FAMILIES],
            [
                "build_dynamic_point_presentation_reduction_candidate_descriptor",
                "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
                "build_dynamic_point_presentation_reduction_sampling_reference_descriptor",
                "build_dynamic_point_presentation_reduction_source_guard_descriptor",
                "build_dynamic_point_presentation_reduction_stop_line_ledger",
                "dynamic_point_presentation_reduction_boundary_descriptor",
                "dynamic_point_presentation_reduction_planning_bundle",
            ],
        )

    def test_each_helper_family_has_required_planning_fields_and_closed_dependencies(self) -> None:
        required_keys = {
            "helper_family",
            "intended_output_keys",
            "allowed_labels",
            "forbidden_interpretations",
            "source_lineage_impact",
            "presentation_count_boundary_dependency",
            "sampling_visibility_boundary_dependency",
            "source_lineage_guard_boundary_dependency",
            "renderer_frame_dependency",
            "formula_dependency",
            "checker_coverage_expectation",
            "helper_creation_authorized",
        }
        for row in PLANNED_HELPER_FAMILIES:
            self.assertEqual(set(row), required_keys)
            self.assertFalse(row["renderer_frame_dependency"], row["helper_family"])
            self.assertFalse(row["formula_dependency"], row["helper_family"])
            self.assertFalse(row["helper_creation_authorized"], row["helper_family"])
            self.assertEqual(row["checker_coverage_expectation"], "presentation_reduction_import_boundary_checker")
            self.assertIn("source_loss_interpretation", row["forbidden_interpretations"])
            self.assertIn("frame_truth_claim", row["forbidden_interpretations"])

    def test_output_shape_is_dict_list_scalar_only(self) -> None:
        self.assertTrue(ALLOWED_OUTPUT_SHAPE["nested_dict"])
        self.assertTrue(ALLOWED_OUTPUT_SHAPE["list"])
        self.assertTrue(ALLOWED_OUTPUT_SHAPE["scalar"])
        forbidden_outputs = [
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
        for key in forbidden_outputs:
            self.assertFalse(ALLOWED_OUTPUT_SHAPE[key], key)

    def test_semantic_assertions_keep_reduction_separate_from_source_loss_and_frame_truth(self) -> None:
        candidate = PLANNED_HELPER_FAMILIES[0]
        self.assertIn("presentation_or_sampling_reduction_candidate", candidate["allowed_labels"])
        self.assertIn("source_loss_not_inferred", candidate["allowed_labels"])
        self.assertIn("source_loss_interpretation", candidate["forbidden_interpretations"])
        self.assertIn("frame_truth_claim", candidate["forbidden_interpretations"])
        self.assertIn("transparent_globe_leak_inference", candidate["forbidden_interpretations"])
        self.assertIn("readiness_claim", candidate["forbidden_interpretations"])

    def test_existing_boundaries_are_references_not_merge_reason(self) -> None:
        count_descriptor = presentation_count_boundary.dynamic_point_presentation_count_boundary_descriptor()
        sampling_descriptor = sampling_visibility_boundary.dynamic_point_sampling_visibility_boundary_descriptor()
        lineage_descriptor = source_lineage_guard_boundary.dynamic_point_source_lineage_guard_boundary_descriptor()
        contract_decision = contract_planning.DECISION_OUTPUT

        self.assertIn("rendered_lower_than_visible", count_descriptor["owned_semantics"])
        self.assertIn("sampling_or_presentation_reduction_candidate", sampling_descriptor["owned_semantics"])
        self.assertIn("presentation_count_boundary", lineage_descriptor["protected_surfaces"])
        self.assertIn("sampling_visibility_boundary", lineage_descriptor["protected_surfaces"])
        self.assertFalse(lineage_descriptor["guard_flags"]["reduced_count_as_source_loss_authorized"])
        self.assertTrue(contract_decision["presentation_reduction_helper_candidate_supported"])
        self.assertFalse(contract_decision["source_loss_interpretation_authorized"])

    def test_decision_output_keeps_all_authorizations_closed(self) -> None:
        true_flags = [
            "presentation_reduction_minimal_extraction_planning_passed",
            "required_checker_available",
            "required_checker_passes_missing_target",
            "presentation_reduction_helper_candidate_supported",
            "descriptor_contract_ledger_candidate",
            "dict_list_scalar_output_only",
        ]
        for key in true_flags:
            self.assertTrue(DECISION_OUTPUT[key], key)

        false_flags = [
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
            "source_loss_interpretation_authorized",
            "frame_truth_claim_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "performance_claimed",
            "c4_odoriba_bypass_authorized",
        ]
        for key in false_flags:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_recommended_next_gate_is_minimal_extraction(self) -> None:
        self.assertEqual(DECISION_OUTPUT["recommended_next_gate"], RECOMMENDED_NEXT_GATE)


if __name__ == "__main__":
    unittest.main()
