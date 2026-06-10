"""Cartography update for the extracted presentation count boundary."""

from __future__ import annotations

import unittest
from pathlib import Path

from render_core import dynamic_point_presentation_count_boundary as presentation_boundary


REPO_ROOT = Path(__file__).resolve().parents[1]

EXTRACTED_HELPER_DELTA = {
    "surface_name": "presentation_count_boundary_descriptors",
    "path": "render_core/dynamic_point_presentation_count_boundary.py",
    "helper_kind": "descriptor_contract_ledger_helper",
    "checker": "scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py",
    "helper_test": "tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_boundary_helpers.py",
    "cartography_status": "extracted_andesite_bridge_descriptor_contract_ledger",
    "listed_as_extracted_helper": True,
    "runtime_dependency_allowed": False,
    "source_movement_authorized": False,
    "formula_movement_authorized": False,
    "frame_buffer_dependency_allowed": False,
    "source_loss_interpretation_allowed": False,
}

UPDATED_CLASSIFICATION_MATRIX = [
    {
        "surface": "presentation_count_boundary_descriptors",
        "previous_classification": "andesite_bridge_extraction_candidate",
        "updated_classification": "extracted_andesite_bridge_descriptor_contract_ledger",
        "map_delta": "new_extracted_helper_inventory_entry",
        "allowed_next_strategy": "local_contract_reuse_only",
        "blocked_strategy": [
            "source_loss_interpretation",
            "frame_truth_inference",
            "transparent_globe_leak_inference",
            "renderer_or_frame_claim",
        ],
    },
    {
        "surface": "visible_rendered_count_semantics",
        "previous_classification": "presentation_count_contract_candidate",
        "updated_classification": "cooled_descriptor_contract_semantics",
        "map_delta": "presentation_count_entropy_reduced",
        "allowed_next_strategy": "use_helper_as_evidence_map_stone",
        "blocked_strategy": [
            "source_completeness_claim",
            "frame_truth_claim",
            "readiness_claim",
        ],
    },
    {
        "surface": "rendered_lower_than_visible_semantics",
        "previous_classification": "sampling_or_presentation_reduction_candidate",
        "updated_classification": "cooled_reduction_candidate_contract",
        "map_delta": "reduction_is_not_source_loss_recorded",
        "allowed_next_strategy": "contract_reuse_as_non_source_loss_evidence",
        "blocked_strategy": ["source_loss_interpretation", "source_lineage_mutation"],
    },
    {
        "surface": "frame_visibility_surface",
        "previous_classification": "frame_visibility_stop_line",
        "updated_classification": "frame_visibility_stop_line",
        "map_delta": "unchanged_stop_line",
        "allowed_next_strategy": "separate_stop_line_closure_only",
        "blocked_strategy": ["frame_buffer_read", "renderer_execution", "render_if_needed_call"],
    },
    {
        "surface": "transparent_globe_leak_fault",
        "previous_classification": "not_inferred_unresolved_fault",
        "updated_classification": "not_inferred_unresolved_fault",
        "map_delta": "unchanged_not_inferred",
        "allowed_next_strategy": "evidence_gap_or_stop_line_review_only",
        "blocked_strategy": ["leak_fix_claim", "visual_correctness_claim", "frame_truth_inference"],
    },
]

EXTRACTED_DYNAMIC_POINT_HELPER_INVENTORY_DELTA = [
    "aggregate_boundary_descriptors",
    "source_lineage_boundary_descriptors",
    "selection_render_policy_boundary_descriptors",
    "payload_coordinate_quality_boundary_descriptors",
    "render_cap_adaptive_sampling_boundary_descriptors",
    "sampling_visibility_boundary_descriptors",
    "presentation_count_boundary_descriptors",
]

REMAINING_SURFACES = [
    {
        "surface": "frame_visibility_surface",
        "classification": "not_observed_frame_stop_line",
        "reason": "frame_visible_token remains not observed and frame buffer is not read",
    },
    {
        "surface": "transparent_globe_leak_fault",
        "classification": "unresolved_not_inferred_fault",
        "reason": "no frame or renderer evidence exists in this local map update",
    },
    {
        "surface": "projection_mask_sampling_formula_surfaces",
        "classification": "granite_or_core_formula_stop_line",
        "reason": "helper captures labels and contracts only, not formulas",
    },
    {
        "surface": "controller_renderer_frame_buffer_runtime",
        "classification": "granite_runtime_stop_line",
        "reason": "render_if_needed, controller, renderer, and frame buffer remain blocked",
    },
    {
        "surface": "source_lineage_loss_interpretation",
        "classification": "forbidden_interpretation_surface",
        "reason": "count reduction is explicitly not source loss",
    },
]

