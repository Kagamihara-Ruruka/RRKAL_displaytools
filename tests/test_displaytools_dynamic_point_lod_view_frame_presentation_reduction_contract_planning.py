from __future__ import annotations

import unittest

from render_core import dynamic_point_presentation_count_boundary as presentation_count_boundary
from render_core import dynamic_point_sampling_visibility_boundary as sampling_visibility_boundary
from render_core import dynamic_point_source_lineage_guard_boundary as source_lineage_guard_boundary
from tests import test_displaytools_dynamic_point_lod_view_frame_post_source_lineage_guard_next_bridge_selection as next_bridge_selection


FUTURE_HELPER_TARGET = "render_core/dynamic_point_presentation_reduction_boundary.py"
FUTURE_CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py"
RECOMMENDED_NEXT_GATE = "dynamic_point_lod_view_frame_presentation_reduction_import_boundary_checker_planning_gate"

PLANNED_HELPER_FAMILIES = [
    "build_dynamic_point_presentation_reduction_candidate_descriptor",
    "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
    "build_dynamic_point_sampling_reduction_reference_descriptor",
    "build_dynamic_point_presentation_reduction_source_guard_descriptor",
    "build_dynamic_point_presentation_reduction_stop_line_ledger",
    "dynamic_point_presentation_reduction_boundary_descriptor",
    "dynamic_point_presentation_reduction_planning_bundle",
]

PRESENTATION_REDUCTION_PLANNING_MATRIX = [
    {
        "surface": "rendered_lower_than_visible",
        "semantic_role": "primary_reduction_observation",
        "allowed_meaning": "presentation_or_sampling_reduction_candidate",
        "forbidden_interpretations": [
            "source_loss",
            "frame_visibility_truth",
            "transparent_globe_leak",
            "visual_correctness",
            "runtime_readiness",
        ],
        "evidence_refs": [
            "presentation_count_boundary",
            "sampling_visibility_runtime_probe_result_interpretation",
        ],
        "runtime_dependency": False,
        "formula_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_guarded_by": "source_lineage_guard_boundary",
        "helper_candidate": "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
        "checker_need": "dedicated_presentation_reduction_import_boundary_checker",
    },
    {
        "surface": "presentation_or_sampling_reduction_candidate",
        "semantic_role": "classification_contract",
        "allowed_meaning": "count_difference_classification_without_source_loss",
        "forbidden_interpretations": [
            "source_completeness_claim",
            "renderer_output_truth",
            "performance_readiness",
        ],
        "evidence_refs": [
            "presentation_count_boundary",
            "sampling_visibility_boundary",
        ],
        "runtime_dependency": False,
        "formula_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_guarded_by": "source_lineage_guard_boundary",
        "helper_candidate": "build_dynamic_point_presentation_reduction_candidate_descriptor",
        "checker_need": "dedicated_presentation_reduction_import_boundary_checker",
    },
    {
        "surface": "presentation_count_boundary_reference",
        "semantic_role": "evidence_reference_not_duplicate_surface",
        "allowed_meaning": "visible_count_and_rendered_count_are_existing_contract_fields",
        "forbidden_interpretations": ["helper_creation_in_this_gate", "formula_movement"],
        "evidence_refs": ["presentation_count_boundary"],
        "runtime_dependency": False,
        "formula_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_guarded_by": "source_lineage_guard_boundary",
        "helper_candidate": "build_dynamic_point_sampling_reduction_reference_descriptor",
        "checker_need": "dedicated_presentation_reduction_import_boundary_checker",
    },
    {
        "surface": "sampling_visibility_boundary_reference",
        "semantic_role": "sampling_observation_reference",
        "allowed_meaning": "sampled_visible_and_count_observations_support_reduction_candidate",
        "forbidden_interpretations": ["sampling_formula_movement", "runtime_probe_expansion"],
        "evidence_refs": ["sampling_visibility_boundary"],
        "runtime_dependency": False,
        "formula_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_guarded_by": "source_lineage_guard_boundary",
        "helper_candidate": "build_dynamic_point_sampling_reduction_reference_descriptor",
        "checker_need": "dedicated_presentation_reduction_import_boundary_checker",
    },
    {
        "surface": "source_lineage_guard_boundary",
        "semantic_role": "source_loss_drift_guard",
        "allowed_meaning": "reduction_does_not_mutate_source_identity",
        "forbidden_interpretations": ["source_lineage_mutation", "reduced_count_as_source_loss"],
        "evidence_refs": ["source_lineage_guard_boundary"],
        "runtime_dependency": False,
        "formula_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_guarded_by": "source_lineage_guard_boundary",
        "helper_candidate": "build_dynamic_point_presentation_reduction_source_guard_descriptor",
        "checker_need": "dedicated_presentation_reduction_import_boundary_checker",
    },
    {
        "surface": "frame_visible_not_observed",
        "semantic_role": "stop_line_ledger",
        "allowed_meaning": "frame_visibility_remains_unobserved",
        "forbidden_interpretations": ["frame_truth_claim", "transparent_globe_leak_inference"],
        "evidence_refs": ["frame_visibility_stop_line_planning"],
        "runtime_dependency": False,
        "formula_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_guarded_by": "source_lineage_guard_boundary",
        "helper_candidate": "build_dynamic_point_presentation_reduction_stop_line_ledger",
        "checker_need": "dedicated_presentation_reduction_import_boundary_checker",
    },
]

