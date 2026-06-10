"""Planning gate for sampling / visibility adapter extraction."""

from __future__ import annotations

import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame sampling / visibility adapter "
    "extraction planning gate. No helper creation, no checker creation, no "
    "probe script change, no production source change, no render_if_needed, no "
    "controller, no renderer, no frame buffer read, no artifact generation, no "
    "formula or renderer behavior change, no correctness/readiness/leak-fix "
    "claim, and no push."
)


OBSERVED_BRIDGE_EVIDENCE_PACKET = {
    "projection_seams_observed": True,
    "mask_seam_observed": True,
    "sampled_visible_token": True,
    "visible_count_observation": 2,
    "rendered_count_observation": 1,
    "reduced_sample_supports_rendered_lt_visible": True,
    "mask_false_supports_mask_can_hide_overlay_without_source_loss": True,
    "source_lineage_guard_supported": True,
    "frame_remains_not_observed": True,
}


ALLOWED_BOUNDARY_CLASSIFICATIONS = {
    "planning_candidate",
    "adapter_extraction_candidate",
    "contract_only_candidate",
    "blocked_by_frame_stop_line",
    "blocked_by_projection_formula",
    "blocked_by_renderer_runtime",
    "blocked_by_source_lineage_guard",
}


ADAPTER_CANDIDATE_MATRIX = [
    {
        "candidate": "DynamicPointSamplingVisibilityAdapter",
        "description": "owns synthetic sampling/count observation",
        "fields": [
            "sampled_visible",
            "visible_count",
            "rendered_count",
            "source_lineage_integrity",
        ],
        "does_not_own": ["projection_formula", "renderer_frame_output", "frame_visible_truth"],
        "classification": "adapter_extraction_candidate",
        "planning_candidate": True,
        "adapter_extraction_candidate": True,
        "contract_only_candidate": False,
        "blocked_by_frame_stop_line": False,
        "blocked_by_projection_formula": False,
        "blocked_by_renderer_runtime": False,
        "blocked_by_source_lineage_guard": False,
    },
    {
        "candidate": "DynamicPointVisibilityCountContract",
        "description": "describes count and visibility observation fields",
        "fields": [
            "source_present",
            "projected_visible",
            "sampled_visible",
            "visible_count",
            "rendered_count",
            "mask_visible",
            "source_lineage_integrity",
            "frame_visible",
        ],
        "does_not_own": ["frame_visible_runtime_truth", "renderer_frame_output"],
        "classification": "contract_only_candidate",
        "planning_candidate": True,
        "adapter_extraction_candidate": False,
        "contract_only_candidate": True,
        "blocked_by_frame_stop_line": False,
        "blocked_by_projection_formula": False,
        "blocked_by_renderer_runtime": False,
        "blocked_by_source_lineage_guard": False,
    },
    {
        "candidate": "DynamicPointMaskVisibilityContract",
        "description": "owns mask-visible and mask-hidden semantics",
        "fields": ["overlay_rendered", "mask_visible", "source_lineage_integrity"],
        "does_not_own": ["source_deletion_interpretation", "mask_formula"],
        "classification": "contract_only_candidate",
        "planning_candidate": True,
        "adapter_extraction_candidate": False,
        "contract_only_candidate": True,
        "blocked_by_frame_stop_line": False,
        "blocked_by_projection_formula": False,
        "blocked_by_renderer_runtime": False,
        "blocked_by_source_lineage_guard": False,
    },
    {
        "candidate": "DynamicPointSamplingReductionContract",
        "description": "owns rendered_count lower than visible_count semantics",
        "fields": ["visible_count", "rendered_count", "reduction_label"],
        "does_not_own": ["source_loss", "provider_filter"],
        "classification": "contract_only_candidate",
        "planning_candidate": True,
        "adapter_extraction_candidate": False,
        "contract_only_candidate": True,
        "blocked_by_frame_stop_line": False,
        "blocked_by_projection_formula": False,
        "blocked_by_renderer_runtime": False,
        "blocked_by_source_lineage_guard": False,
    },
    {
        "candidate": "DynamicPointFrameVisibilityStopLineContract",
        "description": "records frame, renderer, and leak blocked surfaces",
        "fields": ["frame_visible", "frame_rgba", "render_if_needed", "transparent_globe_leak"],
        "does_not_own": ["frame_buffer_read", "renderer_execution", "leak_fix_claim"],
        "classification": "blocked_by_frame_stop_line",
        "planning_candidate": True,
        "adapter_extraction_candidate": False,
        "contract_only_candidate": True,
        "blocked_by_frame_stop_line": True,
        "blocked_by_projection_formula": False,
        "blocked_by_renderer_runtime": True,
        "blocked_by_source_lineage_guard": False,
    },
]


