"""Next bridge selection after computed-but-hidden cartography update."""

from __future__ import annotations

import unittest

from tests import test_displaytools_dynamic_point_post_computed_but_hidden_cartography_update as cartography


CANDIDATE_MATRIX = [
    {
        "candidate": "source_lineage_guard_contract",
        "current_classification": "preferred_andesite_guard_contract_candidate",
        "evidence_refs": [
            "post_computed_but_hidden_cartography_update",
            "computed_but_hidden_boundary",
            "sampling_visibility_boundary",
            "presentation_count_boundary",
            "occlusion_responsibility_boundary",
        ],
        "selectability": "selected",
        "reason_to_select_or_defer": (
            "protects extracted sampling, presentation, and computed-hidden surfaces "
            "from hidden, reduced, or occluded state being reinterpreted as source loss"
        ),
        "helper_required": "future_planning_only",
        "checker_required": "future_planning_only",
        "runtime_risk": "low",
        "formula_risk": "low",
        "frame_renderer_risk": "low",
        "dependency_cycle_risk": "reduces_cycle_risk_across_extracted_surfaces",
        "source_lineage_pollution_risk": "guard_needed_to_keep_pollution_risk_low",
        "recommended_next_action": "select_for_contract_planning",
        "stop_condition": "stop if hidden, reduced, or occluded is treated as source loss",
    },
    {
        "candidate": "occlusion_responsibility_contract",
        "current_classification": "andesite_candidate_near_mask_formula_boundary",
        "evidence_refs": [
            "post_computed_but_hidden_cartography_update",
            "occlusion_responsibility_boundary",
            "sampling_visibility_boundary",
            "computed_but_hidden_boundary",
        ],
        "selectability": "deferred",
        "reason_to_select_or_defer": "useful but overlaps mask visibility and formula stop-lines",
        "helper_required": "future_planning_possible",
        "checker_required": "future_checker_needed_before_extraction",
        "runtime_risk": "medium",
        "formula_risk": "medium",
        "frame_renderer_risk": "medium",
        "dependency_cycle_risk": "medium_overlap_with_mask_and_hidden_contracts",
        "source_lineage_pollution_risk": "guard_required_before_extraction",
        "recommended_next_action": "defer_until_source_lineage_guard_is_planned",
        "stop_condition": "stop if mask formula or frame truth is required",
    },
    {
        "candidate": "mask_visibility_contract",
        "current_classification": "andesite_candidate_partially_covered_by_sampling_visibility",
        "evidence_refs": [
            "post_computed_but_hidden_cartography_update",
            "sampling_visibility_boundary",
            "runtime_probe_result_interpretation",
        ],
        "selectability": "deferred",
        "reason_to_select_or_defer": "valuable but should be sequenced after source guard to avoid source deletion drift",
        "helper_required": "future_planning_possible",
        "checker_required": "future_checker_review_needed",
        "runtime_risk": "low",
        "formula_risk": "medium",
        "frame_renderer_risk": "low",
        "dependency_cycle_risk": "medium_overlap_with_occlusion_contract",
        "source_lineage_pollution_risk": "guard_required_before_extraction",
        "recommended_next_action": "defer_until_guard_boundary_is_selected",
        "stop_condition": "stop if mask hidden is treated as missing source",
    },
    {
        "candidate": "presentation_reduction_contract",
        "current_classification": "andesite_candidate_partially_covered_by_presentation_count",
        "evidence_refs": [
            "post_computed_but_hidden_cartography_update",
            "presentation_count_boundary",
            "sampling_visibility_boundary",
        ],
        "selectability": "deferred",
        "reason_to_select_or_defer": "already partly cooled and lower cycle pressure than source guard",
        "helper_required": "future_planning_possible",
        "checker_required": "presentation_count_checker_context_exists",
        "runtime_risk": "low",
        "formula_risk": "low",
        "frame_renderer_risk": "low",
        "dependency_cycle_risk": "low",
        "source_lineage_pollution_risk": "guard_required_before_expansion",
        "recommended_next_action": "defer_as_lower_entropy_than_source_guard",
        "stop_condition": "stop if rendered lower than visible is treated as source loss",
    },
    {
        "candidate": "frame_visibility_stop_line_closure",
        "current_classification": "granite_stop_line_candidate",
        "evidence_refs": [
            "post_computed_but_hidden_cartography_update",
            "frame_visibility_stop_line_planning",
        ],
        "selectability": "granite_stop_line",
        "reason_to_select_or_defer": "requires frame policy before any extraction path",
        "helper_required": "not_for_this_selection_gate",
        "checker_required": "not_for_this_selection_gate",
        "runtime_risk": "high",
        "formula_risk": "medium",
        "frame_renderer_risk": "high",
        "dependency_cycle_risk": "high_near_frame_runtime",
        "source_lineage_pollution_risk": "not_primary_risk",
        "recommended_next_action": "defer_to_stop_line_route",
        "stop_condition": "stop if frame buffer, renderer, or render_if_needed is required",
    },
    {
        "candidate": "transparent_globe_leak_fault_review",
        "current_classification": "granite_fault_review_stop_line_candidate",
        "evidence_refs": [
            "post_computed_but_hidden_cartography_update",
            "frame_visibility_stop_line_planning",
            "occlusion_responsibility_boundary",
        ],
        "selectability": "granite_stop_line",
        "reason_to_select_or_defer": "leak remains not inferred and must not become a fix or correctness claim",
        "helper_required": "not_for_this_selection_gate",
        "checker_required": "not_for_this_selection_gate",
        "runtime_risk": "high",
        "formula_risk": "medium",
        "frame_renderer_risk": "high",
        "dependency_cycle_risk": "high_near_fault_and_visual_claims",
        "source_lineage_pollution_risk": "not_primary_risk",
        "recommended_next_action": "defer_to_fault_review_route",
        "stop_condition": "stop if transparent-globe leak is inferred or fixed",
    },
]


