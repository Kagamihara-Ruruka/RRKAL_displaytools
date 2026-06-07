import unittest

from render_core.render_plan import (
    build_layer_render_plan_compose_queue_entries,
    build_layer_render_plan_compose_queue_packet_from_states,
    build_layer_render_plan_step_runtime_state,
)


class LayerRenderPlanComposeQueueFixtureTests(unittest.TestCase):
    def test_step_runtime_state_branches_are_pinned(self):
        self.assertEqual(
            build_layer_render_plan_step_runtime_state(0, "bad-step"),
            {"source_order": 0, "malformed": True},
        )
        self.assertEqual(
            build_layer_render_plan_step_runtime_state(
                1,
                {"id": "hidden", "kind": "alpha_compose"},
                visible=False,
            ),
            {"source_order": 1, "kind": "alpha_compose", "visible": False},
        )
        self.assertEqual(
            build_layer_render_plan_step_runtime_state(
                2,
                {"id": "missing", "kind": "runtime_overlay"},
                visible=True,
                overlay_present=False,
            ),
            {
                "source_order": 2,
                "kind": "runtime_overlay",
                "visible": True,
                "overlay_present": False,
            },
        )
        self.assertEqual(
            build_layer_render_plan_step_runtime_state(
                3,
                {"id": "transparent", "kind": "alpha_blend"},
                visible=True,
                overlay_present=True,
                overlay_transparent=True,
            ),
            {
                "source_order": 3,
                "kind": "alpha_blend",
                "visible": True,
                "overlay_present": True,
                "overlay_transparent": True,
            },
        )
        self.assertEqual(
            build_layer_render_plan_step_runtime_state(
                4,
                {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
                visible=False,
                overlay_present=False,
                overlay_transparent=True,
            ),
            {"source_order": 4, "kind": "style_profile_postprocess"},
        )

    def test_queue_entries_skip_reasons_and_order_are_pinned(self):
        steps = [
            "bad-step",
            {"id": "hidden", "kind": "alpha_compose"},
            {"id": "missing", "kind": "runtime_overlay", "layer_id": "aircraft"},
            {"id": "transparent", "kind": "alpha_blend", "blend_mode": "Screen"},
            {"id": "ais_overlay", "kind": "alpha_compose"},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
        ]
        states = [
            build_layer_render_plan_step_runtime_state(0, steps[0]),
            build_layer_render_plan_step_runtime_state(1, steps[1], visible=False),
            build_layer_render_plan_step_runtime_state(2, steps[2], visible=True, overlay_present=False),
            build_layer_render_plan_step_runtime_state(
                3,
                steps[3],
                visible=True,
                overlay_present=True,
                overlay_transparent=True,
            ),
            build_layer_render_plan_step_runtime_state(
                4,
                steps[4],
                visible=True,
                overlay_present=True,
                overlay_transparent=False,
            ),
            build_layer_render_plan_step_runtime_state(5, steps[5]),
        ]

        queue, skipped = build_layer_render_plan_compose_queue_entries(steps, states)

        self.assertEqual(
            skipped,
            [
                {"source_order": 0, "id": "unknown_step", "reason": "malformed_step"},
                {"source_order": 1, "id": "hidden", "kind": "alpha_compose", "reason": "hidden_layer"},
                {"source_order": 2, "id": "missing", "kind": "runtime_overlay", "reason": "missing_overlay"},
                {"source_order": 3, "id": "transparent", "kind": "alpha_blend", "reason": "transparent_overlay"},
            ],
        )
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue[0]["id"], "ais_overlay")
        self.assertEqual(queue[0]["source_order"], 4)
        self.assertEqual(queue[0]["queue_order"], 0)
        self.assertEqual(queue[0]["compose_queue_reason"], "executable_overlay")
        self.assertEqual(queue[1]["id"], "style_profile_postprocess")
        self.assertEqual(queue[1]["source_order"], 5)
        self.assertEqual(queue[1]["queue_order"], 1)
        self.assertEqual(queue[1]["compose_queue_reason"], "postprocess_required")

    def test_packet_schema_key_set_and_embedded_contracts_are_pinned(self):
        steps = [
            {"id": "ais_overlay", "kind": "alpha_compose"},
            {"id": "pins", "kind": "alpha_compose"},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
        ]
        states = [
            build_layer_render_plan_step_runtime_state(0, steps[0], overlay_present=True),
            build_layer_render_plan_step_runtime_state(1, steps[1], overlay_present=True),
            build_layer_render_plan_step_runtime_state(2, steps[2]),
        ]

        packet = build_layer_render_plan_compose_queue_packet_from_states(
            steps,
            states,
            source="test.layer_render_plan_compose_queue",
        )

        self.assertEqual(
            set(packet),
            {
                "schema",
                "source",
                "status",
                "optimization_applied",
                "optimization",
                "input_step_count",
                "executable_step_count",
                "skipped_step_count",
                "queue",
                "skipped_steps",
                "compose_runs_schema",
                "compose_runs",
                "compose_run_count",
                "compose_merge_candidate_run_count",
                "compose_run_parity_contract_schema",
                "compose_run_parity_contract",
                "next_optimization_target",
            },
        )
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_compose_queue.v1")
        self.assertEqual(packet["source"], "test.layer_render_plan_compose_queue")
        self.assertEqual(packet["input_step_count"], 3)
        self.assertEqual(packet["executable_step_count"], 3)
        self.assertEqual(packet["skipped_step_count"], 0)
        self.assertEqual(packet["compose_runs_schema"], "rrkal_displaytools.layer_render_plan_compose_runs.v1")
        self.assertEqual(packet["compose_run_count"], 2)
        self.assertEqual(packet["compose_merge_candidate_run_count"], 1)
        self.assertEqual(packet["compose_run_parity_contract_schema"], "rrkal_displaytools.layer_render_plan_compose_run_parity_contract.v1")

        self.assertEqual(packet["queue"][0]["source_order"], 0)
        self.assertEqual(packet["queue"][0]["queue_order"], 0)
        self.assertEqual(packet["queue"][1]["source_order"], 1)
        self.assertEqual(packet["queue"][1]["queue_order"], 1)
        self.assertEqual(packet["queue"][2]["source_order"], 2)
        self.assertEqual(packet["queue"][2]["queue_order"], 2)

        compose_runs = packet["compose_runs"]
        self.assertEqual(compose_runs[0]["run_kind"], "alpha_compose_overlays")
        self.assertEqual(compose_runs[0]["merge_safe"], True)
        self.assertEqual(compose_runs[0]["step_ids"], ["ais_overlay", "pins"])
        self.assertEqual(compose_runs[0]["start_queue_order"], 0)
        self.assertEqual(compose_runs[0]["end_queue_order"], 1)
        self.assertEqual(compose_runs[1]["run_kind"], "postprocess")
        self.assertEqual(compose_runs[1]["merge_safe"], False)

        contract = packet["compose_run_parity_contract"]
        self.assertEqual(contract["schema"], "rrkal_displaytools.layer_render_plan_compose_run_parity_contract.v1")
        self.assertEqual(contract["status"], "required_before_runtime_merge")
        self.assertEqual(contract["runtime_merge_enabled"], False)
        self.assertEqual(contract["merge_candidate_run_count"], 1)
        self.assertEqual(contract["candidate_run_ids"], ["compose_run_0"])
        self.assertEqual(contract["tolerance"], {"max_abs_diff": 0, "changed_pixel_count": 0})

    def test_contract_fields_do_not_report_pixel_equivalence_or_runtime_merge(self):
        steps = [{"id": "ais_overlay", "kind": "alpha_compose"}]
        states = [build_layer_render_plan_step_runtime_state(0, steps[0], overlay_present=True)]

        packet = build_layer_render_plan_compose_queue_packet_from_states(steps, states)
        contract = packet["compose_run_parity_contract"]

        self.assertIs(contract["runtime_merge_enabled"], False)
        self.assertNotIn("passed", contract)
        self.assertNotIn("visual_parity_passed", contract)
        self.assertNotIn("precommit_gate_passed", contract)
        self.assertEqual(contract["parity_smoke_default_mode"], "contract_only_until_artifacts_then_rgba_diff")
        self.assertEqual(contract["parity_smoke_precommit_command"], "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\\render_compose_parity_smoke.ps1 -ContractOnly")

    def test_deterministic_repeat_call_returns_same_packet(self):
        steps = [
            {"id": "rivers", "kind": "runtime_blend", "layer_id": "rivers"},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
        ]
        states = [
            build_layer_render_plan_step_runtime_state(0, steps[0], overlay_present=True),
            build_layer_render_plan_step_runtime_state(1, steps[1]),
        ]

        first = build_layer_render_plan_compose_queue_packet_from_states(steps, states)
        second = build_layer_render_plan_compose_queue_packet_from_states(steps, states)

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
