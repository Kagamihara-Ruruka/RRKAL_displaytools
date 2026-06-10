"""Cartography update after computed-but-hidden minimal boundary extraction."""

from __future__ import annotations

import importlib
import unittest


EXTRACTED_ANDESITE_SURFACES = [
    {
        "surface": "sampling_visibility_boundary",
        "current_classification": "extracted_andesite_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_sampling_visibility_boundary",
        "owned_semantics": [
            "sampled_visible_token",
            "visible_count_observation",
            "rendered_count_observation",
            "mask_visible_token",
            "source_lineage_integrity_token",
        ],
        "runtime_correctness_claimed": False,
        "frame_visibility_claimed": False,
    },
    {
        "surface": "presentation_count_boundary",
        "current_classification": "extracted_andesite_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_presentation_count_boundary",
        "owned_semantics": [
            "visible_count",
            "rendered_count",
            "rendered_lower_than_visible",
            "sampling_or_presentation_reduction_candidate",
            "source_loss_not_inferred",
        ],
        "runtime_correctness_claimed": False,
        "frame_visibility_claimed": False,
    },
    {
        "surface": "computed_but_hidden_boundary",
        "current_classification": "extracted_andesite_descriptor_contract_ledger",
        "evidence_source": "render_core.dynamic_point_computed_but_hidden_boundary",
        "owned_semantics": [
            "source_present_token",
            "computed_point_token",
            "hidden_visibility_token",
            "hidden_is_not_missing",
            "occluded_is_not_source_lineage_loss",
            "transparent_globe_leak_not_inferred",
        ],
        "runtime_correctness_claimed": False,
        "frame_visibility_claimed": False,
    },
]


GRANITE_STOP_LINES = [
    {
        "surface": "frame_visibility_surface",
        "current_classification": "granite_stop_line",
        "evidence_source": "frame_visibility_stop_line_planning",
        "reason": "frame visibility is still not observed",
        "runtime_risk": "frame_surface_runtime_required",
        "stop_condition": "any frame buffer read is out of scope",
    },
    {
        "surface": "transparent_globe_leak_fault",
        "current_classification": "granite_stop_line",
        "evidence_source": "frame_visibility_stop_line_planning",
        "reason": "leak behavior is not inferred from hidden or mask evidence",
        "runtime_risk": "fault_review_near_renderer_surface",
        "stop_condition": "any leak inference or fix claim is out of scope",
    },
    {
        "surface": "controller_renderer_frame_buffer_runtime",
        "current_classification": "granite_stop_line",
        "evidence_source": "view_frame_occlusion_structure_settlement",
        "reason": "controller, renderer, and frame buffer are runtime surfaces",
        "runtime_risk": "high",
        "stop_condition": "controller or renderer execution is out of scope",
    },
    {
        "surface": "render_if_needed_runtime",
        "current_classification": "granite_stop_line",
        "evidence_source": "runtime_probe_execution_gate_boundary",
        "reason": "render_if_needed remains explicitly uncalled by prior probes",
        "runtime_risk": "high",
        "stop_condition": "render_if_needed call is out of scope",
    },
    {
        "surface": "projection_mask_sampling_formula_surfaces",
        "current_classification": "granite_stop_line",
        "evidence_source": "occlusion_responsibility_boundary",
        "reason": "formula ownership is reference-only and not moved by cartography",
        "runtime_risk": "formula_movement_risk",
        "stop_condition": "projection, mask, sampling, or alpha-compose movement is out of scope",
    },
]


