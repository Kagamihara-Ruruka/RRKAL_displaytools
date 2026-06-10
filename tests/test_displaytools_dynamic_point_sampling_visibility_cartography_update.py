"""Cartography update for the extracted sampling visibility boundary."""

from __future__ import annotations

import unittest
from pathlib import Path

from render_core import dynamic_point_sampling_visibility_boundary as sampling_boundary


REPO_ROOT = Path(__file__).resolve().parents[1]

EXTRACTED_HELPER_DELTA = {
    "surface_name": "sampling_visibility_boundary_descriptors",
    "path": "render_core/dynamic_point_sampling_visibility_boundary.py",
    "helper_kind": "descriptor_contract_ledger_helper",
    "checker": "scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py",
    "helper_test": "tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py",
    "cartography_status": "extracted_andesite_bridge_descriptor_contract_ledger",
    "listed_as_extracted_helper": True,
    "runtime_dependency_allowed": False,
    "source_movement_authorized": False,
    "formula_movement_authorized": False,
}

UPDATED_CLASSIFICATION_MATRIX = [
    {
        "surface": "sampling_visibility_boundary_descriptors",
        "previous_classification": "andesite_bridge_extraction_candidate",
        "updated_classification": "extracted_andesite_bridge_descriptor_contract_ledger",
        "map_delta": "new_extracted_helper_inventory_entry",
        "allowed_next_strategy": "local_contract_reuse_only",
        "blocked_strategy": [
            "formula_movement",
            "runtime_probe_expansion",
            "renderer_or_frame_claim",
        ],
    },
    {
        "surface": "sampling_count_mask_semantics",
        "previous_classification": "observed_andesite_bridge_semantics",
        "updated_classification": "cooled_descriptor_contract_semantics",
        "map_delta": "semantic_entropy_reduced",
        "allowed_next_strategy": "use_helper_as_evidence_map_stone",
        "blocked_strategy": ["source_loss_interpretation", "readiness_claim"],
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
        "blocked_strategy": ["leak_fix_claim", "visual_correctness_claim"],
    },
    {
        "surface": "projection_mask_sampling_formula_surfaces",
        "previous_classification": "granite_or_core_formula_stop_line",
        "updated_classification": "granite_or_core_formula_stop_line",
        "map_delta": "unchanged_formula_stop_line",
        "allowed_next_strategy": "reference_only",
        "blocked_strategy": [
            "project_ais_to_screen_movement",
            "mask_overlay_to_globe_movement",
            "sampling_formula_movement",
        ],
    },
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
        "surface": "artifact_writer_surface",
        "classification": "forbidden_artifact_surface",
        "reason": "no PNG, runtime JSON, state, or output writer belongs to this helper",
    },
]

QUESTIONS_ANSWERED = {
    "helper_listed_as_extracted_descriptor_contract_ledger": True,
    "dynamic_point_map_classification_changed": True,
    "classification_change_summary": (
        "sampling_visibility_boundary_descriptors moved from andesite bridge extraction candidate "
        "to extracted andesite bridge descriptor/contract/ledger helper"
    ),
    "frame_visibility_remains_stop_line": True,
    "transparent_globe_leak_not_inferred": True,
    "recommended_path_choice": "enter_next_andesite_bridge",
    "recommended_next_gate": "dynamic_point_lod_view_frame_next_andesite_bridge_selection_gate",
    "c3_local_map_only": True,
    "rrkal_wide_methodology_authorized": False,
}

