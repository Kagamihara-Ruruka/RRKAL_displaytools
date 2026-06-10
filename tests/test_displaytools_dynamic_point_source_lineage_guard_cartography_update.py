"""Cartography update after source-lineage guard minimal boundary extraction."""

from __future__ import annotations

import importlib
import unittest


EXTRACTED_ANDESITE_SURFACES = [
    {
        "surface": "sampling_visibility_boundary",
        "current_classification": "extracted_andesite_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_sampling_visibility_boundary",
        "protected_by_source_lineage_guard": True,
        "runtime_correctness_claimed": False,
        "source_loss_interpretation_allowed": False,
    },
    {
        "surface": "presentation_count_boundary",
        "current_classification": "extracted_andesite_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_presentation_count_boundary",
        "protected_by_source_lineage_guard": True,
        "runtime_correctness_claimed": False,
        "source_loss_interpretation_allowed": False,
    },
    {
        "surface": "computed_but_hidden_boundary",
        "current_classification": "extracted_andesite_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_computed_but_hidden_boundary",
        "protected_by_source_lineage_guard": True,
        "runtime_correctness_claimed": False,
        "source_loss_interpretation_allowed": False,
    },
    {
        "surface": "source_lineage_guard_boundary",
        "current_classification": "extracted_andesite_bridge_guard_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_source_lineage_guard_boundary",
        "protects": [
            "sampling_visibility",
            "presentation_count",
            "computed_but_hidden",
            "future_mask_visibility",
            "future_occlusion_responsibility",
            "raw_row_compatibility_seam_label_ledger_handoff_only",
        ],
        "runtime_correctness_claimed": False,
        "source_loss_interpretation_allowed": False,
    },
]

REMAINING_CANDIDATE_MATRIX = [
    {
        "candidate": "occlusion_responsibility_contract",
        "current_classification": "remaining_andesite_candidate_after_source_guard",
        "evidence_source": [
            "occlusion_responsibility_boundary",
            "computed_but_hidden_boundary",
            "source_lineage_guard_boundary",
        ],
        "reason_to_select_or_defer": "source guard now reduces source-loss drift, but formula and frame stop-lines still require sequencing",
        "helper_checker_need": "future dedicated planning and checker review",
        "runtime_risk": "medium",
        "dependency_cycle_risk": "medium_mask_occlusion_overlap",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "stop if occlusion is treated as source-lineage loss or needs mask formula movement",
    },
    {
        "candidate": "mask_visibility_contract",
        "current_classification": "remaining_andesite_candidate_partially_supported",
        "evidence_source": [
            "sampling_visibility_boundary",
            "source_lineage_guard_boundary",
        ],
        "reason_to_select_or_defer": "mask-visible semantics are partially cooled and now protected from source deletion drift",
        "helper_checker_need": "future checker need to separate mask label from mask formula",
        "runtime_risk": "low_to_medium",
        "dependency_cycle_risk": "medium_overlap_with_occlusion_contract",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "stop if mask hidden is interpreted as missing source or requires formula movement",
    },
    {
        "candidate": "presentation_reduction_contract",
        "current_classification": "remaining_andesite_candidate_partially_supported",
        "evidence_source": [
            "presentation_count_boundary",
            "sampling_visibility_boundary",
            "source_lineage_guard_boundary",
        ],
        "reason_to_select_or_defer": "reduction semantics are cooled and source guard keeps rendered lower than visible from becoming source loss",
        "helper_checker_need": "future planning can decide whether existing count checker is enough",
        "runtime_risk": "low",
        "dependency_cycle_risk": "low_after_source_guard",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "stop if rendered lower than visible is treated as source loss",
    },
]

GRANITE_STOP_LINES = [
    {
        "surface": "frame_visibility_surface",
        "current_classification": "granite_stop_line",
        "reason": "frame visibility remains not observed",
        "stop_condition": "any frame buffer read is out of scope",
    },
    {
        "surface": "transparent_globe_leak_fault",
        "current_classification": "granite_stop_line",
        "reason": "transparent-globe leak remains not inferred and not fixed",
        "stop_condition": "any leak inference or fix claim is out of scope",
    },
    {
        "surface": "controller_renderer_frame_buffer_runtime",
        "current_classification": "granite_stop_line",
        "reason": "controller, renderer, GUI, and frame buffer remain runtime surfaces",
        "stop_condition": "controller, renderer, GUI, or frame buffer execution is out of scope",
    },
    {
        "surface": "render_if_needed_runtime",
        "current_classification": "granite_stop_line",
        "reason": "render_if_needed remains explicitly blocked",
        "stop_condition": "render_if_needed call is out of scope",
    },
    {
        "surface": "projection_mask_sampling_alpha_formula_surfaces",
        "current_classification": "granite_stop_line",
        "reason": "projection, mask, sampling, and alpha-compose formulas remain unmoved",
        "stop_condition": "formula movement is out of scope",
    },
]

