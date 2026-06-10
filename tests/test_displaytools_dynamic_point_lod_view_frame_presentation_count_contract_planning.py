"""Planning gate for the dynamic point presentation count contract."""

import unittest


PLANNING_MATRIX = [
    {
        "row_id": "visible_count_observation",
        "observed_evidence": "visible_count_observation=2 from the sampling visibility runtime probe interpretation",
        "semantic_meaning": "source-present projected visibility count can be represented as an observation label",
        "allowed_contract_field": "visible_count",
        "forbidden_interpretation": "source lineage completeness or coordinate correctness",
        "dependency_on_runtime": "prior_observation_only",
        "dependency_on_renderer_frame_buffer": "none",
        "source_lineage_impact": "must_not_mutate_source_lineage",
        "extraction_readiness_level": "ready_for_import_boundary_checker_planning",
        "recommended_next_action": "plan_presentation_count_import_boundary_checker",
    },
    {
        "row_id": "rendered_count_observation",
        "observed_evidence": "rendered_count_observation=1 from the sampling visibility runtime probe interpretation",
        "semantic_meaning": "rendered count can be carried as a presentation count observation label",
        "allowed_contract_field": "rendered_count",
        "forbidden_interpretation": "visual correctness or final frame truth",
        "dependency_on_runtime": "prior_observation_only",
        "dependency_on_renderer_frame_buffer": "none",
        "source_lineage_impact": "must_not_mutate_source_lineage",
        "extraction_readiness_level": "ready_for_import_boundary_checker_planning",
        "recommended_next_action": "plan_presentation_count_import_boundary_checker",
    },
    {
        "row_id": "rendered_lower_than_visible",
        "observed_evidence": "visible_count_observation=2 and rendered_count_observation=1",
        "semantic_meaning": "rendered lower than visible is a sampling or presentation reduction candidate",
        "allowed_contract_field": "rendered_lower_than_visible",
        "forbidden_interpretation": "source_loss_or_missing_source",
        "dependency_on_runtime": "prior_observation_only",
        "dependency_on_renderer_frame_buffer": "none",
        "source_lineage_impact": "source_lineage_preserved",
        "extraction_readiness_level": "ready_for_import_boundary_checker_planning",
        "recommended_next_action": "preserve_reduction_candidate_without_source_loss_claim",
    },
    {
        "row_id": "sampling_or_presentation_reduction_candidate",
        "observed_evidence": "reduced sample case preserved source identity while lowering rendered count",
        "semantic_meaning": "count reduction belongs to sampling or presentation semantics until further evidence",
        "allowed_contract_field": "reduction_candidate_label",
        "forbidden_interpretation": "provider_filter_or_database_loss",
        "dependency_on_runtime": "prior_observation_only",
        "dependency_on_renderer_frame_buffer": "none",
        "source_lineage_impact": "source_lineage_guard_required",
        "extraction_readiness_level": "ready_for_import_boundary_checker_planning",
        "recommended_next_action": "encode_as_descriptor_contract_ledger_only",
    },
    {
        "row_id": "presentation_count_contract",
        "observed_evidence": "next andesite bridge selection chose presentation_count_contract as the next candidate",
        "semantic_meaning": "visible and rendered count observations can be cooled into a local contract",
        "allowed_contract_field": "presentation_count_contract_descriptor",
        "forbidden_interpretation": "renderer_behavior_or_frame_output_semantics",
        "dependency_on_runtime": "none_for_planning",
        "dependency_on_renderer_frame_buffer": "none",
        "source_lineage_impact": "read_only_guard",
        "extraction_readiness_level": "planning_candidate",
        "recommended_next_action": "create_checker_planning_gate_before_helper_creation",
    },
    {
        "row_id": "frame_visible_not_observed",
        "observed_evidence": "frame_visible_token=not_observed in the sampling visibility result interpretation",
        "semantic_meaning": "frame visibility remains a stop-line field rather than runtime truth",
        "allowed_contract_field": "frame_visible_not_observed",
        "forbidden_interpretation": "transparent_globe_leak_inference",
        "dependency_on_runtime": "blocked",
        "dependency_on_renderer_frame_buffer": "blocked",
        "source_lineage_impact": "none",
        "extraction_readiness_level": "blocked_stop_line",
        "recommended_next_action": "keep_frame_surface_out_of_count_contract",
    },
    {
        "row_id": "source_lineage_integrity_token",
        "observed_evidence": "source_lineage_integrity_token=true in the second runtime probe interpretation",
        "semantic_meaning": "sampling and mask count observations must not alter source identity",
        "allowed_contract_field": "source_lineage_integrity_token",
        "forbidden_interpretation": "source_lineage_mutation_allowed",
        "dependency_on_runtime": "prior_observation_only",
        "dependency_on_renderer_frame_buffer": "none",
        "source_lineage_impact": "must_remain_true",
        "extraction_readiness_level": "ready_for_import_boundary_checker_planning",
        "recommended_next_action": "carry_as_guard_field",
    },
    {
        "row_id": "transparent_globe_leak_not_inferred",
        "observed_evidence": "frame visibility and renderer path remain unobserved",
        "semantic_meaning": "transparent globe leak remains outside this contract and is not inferred",
        "allowed_contract_field": "transparent_globe_leak_not_inferred",
        "forbidden_interpretation": "transparent_globe_leak_fix_or_fault_proof",
        "dependency_on_runtime": "blocked",
        "dependency_on_renderer_frame_buffer": "blocked",
        "source_lineage_impact": "none",
        "extraction_readiness_level": "contract_only_stop_line",
        "recommended_next_action": "preserve_leak_claim_guard",
    },
]

