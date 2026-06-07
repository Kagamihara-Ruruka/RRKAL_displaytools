import unittest

from render_core.render_plan import (
    build_layer_render_plan_bottleneck_recommendation,
    build_layer_render_plan_execution_phases,
    build_layer_render_plan_execution_summary,
    build_layer_render_plan_phase_timing_contract,
    build_layer_render_plan_phase_timing_runtime_packet,
)


EXECUTION_SUMMARY_KEYS = {
    "schema",
    "source",
    "current_execution_mode",
    "current_apply_helper",
    "runtime_optimization_applied",
    "apply_path_count",
    "batch_decision_count",
    "single_pass_candidate_count",
    "single_pass_blockers",
    "helper_counts",
    "decision_counts",
    "batch_decision_counts",
    "next_refactor_target",
}

PHASE_KEYS = {
    "id",
    "order",
    "status",
    "item_count",
    "decisions",
    "current_runtime_path",
    "future_single_pass_role",
}

PHASE_TIMING_CONTRACT_KEYS = {
    "schema",
    "source",
    "status",
    "runtime_measurements_available",
    "timing_unit",
    "slow_frame_threshold_ms",
    "phase_probe_count",
    "phase_probe_points",
    "summary_fields",
    "next_runtime_step",
}

BOTTLENECK_RECOMMENDATION_KEYS = {
    "schema",
    "source",
    "status",
    "basis_schema",
    "slowest_phase_id",
    "slowest_phase_ms",
    "total_ms",
    "slow_frame",
    "recommended_next_action",
    "target_helper",
    "optimization_boundary",
    "runtime_optimization_applied",
    "next_commit_scope",
}

PHASE_TIMING_RUNTIME_KEYS = {
    "schema",
    "source",
    "status",
    "runtime_measurements_available",
    "timing_unit",
    "total_ms",
    "phase_timing_ms",
    "measured_phase_ids",
    "slowest_phase_id",
    "slowest_phase_ms",
    "slow_frame",
    "slow_frame_threshold_ms",
    "frame_index",
    "next_optimization_use",
    "bottleneck_recommendation_schema",
    "bottleneck_recommendation",
}


