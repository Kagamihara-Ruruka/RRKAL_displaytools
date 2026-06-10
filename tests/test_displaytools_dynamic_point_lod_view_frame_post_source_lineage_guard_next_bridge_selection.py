"""Next bridge selection after source-lineage guard cartography update."""

from __future__ import annotations

import unittest

from tests import test_displaytools_dynamic_point_source_lineage_guard_cartography_update as cartography


EXTRACTED_INVENTORY = [
    "sampling_visibility_boundary",
    "presentation_count_boundary",
    "computed_but_hidden_boundary",
    "source_lineage_guard_boundary",
]

CANDIDATE_COMPARISON_MATRIX = [
    {
        "candidate": "occlusion_responsibility_contract",
        "current_classification": "remaining_andesite_candidate_deferred",
        "evidence_refs": [
            "occlusion_responsibility_boundary",
            "computed_but_hidden_boundary",
            "source_lineage_guard_boundary",
        ],
        "runtime_risk": "medium",
        "formula_risk": "medium_near_mask_and_occlusion_formula",
        "frame_stop_line_risk": "high_near_frame_and_leak_fault_surfaces",
        "dependency_cycle_risk": "medium_mask_occlusion_hidden_overlap",
        "source_loss_drift_guarded_by": "source_lineage_guard_boundary",
        "decision_pressure": "semantically important but closer to mask/frame/leak stop-line surfaces",
        "recommended_status": "deferred",
        "reason": "defer until mask and occlusion boundaries can be planned without formula movement or frame/leak inference",
        "stop_condition": "stop if selecting this requires mask formula, frame visibility, renderer, or leak inference",
    },
    {
        "candidate": "mask_visibility_contract",
        "current_classification": "remaining_andesite_candidate_deferred",
        "evidence_refs": [
            "sampling_visibility_boundary",
            "source_lineage_guard_boundary",
        ],
        "runtime_risk": "low_to_medium",
        "formula_risk": "medium_near_mask_formula",
        "frame_stop_line_risk": "medium_near_occlusion_overlap",
        "dependency_cycle_risk": "medium_overlap_with_occlusion_contract",
        "source_loss_drift_guarded_by": "source_lineage_guard_boundary",
        "decision_pressure": "near mask formula and occlusion overlap",
        "recommended_status": "deferred",
        "reason": "defer until a mask-specific boundary can avoid mask formula movement",
        "stop_condition": "stop if selecting this requires mask formula movement",
    },
    {
        "candidate": "presentation_reduction_contract",
        "current_classification": "remaining_andesite_candidate_selected",
        "evidence_refs": [
            "presentation_count_boundary",
            "sampling_visibility_boundary",
            "source_lineage_guard_boundary",
            "sampling_visibility_runtime_interpretation",
        ],
        "runtime_risk": "low",
        "formula_risk": "low",
        "frame_stop_line_risk": "low_frame_visibility_not_required",
        "dependency_cycle_risk": "low_after_source_lineage_guard",
        "source_loss_drift_guarded_by": "source_lineage_guard_boundary",
        "decision_pressure": "lowest remaining runtime and formula risk while clarifying rendered_count lower than visible_count",
        "recommended_status": "selected",
        "reason": "select because it can clarify presentation or sampling reduction without source loss and without touching frame visibility, renderer, mask formula, or occlusion runtime",
        "stop_condition": "stop if it fully duplicates presentation_count_boundary with no useful semantic surface",
    },
]

FRAME_VISIBILITY_STOP_LINE = {
    "surface": "frame_visibility_surface",
    "current_classification": "granite_stop_line",
    "candidate_in_this_gate": False,
    "reason": "frame visibility remains not observed and remains near renderer, frame buffer, and leak surfaces",
    "runtime_risk": "high",
    "stop_condition": "do not select frame visibility as andesite bridge in this gate",
}

