import unittest

from render_core.render_plan import (
    build_layer_render_plan_composition_apply_action,
    build_layer_render_plan_composition_dispatch_packet,
)


class LayerRenderPlanCompositionDispatchFixtureTests(unittest.TestCase):
    def test_apply_action_output_key_set_and_unknown_kind_are_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "mystery", "kind": "unknown_kind"}
        )

        self.assertEqual(
            set(action),
            {
                "kind",
                "layer_id",
                "blend_mode",
                "apply_helper",
                "phase_id",
                "requires_overlay",
                "single_pass_candidate",
            },
        )
        self.assertEqual(action["kind"], "unknown_kind")
        self.assertEqual(action["layer_id"], "mystery")
        self.assertEqual(action["blend_mode"], "Normal")
        self.assertEqual(action["apply_helper"], "unknown_apply_helper")
        self.assertEqual(action["phase_id"], "compose_overlays")
        self.assertFalse(action["requires_overlay"])
        self.assertFalse(action["single_pass_candidate"])

    def test_runtime_blend_dispatch_packet_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "rivers", "kind": "runtime_blend", "layer_id": "rivers"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(action["apply_helper"], "HybridRenderController.compose_runtime_blend")
        self.assertEqual(action["phase_id"], "compose_overlays")
        self.assertTrue(action["requires_overlay"])
        self.assertTrue(action["single_pass_candidate"])
        self.assertEqual(packet["dispatch"], "runtime_blend")
        self.assertTrue(packet["should_apply"])
        self.assertEqual(packet["skip_reason"], "")

    def test_alpha_blend_dispatch_packet_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "boundary", "kind": "alpha_blend", "blend_mode": "Screen"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(action["apply_helper"], "alpha_blend_compose")
        self.assertEqual(action["blend_mode"], "Screen")
        self.assertTrue(action["requires_overlay"])
        self.assertEqual(packet["dispatch"], "alpha_blend")
        self.assertTrue(packet["should_apply"])

    def test_alpha_compose_dispatch_packet_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "ais_overlay", "kind": "alpha_compose"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(action["apply_helper"], "alpha_compose")
        self.assertTrue(action["requires_overlay"])
        self.assertEqual(packet["dispatch"], "alpha_compose")
        self.assertTrue(packet["should_apply"])

    def test_runtime_overlay_dispatch_packet_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "pins", "kind": "runtime_overlay", "layer_id": "pins"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(action["apply_helper"], "HybridRenderController.compose_runtime_overlay")
        self.assertTrue(action["requires_overlay"])
        self.assertEqual(packet["dispatch"], "runtime_overlay")
        self.assertTrue(packet["should_apply"])

    def test_style_profile_postprocess_dispatch_packet_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, False)

        self.assertEqual(action["apply_helper"], "apply_style_profile")
        self.assertEqual(action["phase_id"], "postprocess")
        self.assertFalse(action["requires_overlay"])
        self.assertFalse(action["single_pass_candidate"])
        self.assertEqual(packet["dispatch"], "style_profile_postprocess")
        self.assertTrue(packet["should_apply"])
        self.assertEqual(packet["skip_reason"], "")

    def test_missing_overlay_dispatch_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "aircraft", "kind": "runtime_overlay", "layer_id": "aircraft"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, False)

        self.assertEqual(packet["dispatch"], "skip")
        self.assertFalse(packet["should_apply"])
        self.assertEqual(packet["skip_reason"], "missing_overlay")
        self.assertTrue(packet["requires_overlay"])
        self.assertFalse(packet["overlay_present"])

    def test_unknown_kind_dispatch_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "mystery", "kind": "unknown_kind"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(packet["dispatch"], "skip")
        self.assertFalse(packet["should_apply"])
        self.assertEqual(packet["skip_reason"], "unknown_apply_action")
        self.assertFalse(packet["requires_overlay"])
        self.assertTrue(packet["overlay_present"])

    def test_dispatch_packet_key_set_is_pinned(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "ais_overlay", "kind": "alpha_compose"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(
            set(packet),
            {
                "schema",
                "source",
                "kind",
                "layer_id",
                "blend_mode",
                "apply_helper",
                "phase_id",
                "requires_overlay",
                "overlay_present",
                "should_apply",
                "dispatch",
                "skip_reason",
                "runtime_optimization_applied",
            },
        )
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_composition_dispatch.v1")
        self.assertEqual(packet["source"], "render_core.render_plan.build_layer_render_plan_composition_dispatch_packet")
        self.assertFalse(packet["runtime_optimization_applied"])

    def test_dispatch_packet_fields_are_labels_not_execution_claims(self):
        action = build_layer_render_plan_composition_apply_action(
            {"id": "rivers", "kind": "runtime_blend", "layer_id": "rivers"}
        )
        packet = build_layer_render_plan_composition_dispatch_packet(action, True)

        self.assertEqual(packet["dispatch"], "runtime_blend")
        self.assertNotIn("pixel_equivalence", packet)
        self.assertNotIn("visual_parity_passed", packet)
        self.assertNotIn("runtime_merge_enabled", packet)
        self.assertNotIn("performance_ready", packet)

    def test_deterministic_repeat_call_returns_same_packets(self):
        step = {"id": "boundary", "kind": "alpha_blend", "blend_mode": "Multiply"}

        first_action = build_layer_render_plan_composition_apply_action(step)
        second_action = build_layer_render_plan_composition_apply_action(step)
        first_packet = build_layer_render_plan_composition_dispatch_packet(first_action, True)
        second_packet = build_layer_render_plan_composition_dispatch_packet(second_action, True)

        self.assertEqual(first_action, second_action)
        self.assertEqual(first_packet, second_packet)


if __name__ == "__main__":
    unittest.main()