FUTURE_HELPER_TARGET_PLANNING = {
    "future_helper_target": "render_core/dynamic_point_sampling_visibility_boundary.py",
    "helper_creation_authorized": False,
    "candidate_helper_names": [
        "build_dynamic_point_sampling_visibility_observation_descriptor",
        "build_dynamic_point_visibility_count_contract_descriptor",
        "build_dynamic_point_mask_visibility_contract_descriptor",
        "build_dynamic_point_sampling_reduction_contract_descriptor",
        "build_dynamic_point_frame_visibility_stop_line_descriptor",
        "dynamic_point_sampling_visibility_boundary_descriptor",
        "dynamic_point_sampling_visibility_planning_bundle",
    ],
    "allowed_future_content": [
        "descriptor_only",
        "contract_only",
        "stop_line_ledger",
        "source_lineage_guard_labels",
    ],
    "blocked_future_content": [
        "projection_formula",
        "mask_formula",
        "sampling_formula_movement",
        "frame_buffer_read",
        "renderer_runtime",
        "artifact_write",
    ],
}


IMPORT_BOUNDARY_CHECKER_NEED = {
    "new_checker_required": True,
    "existing_checker_reusable": False,
    "future_checker_target": (
        "scripts\\validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py"
    ),
    "checker_creation_authorized": False,
}


ACCELERATION_DECISION = {
    "adapter_extraction_planning_passed": True,
    "sampling_visibility_adapter_path_supported": True,
    "production_extraction_authorized": False,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "probe_script_change_authorized": False,
    "production_source_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_instantiation_authorized": False,
    "renderer_execution_authorized": False,
    "frame_buffer_read_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "renderer_behavior_change_authorized": False,
    "compose_order_change_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
    "next_gate": "dynamic_point_lod_view_frame_sampling_visibility_import_boundary_checker_gate",
}


