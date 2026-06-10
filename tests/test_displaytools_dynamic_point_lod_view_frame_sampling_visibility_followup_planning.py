"""Planning fixture for sampling and visibility follow-up probe design."""

from __future__ import annotations

import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame sampling / visibility followup "
    "planning gate. No runtime probe expansion, no probe harness creation, no "
    "production source change, no renderer execution, no controller "
    "instantiation, no artifact generation, no formula or renderer behavior "
    "change, no correctness/readiness/fix claim, and no push."
)


PHASE_A_PREVIOUS_RESULT = {
    "observed": {
        "project_ais_to_screen_called": True,
        "project_aircraft_to_screen_called": True,
        "mask_overlay_to_globe_called": True,
        "source_lineage_integrity_token": True,
        "projected_visible_token": True,
        "overlay_rendered_token": True,
        "mask_visible_token": True,
    },
    "not_observed": {
        "sampled_visible_token": "not_observed",
        "frame_visible_token": "not_observed",
        "visible_count_observation": "not_observed",
        "rendered_count_observation": "not_observed",
        "transparent_globe_leak_behavior": "not_observed",
        "render_if_needed": "not_observed",
        "controller_renderer_path": "not_observed",
    },
}


FOLLOWUP_MATRIX = [
    {
        "entrypoint_candidate": "existing_projection_mask_probe_path",
        "token_candidate": "projected_visible_token",
        "condition_candidate": "mask_visible_true",
        "expected_observation": "projection_and_mask_path_remains_observable",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "sampling_adapter_candidate",
        "token_candidate": "sampled_visible_token",
        "condition_candidate": "sample_ratio_full",
        "expected_observation": "sampling_visibility_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "sampling_adapter_candidate",
        "token_candidate": "sampled_visible_token",
        "condition_candidate": "sample_ratio_reduced",
        "expected_observation": "sampling_reduction_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "sampling_adapter_candidate",
        "token_candidate": "sampled_visible_token",
        "condition_candidate": "adaptive_sampling_disabled",
        "expected_observation": "sampling_baseline_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "sampling_adapter_candidate",
        "token_candidate": "sampled_visible_token",
        "condition_candidate": "adaptive_sampling_enabled_label_only",
        "expected_observation": "adaptive_sampling_label_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "count_observation_candidate",
        "token_candidate": "visible_count_observation",
        "condition_candidate": "sample_ratio_full",
        "expected_observation": "visible_count_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "count_observation_candidate",
        "token_candidate": "rendered_count_observation",
        "condition_candidate": "sample_ratio_reduced",
        "expected_observation": "rendered_count_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "frame_visibility_stop_line",
        "token_candidate": "frame_visible_token",
        "condition_candidate": "frame_visibility_not_authorized",
        "expected_observation": "stop_line_before_frame_buffer_or_renderer",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "existing_projection_mask_probe_path",
        "token_candidate": "mask_visible_token",
        "condition_candidate": "mask_visible_false_synthetic",
        "expected_observation": "synthetic_mask_hidden_candidate",
        "probe_behavior_change_authorized": False,
    },
    {
        "entrypoint_candidate": "render_if_needed_stop_line",
        "token_candidate": "source_lineage_integrity_token",
        "condition_candidate": "frame_visibility_not_authorized",
        "expected_observation": "render_if_needed_remains_blocked",
        "probe_behavior_change_authorized": False,
    },
]


ALLOWED_STRATEGY = {
    "synthetic_data_only": True,
    "one_shot_only": True,
    "stdout_only_packet": True,
    "persistent_artifact": False,
    "live_source": False,
    "db_cache_websocket": False,
    "gui_interaction": False,
    "controller_instantiation_without_future_authorization": False,
}