CANDIDATE_MATRIX = [
    {
        "candidate": "source_lineage_guard_contract",
        "current_classification": "andesite_candidate_guard_contract",
        "evidence_source": [
            "computed_but_hidden_boundary",
            "sampling_visibility_boundary",
            "occlusion_responsibility_boundary",
        ],
        "reason_to_select_or_defer": "selectable after bridge comparison if source guard entropy remains high",
        "helper_checker_need": "dedicated_or_existing_guard_boundary_review_needed",
        "runtime_risk": "low",
        "dependency_cycle_risk": "medium_already_near_existing_source_lineage_boundary",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "do not reinterpret hidden or occluded as source loss",
        "suitable_as_remaining_andesite_candidate": True,
    },
    {
        "candidate": "occlusion_responsibility_contract",
        "current_classification": "andesite_candidate_near_mask_occlusion",
        "evidence_source": [
            "occlusion_responsibility_boundary",
            "sampling_visibility_boundary",
            "computed_but_hidden_boundary",
        ],
        "reason_to_select_or_defer": "selectable only if formula and frame surfaces remain reference-only",
        "helper_checker_need": "future_checker_needed_before_extraction",
        "runtime_risk": "medium",
        "dependency_cycle_risk": "medium_mask_visibility_and_hidden_contract_overlap",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "do not move mask formula or infer frame truth",
        "suitable_as_remaining_andesite_candidate": True,
    },
    {
        "candidate": "mask_visibility_contract",
        "current_classification": "andesite_candidate_already_partially_extracted",
        "evidence_source": [
            "sampling_visibility_boundary",
            "runtime_probe_result_interpretation",
        ],
        "reason_to_select_or_defer": "selectable if it can be kept as mask-visible label contract",
        "helper_checker_need": "may reuse sampling_visibility_boundary_context_or_require_small_checker",
        "runtime_risk": "low",
        "dependency_cycle_risk": "medium_overlaps_occlusion_responsibility_contract",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "do not call mask formula or delete source lineage",
        "suitable_as_remaining_andesite_candidate": True,
    },
    {
        "candidate": "presentation_reduction_contract",
        "current_classification": "andesite_candidate_already_partially_extracted",
        "evidence_source": [
            "presentation_count_boundary",
            "sampling_visibility_boundary",
        ],
        "reason_to_select_or_defer": "selectable if reduction remains candidate and not source loss",
        "helper_checker_need": "presentation_count_checker_context_exists",
        "runtime_risk": "low",
        "dependency_cycle_risk": "low",
        "recommended_next_action": "include_in_next_bridge_selection",
        "stop_condition": "do not convert rendered lower than visible into source loss",
        "suitable_as_remaining_andesite_candidate": True,
    },
    {
        "candidate": "frame_visibility_stop_line_closure",
        "current_classification": "stop_line_closure_candidate_not_andesite_extraction",
        "evidence_source": ["frame_visibility_stop_line_planning"],
        "reason_to_select_or_defer": "defer unless next selection requires stop-line closure",
        "helper_checker_need": "planning_only_until_frame_policy_exists",
        "runtime_risk": "high",
        "dependency_cycle_risk": "high_near_frame_renderer_runtime",
        "recommended_next_action": "defer_to_stop_line_route",
        "stop_condition": "do not read frame buffer or call render_if_needed",
        "suitable_as_remaining_andesite_candidate": False,
    },
    {
        "candidate": "transparent_globe_leak_fault_review",
        "current_classification": "fault_review_stop_line_not_andesite_extraction",
        "evidence_source": [
            "frame_visibility_stop_line_planning",
            "occlusion_responsibility_boundary",
        ],
        "reason_to_select_or_defer": "defer because leak behavior remains not inferred",
        "helper_checker_need": "fault_review_scope_needed_before_any_checker",
        "runtime_risk": "high",
        "dependency_cycle_risk": "high_near_frame_and_visual_claims",
        "recommended_next_action": "defer_to_fault_review_route",
        "stop_condition": "do not infer or fix transparent globe leak",
        "suitable_as_remaining_andesite_candidate": False,
    },
]


