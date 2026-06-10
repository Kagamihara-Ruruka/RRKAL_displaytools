"""Selection gate for the next dynamic point andesite bridge candidate."""

from __future__ import annotations

import unittest


CANDIDATE_IDS = {
    "presentation_count_contract",
    "source_lineage_guard_contract",
    "computed_but_hidden_contract",
    "occlusion_responsibility_contract",
    "projection_shadow_interface_contract",
    "frame_visibility_stop_line_closure",
    "transparent_globe_leak_fault_review",
}

RISK_LEVELS = {"low", "medium", "medium_high", "high"}
BLAST_RADIUS = {"small", "medium", "large"}
NEXT_ACTIONS = {
    "select_for_next_gate",
    "defer_as_already_guarded",
    "defer_until_frame_authorization",
    "defer_as_projection_interface_only",
    "defer_as_fault_review",
}

CANDIDATE_COMPARISON_MATRIX = [
    {
        "candidate_id": "presentation_count_contract",
        "current_classification": "andesite_bridge_descriptor_contract_candidate",
        "evidence_supporting_it": [
            "sampling_visibility_runtime_probe_result_interpretation",
            "sampling_visibility_minimal_boundary",
            "sampling_visibility_cartography_update",
            "occlusion_responsibility_boundary",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "visible_count_observation",
            "rendered_count_observation",
            "sampling_or_presentation_reduction_candidate",
            "source_lineage_integrity_token",
            "frame_visible_not_observed",
        ],
        "must_remain_blocked": [
            "frame_buffer_read",
            "render_if_needed_call",
            "renderer_execution",
            "visual_correctness_claim",
        ],
        "checker_need": "new_dedicated_checker_likely_needed",
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
        "candidate_id": "source_lineage_guard_contract",
        "current_classification": "already_guarded_descriptor_contract_surface",
        "evidence_supporting_it": [
            "source_lineage_boundary_minimal_extraction",
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
        "candidate_id": "computed_but_hidden_contract",
        "current_classification": "andesite_bridge_contract_candidate",
        "evidence_supporting_it": [
            "grafting_path_minimal_evidence",
            "occlusion_responsibility_boundary",
            "view_frame_occlusion_structure_settlement",
            "sampling_visibility_cartography_update",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "hidden_is_not_missing",
            "occluded_is_not_source_lineage_loss",
            "frame_visible_not_observed",
        ],
        "must_remain_blocked": ["frame_visibility_truth", "renderer_execution", "leak_inference"],
        "checker_need": "future_checker_needed_if_helper_planned",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "medium",
        "expected_blast_radius": "small",
        "recommended_next_action": "defer_as_already_guarded",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "occlusion_responsibility_contract",
        "current_classification": "andesite_bridge_contract_candidate_near_runtime_seam",
        "evidence_supporting_it": [
            "occlusion_responsibility_boundary",
            "sampling_visibility_runtime_probe_result_interpretation",
            "sampling_visibility_cartography_update",
        ],
        "extractable_as_descriptor_contract_ledger": [
            "mask_can_hide_overlay_without_source_loss",
            "globe_mask_responsibility_candidate",
            "source_lineage_guard",
        ],
        "must_remain_blocked": ["mask_formula_movement", "alpha_compose_formula", "frame_visibility_truth"],
        "checker_need": "future_checker_needed_if_helper_planned",
        "runtime_need": "not_needed_for_selection_gate",
        "risk_level": "medium",
        "expected_blast_radius": "medium",
        "recommended_next_action": "defer_as_already_guarded",
        "suitable_as_next_gate": False,
        "requires_renderer_controller_frame_buffer": False,
        "requires_formula_movement": False,
        "requires_correctness_or_leak_fix_claim": False,
    },
    {
        "candidate_id": "projection_shadow_interface_contract",
        "current_classification": "core_interface_only",
        "evidence_supporting_it": [
            "projection_interface_shadow_gate",
            "view_frame_occlusion_structure_settlement",
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
        "evidence_supporting_it": [
            "frame_visibility_stop_line_planning",
            "sampling_visibility_cartography_update",
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
        "evidence_supporting_it": [
            "frame_visibility_stop_line_planning",
            "occlusion_responsibility_boundary",
            "sampling_visibility_cartography_update",
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
]

REJECTED_OR_DEFERRED_CANDIDATES = [
    {
        "candidate_id": row["candidate_id"],
        "reason": row["recommended_next_action"],
        "current_classification": row["current_classification"],
    }
    for row in CANDIDATE_COMPARISON_MATRIX
    if not row["suitable_as_next_gate"]
]

SELECTED_NEXT_ANDESITE_BRIDGE_CANDIDATE = {
    "candidate_id": "presentation_count_contract",
    "selection_reason": (
        "It has direct second-probe evidence for visible/rendered counts, can be "
        "described as descriptor/contract/ledger data, has small blast radius, and "
        "does not require renderer, controller, frame buffer, formula movement, or claims."
    ),
    "recommended_next_gate": "dynamic_point_lod_view_frame_presentation_count_contract_planning_gate",
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "runtime_execution_authorized": False,
    "formula_movement_authorized": False,
    "rrkal_wide_methodology_authorized": False,
}

DECISION_OUTPUT = {
    "next_andesite_bridge_selection_gate_passed": True,
    "candidate_matrix_defined": True,
    "candidate_count": 7,
    "selected_candidate": "presentation_count_contract",
    "selected_candidate_suitable_as_next_gate": True,
    "rejected_or_deferred_count": 6,
    "frame_visibility_remains_stop_line": True,
    "transparent_globe_leak_not_inferred": True,
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
    "recommended_next_gate": "dynamic_point_lod_view_frame_presentation_count_contract_planning_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame next andesite bridge selection gate. "
    "No helper creation, no checker creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no formula movement, no correctness/visual "
    "parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_next_andesite_bridge_selection.v1",
    "evidence_sources": {
        "sampling_visibility_cartography_update": "b9b37c1",
        "sampling_visibility_minimal_boundary": "76abda8",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "sampling_visibility_runtime_probe_result_interpretation": "5503eb0",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "grafting_path_minimal_evidence": "87cb579",
        "projection_interface_shadow_gate": "6289c60",
        "earlier_dynamic_point_cartography": "second_cutout_cartography_inventory",
        "runtime_executed_by_this_gate": False,
    },
    "candidate_comparison_matrix": CANDIDATE_COMPARISON_MATRIX,
    "rejected_or_deferred_candidates": REJECTED_OR_DEFERRED_CANDIDATES,
    "selected_next_andesite_bridge_candidate": SELECTED_NEXT_ANDESITE_BRIDGE_CANDIDATE,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointNextAndesiteBridgeSelectionTest(unittest.TestCase):
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
            "rrkal.displaytools.dynamic_point_lod_view_frame_next_andesite_bridge_selection.v1",
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

    def test_selected_candidate_is_presentation_count_contract(self) -> None:
        selected = PACKET["selected_next_andesite_bridge_candidate"]
        self.assertEqual(selected["candidate_id"], "presentation_count_contract")
        self.assertEqual(
            selected["recommended_next_gate"],
            "dynamic_point_lod_view_frame_presentation_count_contract_planning_gate",
        )
        self.assertFalse(selected["helper_creation_authorized"])
        self.assertFalse(selected["checker_creation_authorized"])
        self.assertFalse(selected["runtime_execution_authorized"])
        self.assertFalse(selected["formula_movement_authorized"])
        self.assertFalse(selected["rrkal_wide_methodology_authorized"])

    def test_selected_candidate_has_low_risk_small_blast_radius(self) -> None:
        rows = {row["candidate_id"]: row for row in PACKET["candidate_comparison_matrix"]}
        selected = rows["presentation_count_contract"]
        self.assertTrue(selected["suitable_as_next_gate"])
        self.assertEqual(selected["risk_level"], "low")
        self.assertEqual(selected["expected_blast_radius"], "small")
        self.assertEqual(selected["recommended_next_action"], "select_for_next_gate")
        self.assertFalse(selected["requires_renderer_controller_frame_buffer"])
        self.assertFalse(selected["requires_formula_movement"])
        self.assertFalse(selected["requires_correctness_or_leak_fix_claim"])
        self.assertIn("visible_count_observation", selected["extractable_as_descriptor_contract_ledger"])
        self.assertIn("rendered_count_observation", selected["extractable_as_descriptor_contract_ledger"])

    def test_deferred_candidates_cover_stop_lines_and_interface_only_surfaces(self) -> None:
        deferred = {row["candidate_id"]: row for row in PACKET["rejected_or_deferred_candidates"]}
        self.assertEqual(set(deferred), CANDIDATE_IDS - {"presentation_count_contract"})
        self.assertEqual(deferred["source_lineage_guard_contract"]["reason"], "defer_as_already_guarded")
        self.assertEqual(deferred["computed_but_hidden_contract"]["reason"], "defer_as_already_guarded")
        self.assertEqual(deferred["occlusion_responsibility_contract"]["reason"], "defer_as_already_guarded")
        self.assertEqual(deferred["projection_shadow_interface_contract"]["reason"], "defer_as_projection_interface_only")
        self.assertEqual(deferred["frame_visibility_stop_line_closure"]["reason"], "defer_until_frame_authorization")
        self.assertEqual(deferred["transparent_globe_leak_fault_review"]["reason"], "defer_as_fault_review")

    def test_no_unsuitable_candidate_requires_selection(self) -> None:
        for row in PACKET["candidate_comparison_matrix"]:
            if row["candidate_id"] == "presentation_count_contract":
                continue
            self.assertFalse(row["suitable_as_next_gate"])
        rows = {row["candidate_id"]: row for row in PACKET["candidate_comparison_matrix"]}
        self.assertTrue(rows["frame_visibility_stop_line_closure"]["requires_renderer_controller_frame_buffer"])
        self.assertTrue(rows["transparent_globe_leak_fault_review"]["requires_renderer_controller_frame_buffer"])
        self.assertTrue(rows["transparent_globe_leak_fault_review"]["requires_correctness_or_leak_fix_claim"])
        self.assertFalse(rows["projection_shadow_interface_contract"]["requires_formula_movement"])
        self.assertIn("projection_formula_movement", rows["projection_shadow_interface_contract"]["must_remain_blocked"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["next_andesite_bridge_selection_gate_passed"])
        self.assertTrue(decision["candidate_matrix_defined"])
        self.assertEqual(decision["candidate_count"], 7)
        self.assertEqual(decision["selected_candidate"], "presentation_count_contract")
        self.assertTrue(decision["selected_candidate_suitable_as_next_gate"])
        self.assertEqual(decision["rejected_or_deferred_count"], 6)
        self.assertTrue(decision["frame_visibility_remains_stop_line"])
        self.assertTrue(decision["transparent_globe_leak_not_inferred"])
        for key in (
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
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()