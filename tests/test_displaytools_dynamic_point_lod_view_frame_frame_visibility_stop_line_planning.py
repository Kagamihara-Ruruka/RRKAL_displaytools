"""Planning gate for frame visibility and transparent-globe leak stop-lines."""

from __future__ import annotations

import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame frame visibility stop-line "
    "planning gate. No probe script change, no new runtime execution, no "
    "render_if_needed, no controller, no renderer, no frame buffer read, no "
    "artifact generation, no formula or renderer behavior change, no "
    "correctness/readiness/leak-fix claim, and no push."
)


ALLOWED_FRAME_STOP_LINE_CLASSIFICATIONS = {
    "observed_allowed",
    "not_observed_stop_line",
    "forbidden_runtime_surface",
    "future_authorization_candidate",
    "fault_not_inferred",
}


FRAME_STOP_LINE_MATRIX = [
    {
        "surface": "frame_visible_token",
        "classification": "not_observed_stop_line",
        "current_evidence": "frame_visible_token remains not_observed in the second probe",
        "authorized_now": False,
        "future_handling": "requires explicit frame stop-line or runtime authorization review",
    },
    {
        "surface": "frame_rgba_buffer",
        "classification": "forbidden_runtime_surface",
        "current_evidence": "static scan finds frame_rgba as renderer buffer surface",
        "authorized_now": False,
        "future_handling": "must not be read by this planning gate",
    },
    {
        "surface": "render_if_needed",
        "classification": "forbidden_runtime_surface",
        "current_evidence": "static scan finds render_if_needed controller render entry",
        "authorized_now": False,
        "future_handling": "requires separate runtime authorization if ever considered",
    },
    {
        "surface": "controller_instantiation",
        "classification": "forbidden_runtime_surface",
        "current_evidence": "static scan finds controller construction near runtime entry",
        "authorized_now": False,
        "future_handling": "must stay outside docs/test-only planning",
    },
    {
        "surface": "renderer_execution",
        "classification": "forbidden_runtime_surface",
        "current_evidence": "static scan finds renderer and viewer execution surfaces",
        "authorized_now": False,
        "future_handling": "requires a separate runtime execution gate",
    },
    {
        "surface": "alpha_compose_path",
        "classification": "future_authorization_candidate",
        "current_evidence": "static scan finds alpha_compose as compose-adjacent visibility surface",
        "authorized_now": False,
        "future_handling": "can be mapped later without formula movement",
    },
    {
        "surface": "write_preview_frame_png",
        "classification": "forbidden_runtime_surface",
        "current_evidence": "static scan finds preview PNG writer import",
        "authorized_now": False,
        "future_handling": "artifact-writing surface remains forbidden",
    },
    {
        "surface": "output_path_save",
        "classification": "forbidden_runtime_surface",
        "current_evidence": "static scan finds Image.fromarray and output/write surfaces",
        "authorized_now": False,
        "future_handling": "file output remains forbidden",
    },
    {
        "surface": "transparent_globe_leak_behavior",
        "classification": "fault_not_inferred",
        "current_evidence": "frame visibility was not observed in the second probe",
        "authorized_now": False,
        "future_handling": "may only be treated as an unresolved stop-line",
    },
]


CURRENT_EVIDENCE_CLASSIFICATION = {
    "observed": [
        "projection_seam",
        "aircraft_projection_seam",
        "mask_seam",
        "sampling_token",
        "visible_rendered_count",
        "source_lineage_guard",
    ],
    "not_observed": [
        "frame_visibility",
        "frame_rgba",
        "render_if_needed",
        "controller",
        "renderer",
        "transparent_globe_leak_behavior",
    ],
}


LEAK_CLAIM_GUARD = {
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "frame_visibility_observed": False,
    "frame_buffer_read": False,
    "renderer_executed": False,
}


FUTURE_AUTHORIZATION_DECISION_TREE = [
    {
        "route": "conservative_route",
        "next_gate": "dynamic_point_lod_view_frame_frame_visibility_stop_line_closure_gate",
        "purpose": "close frame and leak stop-lines before extraction planning",
        "authorized_by_this_gate": False,
    },
    {
        "route": "acceleration_route",
        "next_gate": "dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate",
        "purpose": "plan extraction around observed sampling, count, and mask surfaces",
        "authorized_by_this_gate": False,
    },
    {
        "route": "runtime_route",
        "next_gate": "dynamic_point_lod_view_frame_frame_visibility_probe_authorization_review_gate",
        "purpose": "review whether frame visibility probe can ever be authorized",
        "authorized_by_this_gate": False,
    },
]


DECISION_OUTPUT = {
    "frame_visibility_stop_line_planning_passed": True,
    "frame_stop_line_matrix_defined": True,
    "current_evidence_classification_defined": True,
    "leak_claim_guard_defined": True,
    "future_authorization_decision_tree_defined": True,
    "frame_visibility_observed": False,
    "frame_buffer_read": False,
    "renderer_executed": False,
    "controller_instantiated": False,
    "render_if_needed_called": False,
    "artifact_generation_authorized": False,
    "formula_change_authorized": False,
    "renderer_behavior_change_authorized": False,
    "compose_order_change_authorized": False,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "readiness_claimed": False,
    "recommended_next_gate": (
        "dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate"
    ),
}