class LayerRenderPlanExecutionPhaseTimingTests(unittest.TestCase):
    def test_execution_summary_key_set_counts_and_blockers(self):
        apply_path = [
            {"id": "lakes", "apply_helper": "alpha_compose", "decision": "compose_dirty_overlay", "single_pass_candidate": True},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess", "apply_helper": "apply_style_profile", "decision": "compose_cached_overlay", "single_pass_candidate": False},
            "malformed",
        ]
        batch_decisions = [
            {"scope": "batch", "decision": "rebuild_batch"},
            {"scope": "layer", "decision": "compose_dirty_overlay"},
            {"scope": "layer"},
            "malformed",
        ]

        packet = build_layer_render_plan_execution_summary(apply_path, batch_decisions)

        self.assertEqual(set(packet.keys()), EXECUTION_SUMMARY_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_execution_summary.v1")
        self.assertEqual(packet["source"], "render_core.render_plan.build_layer_render_plan_execution_summary")
        self.assertEqual(packet["current_execution_mode"], "centralized_overlay_composition")
        self.assertEqual(packet["current_apply_helper"], "HybridRenderController.apply_layer_render_plan_composition")
        self.assertFalse(packet["runtime_optimization_applied"])
        self.assertEqual(packet["apply_path_count"], 3)
        self.assertEqual(packet["batch_decision_count"], 4)
        self.assertEqual(packet["single_pass_candidate_count"], 1)
        self.assertEqual(packet["single_pass_blockers"], ["style_profile_postprocess"])
        self.assertEqual(packet["helper_counts"], {"alpha_compose": 1, "apply_style_profile": 1})
        self.assertEqual(packet["decision_counts"], {"compose_dirty_overlay": 1, "compose_cached_overlay": 1})
        self.assertEqual(packet["batch_decision_counts"], {"rebuild_batch": 1, "compose_dirty_overlay": 1, "unknown_decision": 1})

    def test_execution_summary_deterministic_repeat_call(self):
        apply_path = [{"id": "rivers", "apply_helper": "alpha_compose", "decision": "compose_cached_overlay", "single_pass_candidate": True}]
        batch_decisions = [{"scope": "layer", "decision": "compose_cached_overlay"}]

        self.assertEqual(
            build_layer_render_plan_execution_summary(apply_path, batch_decisions),
            build_layer_render_plan_execution_summary(list(apply_path), list(batch_decisions)),
        )

    def test_execution_phases_order_and_decisions(self):
        apply_path = [
            {"id": "lakes", "kind": "alpha_compose", "single_pass_candidate": True},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess", "single_pass_candidate": False},
        ]
        batch_decisions = [
            {"scope": "batch", "decision": "reuse_batch"},
            {"scope": "batch", "decision": "rebuild_batch"},
            {"scope": "layer", "decision": "compose_cached_overlay"},
        ]
        summary = {"single_pass_blockers": ["style_profile_postprocess"]}

        phases = build_layer_render_plan_execution_phases(apply_path, batch_decisions, summary)

        self.assertEqual([phase["id"] for phase in phases], ["prepare_batches", "compose_overlays", "postprocess", "future_single_pass_candidate"])
        self.assertEqual([phase["order"] for phase in phases], [0, 1, 2, 3])
        self.assertEqual(set(phases[0].keys()), PHASE_KEYS)
        self.assertEqual(set(phases[1].keys()), PHASE_KEYS)
        self.assertEqual(set(phases[2].keys()), PHASE_KEYS)
        self.assertEqual(set(phases[3].keys()), PHASE_KEYS | {"blockers"})
        self.assertEqual(phases[0]["decisions"], ["rebuild_batch", "reuse_batch"])
        self.assertEqual(phases[1]["decisions"], ["compose_cached_overlay"])
        self.assertEqual(phases[2]["decisions"], ["postprocess_each_frame"])
        self.assertEqual(phases[3]["decisions"], ["single_pass_candidate"])
        self.assertEqual(phases[3]["blockers"], ["style_profile_postprocess"])

    def test_execution_phases_empty_inputs_use_none_decisions(self):
        phases = build_layer_render_plan_execution_phases([], [], {})

        self.assertEqual(phases[0]["decisions"], ["none"])
        self.assertEqual(phases[1]["decisions"], ["none"])
        self.assertEqual(phases[2]["item_count"], 0)
        self.assertEqual(phases[3]["item_count"], 0)
        self.assertEqual(phases[3]["blockers"], [])

    def test_phase_timing_contract_key_set_and_probe_order(self):
        phases = [
            {"id": "prepare_batches", "order": 0},
            {"id": "compose_overlays", "order": 1},
            {"order": 9},
            "malformed",
        ]

        packet = build_layer_render_plan_phase_timing_contract(phases)

        self.assertEqual(set(packet.keys()), PHASE_TIMING_CONTRACT_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_phase_timing_contract.v1")
        self.assertEqual(packet["source"], "render_core.render_plan.build_layer_render_plan_phase_timing_contract")
        self.assertEqual(packet["status"], "probe_contract_ready")
        self.assertFalse(packet["runtime_measurements_available"])
        self.assertEqual(packet["timing_unit"], "milliseconds")
        self.assertEqual(packet["slow_frame_threshold_ms"], 33.3)
        self.assertEqual(packet["phase_probe_count"], 3)
        self.assertEqual([point["phase_id"] for point in packet["phase_probe_points"]], ["prepare_batches", "compose_overlays", "unknown_phase"])
        self.assertEqual(packet["phase_probe_points"][0]["probe_key"], "phase_ms.prepare_batches")
        self.assertEqual(packet["summary_fields"], ["total_ms", "phase_timing_ms", "slowest_phase_id", "frame_index"])

    def test_bottleneck_recommendation_branches(self):
        cases = {
            "prepare_batches": ("reuse_static_geometry_batches", "HybridRenderController.compile_layer_render_plan"),
            "compose_overlays": ("collapse_overlay_composition_passes", "HybridRenderController.apply_layer_render_plan_composition"),
            "postprocess": ("fold_or_defer_style_profile_postprocess", "apply_style_profile"),
            "future_single_pass_candidate": ("prototype_single_taichi_composite_pass", "HybridRenderController.apply_layer_render_plan_composition"),
            "unknown": ("collect_more_runtime_phase_timing", "render_core.render_plan.build_layer_render_plan_phase_timing_runtime_packet"),
        }

        for phase_id, (action, target_helper) in cases.items():
            with self.subTest(phase_id=phase_id):
                packet = build_layer_render_plan_bottleneck_recommendation(
                    {
                        "schema": "rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1",
                        "runtime_measurements_available": True,
                        "slowest_phase_id": phase_id,
                        "slowest_phase_ms": 12.345,
                        "total_ms": 45.678,
                        "slow_frame": True,
                    }
                )
                self.assertEqual(set(packet.keys()), BOTTLENECK_RECOMMENDATION_KEYS)
                self.assertEqual(packet["status"], "ready")
                self.assertEqual(packet["recommended_next_action"], action)
                self.assertEqual(packet["target_helper"], target_helper)
                self.assertFalse(packet["runtime_optimization_applied"])

    def test_bottleneck_recommendation_waits_without_measurements(self):
        packet = build_layer_render_plan_bottleneck_recommendation({})

        self.assertEqual(packet["status"], "waiting_for_runtime_metadata")
        self.assertEqual(packet["slowest_phase_id"], "unavailable")
        self.assertEqual(packet["recommended_next_action"], "collect_more_runtime_phase_timing")
        self.assertFalse(packet["runtime_optimization_applied"])

    def test_phase_timing_runtime_packet_empty_and_slow_threshold(self):
        packet = build_layer_render_plan_phase_timing_runtime_packet({}, 2, 33.3)

        self.assertEqual(set(packet.keys()), PHASE_TIMING_RUNTIME_KEYS)
        self.assertEqual(packet["status"], "unavailable")
        self.assertFalse(packet["runtime_measurements_available"])
        self.assertEqual(packet["phase_timing_ms"], {})
        self.assertEqual(packet["measured_phase_ids"], [])
        self.assertIsNone(packet["slowest_phase_id"])
        self.assertEqual(packet["slowest_phase_ms"], 0.0)
        self.assertFalse(packet["slow_frame"])
        self.assertEqual(packet["slow_frame_threshold_ms"], 33.3)
        self.assertEqual(packet["bottleneck_recommendation"]["status"], "waiting_for_runtime_metadata")

    def test_phase_timing_runtime_packet_rounding_order_and_bottleneck(self):
        packet = build_layer_render_plan_phase_timing_runtime_packet(
            {"prepare_batches": 5.5555, "compose_overlays": 12.3456, 3: 99.9},
            4,
            40.4444,
        )

        self.assertEqual(packet["status"], "measured")
        self.assertTrue(packet["runtime_measurements_available"])
        self.assertEqual(packet["total_ms"], 40.444)
        self.assertEqual(packet["phase_timing_ms"], {"prepare_batches": 5.556, "compose_overlays": 12.346})
        self.assertEqual(packet["measured_phase_ids"], ["prepare_batches", "compose_overlays"])
        self.assertEqual(packet["slowest_phase_id"], "compose_overlays")
        self.assertEqual(packet["slowest_phase_ms"], 12.346)
        self.assertTrue(packet["slow_frame"])
        self.assertEqual(packet["bottleneck_recommendation_schema"], "rrkal_displaytools.layer_render_plan_bottleneck_recommendation.v1")
        self.assertEqual(packet["bottleneck_recommendation"]["recommended_next_action"], "collapse_overlay_composition_passes")
        self.assertFalse(packet["bottleneck_recommendation"]["runtime_optimization_applied"])

    def test_phase_timing_runtime_packet_is_deterministic(self):
        timings = {"prepare_batches": 1.2, "postprocess": 0.5}

        self.assertEqual(
            build_layer_render_plan_phase_timing_runtime_packet(timings, 1, 10.0),
            build_layer_render_plan_phase_timing_runtime_packet(dict(timings), 1, 10.0),
        )


if __name__ == "__main__":
    unittest.main()