DECISION_OUTPUT = {
    "cartography_update_gate_passed": True,
    "sampling_visibility_helper_added_to_extracted_inventory": True,
    "sampling_visibility_boundary_is_descriptor_contract_ledger_helper": True,
    "sampling_visibility_map_delta_recorded": True,
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
    "recommended_next_gate": "dynamic_point_lod_view_frame_next_andesite_bridge_selection_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point sampling visibility cartography update gate. "
    "No helper creation, no production source change, no runtime probe change, "
    "no render_if_needed, no controller, no renderer, no frame buffer read, "
    "no artifact generation, no projection/mask/sampling formula movement, "
    "no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide "
    "methodology promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_sampling_visibility_cartography_update.v1",
    "evidence_sources": {
        "sampling_visibility_minimal_boundary": "76abda8",
        "sampling_visibility_import_boundary_checker": "21fc04b",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "sampling_visibility_runtime_probe_result_interpretation": "5503eb0",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "earlier_dynamic_point_cartography": "second_cutout_cartography_inventory",
        "runtime_executed_by_this_gate": False,
    },
    "extracted_helper_inventory_delta": EXTRACTED_HELPER_DELTA,
    "updated_classification_matrix": UPDATED_CLASSIFICATION_MATRIX,
    "remaining_surfaces": REMAINING_SURFACES,
    "questions_answered": QUESTIONS_ANSWERED,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSamplingVisibilityCartographyUpdateTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "extracted_helper_inventory_delta",
                "updated_classification_matrix",
                "remaining_surfaces",
                "questions_answered",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_sampling_visibility_cartography_update.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_helper_inventory_delta_points_to_existing_extracted_helper(self) -> None:
        delta = PACKET["extracted_helper_inventory_delta"]
        self.assertEqual(delta["path"], "render_core/dynamic_point_sampling_visibility_boundary.py")
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

    def test_helper_bundle_supports_extracted_cartography_entry(self) -> None:
        bundle = sampling_boundary.dynamic_point_sampling_visibility_planning_bundle()
        descriptor = bundle["boundary_descriptor"]
        self.assertTrue(bundle["minimal_extraction_gate_passed"])
        self.assertEqual(descriptor["helper_surface"], "descriptor_contract_ledger_only")
        self.assertIn("sampled_visible_token", descriptor["owned_semantics"])
        self.assertIn("visible_count_observation", descriptor["owned_semantics"])
        self.assertIn("rendered_count_observation", descriptor["owned_semantics"])
        self.assertIn("mask_visible_token", descriptor["owned_semantics"])
        self.assertIn("frame_visibility_stop_line", descriptor["owned_semantics"])
        self.assertIn("transparent_globe_leak_not_inferred", descriptor["owned_semantics"])

    def test_updated_classification_records_local_map_delta(self) -> None:
        rows = {row["surface"]: row for row in PACKET["updated_classification_matrix"]}
        self.assertEqual(
            rows["sampling_visibility_boundary_descriptors"]["updated_classification"],
            "extracted_andesite_bridge_descriptor_contract_ledger",
        )
        self.assertEqual(
            rows["sampling_visibility_boundary_descriptors"]["map_delta"],
            "new_extracted_helper_inventory_entry",
        )
        self.assertEqual(
            rows["sampling_count_mask_semantics"]["updated_classification"],
            "cooled_descriptor_contract_semantics",
        )
        self.assertEqual(
            rows["frame_visibility_surface"]["updated_classification"],
            "frame_visibility_stop_line",
        )
        self.assertEqual(
            rows["transparent_globe_leak_fault"]["updated_classification"],
            "not_inferred_unresolved_fault",
        )
        self.assertEqual(
            rows["projection_mask_sampling_formula_surfaces"]["updated_classification"],
            "granite_or_core_formula_stop_line",
        )

    def test_remaining_surfaces_keep_stop_lines(self) -> None:
        rows = {row["surface"]: row for row in PACKET["remaining_surfaces"]}
        self.assertEqual(rows["frame_visibility_surface"]["classification"], "not_observed_frame_stop_line")
        self.assertEqual(rows["transparent_globe_leak_fault"]["classification"], "unresolved_not_inferred_fault")
        self.assertEqual(rows["projection_mask_sampling_formula_surfaces"]["classification"], "granite_or_core_formula_stop_line")
        self.assertEqual(rows["controller_renderer_frame_buffer_runtime"]["classification"], "granite_runtime_stop_line")
        self.assertEqual(rows["artifact_writer_surface"]["classification"], "forbidden_artifact_surface")

    def test_required_questions_are_answered(self) -> None:
        answers = PACKET["questions_answered"]
        self.assertTrue(answers["helper_listed_as_extracted_descriptor_contract_ledger"])
        self.assertTrue(answers["dynamic_point_map_classification_changed"])
        self.assertTrue(answers["frame_visibility_remains_stop_line"])
        self.assertTrue(answers["transparent_globe_leak_not_inferred"])
        self.assertEqual(answers["recommended_path_choice"], "enter_next_andesite_bridge")
        self.assertEqual(
            answers["recommended_next_gate"],
            "dynamic_point_lod_view_frame_next_andesite_bridge_selection_gate",
        )
        self.assertTrue(answers["c3_local_map_only"])
        self.assertFalse(answers["rrkal_wide_methodology_authorized"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["cartography_update_gate_passed"])
        self.assertTrue(decision["sampling_visibility_helper_added_to_extracted_inventory"])
        self.assertTrue(decision["sampling_visibility_boundary_is_descriptor_contract_ledger_helper"])
        self.assertTrue(decision["sampling_visibility_map_delta_recorded"])
        self.assertTrue(decision["frame_visibility_remains_stop_line"])
        for key in (
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
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()