PACKET = {
    "schema": (
        "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_"
        "adapter_extraction_planning.v1"
    ),
    "evidence_sources": {
        "frame_visibility_stop_line_planning": "4dc02a2",
        "sampling_visibility_runtime_probe_result_interpretation": "5503eb0",
        "sampling_visibility_probe_script_update": "af4d023",
        "grafting_path_minimal_evidence": "87cb579",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "current_monolith_static_scan": True,
        "runtime_executed_by_this_gate": False,
    },
    "observed_bridge_evidence_packet": OBSERVED_BRIDGE_EVIDENCE_PACKET,
    "adapter_candidate_matrix": ADAPTER_CANDIDATE_MATRIX,
    "future_helper_target_planning": FUTURE_HELPER_TARGET_PLANNING,
    "import_boundary_checker_need": IMPORT_BOUNDARY_CHECKER_NEED,
    "acceleration_decision": ACCELERATION_DECISION,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSamplingVisibilityAdapterExtractionPlanningTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "observed_bridge_evidence_packet",
                "adapter_candidate_matrix",
                "future_helper_target_planning",
                "import_boundary_checker_need",
                "acceleration_decision",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_"
            "adapter_extraction_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_observed_bridge_evidence_packet(self) -> None:
        evidence = PACKET["observed_bridge_evidence_packet"]
        self.assertTrue(evidence["projection_seams_observed"])
        self.assertTrue(evidence["mask_seam_observed"])
        self.assertTrue(evidence["sampled_visible_token"])
        self.assertEqual(evidence["visible_count_observation"], 2)
        self.assertEqual(evidence["rendered_count_observation"], 1)
        self.assertTrue(evidence["reduced_sample_supports_rendered_lt_visible"])
        self.assertTrue(evidence["mask_false_supports_mask_can_hide_overlay_without_source_loss"])
        self.assertTrue(evidence["source_lineage_guard_supported"])
        self.assertTrue(evidence["frame_remains_not_observed"])

    def test_adapter_candidate_matrix(self) -> None:
        rows = {row["candidate"]: row for row in PACKET["adapter_candidate_matrix"]}
        self.assertEqual(
            set(rows),
            {
                "DynamicPointSamplingVisibilityAdapter",
                "DynamicPointVisibilityCountContract",
                "DynamicPointMaskVisibilityContract",
                "DynamicPointSamplingReductionContract",
                "DynamicPointFrameVisibilityStopLineContract",
            },
        )
        for row in rows.values():
            self.assertIn(row["classification"], ALLOWED_BOUNDARY_CLASSIFICATIONS)
            self.assertTrue(row["planning_candidate"])
        self.assertTrue(rows["DynamicPointSamplingVisibilityAdapter"]["adapter_extraction_candidate"])
        self.assertIn(
            "projection_formula",
            rows["DynamicPointSamplingVisibilityAdapter"]["does_not_own"],
        )
        self.assertIn(
            "renderer_frame_output",
            rows["DynamicPointSamplingVisibilityAdapter"]["does_not_own"],
        )
        self.assertIn("frame_visible", rows["DynamicPointVisibilityCountContract"]["fields"])
        self.assertIn(
            "source_deletion_interpretation",
            rows["DynamicPointMaskVisibilityContract"]["does_not_own"],
        )
        self.assertIn("source_loss", rows["DynamicPointSamplingReductionContract"]["does_not_own"])
        self.assertTrue(
            rows["DynamicPointFrameVisibilityStopLineContract"]["blocked_by_frame_stop_line"]
        )
        self.assertTrue(
            rows["DynamicPointFrameVisibilityStopLineContract"]["blocked_by_renderer_runtime"]
        )

    def test_candidate_boundary_booleans_are_non_authorizing(self) -> None:
        for row in PACKET["adapter_candidate_matrix"]:
            self.assertFalse(row["blocked_by_projection_formula"])
            self.assertFalse(row["blocked_by_source_lineage_guard"])
            if row["candidate"] != "DynamicPointFrameVisibilityStopLineContract":
                self.assertFalse(row["blocked_by_frame_stop_line"])
                self.assertFalse(row["blocked_by_renderer_runtime"])

    def test_future_helper_target_planning_without_creation(self) -> None:
        target = PACKET["future_helper_target_planning"]
        self.assertEqual(
            target["future_helper_target"],
            "render_core/dynamic_point_sampling_visibility_boundary.py",
        )
        self.assertFalse(target["helper_creation_authorized"])
        self.assertEqual(
            target["candidate_helper_names"],
            [
                "build_dynamic_point_sampling_visibility_observation_descriptor",
                "build_dynamic_point_visibility_count_contract_descriptor",
                "build_dynamic_point_mask_visibility_contract_descriptor",
                "build_dynamic_point_sampling_reduction_contract_descriptor",
                "build_dynamic_point_frame_visibility_stop_line_descriptor",
                "dynamic_point_sampling_visibility_boundary_descriptor",
                "dynamic_point_sampling_visibility_planning_bundle",
            ],
        )
        self.assertIn("descriptor_only", target["allowed_future_content"])
        self.assertIn("frame_buffer_read", target["blocked_future_content"])
        self.assertIn("renderer_runtime", target["blocked_future_content"])

    def test_import_boundary_checker_need(self) -> None:
        checker = PACKET["import_boundary_checker_need"]
        self.assertTrue(checker["new_checker_required"])
        self.assertFalse(checker["existing_checker_reusable"])
        self.assertEqual(
            checker["future_checker_target"],
            "scripts\\validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py",
        )
        self.assertFalse(checker["checker_creation_authorized"])

    def test_acceleration_decision_is_planning_only(self) -> None:
        decision = PACKET["acceleration_decision"]
        self.assertTrue(decision["adapter_extraction_planning_passed"])
        self.assertTrue(decision["sampling_visibility_adapter_path_supported"])
        for key in (
            "production_extraction_authorized",
            "helper_creation_authorized",
            "checker_creation_authorized",
            "probe_script_change_authorized",
            "production_source_change_authorized",
            "render_if_needed_authorized",
            "controller_instantiation_authorized",
            "renderer_execution_authorized",
            "frame_buffer_read_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "renderer_behavior_change_authorized",
            "compose_order_change_authorized",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "transparent_globe_leak_fix_claimed",
            "readiness_claimed",
        ):
            self.assertIs(decision[key], False, key)
        self.assertEqual(
            decision["next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_import_boundary_checker_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker creation", BOUNDARY_STATEMENT)
        self.assertIn("no renderer", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