DECISION_OUTPUT = {
    "next_bridge_selection_passed": True,
    "extracted_inventory_count": 4,
    "remaining_candidate_count": 3,
    "frame_visibility_surface_classification": "granite_stop_line",
    "selected_next_bridge_candidate": "presentation_reduction_contract",
    "deferred_candidates": [
        "occlusion_responsibility_contract",
        "mask_visibility_contract",
    ],
    "source_lineage_guard_reduces_source_loss_drift_for_all_candidates": True,
    "presentation_reduction_not_complete_duplicate": True,
    "runtime_execution_authorized": False,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "checker_modification_authorized": False,
    "render_core_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_gui_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "real_source_read_authorized": False,
    "source_lineage_mutation_authorized": False,
    "raw_row_seam_runtime_authorized": False,
    "direct_c3_to_c1_integration_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_presentation_reduction_contract_planning_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point post-source-lineage-guard next bridge selection gate. "
    "No helper creation, no checker creation, no render_core change, no runtime/probe/renderer/"
    "frame/formula/source behavior change, no c_4/Odoriba bypass, no source-loss/leak/"
    "correctness/readiness claim, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_post_source_lineage_guard_next_bridge_selection.v1",
    "extracted_inventory": EXTRACTED_INVENTORY,
    "candidate_comparison_matrix": CANDIDATE_COMPARISON_MATRIX,
    "frame_visibility_stop_line": FRAME_VISIBILITY_STOP_LINE,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointPostSourceLineageGuardNextBridgeSelectionTest(unittest.TestCase):
    def test_cartography_prerequisite_registered_four_extracted_surfaces(self) -> None:
        decision = cartography.PACKET["decision_output"]
        self.assertTrue(decision["cartography_update_passed"])
        self.assertTrue(decision["source_lineage_guard_boundary_registered"])
        self.assertEqual(decision["extracted_andesite_surface_count"], 4)
        self.assertEqual(
            {row["surface"] for row in cartography.PACKET["extracted_andesite_surfaces"]},
            set(EXTRACTED_INVENTORY),
        )

    def test_extracted_inventory_count_remains_four(self) -> None:
        self.assertEqual(set(PACKET["extracted_inventory"]), set(EXTRACTED_INVENTORY))
        self.assertEqual(PACKET["decision_output"]["extracted_inventory_count"], 4)

    def test_candidate_matrix_compares_exactly_three_remaining_mainline_candidates(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]}
        self.assertEqual(
            set(rows),
            {
                "occlusion_responsibility_contract",
                "mask_visibility_contract",
                "presentation_reduction_contract",
            },
        )
        self.assertEqual(PACKET["decision_output"]["remaining_candidate_count"], 3)

    def test_candidate_matrix_contains_required_risk_fields(self) -> None:
        required = {
            "candidate",
            "current_classification",
            "evidence_refs",
            "runtime_risk",
            "formula_risk",
            "frame_stop_line_risk",
            "dependency_cycle_risk",
            "source_loss_drift_guarded_by",
            "decision_pressure",
            "recommended_status",
            "reason",
            "stop_condition",
        }
        for row in PACKET["candidate_comparison_matrix"]:
            self.assertEqual(set(row), required)
            self.assertEqual(row["source_loss_drift_guarded_by"], "source_lineage_guard_boundary")
            self.assertTrue(row["evidence_refs"])
            self.assertTrue(row["runtime_risk"])
            self.assertTrue(row["formula_risk"])
            self.assertTrue(row["frame_stop_line_risk"])
            self.assertTrue(row["dependency_cycle_risk"])
            self.assertTrue(row["recommended_status"])

    def test_frame_visibility_is_granite_stop_line_not_candidate(self) -> None:
        stop_line = PACKET["frame_visibility_stop_line"]
        self.assertEqual(stop_line["surface"], "frame_visibility_surface")
        self.assertEqual(stop_line["current_classification"], "granite_stop_line")
        self.assertFalse(stop_line["candidate_in_this_gate"])
        self.assertEqual(PACKET["decision_output"]["frame_visibility_surface_classification"], "granite_stop_line")
        self.assertNotIn(
            "frame_visibility_surface",
            {row["candidate"] for row in PACKET["candidate_comparison_matrix"]},
        )

    def test_selected_candidate_is_presentation_reduction_contract(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]}
        selected = rows["presentation_reduction_contract"]
        self.assertEqual(selected["recommended_status"], "selected")
        self.assertEqual(selected["runtime_risk"], "low")
        self.assertEqual(selected["formula_risk"], "low")
        self.assertEqual(selected["frame_stop_line_risk"], "low_frame_visibility_not_required")
        self.assertEqual(selected["dependency_cycle_risk"], "low_after_source_lineage_guard")
        self.assertIn("presentation_count_boundary", selected["evidence_refs"])
        self.assertIn("source_lineage_guard_boundary", selected["evidence_refs"])
        self.assertEqual(
            PACKET["decision_output"]["selected_next_bridge_candidate"],
            "presentation_reduction_contract",
        )
        self.assertTrue(PACKET["decision_output"]["presentation_reduction_not_complete_duplicate"])

    def test_deferred_candidates_are_occlusion_and_mask_visibility(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]}
        self.assertEqual(rows["occlusion_responsibility_contract"]["recommended_status"], "deferred")
        self.assertEqual(rows["mask_visibility_contract"]["recommended_status"], "deferred")
        self.assertEqual(
            set(PACKET["decision_output"]["deferred_candidates"]),
            {"occlusion_responsibility_contract", "mask_visibility_contract"},
        )
        self.assertIn("mask formula", rows["mask_visibility_contract"]["stop_condition"])
        self.assertIn("frame visibility", rows["occlusion_responsibility_contract"]["stop_condition"])

    def test_selection_reason_does_not_require_runtime_formula_frame_or_leak(self) -> None:
        selected = {
            row["candidate"]: row for row in PACKET["candidate_comparison_matrix"]
        }["presentation_reduction_contract"]
        self.assertIn("without source loss", selected["reason"])
        self.assertIn("without touching frame visibility", selected["reason"])
        self.assertIn("mask formula", selected["reason"])
        self.assertNotIn("leak fix", selected["reason"])
        self.assertNotIn("visual correctness", selected["reason"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["next_bridge_selection_passed"])
        self.assertTrue(decision["source_lineage_guard_reduces_source_loss_drift_for_all_candidates"])
        for key in (
            "runtime_execution_authorized",
            "helper_creation_authorized",
            "checker_creation_authorized",
            "checker_modification_authorized",
            "render_core_change_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_gui_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "real_source_read_authorized",
            "source_lineage_mutation_authorized",
            "raw_row_seam_runtime_authorized",
            "direct_c3_to_c1_integration_authorized",
            "c4_odoriba_bypass_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_recommended_next_gate(self) -> None:
        self.assertEqual(
            PACKET["decision_output"]["recommended_next_gate"],
            "dynamic_point_lod_view_frame_presentation_reduction_contract_planning_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("Docs/test-only", BOUNDARY_STATEMENT)
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker creation", BOUNDARY_STATEMENT)
        self.assertIn("no render_core change", BOUNDARY_STATEMENT)
        self.assertIn("no runtime/probe/renderer/frame/formula/source behavior change", BOUNDARY_STATEMENT)
        self.assertIn("no c_4/Odoriba bypass", BOUNDARY_STATEMENT)
        self.assertIn("no source-loss/leak/correctness/readiness claim", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()