FORBIDDEN_STRATEGY = {
    "render_if_needed_call": True,
    "renderer_execution": True,
    "frame_buffer_read": True,
    "png_runtime_json_state_write": True,
    "projection_mask_sampling_compose_formula_change": True,
    "renderer_behavior_change": True,
    "coordinate_correctness_claim": True,
    "visual_correctness_claim": True,
    "transparent_globe_leak_fix_claim": True,
    "readiness_claim": True,
}


ORACLE_RULES = [
    {
        "condition": "projected true + sampled false",
        "verdict": "sampling_responsibility_candidate",
    },
    {
        "condition": "sampled true + overlay false",
        "verdict": "overlay_render_responsibility_candidate",
    },
    {
        "condition": "overlay true + mask false",
        "verdict": "globe_mask_responsibility_candidate",
    },
    {
        "condition": "mask false + frame true",
        "verdict": "transparent_globe_leak_candidate",
    },
    {
        "condition": "source true + frame false",
        "verdict": "computed_but_hidden_supported",
    },
    {
        "condition": "source lineage changed",
        "verdict": "source_lineage_pollution_fail",
    },
    {
        "condition": "visible count observed but rendered count not observed",
        "verdict": "count_surface_partial",
    },
    {
        "condition": "rendered count lower than visible count",
        "verdict": "sampling_or_presentation_reduction_candidate",
    },
]


NEXT_AUTHORIZATION_DRAFT = {
    "next_gate": "dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design_gate",
    "may_consider_probe_harness_change": True,
    "this_gate_executes_runtime_probe": False,
    "this_gate_modifies_probe_script": False,
    "this_gate_authorizes_render_if_needed": False,
    "this_gate_authorizes_controller": False,
    "this_gate_authorizes_renderer": False,
    "this_gate_authorizes_artifact_write": False,
}


