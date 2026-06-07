import unittest

from render_core.render_plan import (
    build_layer_render_plan_adapter_boundary_contract,
    build_layer_render_plan_adapter_payload,
    build_layer_render_plan_adapter_payload_contract,
    build_layer_render_plan_adapter_payload_summary,
    build_layer_render_plan_compile_input,
    build_layer_render_plan_single_pass_preflight_contract,
)


SINGLE_PASS_PREFLIGHT_KEYS = {
    "schema",
    "source",
    "status",
    "runtime_single_pass_enabled",
    "runtime_path_unchanged",
    "merge_candidate_run_count",
    "candidate_run_ids",
    "single_pass_candidate_count",
    "runtime_measurements_available",
    "required_before_enable",
    "parity_gate",
    "timing_gate",
    "review_gate",
    "next_runtime_step",
}

ADAPTER_BOUNDARY_KEYS = {
    "schema",
    "source",
    "status",
    "runtime_path_unchanged",
    "controller_owned_inputs",
    "core_owned_decisions",
    "forbidden_in_render_core",
    "adapter_payload_fields",
    "visible_layer_count",
    "dirty_flag_count",
    "composition_step_count",
    "next_extraction_target",
}

ADAPTER_PAYLOAD_SUMMARY_KEYS = {
    "schema",
    "source",
    "status",
    "runtime_path_unchanged",
    "payload_boundary",
    "visible_layer_ids",
    "dirty_flag_ids",
    "composition_step_ids",
    "compose_queue_ids",
    "skipped_step_ids",
    "compose_run_ids",
    "visible_layer_count",
    "dirty_flag_count",
    "composition_step_count",
    "compose_queue_count",
    "skipped_step_count",
    "compose_run_count",
    "next_extraction_target",
}

ADAPTER_PAYLOAD_KEYS = {
    "schema",
    "source",
    "status",
    "contract_role",
    "runtime_path_unchanged",
    "payload_boundary",
    "summary_schema",
    "summary",
    "cache_key",
    "invalidation_reasons",
    "invalidation_scope",
    "batch_decisions",
    "apply_path",
    "execution_summary",
    "execution_phases",
    "phase_timing_contract",
    "phase_timing_runtime",
    "bottleneck_recommendation",
    "runtime_snapshot",
    "composition_steps",
    "compose_queue_packet",
    "next_extraction_target",
}

COMPILE_INPUT_KEYS = {
    "schema",
    "source",
    "status",
    "runtime_path_unchanged",
    "composition_steps",
    "runtime_snapshot",
    "compose_queue_packet",
    "style_profile",
    "boundary_layer_ids",
    "layer_opacity",
    "layer_blend",
    "phase_timing_runtime",
    "cached_plan_available",
    "previous_cache_key",
    "frame_index",
    "boundary",
}

ADAPTER_PAYLOAD_CONTRACT_KEYS = {
    "schema",
    "source",
    "status",
    "required_field_count",
    "present_field_count",
    "missing_field_count",
    "required_fields",
    "missing_fields",
    "payload_schema",
    "payload_status",
    "payload_contract_role",
    "payload_boundary",
    "runtime_path_unchanged",
    "next_extraction_gate",
}

COVERED_HELPERS = {
    "build_layer_render_plan_single_pass_preflight_contract",
    "build_layer_render_plan_adapter_boundary_contract",
    "build_layer_render_plan_adapter_payload_summary",
    "build_layer_render_plan_adapter_payload",
    "build_layer_render_plan_compile_input",
    "build_layer_render_plan_adapter_payload_contract",
}

EXCLUDED_HELPERS = {
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
    "_payload_list",
    "_payload_dict",
    "build_compiled_layer_render_plan_packet_from_adapter_payload",
    "build_reused_compiled_layer_render_plan_packet_from_adapter_payload",
    "build_compiled_layer_render_plan_packet",
    "build_reused_compiled_layer_render_plan_packet",
    "build_layer_render_plan_batch_decisions",
}


