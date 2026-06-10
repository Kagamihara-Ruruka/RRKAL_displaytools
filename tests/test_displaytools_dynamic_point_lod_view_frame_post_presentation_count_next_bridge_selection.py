"""Select the next dynamic point bridge after presentation count extraction."""

from __future__ import annotations

import unittest


CANDIDATE_IDS = {
    "computed_but_hidden_contract",
    "occlusion_responsibility_contract",
    "source_lineage_guard_contract",
    "projection_shadow_interface_contract",
    "frame_visibility_stop_line_closure",
    "transparent_globe_leak_fault_review",
    "presentation_count_contract_followup",
}

RISK_LEVELS = {"low", "medium", "medium_high", "high"}
BLAST_RADIUS = {"small", "medium", "large"}
NEXT_ACTIONS = {
    "select_for_next_gate",
    "defer_as_already_extracted",
    "defer_as_already_guarded",
    "defer_until_mask_alpha_boundary",
    "defer_until_frame_authorization",
    "defer_as_projection_interface_only",
    "defer_as_fault_review",
}

CANDIDATE_COMPARISON_MATRIX = [
    {
        "candidate_id": "computed_but_hidden_contract",
        "current_classification": "andesite_bridge_contract_candidate",
        "post_presentation_count_status": "best_remaining_low_risk_bridge",
        "evidence_supporting_it": [
            "presentation_count_cartography_update",
            "occlusion_responsibility_boundary",
            "grafting_path_minimal_evidence",
            "view_frame_occlusion_structure_settlement",
            "sampling_visibility_minimal_boundary",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "source_present_can_be_true_while_frame_visible_false",
            "hidden_is_not_missing",
            "occluded_is_not_source_lineage_loss",
            "computed_but_hidden_semantics",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
        ],
        "must_remain_blocked": [
            "frame_buffer_read",
            "renderer_execution",
            "render_if_needed_call",
            "transparent_globe_leak_inference",
            "source_loss_interpretation",
        ],
        "checker_need": "dedicated_checker_likely_needed_before_helper",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "low",
        "expected_blast_radius": "small",
        "recommended_next_action": "select_for_next_gate",
        "suitable_as_next_gate": True,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "occlusion_responsibility_contract",
        "current_classification": "andesite_bridge_contract_candidate_near_mask_alpha_seam",
        "post_presentation_count_status": "valuable_but_closer_to_runtime_seam",
        "evidence_supporting_it": [
            "occlusion_responsibility_boundary",
            "sampling_visibility_runtime_probe_result_interpretation",
            "sampling_visibility_minimal_boundary",
            "presentation_count_cartography_update",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "mask_can_hide_overlay_without_source_loss",
            "globe_mask_responsibility_candidate",
            "source_lineage_guard",
        ],
        "must_remain_blocked": [
            "mask_formula_movement",
            "alpha_compose_formula",
            "frame_visibility_truth",
            "transparent_globe_leak_inference",
        ],
        "checker_need": "future_checker_needed_if_helper_planned",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "medium",
        "expected_blast_radius": "medium",
        "recommended_next_action": "defer_until_mask_alpha_boundary",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "source_lineage_guard_contract",
        "current_classification": "already_extracted_guard_surface",
        "post_presentation_count_status": "guard_reused_by_new_candidates",
        "evidence_supporting_it": [
            "source_lineage_minimal_extraction",
            "presentation_count_minimal_boundary",
            "sampling_visibility_minimal_boundary",
            "occlusion_responsibility_boundary",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "source_lineage_integrity_token",
            "source_present_not_visibility_truth",
            "source_loss_interpretation_blocked",
        ],
        "must_remain_blocked": ["provider_runtime", "live_source", "cache_database_io"],
        "checker_need": "existing_lineage_checker_context_exists",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "low",
        "expected_blast_radius": "small",
        "recommended_next_action": "defer_as_already_guarded",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "projection_shadow_interface_contract",
        "current_classification": "core_interface_only",
        "post_presentation_count_status": "not_an_andesite_extraction_target",
        "evidence_supporting_it": [
            "projection_interface_shadow_gate",
            "view_frame_occlusion_structure_settlement",
            "runtime_probe_execution_gate",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "projection_policy_ref",
            "flip_policy_ref",
            "mask_policy_ref",
            "formula_behavior_not_executed",
        ],
        "must_remain_blocked": [
            "project_ais_to_screen_movement",
            "project_aircraft_to_screen_movement",
            "projection_formula_movement",
            "coordinate_correctness_claim",
        ],
        "checker_need": "existing_shadow_checker_context_exists",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "medium_high",
        "expected_blast_radius": "medium",
        "recommended_next_action": "defer_as_projection_interface_only",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "frame_visibility_stop_line_closure",
        "current_classification": "not_observed_frame_stop_line",
        "post_presentation_count_status": "still_requires_frame_authorization",
        "evidence_supporting_it": [
            "frame_visibility_stop_line_planning",
            "presentation_count_cartography_update",
            "sampling_visibility_runtime_probe_result_interpretation",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "frame_visible_not_observed",
            "frame_buffer_read_blocked",
            "render_if_needed_call_blocked",
        ],
        "must_remain_blocked": ["frame_rgba", "renderer_execution", "controller_instantiation"],
        "checker_need": "not_prioritized_until_runtime_surface_policy_closes",
        "runtime_need": "would_need_future_authorization_for_observation",
        "risk_level": "high",
        "expected_blast_radius": "large",
        "recommended_next_action": "defer_until_frame_authorization",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": True,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "transparent_globe_leak_fault_review",
        "current_classification": "unresolved_not_inferred_fault",
        "post_presentation_count_status": "still_fault_review_not_contract_extraction",
        "evidence_supporting_it": [
            "frame_visibility_stop_line_planning",
            "occlusion_responsibility_boundary",
            "presentation_count_cartography_update",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "transparent_globe_leak_not_inferred",
            "leak_fix_claim_blocked",
            "fault_review_only",
        ],
        "must_remain_blocked": ["leak_fix_claim", "visual_correctness_claim", "frame_visibility_inference"],
        "checker_need": "not_prioritized_until_fault_review_scope_exists",
        "runtime_need": "would_need_future_frame_or_renderer_authorization",
        "risk_level": "high",
        "expected_blast_radius": "large",
        "recommended_next_action": "defer_as_fault_review",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": True,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": True,
    },
    {
        "candidate_id": "presentation_count_contract_followup",
        "current_classification": "extracted_andesite_bridge_descriptor_contract_ledger",
        "post_presentation_count_status": "already_extracted",
        "evidence_supporting_it": [
            "presentation_count_minimal_boundary",
            "presentation_count_cartography_update",
            "presentation_count_import_boundary_checker",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "visible_count",
            "rendered_count",
            "rendered_lower_than_visible",
            "source_loss_not_inferred",
        ],
        "must_remain_blocked": [
            "source_loss_interpretation",
            "frame_truth_claim",
            "readiness_claim",
        ],
        "checker_need": "already_available",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "low",
        "expected_blast_radius": "small",
        "recommended_next_action": "defer_as_already_extracted",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
]

REJECTED_OR_DEFERRED_CANDIDATES = [
    {
        "candidate_id": row["candidate_id"],
        "reason": row["recommended_next_action"],
        "current_classification": row["current_classification"],
        "post_presentation_count_status": row["post_presentation_count_status"],
    }
    for row in CANDIDATE_COMPARISON_MATRIX
    if not row["suitable_as_next_gate"]
]

SELECTED_NEXT_ANDESITE_BRIDGE_CANDIDATE = {
    "candidate_id": "computed_but_hidden_contract",
    "selection_reason": (
        "After presentation count was extracted, the lowest-risk remaining bridge is the "
        "semantic contract that a computed point can be hidden without becoming missing. "
        "It is descriptor/contract/ledger-shaped and does not require frame buffer, "
        "renderer, formula movement, source-loss interpretation, or leak-fix claims."
    ),
    "recommended_next_gate": "dynamic_point_lod_view_frame_computed_but_hidden_contract_planning_gate",
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "runtime_execution_authorized": False,
    "formula_movement_authorized": False,
    "rrkal_wide_methodology_authorized": False,
}

DECISION_OUTPUT = {
    "post_presentation_count_next_bridge_selection_gate_passed": True,
    "candidate_matrix_defined": True,
    "candidate_count": 7,
    "presentation_count_already_extracted": True,
    "selected_candidate": "computed_but_hidden_contract",
    "selected_candidate_suitable_as_next_gate": True,
    "rejected_or_deferred_count": 6,
    "frame_visibility_remains_stop_line": True,
    "transparent_globe_leak_not_inferred": True,
    "source_loss_interpretation_authorized": False,
    "production_source_change_authorized": False,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "runtime_probe_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_computed_but_hidden_contract_planning_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame post-presentation-count next bridge selection gate. "
    "No helper creation, no checker creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no formula movement, no source-loss "
    "interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/"
    "leak-fix claim, no RRKAL-wide methodology promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection.v1",
    "evidence_sources": {
        "presentation_count_cartography_update": "a5fe556",
        "presentation_count_minimal_boundary": "82e8acb",
        "sampling_visibility_minimal_boundary": "76abda8",
        "sampling_visibility_cartography_update": "b9b37c1",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "grafting_path_minimal_evidence": "87cb579",
        "projection_interface_shadow_gate": "6289c60",
        "runtime_executed_by_this_gate": False,
    },
    "candidate_comparison_matrix": CANDIDATE_COMPARISON_MATRIX,
    "rejected_or_deferred_candidates": REJECTED_OR_DEFERRED_CANDIDATES,
    "selected_next_andesite_bridge_candidate": SELECTED_NEXT_ANDESITE_BRIDGE_CANDIDATE,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointPostPresentationCountNextBridgeSelectionTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "candidate_comparison_matrix",
                "rejected_or_deferred_candidates",
                "selected_next_andesite_bridge_candidate",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_all_required_candidates_are_compared(self) -> None:
        self.assertEqual(
            {row["candidate_id"] for row in PACKET["candidate_comparison_matrix"]},
            CANDIDATE_IDS,
        )
        for row in PACKET["candidate_comparison_matrix"]:
            self.assertEqual(
                set(row),
                {
                    "candidate_id",
                    "current_classification",
                    "post_presentation_count_status",
                    "evidence_supporting_it",
                    "extractable_as_descriptor_contract_ledger",
                    "must_remain_blocked",
                    "checker_need",
                    "runtime_need",
                    "risk_level",
                    "expected_blast_radius",
                    "recommended_next_action",
                    "suitable_as_next_gate",
                    "requires_renderer_controller_frame_buffer",
                    "requires_formula_movement",
                    "requires_correctness_or_leak_fix_claim",
                },
            )
            self.assertIn(row["risk_level"], RISK_LEVELS)
            self.assertIn(row["expected_blast_radius"], BLAST_RADIUS)
            self.assertIn(row["recommended_next_action"], NEXT_ACTIONS)
            self.assertTrue(row["evidence_supporting_it"])
            self.assertTrue(row["extractable_as_descriptor_contract_ledger"])
            self.assertTrue(row["must_remain_blocked"])

    def test_selected_candidate_is_computed_but_hidden_contract(self) -> None:
        selected = PACKET["selected_next_andesite_bridge_candidate"]
        self.assertEqual(selected["candidate_id"], "computed_but_hidden_contract")
        self.assertEqual(
            selected["recommended_next_gate"],
            "dynamic_point_lod_view_frame_computed_but_hidden_contract_planning_gate",
        )
        self.assertFalse(selected["helper_creation_authorized"])
        self.assertFalse(selected["checker_creation_authorized"])
        self.assertFalse(selected["runtime_execution_authorized"])
        self.assertFalse(selected["formula_movement_authorized"])
        self.assertFalse(selected["rrkal_wide_methodology_authorized"])

    def test_selected_candidate_has_low_risk_small_blast_radius(self) -> None:
        rows = {row["candidate_id"]: row for row in PACKET["candidate_comparison_matrix"]}
        selected = rows["computed_but_hidden_contract"]
        self.assertTrue(selected["suitable_as_next_gate"])
        self.assertEqual(selected["risk_level"], "low")
        self.assertEqual(selected["expected_blast_radius"], "small")
        self.assertEqual(selected["recommended_next_action"], "select_for_next_gate")
        self.assertFalse(selected["requires_renderer_controller_frame_buffer"])
        self.assertFalse(selected["requires_formula_movement"])
        self.assertFalse(selected["requires_correctness_or_leak_fix_claim"])
        self.assertIn(
            "source_present_can_be_true_while_frame_visible_false",
            selected["extractable_as_descriptor_contract_ledger"],
        )
        self.assertIn("hidden_is_not_missing", selected["extractable_as_descriptor_contract_ledger"])
        self.assertIn("occluded_is_not_source_lineage_loss", selected["extractable_as_descriptor_contract_ledger"])

    def test_deferred_candidates_cover_extracted_guarded_and_stop_line_surfaces(self) -> None:
        deferred = {row["candidate_id"]: row for row in PACKET["rejected_or_deferred_candidates"]}
        self.assertEqual(set(deferred), CANDIDATE_IDS - {"computed_but_hidden_contract"})
        self.assertEqual(deferred["presentation_count_contract_followup"]["reason"], "defer_as_already_extracted")
        self.assertEqual(deferred["source_lineage_guard_contract"]["reason"], "defer_as_already_guarded")
        self.assertEqual(deferred["occlusion_responsibility_contract"]["reason"], "defer_until_mask_alpha_boundary")
        self.assertEqual(deferred["projection_shadow_interface_contract"]["reason"], "defer_as_projection_interface_only")
        self.assertEqual(deferred["frame_visibility_stop_line_closure"]["reason"], "defer_until_frame_authorization")
        self.assertEqual(deferred["transparent_globe_leak_fault_review"]["reason"], "defer_as_fault_review")

    def test_high_risk_frame_and_leak_paths_remain_deferred(self) -> None:
        rows = {row["candidate_id"]: row for row in PACKET["candidate_comparison_matrix"]}
        self.assertTrue(rows["frame_visibility_stop_line_closure"]["requires_renderer_controller_frame_buffer"])
        self.assertTrue(rows["transparent_globe_leak_fault_review"]["requires_renderer_controller_frame_buffer"])
        self.assertTrue(rows["transparent_globe_leak_fault_review"]["requires_correctness_or_leak_fix_claim"])
        self.assertFalse(rows["frame_visibility_stop_line_closure"]["suitable_as_next_gate"])
        self.assertFalse(rows["transparent_globe_leak_fault_review"]["suitable_as_next_gate"])

    def test_occlusion_responsibility_is_deferred_because_mask_alpha_seam_is_closer(self) -> None:
        rows = {row["candidate_id"]: row for row in PACKET["candidate_comparison_matrix"]}
        occlusion = rows["occlusion_responsibility_contract"]
        self.assertFalse(occlusion["suitable_as_next_gate"])
        self.assertEqual(occlusion["recommended_next_action"], "defer_until_mask_alpha_boundary")
        self.assertIn("mask_formula_movement", occlusion["must_remain_blocked"])
        self.assertIn("alpha_compose_formula", occlusion["must_remain_blocked"])
        self.assertIn("frame_visibility_truth", occlusion["must_remain_blocked"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["post_presentation_count_next_bridge_selection_gate_passed"])
        self.assertTrue(decision["candidate_matrix_defined"])
        self.assertEqual(decision["candidate_count"], 7)
        self.assertTrue(decision["presentation_count_already_extracted"])
        self.assertEqual(decision["selected_candidate"], "computed_but_hidden_contract")
        self.assertTrue(decision["selected_candidate_suitable_as_next_gate"])
        self.assertEqual(decision["rejected_or_deferred_count"], 6)
        self.assertTrue(decision["frame_visibility_remains_stop_line"])
        self.assertTrue(decision["transparent_globe_leak_not_inferred"])
        for key in (
            "source_loss_interpretation_authorized",
            "production_source_change_authorized",
            "helper_creation_authorized",
            "checker_creation_authorized",
            "runtime_probe_change_authorized",
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
            self.assertIs(decision[key], False, key)

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker creation", BOUNDARY_STATEMENT)
        self.assertIn("no render_core change", BOUNDARY_STATEMENT)
        self.assertIn("no runtime probe change", BOUNDARY_STATEMENT)
        self.assertIn("no controller", BOUNDARY_STATEMENT)
        self.assertIn("no renderer", BOUNDARY_STATEMENT)
        self.assertIn("no source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no transparent-globe leak inference", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