DECISION_OUTPUT = {
    "planning_gate_passed": True,
    "previous_probe_result_absorbed": True,
    "followup_matrix_defined": True,
    "oracle_planning_defined": True,
    "next_probe_design_cooled": True,
    "runtime_probe_expansion_authorized": False,
    "probe_harness_creation_authorized": False,
    "production_source_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_instantiation_authorized": False,
    "renderer_execution_authorized": False,
    "artifact_generation_authorized": False,
    "formula_change_authorized": False,
    "renderer_behavior_change_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
    "recommended_next_gate": (
        "dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design_gate"
    ),
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_followup_planning.v1",
    "phase_a_previous_result": PHASE_A_PREVIOUS_RESULT,
    "followup_matrix": FOLLOWUP_MATRIX,
    "allowed_strategy": ALLOWED_STRATEGY,
    "forbidden_strategy": FORBIDDEN_STRATEGY,
    "oracle_rules": ORACLE_RULES,
    "next_authorization_draft": NEXT_AUTHORIZATION_DRAFT,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSamplingVisibilityFollowupPlanningTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "phase_a_previous_result",
                "followup_matrix",
                "allowed_strategy",
                "forbidden_strategy",
                "oracle_rules",
                "next_authorization_draft",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_followup_planning.v1",
        )

    def test_phase_a_observed_and_not_observed_results(self) -> None:
        observed = PACKET["phase_a_previous_result"]["observed"]
        for key in (
            "project_ais_to_screen_called",
            "project_aircraft_to_screen_called",
            "mask_overlay_to_globe_called",
            "source_lineage_integrity_token",
            "projected_visible_token",
            "overlay_rendered_token",
            "mask_visible_token",
        ):
            self.assertIs(observed[key], True, key)
        not_observed = PACKET["phase_a_previous_result"]["not_observed"]
        self.assertEqual(
            set(not_observed),
            {
                "sampled_visible_token",
                "frame_visible_token",
                "visible_count_observation",
                "rendered_count_observation",
                "transparent_globe_leak_behavior",
                "render_if_needed",
                "controller_renderer_path",
            },
        )
        for value in not_observed.values():
            self.assertEqual(value, "not_observed")

    def test_followup_matrix_selected_dimensions(self) -> None:
        rows = PACKET["followup_matrix"]
        entrypoints = {row["entrypoint_candidate"] for row in rows}
        tokens = {row["token_candidate"] for row in rows}
        conditions = {row["condition_candidate"] for row in rows}
        self.assertEqual(
            entrypoints,
            {
                "existing_projection_mask_probe_path",
                "sampling_adapter_candidate",
                "count_observation_candidate",
                "frame_visibility_stop_line",
                "render_if_needed_stop_line",
            },
        )
        self.assertTrue(
            {
                "source_present_token",
                "projected_visible_token",
                "sampled_visible_token",
                "overlay_rendered_token",
                "mask_visible_token",
                "frame_visible_token",
                "visible_count_observation",
                "rendered_count_observation",
                "source_lineage_integrity_token",
            }.issuperset(tokens)
        )
        self.assertEqual(
            conditions,
            {
                "sample_ratio_full",
                "sample_ratio_reduced",
                "adaptive_sampling_disabled",
                "adaptive_sampling_enabled_label_only",
                "mask_visible_true",
                "mask_visible_false_synthetic",
                "frame_visibility_not_authorized",
            },
        )
        for row in rows:
            self.assertIs(row["probe_behavior_change_authorized"], False)

    def test_allowed_and_forbidden_strategy_boundaries(self) -> None:
        allowed = PACKET["allowed_strategy"]
        self.assertTrue(allowed["synthetic_data_only"])
        self.assertTrue(allowed["one_shot_only"])
        self.assertTrue(allowed["stdout_only_packet"])
        for key in (
            "persistent_artifact",
            "live_source",
            "db_cache_websocket",
            "gui_interaction",
            "controller_instantiation_without_future_authorization",
        ):
            self.assertIs(allowed[key], False, key)
        for value in PACKET["forbidden_strategy"].values():
            self.assertIs(value, True)

    def test_oracle_rules_cover_required_verdicts(self) -> None:
        verdicts = {row["verdict"] for row in PACKET["oracle_rules"]}
        self.assertEqual(
            verdicts,
            {
                "sampling_responsibility_candidate",
                "overlay_render_responsibility_candidate",
                "globe_mask_responsibility_candidate",
                "transparent_globe_leak_candidate",
                "computed_but_hidden_supported",
                "source_lineage_pollution_fail",
                "count_surface_partial",
                "sampling_or_presentation_reduction_candidate",
            },
        )

    def test_next_authorization_draft_is_planning_only(self) -> None:
        draft = PACKET["next_authorization_draft"]
        self.assertEqual(
            draft["next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design_gate",
        )
        self.assertTrue(draft["may_consider_probe_harness_change"])
        for key in (
            "this_gate_executes_runtime_probe",
            "this_gate_modifies_probe_script",
            "this_gate_authorizes_render_if_needed",
            "this_gate_authorizes_controller",
            "this_gate_authorizes_renderer",
            "this_gate_authorizes_artifact_write",
        ):
            self.assertIs(draft[key], False, key)

    def test_decision_output_and_boundary(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["planning_gate_passed"])
        self.assertTrue(decision["previous_probe_result_absorbed"])
        self.assertTrue(decision["followup_matrix_defined"])
        self.assertTrue(decision["oracle_planning_defined"])
        self.assertTrue(decision["next_probe_design_cooled"])
        for key in (
            "runtime_probe_expansion_authorized",
            "probe_harness_creation_authorized",
            "production_source_change_authorized",
            "render_if_needed_authorized",
            "controller_instantiation_authorized",
            "renderer_execution_authorized",
            "artifact_generation_authorized",
            "formula_change_authorized",
            "renderer_behavior_change_authorized",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "transparent_globe_leak_fix_claimed",
            "readiness_claimed",
        ):
            self.assertIs(decision[key], False, key)
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design_gate",
        )
        self.assertIn("No runtime probe expansion", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