DECISION_OUTPUT = {
    "presentation_count_contract_planning_passed": True,
    "visible_count_contract_field_allowed": True,
    "rendered_count_contract_field_allowed": True,
    "rendered_lower_than_visible_means_reduction_candidate_only": True,
    "rendered_lower_than_visible_source_loss_interpretation_allowed": False,
    "frame_visible_not_observed_blocks_leak_inference": True,
    "import_boundary_checker_planning_supported": True,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "runtime_probe_expansion_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "transparent_globe_leak_inferred": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame presentation count contract planning gate. "
    "No helper creation, no checker creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no projection/mask/sampling formula movement, "
    "no source-loss interpretation from rendered lower than visible, no transparent-globe leak inference, "
    "no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push."
)


class DynamicPointPresentationCountContractPlanningTest(unittest.TestCase):
    def test_required_rows_are_present(self):
        row_ids = {row["row_id"] for row in PLANNING_MATRIX}
        self.assertEqual(
            {
                "visible_count_observation",
                "rendered_count_observation",
                "rendered_lower_than_visible",
                "sampling_or_presentation_reduction_candidate",
                "presentation_count_contract",
                "frame_visible_not_observed",
                "source_lineage_integrity_token",
                "transparent_globe_leak_not_inferred",
            },
            row_ids,
        )

    def test_each_row_has_required_planning_fields(self):
        required_fields = {
            "row_id",
            "observed_evidence",
            "semantic_meaning",
            "allowed_contract_field",
            "forbidden_interpretation",
            "dependency_on_runtime",
            "dependency_on_renderer_frame_buffer",
            "source_lineage_impact",
            "extraction_readiness_level",
            "recommended_next_action",
        }
        for row in PLANNING_MATRIX:
            self.assertEqual(required_fields, set(row))
            for value in row.values():
                self.assertIsInstance(value, str)
                self.assertTrue(value)

    def test_visible_and_rendered_counts_are_allowed_contract_fields(self):
        self.assertTrue(DECISION_OUTPUT["visible_count_contract_field_allowed"])
        self.assertTrue(DECISION_OUTPUT["rendered_count_contract_field_allowed"])
        fields = {row["allowed_contract_field"] for row in PLANNING_MATRIX}
        self.assertIn("visible_count", fields)
        self.assertIn("rendered_count", fields)

    def test_rendered_lower_than_visible_is_not_source_loss(self):
        self.assertTrue(
            DECISION_OUTPUT["rendered_lower_than_visible_means_reduction_candidate_only"]
        )
        self.assertFalse(
            DECISION_OUTPUT["rendered_lower_than_visible_source_loss_interpretation_allowed"]
        )
        reduction_row = next(
            row for row in PLANNING_MATRIX if row["row_id"] == "rendered_lower_than_visible"
        )
        self.assertEqual("source_loss_or_missing_source", reduction_row["forbidden_interpretation"])
        self.assertEqual("source_lineage_preserved", reduction_row["source_lineage_impact"])

    def test_frame_visibility_blocks_leak_inference(self):
        self.assertTrue(DECISION_OUTPUT["frame_visible_not_observed_blocks_leak_inference"])
        self.assertFalse(DECISION_OUTPUT["transparent_globe_leak_inferred"])
        self.assertFalse(DECISION_OUTPUT["transparent_globe_leak_fix_claimed"])
        frame_row = next(
            row for row in PLANNING_MATRIX if row["row_id"] == "frame_visible_not_observed"
        )
        self.assertEqual("blocked", frame_row["dependency_on_runtime"])
        self.assertEqual("blocked", frame_row["dependency_on_renderer_frame_buffer"])

    def test_next_checker_planning_supported_but_not_created(self):
        self.assertTrue(DECISION_OUTPUT["import_boundary_checker_planning_supported"])
        self.assertFalse(DECISION_OUTPUT["helper_creation_authorized"])
        self.assertFalse(DECISION_OUTPUT["checker_creation_authorized"])
        self.assertEqual(
            "dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning_gate",
            DECISION_OUTPUT["recommended_next_gate"],
        )

    def test_runtime_renderer_frame_and_artifact_boundaries_remain_closed(self):
        self.assertFalse(DECISION_OUTPUT["runtime_probe_expansion_authorized"])
        self.assertFalse(DECISION_OUTPUT["render_if_needed_authorized"])
        self.assertFalse(DECISION_OUTPUT["controller_renderer_frame_buffer_authorized"])
        self.assertFalse(DECISION_OUTPUT["artifact_generation_authorized"])
        self.assertFalse(DECISION_OUTPUT["formula_movement_authorized"])

    def test_no_correctness_readiness_or_global_methodology_claims(self):
        self.assertFalse(DECISION_OUTPUT["coordinate_correctness_claimed"])
        self.assertFalse(DECISION_OUTPUT["visual_parity_claimed"])
        self.assertFalse(DECISION_OUTPUT["readiness_claimed"])
        self.assertFalse(DECISION_OUTPUT["rrkal_wide_methodology_authorized"])
        self.assertIn("no correctness/visual parity/readiness/leak-fix claim", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()