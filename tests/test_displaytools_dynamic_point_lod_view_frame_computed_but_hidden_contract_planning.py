"""Planning gate for dynamic point computed-but-hidden contract."""

from __future__ import annotations

import unittest


CANDIDATE_HELPER_TARGET = "render_core/dynamic_point_computed_but_hidden_boundary.py"
FUTURE_CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py"

CONTRACT_LABELS = [
    "source_present_token",
    "computed_point_token",
    "hidden_visibility_token",
    "frame_visible_not_observed",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "computed_but_hidden_contract",
    "transparent_globe_leak_not_inferred",
]

STOP_LINE_LEDGER = {
    "frame_visibility": "frame_visible_not_observed",
    "frame_buffer_read_blocked": True,
    "renderer_execution_blocked": True,
    "transparent_globe_leak": "transparent_globe_leak_not_inferred",
    "source_loss": "source_loss_not_inferred",
}

PLANNING_MATRIX = [
    {
        "surface": "source_present_token",
        "semantic_meaning": "source identity exists before visibility judgement",
        "allowed_contract_role": "lineage_presence_label",
        "forbidden_interpretation": "visibility_hidden_does_not_delete_source",
        "helper_candidate": "descriptor_contract_ledger_only",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
    {
        "surface": "computed_point_token",
        "semantic_meaning": "point has reached computed dynamic point state",
        "allowed_contract_role": "computed_presence_label",
        "forbidden_interpretation": "computed_does_not_claim_coordinate_correctness",
        "helper_candidate": "descriptor_contract_ledger_only",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
    {
        "surface": "hidden_visibility_token",
        "semantic_meaning": "visibility can be hidden after computation",
        "allowed_contract_role": "hidden_visibility_label",
        "forbidden_interpretation": "hidden_is_not_missing",
        "helper_candidate": "descriptor_contract_ledger_only",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
    {
        "surface": "frame_visible_not_observed",
        "semantic_meaning": "frame visibility remains outside current evidence",
        "allowed_contract_role": "stop_line_label",
        "forbidden_interpretation": "frame_truth_not_claimed",
        "helper_candidate": "stop_line_ledger_only",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
    {
        "surface": "hidden_is_not_missing",
        "semantic_meaning": "hidden visibility is not source absence",
        "allowed_contract_role": "semantic_guard_label",
        "forbidden_interpretation": "hidden_as_missing",
        "helper_candidate": "contract_guard_candidate",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
    {
        "surface": "occluded_is_not_source_lineage_loss",
        "semantic_meaning": "occlusion cannot be reinterpreted as source lineage loss",
        "allowed_contract_role": "source_lineage_guard_label",
        "forbidden_interpretation": "occluded_as_source_lineage_loss",
        "helper_candidate": "contract_guard_candidate",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
    {
        "surface": "transparent_globe_leak_not_inferred",
        "semantic_meaning": "frame and leak behavior remain unobserved",
        "allowed_contract_role": "fault_stop_line_label",
        "forbidden_interpretation": "transparent_globe_leak_inference_or_fix",
        "helper_candidate": "stop_line_ledger_only",
        "runtime_dependency": False,
        "renderer_frame_dependency": False,
        "source_lineage_mutation_allowed": False,
    },
]

DECISION_OUTPUT = {
    "computed_but_hidden_contract_planning_gate_passed": True,
    "candidate_helper_target": CANDIDATE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "contract_labels_defined": True,
    "stop_line_ledger_defined": True,
    "computed_but_hidden_helper_candidate_supported": True,
    "descriptor_contract_ledger_candidate": True,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "render_core_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "hidden_as_missing_authorized": False,
    "source_lineage_loss_interpretation_authorized": False,
    "transparent_globe_leak_inferred": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_planning_gate",
}

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_computed_but_hidden_contract_planning.v1",
    "evidence_sources": {
        "post_presentation_count_next_bridge_selection": "d25e94c",
        "presentation_count_cartography_update": "a5fe556",
        "sampling_visibility_minimal_boundary": "76abda8",
        "occlusion_responsibility_boundary": "44356e9",
        "grafting_path_minimal_evidence": "87cb579",
        "view_frame_occlusion_structure_settlement": "df40770",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "runtime_executed_by_this_gate": False,
    },
    "candidate_helper_target": CANDIDATE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "contract_labels": CONTRACT_LABELS,
    "stop_line_ledger": STOP_LINE_LEDGER,
    "planning_matrix": PLANNING_MATRIX,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": (
        "Docs/test-only dynamic point LOD view-frame computed-but-hidden contract planning gate. "
        "No helper creation, no checker creation, no render_core change, no runtime probe change, "
        "no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, "
        "no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing "
        "interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, "
        "no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push."
    ),
}


class DynamicPointComputedButHiddenContractPlanningTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "candidate_helper_target",
                "future_checker_target",
                "contract_labels",
                "stop_line_ledger",
                "planning_matrix",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_computed_but_hidden_contract_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_future_targets_are_planned_only(self) -> None:
        self.assertEqual(PACKET["candidate_helper_target"], CANDIDATE_HELPER_TARGET)
        self.assertEqual(PACKET["future_checker_target"], FUTURE_CHECKER_TARGET)
        self.assertFalse(PACKET["decision_output"]["helper_creation_authorized"])
        self.assertFalse(PACKET["decision_output"]["checker_creation_authorized"])
        self.assertFalse(PACKET["decision_output"]["render_core_change_authorized"])

    def test_required_contract_labels_are_defined(self) -> None:
        self.assertEqual(
            set(PACKET["contract_labels"]),
            {
                "source_present_token",
                "computed_point_token",
                "hidden_visibility_token",
                "frame_visible_not_observed",
                "hidden_is_not_missing",
                "occluded_is_not_source_lineage_loss",
                "computed_but_hidden_contract",
                "transparent_globe_leak_not_inferred",
            },
        )

    def test_stop_line_ledger_blocks_frame_runtime_and_leak_inference(self) -> None:
        ledger = PACKET["stop_line_ledger"]
        self.assertEqual(ledger["frame_visibility"], "frame_visible_not_observed")
        self.assertTrue(ledger["frame_buffer_read_blocked"])
        self.assertTrue(ledger["renderer_execution_blocked"])
        self.assertEqual(ledger["transparent_globe_leak"], "transparent_globe_leak_not_inferred")
        self.assertEqual(ledger["source_loss"], "source_loss_not_inferred")

    def test_planning_matrix_separates_hidden_missing_and_source_lineage_loss(self) -> None:
        rows = {row["surface"]: row for row in PACKET["planning_matrix"]}
        self.assertEqual(rows["hidden_visibility_token"]["forbidden_interpretation"], "hidden_is_not_missing")
        self.assertEqual(rows["hidden_is_not_missing"]["forbidden_interpretation"], "hidden_as_missing")
        self.assertEqual(
            rows["occluded_is_not_source_lineage_loss"]["forbidden_interpretation"],
            "occluded_as_source_lineage_loss",
        )
        for row in rows.values():
            self.assertFalse(row["runtime_dependency"])
            self.assertFalse(row["renderer_frame_dependency"])
            self.assertFalse(row["source_lineage_mutation_allowed"])

    def test_decision_output_is_non_authorizing(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["computed_but_hidden_contract_planning_gate_passed"])
        self.assertTrue(decision["computed_but_hidden_helper_candidate_supported"])
        self.assertTrue(decision["descriptor_contract_ledger_candidate"])
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
            "hidden_as_missing_authorized",
            "source_lineage_loss_interpretation_authorized",
            "transparent_globe_leak_inferred",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_recommended_next_gate_is_checker_planning(self) -> None:
        self.assertEqual(
            PACKET["decision_output"]["recommended_next_gate"],
            "dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_planning_gate",
        )

    def test_boundary_statement(self) -> None:
        statement = PACKET["boundary_statement"]
        self.assertIn("No helper creation", statement)
        self.assertIn("no checker creation", statement)
        self.assertIn("no render_core change", statement)
        self.assertIn("no frame buffer read", statement)
        self.assertIn("no hidden-as-missing interpretation", statement)
        self.assertIn("no source-lineage-loss interpretation", statement)
        self.assertIn("no transparent-globe leak inference", statement)
        self.assertIn("no RRKAL-wide methodology promotion", statement)
        self.assertIn("no push", statement)


if __name__ == "__main__":
    unittest.main()