QUESTIONS_ANSWERED = {
    "helper_listed_as_extracted_descriptor_contract_ledger": True,
    "dynamic_point_map_classification_changed": True,
    "classification_change_summary": (
        "presentation_count_boundary_descriptors moved from andesite bridge extraction candidate "
        "to extracted andesite bridge descriptor/contract/ledger helper"
    ),
    "visible_rendered_count_semantics_cooled": True,
    "rendered_lower_than_visible_is_source_loss": False,
    "frame_visibility_remains_stop_line": True,
    "transparent_globe_leak_not_inferred": True,
    "recommended_path_choice": "refresh_next_andesite_bridge_selection",
    "recommended_next_gate": "dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection_gate",
    "c3_local_map_only": True,
    "rrkal_wide_methodology_authorized": False,
}

DECISION_OUTPUT = {
    "cartography_update_gate_passed": True,
    "presentation_count_helper_added_to_extracted_inventory": True,
    "presentation_count_boundary_is_descriptor_contract_ledger_helper": True,
    "presentation_count_map_delta_recorded": True,
    "visible_rendered_count_contract_semantics_cooled": True,
    "rendered_lower_than_visible_remains_reduction_candidate_only": True,
    "source_loss_interpretation_authorized": False,
    "frame_visibility_remains_stop_line": True,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "production_source_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point presentation count cartography update gate. "
    "No helper creation, no production source change, no runtime probe change, "
    "no render_if_needed, no controller, no renderer, no frame buffer read, "
    "no artifact generation, no projection/mask/sampling formula movement, "
    "no source-loss interpretation, no transparent-globe leak inference, "
    "no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide "
    "methodology promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_presentation_count_cartography_update.v1",
    "evidence_sources": {
        "presentation_count_minimal_boundary": "82e8acb",
        "presentation_count_minimal_extraction_planning": "3510a25",
        "presentation_count_import_boundary_checker": "31b0e18",
        "presentation_count_contract_planning": "ca7327c",
        "next_andesite_bridge_selection": "650333f",
        "sampling_visibility_cartography_update": "b9b37c1",
        "sampling_visibility_minimal_boundary": "76abda8",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "runtime_executed_by_this_gate": False,
    },
    "extracted_helper_inventory_delta": EXTRACTED_HELPER_DELTA,
    "extracted_dynamic_point_helper_inventory_delta": EXTRACTED_DYNAMIC_POINT_HELPER_INVENTORY_DELTA,
    "updated_classification_matrix": UPDATED_CLASSIFICATION_MATRIX,
    "remaining_surfaces": REMAINING_SURFACES,
    "questions_answered": QUESTIONS_ANSWERED,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointPresentationCountCartographyUpdateTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "extracted_helper_inventory_delta",
                "extracted_dynamic_point_helper_inventory_delta",
                "updated_classification_matrix",
                "remaining_surfaces",
                "questions_answered",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_presentation_count_cartography_update.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_helper_inventory_delta_points_to_existing_extracted_helper(self) -> None:
        delta = PACKET["extracted_helper_inventory_delta"]
        self.assertEqual(delta["path"], "render_core/dynamic_point_presentation_count_boundary.py")
        self.assertTrue((REPO_ROOT / delta["path"]).exists())
        self.assertTrue(delta["listed_as_extracted_helper"])
        self.assertEqual(delta["helper_kind"], "descriptor_contract_ledger_helper")
        self.assertEqual(
            delta["cartography_status"],
            "extracted_andesite_bridge_descriptor_contract_ledger",
        )
        self.assertFalse(delta["runtime_dependency_allowed"])
        self.assertFalse(delta["source_movement_authorized"])
        self.assertFalse(delta["formula_movement_authorized"])
        self.assertFalse(delta["frame_buffer_dependency_allowed"])
        self.assertFalse(delta["source_loss_interpretation_allowed"])

    def test_helper_bundle_supports_extracted_cartography_entry(self) -> None:
        bundle = presentation_boundary.dynamic_point_presentation_count_planning_bundle()
        descriptor = presentation_boundary.dynamic_point_presentation_count_boundary_descriptor()
        self.assertTrue(bundle["minimal_extraction_gate_passed"])
        self.assertTrue(bundle["helper_created"])
        self.assertTrue(bundle["checker_protected"])
        self.assertEqual(descriptor["scope"], "descriptor_contract_ledger_only")
        self.assertIn("visible_count", descriptor["owned_semantics"])
        self.assertIn("rendered_count", descriptor["owned_semantics"])
        self.assertIn("rendered_lower_than_visible", descriptor["owned_semantics"])
        self.assertIn("source_loss_not_inferred", descriptor["owned_semantics"])
        self.assertIn("frame_visible_not_observed", descriptor["owned_semantics"])
        self.assertIn("transparent_globe_leak_not_inferred", descriptor["owned_semantics"])

    def test_dynamic_point_extracted_inventory_has_new_presentation_count_entry(self) -> None:
        inventory = PACKET["extracted_dynamic_point_helper_inventory_delta"]
        self.assertIn("sampling_visibility_boundary_descriptors", inventory)
        self.assertIn("presentation_count_boundary_descriptors", inventory)
        self.assertEqual(inventory[-1], "presentation_count_boundary_descriptors")
        self.assertEqual(len(inventory), 7)

    def test_updated_classification_records_local_map_delta(self) -> None:
        rows = {row["surface"]: row for row in PACKET["updated_classification_matrix"]}
        self.assertEqual(
            rows["presentation_count_boundary_descriptors"]["updated_classification"],
            "extracted_andesite_bridge_descriptor_contract_ledger",
        )
        self.assertEqual(
            rows["presentation_count_boundary_descriptors"]["map_delta"],
            "new_extracted_helper_inventory_entry",
        )
        self.assertEqual(
            rows["visible_rendered_count_semantics"]["updated_classification"],
            "cooled_descriptor_contract_semantics",
        )
        self.assertEqual(
            rows["rendered_lower_than_visible_semantics"]["updated_classification"],
            "cooled_reduction_candidate_contract",
        )
        self.assertEqual(
            rows["frame_visibility_surface"]["updated_classification"],
            "frame_visibility_stop_line",
        )
        self.assertEqual(
            rows["transparent_globe_leak_fault"]["updated_classification"],
            "not_inferred_unresolved_fault",
        )

    def test_remaining_surfaces_keep_stop_lines(self) -> None:
        rows = {row["surface"]: row for row in PACKET["remaining_surfaces"]}
        self.assertEqual(rows["frame_visibility_surface"]["classification"], "not_observed_frame_stop_line")
        self.assertEqual(rows["transparent_globe_leak_fault"]["classification"], "unresolved_not_inferred_fault")
        self.assertEqual(rows["projection_mask_sampling_formula_surfaces"]["classification"], "granite_or_core_formula_stop_line")
        self.assertEqual(rows["controller_renderer_frame_buffer_runtime"]["classification"], "granite_runtime_stop_line")
        self.assertEqual(rows["source_lineage_loss_interpretation"]["classification"], "forbidden_interpretation_surface")

    def test_required_questions_are_answered(self) -> None:
        answers = PACKET["questions_answered"]
        self.assertTrue(answers["helper_listed_as_extracted_descriptor_contract_ledger"])
        self.assertTrue(answers["dynamic_point_map_classification_changed"])
        self.assertTrue(answers["visible_rendered_count_semantics_cooled"])
        self.assertFalse(answers["rendered_lower_than_visible_is_source_loss"])
        self.assertTrue(answers["frame_visibility_remains_stop_line"])
        self.assertTrue(answers["transparent_globe_leak_not_inferred"])
        self.assertEqual(answers["recommended_path_choice"], "refresh_next_andesite_bridge_selection")
        self.assertEqual(
            answers["recommended_next_gate"],
            "dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection_gate",
        )
        self.assertTrue(answers["c3_local_map_only"])
        self.assertFalse(answers["rrkal_wide_methodology_authorized"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["cartography_update_gate_passed"])
        self.assertTrue(decision["presentation_count_helper_added_to_extracted_inventory"])
        self.assertTrue(decision["presentation_count_boundary_is_descriptor_contract_ledger_helper"])
        self.assertTrue(decision["presentation_count_map_delta_recorded"])
        self.assertTrue(decision["visible_rendered_count_contract_semantics_cooled"])
        self.assertTrue(decision["rendered_lower_than_visible_remains_reduction_candidate_only"])
        self.assertTrue(decision["frame_visibility_remains_stop_line"])
        for key in (
            "source_loss_interpretation_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "production_source_change_authorized",
            "runtime_probe_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no runtime probe change", BOUNDARY_STATEMENT)
        self.assertIn("no renderer", BOUNDARY_STATEMENT)
        self.assertIn("no frame buffer read", BOUNDARY_STATEMENT)
        self.assertIn("no source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no transparent-globe leak inference", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