class LayerRenderPlanAdapterPreflightTests(unittest.TestCase):
    def _runtime_snapshot(self):
        return {
            "frame_index": 7,
            "visible_layers": ["lakes", "rivers"],
            "dirty_flags": {"rivers": True, "lakes": False},
        }

    def _composition_steps(self):
        return [
            {"id": "lakes", "kind": "runtime_blend"},
            {"layer_id": "rivers", "kind": "runtime_blend"},
        ]

    def _compose_queue_packet(self):
        return {
            "queue": [{"id": "lakes"}, {"layer_id": "rivers"}],
            "skipped_steps": [{"id": "hidden_roads"}],
            "compose_runs": [{"id": "run_0"}, {"id": "run_1"}],
        }

    def _adapter_payload(self):
        return build_layer_render_plan_adapter_payload(
            self._runtime_snapshot(),
            self._composition_steps(),
            self._compose_queue_packet(),
            "cache-key-1",
            ["cache_key_changed"],
            [{"scope": "plan"}],
            [{"id": "lakes", "decision": "reuse_batch"}],
            [{"id": "lakes", "apply_helper": "compose_runtime_blend"}],
            {"single_pass_candidate_count": 1},
            [{"id": "prepare_batches"}],
            {"schema": "phase-contract"},
            {"runtime_measurements_available": False},
            {"recommended_next_action": "collect_more_runtime_phase_timing"},
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

    def test_single_pass_preflight_empty_input(self):
        packet = build_layer_render_plan_single_pass_preflight_contract([], {}, {})

        self.assertEqual(set(packet), SINGLE_PASS_PREFLIGHT_KEYS)
        self.assertEqual(packet["status"], "no_candidates")
        self.assertFalse(packet["runtime_single_pass_enabled"])
        self.assertTrue(packet["runtime_path_unchanged"])
        self.assertEqual(packet["merge_candidate_run_count"], 0)
        self.assertEqual(packet["candidate_run_ids"], [])
        self.assertEqual(packet["single_pass_candidate_count"], 0)
        self.assertFalse(packet["runtime_measurements_available"])

    def test_single_pass_preflight_candidates_and_blockers(self):
        compose_runs = [
            {"id": "merge_run", "merge_safe": True},
            {"id": "blocked_run", "merge_safe": False},
        ]
        execution_summary = {"single_pass_candidate_count": "2"}
        phase_timing_runtime = {"runtime_measurements_available": True}

        packet = build_layer_render_plan_single_pass_preflight_contract(
            compose_runs,
            execution_summary,
            phase_timing_runtime,
        )

        self.assertEqual(set(packet), SINGLE_PASS_PREFLIGHT_KEYS)
        self.assertEqual(packet["status"], "ready_for_parity_smoke")
        self.assertFalse(packet["runtime_single_pass_enabled"])
        self.assertEqual(packet["merge_candidate_run_count"], 1)
        self.assertEqual(packet["candidate_run_ids"], ["merge_run"])
        self.assertEqual(packet["single_pass_candidate_count"], 2)
        self.assertTrue(packet["runtime_measurements_available"])

    def test_single_pass_preflight_deterministic_repeat_call(self):
        args = ([{"id": "run", "merge_safe": True}], {"single_pass_candidate_count": 1}, {})

        self.assertEqual(
            build_layer_render_plan_single_pass_preflight_contract(*args),
            build_layer_render_plan_single_pass_preflight_contract(list(args[0]), dict(args[1]), dict(args[2])),
        )

    def test_adapter_boundary_contract_schema_fields_and_forbidden_boundary(self):
        packet = build_layer_render_plan_adapter_boundary_contract(
            self._runtime_snapshot(),
            self._composition_steps(),
        )

        self.assertEqual(set(packet), ADAPTER_BOUNDARY_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_adapter_boundary.v1")
        self.assertEqual(packet["source"], "render_core.render_plan.build_layer_render_plan_adapter_boundary_contract")
        self.assertEqual(packet["status"], "documented_boundary")
        self.assertTrue(packet["runtime_path_unchanged"])
        self.assertIn("runtime_snapshot", packet["adapter_payload_fields"])
        self.assertIn("step_runtime_states", packet["controller_owned_inputs"])
        self.assertIn("execution_summary", packet["core_owned_decisions"])
        self.assertIn("metadata file writes", packet["forbidden_in_render_core"])
        self.assertIn("np.ndarray overlay object ownership", packet["forbidden_in_render_core"])
        self.assertEqual(packet["visible_layer_count"], 2)
        self.assertEqual(packet["dirty_flag_count"], 2)
        self.assertEqual(packet["composition_step_count"], 2)

    def test_adapter_payload_summary_empty_and_populated_inputs(self):
        empty_packet = build_layer_render_plan_adapter_payload_summary({}, [], {})

        self.assertEqual(set(empty_packet), ADAPTER_PAYLOAD_SUMMARY_KEYS)
        self.assertEqual(empty_packet["status"], "normalized_summary")
        self.assertEqual(empty_packet["visible_layer_count"], 0)
        self.assertEqual(empty_packet["compose_queue_count"], 0)

        packet = build_layer_render_plan_adapter_payload_summary(
            self._runtime_snapshot(),
            self._composition_steps(),
            self._compose_queue_packet(),
        )

        self.assertEqual(set(packet), ADAPTER_PAYLOAD_SUMMARY_KEYS)
        self.assertEqual(packet["visible_layer_ids"], ["lakes", "rivers"])
        self.assertEqual(packet["dirty_flag_ids"], ["lakes", "rivers"])
        self.assertEqual(packet["composition_step_ids"], ["lakes", "rivers"])
        self.assertEqual(packet["compose_queue_ids"], ["lakes", "rivers"])
        self.assertEqual(packet["skipped_step_ids"], ["hidden_roads"])
        self.assertEqual(packet["compose_run_ids"], ["run_0", "run_1"])
        self.assertEqual(packet["payload_boundary"], "serializable_summary_only_no_overlay_arrays")

    def test_adapter_payload_minimal_synthetic_inputs_are_data_only(self):
        runtime_snapshot = self._runtime_snapshot()
        composition_steps = self._composition_steps()
        compose_queue_packet = self._compose_queue_packet()
        apply_path = [{"id": "lakes", "current_runtime_path": "HybridRenderController.apply_layer_render_plan_composition"}]

        packet = build_layer_render_plan_adapter_payload(
            runtime_snapshot,
            composition_steps,
            compose_queue_packet,
            "cache-key-1",
            ["cache_key_changed"],
            [{"scope": "plan"}],
            [{"id": "lakes", "decision": "reuse_batch"}],
            apply_path,
            {"single_pass_candidate_count": 1},
            [{"id": "prepare_batches"}],
            {"schema": "phase-contract"},
            {"runtime_measurements_available": False},
            {"recommended_next_action": "collect_more_runtime_phase_timing"},
        )

        self.assertEqual(set(packet), ADAPTER_PAYLOAD_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_adapter_payload.v1")
        self.assertEqual(packet["status"], "normalized_payload")
        self.assertTrue(packet["runtime_path_unchanged"])
        self.assertEqual(packet["payload_boundary"], "serializable_controller_to_core_payload_no_overlay_arrays")
        self.assertIs(packet["runtime_snapshot"], runtime_snapshot)
        self.assertIs(packet["composition_steps"], composition_steps)
        self.assertIs(packet["compose_queue_packet"], compose_queue_packet)
        self.assertIs(packet["apply_path"], apply_path)
        self.assertEqual(packet["summary_schema"], "rrkal_displaytools.layer_render_plan_adapter_payload_summary.v1")

    def test_compile_input_minimal_synthetic_payload_and_determinism(self):
        kwargs = {
            "composition_steps": self._composition_steps(),
            "runtime_snapshot": self._runtime_snapshot(),
            "compose_queue_packet": self._compose_queue_packet(),
            "style_profile": {"name": "default"},
            "boundary_layer_ids": ["borders"],
            "layer_opacity": {"lakes": 0.5},
            "layer_blend": {"lakes": "Normal"},
            "phase_timing_runtime": {"runtime_measurements_available": False},
            "cached_plan_available": 1,
            "previous_cache_key": "old-key",
            "frame_index": "3",
        }

        packet = build_layer_render_plan_compile_input(**kwargs)

        self.assertEqual(set(packet), COMPILE_INPUT_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_compile_input.v1")
        self.assertEqual(packet["status"], "packaged")
        self.assertTrue(packet["cached_plan_available"])
        self.assertEqual(packet["frame_index"], 3)
        self.assertIn("no cache decision", packet["boundary"])
        self.assertEqual(packet, build_layer_render_plan_compile_input(**dict(kwargs)))

    def test_adapter_payload_contract_incomplete_and_ready(self):
        incomplete = build_layer_render_plan_adapter_payload_contract({})

        self.assertEqual(set(incomplete), ADAPTER_PAYLOAD_CONTRACT_KEYS)
        self.assertEqual(incomplete["status"], "incomplete")
        self.assertEqual(incomplete["present_field_count"], 0)
        self.assertEqual(incomplete["missing_field_count"], incomplete["required_field_count"])
        self.assertEqual(incomplete["payload_schema"], "unavailable")
        self.assertFalse(incomplete["runtime_path_unchanged"])

        payload = self._adapter_payload()
        packet = build_layer_render_plan_adapter_payload_contract(payload)

        self.assertEqual(set(packet), ADAPTER_PAYLOAD_CONTRACT_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_adapter_payload_contract.v1")
        self.assertEqual(packet["source"], "render_core.render_plan.build_layer_render_plan_adapter_payload_contract")
        self.assertEqual(packet["status"], "ready")
        self.assertEqual(packet["missing_fields"], [])
        self.assertEqual(packet["payload_schema"], "rrkal_displaytools.layer_render_plan_adapter_payload.v1")
        self.assertEqual(packet["payload_contract_role"], "primary_payload_contract")
        self.assertEqual(packet["payload_boundary"], "serializable_controller_to_core_payload_no_overlay_arrays")
        self.assertTrue(packet["runtime_path_unchanged"])

    def test_bundle_outputs_are_dict_list_scalar_packets_without_controller_instance(self):
        packets = [
            build_layer_render_plan_single_pass_preflight_contract([], {}, {}),
            build_layer_render_plan_adapter_boundary_contract(self._runtime_snapshot(), self._composition_steps()),
            build_layer_render_plan_adapter_payload_summary(self._runtime_snapshot(), self._composition_steps(), self._compose_queue_packet()),
            self._adapter_payload(),
            build_layer_render_plan_compile_input(
                composition_steps=[],
                runtime_snapshot={},
                compose_queue_packet={},
                style_profile="default",
                boundary_layer_ids=[],
                layer_opacity={},
                layer_blend={},
                phase_timing_runtime={},
                cached_plan_available=False,
                previous_cache_key=None,
                frame_index=0,
            ),
            build_layer_render_plan_adapter_payload_contract(self._adapter_payload()),
        ]

        for packet in packets:
            with self.subTest(schema=packet.get("schema")):
                self.assertIsInstance(packet, dict)
                self.assert_packet_scalars_only(packet)

    def test_gate_excludes_compiled_reused_alpha_apply_path_and_batch_helpers(self):
        self.assertFalse(COVERED_HELPERS.intersection(EXCLUDED_HELPERS))


if __name__ == "__main__":
    unittest.main()