DECISION_OUTPUT = {
    "cartography_update_passed": True,
    "source_lineage_guard_boundary_registered": True,
    "extracted_andesite_surface_count": 4,
    "remaining_candidate_count": 3,
    "granite_stop_line_count": 5,
    "dependency_cycle_watch_enabled": True,
    "next_bridge_selection_required": True,
    "c4_odoriba_mediation_required": True,
    "direct_c3_to_c1_dependency_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "raw_row_seam_runtime_authorized": False,
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
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_post_source_lineage_guard_next_bridge_selection_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point source-lineage guard cartography update gate. "
    "No helper creation, no checker creation or checker modification, no render_core change, "
    "no runtime probe change, no taichi_global_bathymetry.py change, no render_if_needed, "
    "no controller, no renderer, no GUI, no frame buffer read, no artifact generation, "
    "no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, "
    "no source-lineage mutation, no raw-row seam runtime authorization, no direct c_3-to-c_1 "
    "integration, no c_4/Odoriba bypass, no transparent-globe leak inference or fix claim, "
    "no correctness or visual parity claim, no readiness claim, no RRKAL-wide methodology "
    "promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_source_lineage_guard_cartography_update.v1",
    "extracted_andesite_surfaces": EXTRACTED_ANDESITE_SURFACES,
    "remaining_candidate_matrix": REMAINING_CANDIDATE_MATRIX,
    "granite_stop_lines": GRANITE_STOP_LINES,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSourceLineageGuardCartographyUpdateTest(unittest.TestCase):
    def test_source_lineage_guard_helper_evidence_is_registered(self) -> None:
        module = importlib.import_module("render_core.dynamic_point_source_lineage_guard_boundary")
        descriptor = module.dynamic_point_source_lineage_guard_boundary_descriptor()
        bundle = module.dynamic_point_source_lineage_guard_planning_bundle()
        self.assertEqual(descriptor["classification"], "source_lineage_guard_minimal_boundary")
        self.assertEqual(descriptor["scope"], "minimal_descriptor_contract_ledger_surface")
        self.assertTrue(bundle["decision"]["helper_created"])
        self.assertTrue(bundle["decision"]["checker_passed"])
        self.assertFalse(bundle["decision"]["source_lineage_mutation_authorized"])
        self.assertTrue(bundle["decision"]["c4_odoriba_mediation_required"])

    def test_extracted_andesite_inventory_now_has_four_surfaces(self) -> None:
        self.assertEqual(
            {row["surface"] for row in PACKET["extracted_andesite_surfaces"]},
            {
                "sampling_visibility_boundary",
                "presentation_count_boundary",
                "computed_but_hidden_boundary",
                "source_lineage_guard_boundary",
            },
        )
        self.assertEqual(PACKET["decision_output"]["extracted_andesite_surface_count"], 4)

    def test_source_lineage_guard_classification_and_protected_surfaces(self) -> None:
        rows = {row["surface"]: row for row in PACKET["extracted_andesite_surfaces"]}
        guard = rows["source_lineage_guard_boundary"]
        self.assertEqual(
            guard["current_classification"],
            "extracted_andesite_bridge_guard_descriptor_contract_ledger",
        )
        self.assertEqual(
            set(guard["protects"]),
            {
                "sampling_visibility",
                "presentation_count",
                "computed_but_hidden",
                "future_mask_visibility",
                "future_occlusion_responsibility",
                "raw_row_compatibility_seam_label_ledger_handoff_only",
            },
        )
        self.assertFalse(guard["runtime_correctness_claimed"])
        self.assertFalse(guard["source_loss_interpretation_allowed"])

    def test_remaining_candidate_matrix_has_required_candidates(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["remaining_candidate_matrix"]}
        self.assertEqual(
            set(rows),
            {
                "occlusion_responsibility_contract",
                "mask_visibility_contract",
                "presentation_reduction_contract",
            },
        )
        for row in rows.values():
            self.assertTrue(row["evidence_source"])
            self.assertTrue(row["reason_to_select_or_defer"])
            self.assertTrue(row["helper_checker_need"])
            self.assertTrue(row["runtime_risk"])
            self.assertTrue(row["dependency_cycle_risk"])
            self.assertTrue(row["recommended_next_action"])
            self.assertTrue(row["stop_condition"])

    def test_granite_stop_line_inventory_remains_blocked(self) -> None:
        self.assertEqual(
            {row["surface"] for row in PACKET["granite_stop_lines"]},
            {
                "frame_visibility_surface",
                "transparent_globe_leak_fault",
                "controller_renderer_frame_buffer_runtime",
                "render_if_needed_runtime",
                "projection_mask_sampling_alpha_formula_surfaces",
            },
        )
        for row in PACKET["granite_stop_lines"]:
            self.assertEqual(row["current_classification"], "granite_stop_line")
            self.assertTrue(row["stop_condition"])
        self.assertEqual(PACKET["decision_output"]["granite_stop_line_count"], 5)

    def test_c4_odoriba_and_raw_row_boundaries_remain_non_runtime(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["c4_odoriba_mediation_required"])
        self.assertFalse(decision["direct_c3_to_c1_dependency_authorized"])
        self.assertFalse(decision["c4_odoriba_bypass_authorized"])
        self.assertFalse(decision["raw_row_seam_runtime_authorized"])

    def test_decision_output_recommends_next_bridge_selection_gate(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["cartography_update_passed"])
        self.assertTrue(decision["source_lineage_guard_boundary_registered"])
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        self.assertTrue(decision["next_bridge_selection_required"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_post_source_lineage_guard_next_bridge_selection_gate",
        )

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        for key in (
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
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker creation or checker modification", BOUNDARY_STATEMENT)
        self.assertIn("no render_core change", BOUNDARY_STATEMENT)
        self.assertIn("no runtime probe change", BOUNDARY_STATEMENT)
        self.assertIn("no source-lineage mutation", BOUNDARY_STATEMENT)
        self.assertIn("no raw-row seam runtime authorization", BOUNDARY_STATEMENT)
        self.assertIn("no direct c_3-to-c_1 integration", BOUNDARY_STATEMENT)
        self.assertIn("no c_4/Odoriba bypass", BOUNDARY_STATEMENT)
        self.assertIn("no transparent-globe leak inference", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()