DECISION_OUTPUT = {
    "presentation_reduction_contract_planning_passed": True,
    "presentation_reduction_helper_candidate_supported": True,
    "descriptor_contract_ledger_candidate": True,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
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

PRESENTATION_REDUCTION_PLANNING_PACKET = {
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "planned_helper_families": PLANNED_HELPER_FAMILIES,
    "planning_matrix": PRESENTATION_REDUCTION_PLANNING_MATRIX,
    "decision_output": DECISION_OUTPUT,
    "distinct_from_presentation_count_boundary": True,
    "boundary_statement": (
        "Docs/test-only dynamic point LOD view-frame presentation reduction contract planning gate. "
        "No helper creation, no checker creation, no render_core change, no runtime/probe/renderer/"
        "frame/formula/source behavior change, no source-loss/frame-truth/leak/correctness/"
        "readiness claim, no c_4/Odoriba bypass, and no push."
    ),
}


def _matrix_by_surface() -> dict[str, dict[str, object]]:
    return {row["surface"]: row for row in PRESENTATION_REDUCTION_PLANNING_MATRIX}


class DynamicPointPresentationReductionContractPlanningTest(unittest.TestCase):
    def test_prior_selection_chose_presentation_reduction_contract(self) -> None:
        decision = next_bridge_selection.DECISION_OUTPUT
        self.assertEqual(decision["selected_next_bridge_candidate"], "presentation_reduction_contract")
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_presentation_reduction_contract_planning_gate",
        )
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["helper_creation_authorized"])
        self.assertFalse(decision["checker_creation_authorized"])

    def test_future_targets_are_planned_only(self) -> None:
        self.assertEqual(FUTURE_HELPER_TARGET, "render_core/dynamic_point_presentation_reduction_boundary.py")
        self.assertEqual(
            FUTURE_CHECKER_TARGET,
            "scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py",
        )
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])
        self.assertFalse(DECISION_OUTPUT["checker_creation_authorized"])
        self.assertFalse(DECISION_OUTPUT["render_core_change_authorized"])

    def test_planned_helper_families_define_distinct_reduction_surface(self) -> None:
        self.assertEqual(
            PLANNED_HELPER_FAMILIES,
            [
                "build_dynamic_point_presentation_reduction_candidate_descriptor",
                "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
                "build_dynamic_point_sampling_reduction_reference_descriptor",
                "build_dynamic_point_presentation_reduction_source_guard_descriptor",
                "build_dynamic_point_presentation_reduction_stop_line_ledger",
                "dynamic_point_presentation_reduction_boundary_descriptor",
                "dynamic_point_presentation_reduction_planning_bundle",
            ],
        )
        self.assertTrue(PRESENTATION_REDUCTION_PLANNING_PACKET["distinct_from_presentation_count_boundary"])

    def test_rendered_lower_than_visible_semantics_are_reduction_only(self) -> None:
        row = _matrix_by_surface()["rendered_lower_than_visible"]
        self.assertEqual(row["allowed_meaning"], "presentation_or_sampling_reduction_candidate")
        self.assertIn("source_loss", row["forbidden_interpretations"])
        self.assertIn("frame_visibility_truth", row["forbidden_interpretations"])
        self.assertIn("transparent_globe_leak", row["forbidden_interpretations"])
        self.assertIn("visual_correctness", row["forbidden_interpretations"])
        self.assertIn("runtime_readiness", row["forbidden_interpretations"])
        self.assertFalse(row["runtime_dependency"])
        self.assertFalse(row["formula_dependency"])
        self.assertFalse(row["renderer_frame_dependency"])

    def test_existing_boundaries_are_evidence_not_runtime_dependencies(self) -> None:
        count_descriptor = presentation_count_boundary.dynamic_point_presentation_count_boundary_descriptor()
        sampling_descriptor = sampling_visibility_boundary.dynamic_point_sampling_visibility_boundary_descriptor()
        lineage_descriptor = source_lineage_guard_boundary.dynamic_point_source_lineage_guard_boundary_descriptor()

        count_semantics = count_descriptor["owned_semantics"]
        self.assertIn("rendered_lower_than_visible", count_semantics)
        self.assertIn("sampling_or_presentation_reduction_candidate", count_semantics)
        self.assertIn("source_loss_not_inferred", count_semantics)
        self.assertIn("frame_visible_not_observed", count_semantics)
        self.assertIn("transparent_globe_leak_not_inferred", count_semantics)
        self.assertIn("source_loss_interpretation", count_descriptor["blocked_actions"])
        self.assertIn("frame_buffer_read", count_descriptor["blocked_actions"])
        self.assertIn("sampling_formula_movement", count_descriptor["blocked_actions"])

        sampling_semantics = sampling_descriptor["owned_semantics"]
        self.assertIn("visible_count_observation", sampling_semantics)
        self.assertIn("rendered_count_observation", sampling_semantics)
        self.assertIn("sampling_or_presentation_reduction_candidate", sampling_semantics)
        self.assertIn("transparent_globe_leak_not_inferred", sampling_semantics)
        self.assertIn("sampling_formula_movement", sampling_descriptor["blocked_actions"])
        self.assertIn("runtime_probe_call", sampling_descriptor["blocked_actions"])
        self.assertIn("frame_buffer_read", sampling_descriptor["blocked_actions"])

        protected = lineage_descriptor["protected_surfaces"]
        self.assertIn("presentation_count_boundary", protected)
        self.assertIn("sampling_visibility_boundary", protected)
        self.assertFalse(lineage_descriptor["guard_flags"]["source_lineage_mutation_authorized"])
        self.assertFalse(lineage_descriptor["guard_flags"]["reduced_count_as_source_loss_authorized"])

    def test_matrix_includes_source_guard_and_stop_lines(self) -> None:
        matrix = _matrix_by_surface()
        self.assertIn("source_lineage_guard_boundary", matrix)
        self.assertIn("frame_visible_not_observed", matrix)
        self.assertEqual(
            matrix["source_lineage_guard_boundary"]["allowed_meaning"],
            "reduction_does_not_mutate_source_identity",
        )
        self.assertIn(
            "reduced_count_as_source_loss",
            matrix["source_lineage_guard_boundary"]["forbidden_interpretations"],
        )
        self.assertIn(
            "transparent_globe_leak_inference",
            matrix["frame_visible_not_observed"]["forbidden_interpretations"],
        )

    def test_decision_output_keeps_all_authorizations_closed(self) -> None:
        required_true = [
            "presentation_reduction_contract_planning_passed",
            "presentation_reduction_helper_candidate_supported",
            "descriptor_contract_ledger_candidate",
        ]
        for key in required_true:
            self.assertTrue(DECISION_OUTPUT[key], key)

        required_false = [
            "helper_creation_authorized",
            "checker_creation_authorized",
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

    def test_recommended_next_gate_is_checker_planning(self) -> None:
        self.assertEqual(DECISION_OUTPUT["recommended_next_gate"], RECOMMENDED_NEXT_GATE)


if __name__ == "__main__":
    unittest.main()
