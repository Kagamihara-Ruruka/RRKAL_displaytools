import unittest

from render_core.render_plan import (
    build_compiled_layer_render_plan_packet,
    build_compiled_layer_render_plan_packet_from_adapter_payload,
    build_reused_compiled_layer_render_plan_packet,
    build_reused_compiled_layer_render_plan_packet_from_adapter_payload,
)


COMPILED_PACKET_KEYS = {
    "schema",
    "source",
    "status",
    "cache_status",
    "cache_reuse_decision",
    "cache_key",
    "cache_invalidation_reasons",
    "cache_invalidation_reason_schema",
    "cache_invalidation_scope",
    "cache_invalidation_scope_schema",
    "batch_decisions",
    "batch_decision_schema",
    "batch_decision_count",
    "apply_path",
    "apply_path_schema",
    "apply_path_count",
    "execution_summary",
    "execution_summary_schema",
    "execution_phases",
    "execution_phases_schema",
    "execution_phase_count",
    "phase_timing_contract",
    "phase_timing_contract_schema",
    "phase_timing_runtime",
    "phase_timing_runtime_schema",
    "bottleneck_recommendation",
    "bottleneck_recommendation_schema",
    "single_pass_preflight_contract",
    "single_pass_preflight_contract_schema",
    "adapter_boundary_contract",
    "adapter_boundary_contract_schema",
    "adapter_payload",
    "adapter_payload_schema",
    "adapter_payload_contract",
    "adapter_payload_contract_schema",
    "adapter_payload_summary",
    "adapter_payload_summary_schema",
    "reuse_policy",
    "reuse_status_values",
    "runtime_optimization_applied",
    "optimization_target",
    "frame_index",
    "runtime_snapshot",
    "dirty_flags",
    "batch_targets",
    "composition_steps",
    "composition_step_count",
    "compose_queue",
    "compose_queue_schema",
    "compose_queue_packet",
    "compose_queue_count",
    "compose_queue_skipped_count",
    "compose_runs",
    "compose_runs_schema",
    "compose_run_count",
    "compose_merge_candidate_run_count",
    "compose_run_parity_contract",
    "compose_run_parity_contract_schema",
    "compose_order",
    "apply_helper",
    "single_pass_ready",
    "reuse_boundary",
}

REUSED_EXTRA_KEYS = {
    "cached_only_marker",
}

TARGET_HELPERS = {
    "build_compiled_layer_render_plan_packet_from_adapter_payload",
    "build_reused_compiled_layer_render_plan_packet_from_adapter_payload",
    "build_compiled_layer_render_plan_packet",
    "build_reused_compiled_layer_render_plan_packet",
}

EXCLUDED_HELPERS = {
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
    "build_layer_render_plan_batch_decisions",
}