PACKET = {
    "schema": (
        "rrkal.displaytools.dynamic_point_lod_view_frame_frame_visibility_"
        "stop_line_planning.v1"
    ),
    "evidence_sources": {
        "sampling_visibility_runtime_probe_result_interpretation": "5503eb0",
        "sampling_visibility_probe_script_update": "af4d023",
        "occlusion_responsibility_boundary": "44356e9",
        "view_frame_occlusion_structure_settlement": "df40770",
        "current_monolith_static_scan": True,
        "runtime_executed_by_this_gate": False,
    },
    "frame_stop_line_matrix": FRAME_STOP_LINE_MATRIX,
    "current_evidence_classification": CURRENT_EVIDENCE_CLASSIFICATION,
    "leak_claim_guard": LEAK_CLAIM_GUARD,
    "future_authorization_decision_tree": FUTURE_AUTHORIZATION_DECISION_TREE,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointFrameVisibilityStopLinePlanningTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "frame_stop_line_matrix",
                "current_evidence_classification",
                "leak_claim_guard",
                "future_authorization_decision_tree",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_frame_visibility_"
            "stop_line_planning.v1",
        )

    def test_frame_stop_line_matrix_surfaces_and_classifications(self) -> None:
        rows = {row["surface"]: row for row in PACKET["frame_stop_line_matrix"]}
        self.assertEqual(
            set(rows),
            {
                "frame_visible_token",
                "frame_rgba_buffer",
                "render_if_needed",
                "controller_instantiation",
                "renderer_execution",
                "alpha_compose_path",
                "write_preview_frame_png",
                "output_path_save",
                "transparent_globe_leak_behavior",
            },
        )
        for row in rows.values():
            self.assertIn(row["classification"], ALLOWED_FRAME_STOP_LINE_CLASSIFICATIONS)
            self.assertFalse(row["authorized_now"])
        self.assertEqual(rows["frame_visible_token"]["classification"], "not_observed_stop_line")
        self.assertEqual(rows["frame_rgba_buffer"]["classification"], "forbidden_runtime_surface")
        self.assertEqual(rows["render_if_needed"]["classification"], "forbidden_runtime_surface")
        self.assertEqual(rows["alpha_compose_path"]["classification"], "future_authorization_candidate")
        self.assertEqual(rows["transparent_globe_leak_behavior"]["classification"], "fault_not_inferred")

    def test_current_evidence_classification(self) -> None:
        classification = PACKET["current_evidence_classification"]
        self.assertEqual(
            set(classification["observed"]),
            {
                "projection_seam",
                "aircraft_projection_seam",
                "mask_seam",
                "sampling_token",
                "visible_rendered_count",
                "source_lineage_guard",
            },
        )
        self.assertEqual(
            set(classification["not_observed"]),
            {
                "frame_visibility",
                "frame_rgba",
                "render_if_needed",
                "controller",
                "renderer",
                "transparent_globe_leak_behavior",
            },
        )

    def test_leak_claim_guard(self) -> None:
        guard = PACKET["leak_claim_guard"]
        self.assertFalse(guard["transparent_globe_leak_inferred"])
        self.assertFalse(guard["transparent_globe_leak_fix_claimed"])
        self.assertFalse(guard["frame_visibility_observed"])
        self.assertFalse(guard["frame_buffer_read"])
        self.assertFalse(guard["renderer_executed"])

    def test_future_authorization_decision_tree(self) -> None:
        tree = {row["route"]: row for row in PACKET["future_authorization_decision_tree"]}
        self.assertEqual(
            set(tree),
            {"conservative_route", "acceleration_route", "runtime_route"},
        )
        self.assertEqual(
            tree["conservative_route"]["next_gate"],
            "dynamic_point_lod_view_frame_frame_visibility_stop_line_closure_gate",
        )
        self.assertEqual(
            tree["acceleration_route"]["next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate",
        )
        self.assertEqual(
            tree["runtime_route"]["next_gate"],
            "dynamic_point_lod_view_frame_frame_visibility_probe_authorization_review_gate",
        )
        for row in tree.values():
            self.assertFalse(row["authorized_by_this_gate"])

    def test_decision_output_recommends_acceleration_with_stop_lines(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["frame_visibility_stop_line_planning_passed"])
        self.assertTrue(decision["frame_stop_line_matrix_defined"])
        self.assertTrue(decision["current_evidence_classification_defined"])
        self.assertTrue(decision["leak_claim_guard_defined"])
        self.assertTrue(decision["future_authorization_decision_tree_defined"])
        for key in (
            "frame_visibility_observed",
            "frame_buffer_read",
            "renderer_executed",
            "controller_instantiated",
            "render_if_needed_called",
            "artifact_generation_authorized",
            "formula_change_authorized",
            "renderer_behavior_change_authorized",
            "compose_order_change_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "readiness_claimed",
        ):
            self.assertIs(decision[key], False, key)
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("No probe script change", BOUNDARY_STATEMENT)
        self.assertIn("no renderer", BOUNDARY_STATEMENT)
        self.assertIn("no frame buffer read", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