DECISION_OUTPUT = {
    "cartography_update_passed": True,
    "computed_but_hidden_boundary_registered": True,
    "extracted_andesite_surface_count": 3,
    "remaining_andesite_candidate_count": 4,
    "granite_stop_line_count": 5,
    "dependency_cycle_watch_enabled": True,
    "next_bridge_selection_required": True,
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
    "recommended_next_gate": "dynamic_point_lod_view_frame_post_computed_but_hidden_next_bridge_selection_gate",
}


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point post-computed-but-hidden cartography update gate. "
    "No helper creation, no checker creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry.py change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing "
    "interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, "
    "no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide "
    "methodology promotion, and no push."
)


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_post_computed_but_hidden_cartography_update.v1",
    "evidence_sources": {
        "computed_but_hidden_boundary": "b7b11a5",
        "computed_but_hidden_boundary_helpers": "b7b11a5",
        "presentation_count_boundary": "d25e94c_lineage",
        "sampling_visibility_boundary": "76abda8_lineage",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "next_andesite_bridge_selection_evidence": "650333f",
        "runtime_executed_by_this_gate": False,
    },
    "extracted_andesite_surfaces": EXTRACTED_ANDESITE_SURFACES,
    "granite_stop_lines": GRANITE_STOP_LINES,
    "candidate_matrix": CANDIDATE_MATRIX,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointPostComputedButHiddenCartographyUpdateTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "extracted_andesite_surfaces",
                "granite_stop_lines",
                "candidate_matrix",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_post_computed_but_hidden_cartography_update.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_computed_but_hidden_helper_is_registered_as_descriptor_contract_ledger_only(self) -> None:
        module = importlib.import_module("render_core.dynamic_point_computed_but_hidden_boundary")
        descriptor = module.dynamic_point_computed_but_hidden_boundary_descriptor()
        bundle = module.dynamic_point_computed_but_hidden_planning_bundle()
        self.assertEqual(descriptor["scope"], "minimal_descriptor_contract_ledger_surface")
        self.assertTrue(bundle["decision"]["dict_list_scalar_output_only"])
        self.assertTrue(bundle["decision"]["hidden_is_not_missing"])
        self.assertTrue(bundle["decision"]["occluded_is_not_source_lineage_loss"])
        self.assertTrue(bundle["decision"]["transparent_globe_leak_not_inferred"])
        self.assertFalse(bundle["decision"]["visual_parity_claimed"])
        self.assertFalse(bundle["decision"]["readiness_claimed"])
        self.assertFalse(bundle["decision"]["transparent_globe_leak_fix_claimed"])

    def test_extracted_andesite_surface_inventory(self) -> None:
        self.assertEqual(
            {row["surface"] for row in PACKET["extracted_andesite_surfaces"]},
            {
                "sampling_visibility_boundary",
                "presentation_count_boundary",
                "computed_but_hidden_boundary",
            },
        )
        for row in PACKET["extracted_andesite_surfaces"]:
            self.assertEqual(row["current_classification"], "extracted_andesite_descriptor_contract_ledger")
            self.assertTrue(row["owned_semantics"])
            self.assertFalse(row["runtime_correctness_claimed"])
            self.assertFalse(row["frame_visibility_claimed"])

    def test_granite_stop_line_inventory(self) -> None:
        self.assertEqual(
            {row["surface"] for row in PACKET["granite_stop_lines"]},
            {
                "frame_visibility_surface",
                "transparent_globe_leak_fault",
                "controller_renderer_frame_buffer_runtime",
                "render_if_needed_runtime",
                "projection_mask_sampling_formula_surfaces",
            },
        )
        for row in PACKET["granite_stop_lines"]:
            self.assertEqual(row["current_classification"], "granite_stop_line")
            self.assertTrue(row["evidence_source"])
            self.assertTrue(row["reason"])
            self.assertTrue(row["runtime_risk"])
            self.assertTrue(row["stop_condition"])

    def test_remaining_candidate_matrix(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["candidate_matrix"]}
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
        for row in rows.values():
            self.assertEqual(
                set(row),
                {
                    "candidate",
                    "current_classification",
                    "evidence_source",
                    "reason_to_select_or_defer",
                    "helper_checker_need",
                    "runtime_risk",
                    "dependency_cycle_risk",
                    "recommended_next_action",
                    "stop_condition",
                    "suitable_as_remaining_andesite_candidate",
                },
            )
            self.assertTrue(row["evidence_source"])
            self.assertTrue(row["reason_to_select_or_defer"])
            self.assertTrue(row["helper_checker_need"])
            self.assertTrue(row["runtime_risk"])
            self.assertTrue(row["dependency_cycle_risk"])
            self.assertTrue(row["recommended_next_action"])
            self.assertTrue(row["stop_condition"])

    def test_remaining_andesite_candidate_count_excludes_frame_and_leak_stop_lines(self) -> None:
        candidates = [
            row for row in PACKET["candidate_matrix"]
            if row["suitable_as_remaining_andesite_candidate"]
        ]
        self.assertEqual(len(candidates), 4)
        self.assertEqual(
            {row["candidate"] for row in candidates},
            {
                "source_lineage_guard_contract",
                "occlusion_responsibility_contract",
                "mask_visibility_contract",
                "presentation_reduction_contract",
            },
        )
        deferred = [
            row for row in PACKET["candidate_matrix"]
            if not row["suitable_as_remaining_andesite_candidate"]
        ]
        self.assertEqual(
            {row["candidate"] for row in deferred},
            {"frame_visibility_stop_line_closure", "transparent_globe_leak_fault_review"},
        )

    def test_dependency_cycle_watch_and_decision_output(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["cartography_update_passed"])
        self.assertTrue(decision["computed_but_hidden_boundary_registered"])
        self.assertEqual(decision["extracted_andesite_surface_count"], 3)
        self.assertEqual(decision["remaining_andesite_candidate_count"], 4)
        self.assertEqual(decision["granite_stop_line_count"], 5)
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        self.assertTrue(decision["next_bridge_selection_required"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_post_computed_but_hidden_next_bridge_selection_gate",
        )

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        for key in (
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