class LayerRenderPlanCompiledReusedPacketTests(unittest.TestCase):
    def _runtime_snapshot(self):
        return {
            "frame_index": 5,
            "dirty_flags": {"lakes": True},
            "batch_targets": [{"id": "globe_material"}],
            "compose_order": ["globe_rgba", "lakes"],
        }

    def _composition_steps(self):
        return [{"id": "lakes", "kind": "runtime_blend"}]

    def _compose_queue_packet(self):
        return {
            "queue": [{"id": "lakes"}],
            "executable_step_count": 1,
            "skipped_step_count": 0,
            "compose_runs": [{"id": "run_0", "merge_safe": True}],
            "compose_run_count": 1,
            "compose_merge_candidate_run_count": 1,
            "compose_run_parity_contract": {"status": "blocked_until_visual_review"},
        }

    def _batch_decisions(self):
        return [{"id": "lakes", "scope": "layer", "decision": "compose_cached_overlay"}]

    def _apply_path(self):
        return [
            {
                "id": "lakes",
                "apply_helper": "compose_runtime_blend",
                "current_runtime_path": "HybridRenderController.apply_layer_render_plan_composition",
            }
        ]

    def _execution_summary(self):
        return {"single_pass_candidate_count": 1, "single_pass_blockers": []}

    def _execution_phases(self):
        return [{"id": "prepare_batches"}, {"id": "compose_overlays"}]

    def _phase_timing_contract(self):
        return {"schema": "phase-contract", "runtime_measurements_available": False}

    def _phase_timing_runtime(self):
        return {"schema": "phase-runtime", "runtime_measurements_available": False}

    def _bottleneck_recommendation(self):
        return {"recommended_next_action": "collect_more_runtime_phase_timing"}

    def _adapter_payload(self):
        return {
            "schema": "rrkal_displaytools.layer_render_plan_adapter_payload.v1",
            "status": "normalized_payload",
            "contract_role": "primary_payload_contract",
            "payload_boundary": "serializable_controller_to_core_payload_no_overlay_arrays",
            "runtime_path_unchanged": True,
            "cache_key": "cache-key-1",
            "runtime_snapshot": self._runtime_snapshot(),
            "composition_steps": self._composition_steps(),
            "compose_queue_packet": self._compose_queue_packet(),
            "invalidation_reasons": ["cache_key_changed"],
            "invalidation_scope": [{"scope": "plan"}],
            "batch_decisions": self._batch_decisions(),
            "apply_path": self._apply_path(),
            "execution_summary": self._execution_summary(),
            "execution_phases": self._execution_phases(),
            "phase_timing_contract": self._phase_timing_contract(),
            "phase_timing_runtime": self._phase_timing_runtime(),
            "bottleneck_recommendation": self._bottleneck_recommendation(),
            "summary": {"status": "normalized_summary", "compose_queue_count": 1},
        }

    def _compiled_packet(self):
        return build_compiled_layer_render_plan_packet(
            "cache-key-1",
            ["cache_key_changed"],
            [{"scope": "plan"}],
            self._batch_decisions(),
            self._apply_path(),
            self._execution_summary(),
            self._execution_phases(),
            self._phase_timing_contract(),
            self._phase_timing_runtime(),
            self._bottleneck_recommendation(),
            5,
            self._runtime_snapshot(),
            self._composition_steps(),
            self._compose_queue_packet(),
            self._adapter_payload(),
            source="unit-test-source",
        )

    def assert_packet_scalars_only(self, value):
        if isinstance(value, dict):
            for key, item in value.items():
                self.assertIsInstance(key, str)
                self.assert_packet_scalars_only(item)
        elif isinstance(value, list):
            for item in value:
                self.assert_packet_scalars_only(item)
        else:
            self.assertIsInstance(value, (str, int, float, bool, type(None)))

    def test_compiled_packet_direct_builder_key_set_and_cache_miss_status(self):
        packet = self._compiled_packet()

        self.assertEqual(set(packet), COMPILED_PACKET_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.compiled_layer_render_plan.v1")
        self.assertEqual(packet["source"], "unit-test-source")
        self.assertEqual(packet["status"], "compiled_snapshot")
        self.assertEqual(packet["cache_status"], "compiled")
        self.assertEqual(packet["cache_reuse_decision"], "compiled")
        self.assertFalse(packet["runtime_optimization_applied"])
        self.assertFalse(packet["single_pass_ready"])
        self.assertEqual(packet["reuse_status_values"], ["compiled", "reused"])
        self.assertEqual(packet["reuse_boundary"], "valid_until_dirty_flags_or_camera_change")

    def test_compiled_packet_direct_builder_passthrough_fields(self):
        adapter_payload = self._adapter_payload()
        apply_path = adapter_payload["apply_path"]
        packet = build_compiled_layer_render_plan_packet(
            adapter_payload["cache_key"],
            adapter_payload["invalidation_reasons"],
            adapter_payload["invalidation_scope"],
            adapter_payload["batch_decisions"],
            apply_path,
            adapter_payload["execution_summary"],
            adapter_payload["execution_phases"],
            adapter_payload["phase_timing_contract"],
            adapter_payload["phase_timing_runtime"],
            adapter_payload["bottleneck_recommendation"],
            5,
            adapter_payload["runtime_snapshot"],
            adapter_payload["composition_steps"],
            adapter_payload["compose_queue_packet"],
            adapter_payload,
            source="unit-test-source",
        )

        self.assertIs(packet["adapter_payload"], adapter_payload)
        self.assertIs(packet["adapter_payload_summary"], adapter_payload["summary"])
        self.assertIs(packet["apply_path"], apply_path)
        self.assertEqual(packet["apply_path_count"], 1)
        self.assertEqual(packet["batch_decision_count"], 1)
        self.assertEqual(packet["execution_phase_count"], 2)
        self.assertEqual(packet["compose_queue_count"], 1)
        self.assertEqual(packet["compose_queue_skipped_count"], 0)
        self.assertEqual(packet["compose_run_count"], 1)
        self.assertEqual(packet["compose_merge_candidate_run_count"], 1)

    def test_compiled_packet_from_adapter_payload(self):
        adapter_payload = self._adapter_payload()
        packet = build_compiled_layer_render_plan_packet_from_adapter_payload(
            adapter_payload,
            9,
            source="from-adapter-source",
        )

        self.assertEqual(set(packet), COMPILED_PACKET_KEYS)
        self.assertEqual(packet["source"], "from-adapter-source")
        self.assertEqual(packet["frame_index"], 9)
        self.assertEqual(packet["cache_key"], "cache-key-1")
        self.assertIs(packet["adapter_payload"], adapter_payload)
        self.assertEqual(packet["cache_status"], "compiled")

    def test_reused_packet_direct_builder_preserves_cached_fields_and_overrides_runtime_fields(self):
        cached_plan = dict(self._compiled_packet())
        cached_plan["cached_only_marker"] = "preserved"
        cached_plan["execution_phases_schema"] = "custom-phase-schema"

        packet = build_reused_compiled_layer_render_plan_packet(
            cached_plan,
            ["cache_key_match"],
            [{"scope": "reuse"}],
            [],
            [],
            {"single_pass_candidate_count": 0},
            [],
            {},
            {},
            {},
            12,
            self._runtime_snapshot(),
            self._compose_queue_packet(),
            self._adapter_payload(),
        )

        self.assertEqual(set(packet), COMPILED_PACKET_KEYS | REUSED_EXTRA_KEYS)
        self.assertEqual(packet["cached_only_marker"], "preserved")
        self.assertEqual(packet["cache_status"], "reused")
        self.assertEqual(packet["cache_reuse_decision"], "reused")
        self.assertEqual(packet["cache_invalidation_reasons"], ["cache_key_match"])
        self.assertEqual(packet["cache_invalidation_scope"], [{"scope": "reuse"}])
        self.assertEqual(packet["batch_decision_count"], 0)
        self.assertEqual(packet["apply_path_count"], 0)
        self.assertEqual(packet["execution_phase_count"], 0)
        self.assertEqual(packet["execution_phases_schema"], "custom-phase-schema")
        self.assertEqual(packet["frame_index"], 12)
        self.assertFalse(packet["single_pass_preflight_contract"]["runtime_single_pass_enabled"])

    def test_reused_packet_from_adapter_payload(self):
        cached_plan = self._compiled_packet()
        adapter_payload = self._adapter_payload()

        packet = build_reused_compiled_layer_render_plan_packet_from_adapter_payload(
            cached_plan,
            adapter_payload,
            13,
        )

        self.assertEqual(set(packet), COMPILED_PACKET_KEYS)
        self.assertEqual(packet["cache_status"], "reused")
        self.assertEqual(packet["cache_reuse_decision"], "reused")
        self.assertEqual(packet["frame_index"], 13)
        self.assertIs(packet["adapter_payload"], adapter_payload)
        self.assertEqual(packet["cache_invalidation_reasons"], ["cache_key_changed"])

    def test_deterministic_repeat_calls(self):
        adapter_payload = self._adapter_payload()

        self.assertEqual(
            build_compiled_layer_render_plan_packet_from_adapter_payload(adapter_payload, 1, source="source-a"),
            build_compiled_layer_render_plan_packet_from_adapter_payload(dict(adapter_payload), 1, source="source-a"),
        )
        self.assertEqual(
            build_reused_compiled_layer_render_plan_packet_from_adapter_payload(self._compiled_packet(), adapter_payload, 2),
            build_reused_compiled_layer_render_plan_packet_from_adapter_payload(dict(self._compiled_packet()), dict(adapter_payload), 2),
        )

    def test_packets_are_dict_list_scalar_outputs_for_synthetic_inputs(self):
        packets = [
            self._compiled_packet(),
            build_compiled_layer_render_plan_packet_from_adapter_payload(self._adapter_payload(), 1, source="source-a"),
            build_reused_compiled_layer_render_plan_packet(self._compiled_packet(), [], [], [], [], {}, [], {}, {}, {}, 2, {}, {}, self._adapter_payload()),
            build_reused_compiled_layer_render_plan_packet_from_adapter_payload(self._compiled_packet(), self._adapter_payload(), 3),
        ]

        for packet in packets:
            with self.subTest(cache_status=packet.get("cache_status")):
                self.assertIsInstance(packet, dict)
                self.assert_packet_scalars_only(packet)

    def test_gate_excludes_alpha_apply_path_and_batch_decision_helpers(self):
        self.assertFalse(TARGET_HELPERS.intersection(EXCLUDED_HELPERS))


if __name__ == "__main__":
    unittest.main()
