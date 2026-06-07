import unittest

import taichi_global_bathymetry as tgb


class AdaptiveRenderQualityPolicyFixtureTests(unittest.TestCase):
    def setUp(self):
        self.policy = tgb.AdaptiveRenderQualityPolicy()

    def test_unknown_render_timing_uses_full_quality(self):
        decision = self.policy.decision(800, 600, None, "regional", 30.0)

        self.assertEqual(decision["width"], 800)
        self.assertEqual(decision["height"], 600)
        self.assertEqual(decision["pixels"], 480_000)
        self.assertEqual(decision["render_ms"], None)
        self.assertEqual(decision["pressure"], 1.0)
        self.assertEqual(decision["suggested_render_scale"], 1.0)
        self.assertEqual(decision["overlay_budget"], "full")

    def test_pressure_at_or_below_1_15_is_full(self):
        decision = self.policy.decision(800, 600, 38.0, "regional", 30.0)

        self.assertLessEqual(decision["pressure"], 1.15)
        self.assertEqual(decision["suggested_render_scale"], 1.0)
        self.assertEqual(decision["overlay_budget"], "full")

    def test_pressure_between_1_15_and_2_reduces_overlays(self):
        decision = self.policy.decision(800, 600, 50.0, "regional", 30.0)

        self.assertGreater(decision["pressure"], 1.15)
        self.assertLessEqual(decision["pressure"], 2.0)
        self.assertEqual(decision["suggested_render_scale"], 0.85)
        self.assertEqual(decision["overlay_budget"], "reduced overlays")

    def test_pressure_between_2_and_4_samples_realtime_overlays(self):
        decision = self.policy.decision(800, 600, 100.0, "regional", 30.0)

        self.assertGreater(decision["pressure"], 2.0)
        self.assertLessEqual(decision["pressure"], 4.0)
        self.assertEqual(decision["suggested_render_scale"], 0.70)
        self.assertEqual(decision["overlay_budget"], "sample realtime overlays")

    def test_pressure_above_4_uses_aggressive_sampling(self):
        decision = self.policy.decision(800, 600, 150.0, "regional", 30.0)

        self.assertGreater(decision["pressure"], 4.0)
        self.assertEqual(decision["suggested_render_scale"], 0.55)
        self.assertEqual(decision["overlay_budget"], "aggressive realtime sampling")

    def test_large_canvas_guardrail_limits_full_quality(self):
        decision = self.policy.decision(3000, 2000, 20.0, "global", 30.0)

        self.assertEqual(decision["pixels"], 6_000_000)
        self.assertEqual(decision["suggested_render_scale"], 0.85)
        self.assertEqual(decision["overlay_budget"], "large-display guardrail")

    def test_width_height_coerce_to_at_least_one(self):
        decision = self.policy.decision(0, -20, None, "regional", 30.0)

        self.assertEqual(decision["width"], 1)
        self.assertEqual(decision["height"], 1)
        self.assertEqual(decision["pixels"], 1)

    def test_target_fps_floor_behavior(self):
        decision = self.policy.decision(800, 600, 1000.0, "regional", 0.0)

        self.assertEqual(decision["target_fps"], 0.0)
        self.assertEqual(decision["target_ms"], 1000.0)
        self.assertEqual(decision["pressure"], 1.0)
        self.assertEqual(decision["overlay_budget"], "full")

    def test_negative_render_ms_coerces_to_zero(self):
        decision = self.policy.decision(800, 600, -10.0, "regional", 30.0)

        self.assertEqual(decision["render_ms"], 0.0)
        self.assertEqual(decision["pressure"], 0.0)
        self.assertEqual(decision["suggested_render_scale"], 1.0)
        self.assertEqual(decision["overlay_budget"], "full")

    def test_decision_output_keys_are_pinned(self):
        decision = self.policy.decision(800, 600, 20.0, "regional", 30.0)

        self.assertEqual(
            set(decision),
            {
                "width",
                "height",
                "pixels",
                "lod",
                "render_ms",
                "target_fps",
                "target_ms",
                "pressure",
                "suggested_render_scale",
                "overlay_budget",
            },
        )

    def test_deterministic_repeat_call_returns_same_output(self):
        args = (800, 600, 50.0, "regional", 30.0)

        self.assertEqual(self.policy.decision(*args), self.policy.decision(*args))

    def test_text_output_line_order_and_formatting_are_pinned(self):
        text = self.policy.text(800, 600, 50.0, "regional", 30.0)

        self.assertEqual(
            text.splitlines(),
            [
                "Adaptive render quality policy",
                "",
                "- canvas: 800 x 600",
                "- pixels: 480,000",
                "- lod: regional",
                "- last render: 50.00 ms",
                "- target fps: 30.0",
                "- pressure: 1.50x",
                "- suggested render scale: 0.85",
                "- overlay budget: reduced overlays",
                "",
                "Rule: this policy reports recommendations only; it does not silently degrade scientific output.",
            ],
        )

    def test_text_unknown_render_timing_formatting_is_pinned(self):
        text = self.policy.text(1, 1, None, "global", 0.0)

        self.assertEqual(
            text.splitlines(),
            [
                "Adaptive render quality policy",
                "",
                "- canvas: 1 x 1",
                "- pixels: 1",
                "- lod: global",
                "- last render: unknown",
                "- target fps: 0.0",
                "- pressure: 1.00x",
                "- suggested render scale: 1.00",
                "- overlay budget: full",
                "",
                "Rule: this policy reports recommendations only; it does not silently degrade scientific output.",
            ],
        )


if __name__ == "__main__":
    unittest.main()