SELECTED_NEXT_BRIDGE = {
    "selected_next_bridge_candidate": "source_lineage_guard_contract",
    "selection_reason": (
        "It is descriptor, contract, and ledger expressible; protects the three "
        "extracted andesite surfaces from source-loss drift; lowers dependency-cycle "
        "risk before occlusion, mask, or reduction expansion; and needs no runtime, "
        "frame, renderer, or formula access."
    ),
    "recommended_next_gate": "dynamic_point_lod_view_frame_source_lineage_guard_contract_planning_gate",
}


DECISION_OUTPUT = {
    "next_bridge_selection_passed": True,
    "selected_next_bridge_candidate": SELECTED_NEXT_BRIDGE["selected_next_bridge_candidate"],
    "selection_reason": SELECTED_NEXT_BRIDGE["selection_reason"],
    "deferred_candidate_count": 3,
    "granite_stop_line_candidate_count": 2,
    "dependency_cycle_watch_enabled": True,
    "source_lineage_guard_priority_reviewed": True,
    "runtime_execution_authorized": False,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "render_core_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "hidden_as_missing_interpretation_authorized": False,
    "source_lineage_loss_interpretation_authorized": False,
    "transparent_globe_leak_inferred": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": SELECTED_NEXT_BRIDGE["recommended_next_gate"],
}


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point post-computed-but-hidden next bridge selection gate. "
    "No helper creation, no checker creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry.py change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing "
    "interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, "
    "no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide "
    "methodology promotion, and no push."
)


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_post_computed_but_hidden_next_bridge_selection.v1",
    "evidence_sources": {
        "post_computed_but_hidden_cartography_update": "a357bbe",
        "computed_but_hidden_boundary": "b7b11a5",
        "presentation_count_boundary": "d25e94c_lineage",
        "sampling_visibility_boundary": "76abda8_lineage",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "grafting_path_minimal_evidence": "87cb579",
        "previous_next_andesite_bridge_selection": "650333f",
        "runtime_executed_by_this_gate": False,
    },
    "candidate_comparison_matrix": CANDIDATE_MATRIX,
    "selected_next_bridge": SELECTED_NEXT_BRIDGE,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointPostComputedButHiddenNextBridgeSelectionTest(unittest.TestCase):
    def test_packet_shape_and_schema(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "candidate_comparison_matrix",
                "selected_next_bridge",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_post_computed_but_hidden_next_bridge_selection.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_cartography_prerequisite_registered_three_extracted_surfaces(self) -> None:
        decision = cartography.PACKET["decision_output"]
        self.assertTrue(decision["cartography_update_passed"])
        self.assertTrue(decision["computed_but_hidden_boundary_registered"])
        self.assertEqual(decision["extracted_andesite_surface_count"], 3)
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        self.assertTrue(decision["next_bridge_selection_required"])

    def test_candidate_matrix_has_required_rows_and_fields(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]}
        self.assertEqual(
            set(rows),
            {
                "source_lineage_guard_contract",
                "occlusion_responsibility_contract",
                "mask_visibility_contract",
                "presentation_reduction_contract",
                "frame_visibility_stop_line_closure",
                "transparent_globe_leak_fault_review",
            },
        )
        required = {
            "candidate",
            "current_classification",
            "evidence_refs",
            "selectability",
            "reason_to_select_or_defer",
            "helper_required",
            "checker_required",
            "runtime_risk",
            "formula_risk",
            "frame_renderer_risk",
            "dependency_cycle_risk",
            "source_lineage_pollution_risk",
            "recommended_next_action",
            "stop_condition",
        }
        for row in rows.values():
            self.assertEqual(set(row), required)
            self.assertTrue(row["evidence_refs"])
            self.assertTrue(row["reason_to_select_or_defer"])
            self.assertTrue(row["stop_condition"])

    def test_source_lineage_guard_is_selected_after_comparison(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]}
        selected = rows["source_lineage_guard_contract"]
        self.assertEqual(selected["selectability"], "selected")
        self.assertEqual(selected["runtime_risk"], "low")
        self.assertEqual(selected["formula_risk"], "low")
        self.assertEqual(selected["frame_renderer_risk"], "low")
        self.assertEqual(
            selected["dependency_cycle_risk"],
            "reduces_cycle_risk_across_extracted_surfaces",
        )
        self.assertEqual(
            selected["recommended_next_action"],
            "select_for_contract_planning",
        )
        self.assertIn("computed_but_hidden_boundary", selected["evidence_refs"])
        self.assertIn("presentation_count_boundary", selected["evidence_refs"])
        self.assertIn("sampling_visibility_boundary", selected["evidence_refs"])

    def test_deferred_and_granite_candidates_are_classified(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]}
        deferred = {
            candidate for candidate, row in rows.items()
            if row["selectability"] == "deferred"
        }
        granite = {
            candidate for candidate, row in rows.items()
            if row["selectability"] == "granite_stop_line"
        }
        self.assertEqual(
            deferred,
            {
                "occlusion_responsibility_contract",
                "mask_visibility_contract",
                "presentation_reduction_contract",
            },
        )
        self.assertEqual(
            granite,
            {
                "frame_visibility_stop_line_closure",
                "transparent_globe_leak_fault_review",
            },
        )
        self.assertEqual(rows["frame_visibility_stop_line_closure"]["frame_renderer_risk"], "high")
        self.assertEqual(rows["transparent_globe_leak_fault_review"]["frame_renderer_risk"], "high")

    def test_selection_does_not_infer_source_loss_or_leak(self) -> None:
        for row in PACKET["candidate_comparison_matrix"]:
            self.assertNotIn("treat as source loss", row["reason_to_select_or_defer"])
            self.assertNotIn("leak fixed", row["reason_to_select_or_defer"])
        decision = PACKET["decision_output"]
        self.assertFalse(decision["hidden_as_missing_interpretation_authorized"])
        self.assertFalse(decision["source_lineage_loss_interpretation_authorized"])
        self.assertFalse(decision["transparent_globe_leak_inferred"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])

    def test_decision_output(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["next_bridge_selection_passed"])
        self.assertEqual(decision["selected_next_bridge_candidate"], "source_lineage_guard_contract")
        self.assertTrue(decision["selection_reason"])
        self.assertEqual(decision["deferred_candidate_count"], 3)
        self.assertEqual(decision["granite_stop_line_candidate_count"], 2)
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        self.assertTrue(decision["source_lineage_guard_priority_reviewed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_source_lineage_guard_contract_planning_gate",
        )

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        for key in (
            "runtime_execution_authorized",
            "helper_creation_authorized",
            "checker_creation_authorized",
            "render_core_change_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "hidden_as_missing_interpretation_authorized",
            "source_lineage_loss_interpretation_authorized",
            "transparent_globe_leak_inferred",
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
        self.assertIn("no frame buffer read", BOUNDARY_STATEMENT)
        self.assertIn("no hidden-as-missing interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no source-lineage-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no transparent-globe leak inference", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
