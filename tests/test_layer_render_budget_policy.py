import unittest

import taichi_global_bathymetry as tgb


class LayerRenderBudgetPolicyFixtureTests(unittest.TestCase):
    def setUp(self):
        self.policy = tgb.LayerRenderBudgetPolicy()

    def test_warming_up_without_render_timing(self):
        decision = self.policy.decision(800, 600, None, "regional", 30.0, False, {"globe": True})

        self.assertEqual(decision["state"], "warming-up")
        self.assertEqual(decision["current_ms"], 0.0)
        self.assertEqual(decision["pressure"], 0.0)
        self.assertEqual(decision["visible_cost"], 10)
        self.assertEqual(decision["vector_cost"], 0)
        self.assertFalse(decision["defer_vector_overlays"])
        self.assertFalse(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.004)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.001)
        self.assertEqual(decision["vector_point_stride"], 1)

    def test_under_budget_static_layers_default_quantum(self):
        decision = self.policy.decision(800, 600, 20.0, "regional", 30.0, False, {"globe": True, "scale": True})

        self.assertEqual(decision["state"], "within-budget")
        self.assertAlmostEqual(decision["target_ms"], 1000.0 / 30.0)
        self.assertEqual(decision["current_ms"], 20.0)
        self.assertAlmostEqual(decision["pressure"], 0.6)
        self.assertEqual(decision["megapixels"], 1.0)
        self.assertEqual(decision["visible_cost"], 11)
        self.assertEqual(decision["vector_cost"], 0)
        self.assertFalse(decision["heavy_canvas"])
        self.assertFalse(decision["interaction_active"])
        self.assertFalse(decision["defer_vector_overlays"])
        self.assertFalse(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.004)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.001)
        self.assertEqual(decision["vector_point_stride"], 1)
        self.assertEqual(decision["lod"], "regional")

    def test_over_budget_vector_layers_prefer_static_cache(self):
        decision = self.policy.decision(
            800,
            600,
            50.0,
            "global",
            30.0,
            False,
            {"rivers": True, "borders": True},
        )

        self.assertEqual(decision["state"], "over-budget")
        self.assertEqual(decision["visible_cost"], 13)
        self.assertEqual(decision["vector_cost"], 13)
        self.assertFalse(decision["defer_vector_overlays"])
        self.assertTrue(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.08)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.008)
        self.assertEqual(decision["vector_point_stride"], 3)

    def test_regional_over_budget_vector_layers_use_stride_two(self):
        decision = self.policy.decision(
            800,
            600,
            50.0,
            "regional",
            30.0,
            False,
            {"rivers": True, "borders": True},
        )

        self.assertEqual(decision["state"], "over-budget")
        self.assertFalse(decision["defer_vector_overlays"])
        self.assertTrue(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.08)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.008)
        self.assertEqual(decision["vector_point_stride"], 2)

    def test_dragging_over_budget_defers_vector_overlays(self):
        decision = self.policy.decision(
            800,
            600,
            50.0,
            "regional",
            30.0,
            True,
            {"rivers": True, "borders": True},
        )

        self.assertEqual(decision["state"], "over-budget")
        self.assertTrue(decision["interaction_active"])
        self.assertTrue(decision["defer_vector_overlays"])
        self.assertTrue(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.45)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.025)
        self.assertEqual(decision["vector_point_stride"], 5)

    def test_heavy_canvas_interaction_over_budget_without_vector_uses_interaction_cache(self):
        decision = self.policy.decision(2000, 1600, 50.0, "regional", 30.0, True, {"globe": True})

        self.assertEqual(decision["state"], "over-budget")
        self.assertTrue(decision["heavy_canvas"])
        self.assertEqual(decision["vector_cost"], 0)
        self.assertFalse(decision["defer_vector_overlays"])
        self.assertTrue(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.18)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.014)
        self.assertEqual(decision["vector_point_stride"], 4)

    def test_global_heavy_canvas_uses_global_quantum_when_within_budget(self):
        decision = self.policy.decision(2000, 1600, 20.0, "global", 30.0, False, {"globe": True})

        self.assertEqual(decision["state"], "within-budget")
        self.assertEqual(decision["megapixels"], 3.2)
        self.assertTrue(decision["heavy_canvas"])
        self.assertFalse(decision["prefer_static_cache"])
        self.assertEqual(decision["vector_cache_degrees"], 0.012)
        self.assertEqual(decision["vector_cache_zoom_step"], 0.002)
        self.assertEqual(decision["vector_point_stride"], 2)

    def test_unknown_visible_layer_uses_default_cost(self):
        decision = self.policy.decision(800, 600, 20.0, "regional", 30.0, False, {"custom_layer": True})

        self.assertEqual(decision["visible_cost"], 1)
        self.assertEqual(decision["vector_cost"], 0)

    def test_decision_output_keys_are_pinned(self):
        decision = self.policy.decision(800, 600, 20.0, "regional", 30.0, False, {})

        self.assertEqual(
            set(decision),
            {
                "state",
                "target_ms",
                "current_ms",
                "pressure",
                "megapixels",
                "visible_cost",
                "vector_cost",
                "heavy_canvas",
                "interaction_active",
                "defer_vector_overlays",
                "prefer_static_cache",
                "vector_cache_degrees",
                "vector_cache_zoom_step",
                "vector_point_stride",
                "lod",
            },
        )

    def test_deterministic_repeat_call_returns_same_output(self):
        args = (800, 600, 50.0, "regional", 30.0, True, {"rivers": True, "borders": True})

        self.assertEqual(self.policy.decision(*args), self.policy.decision(*args))

    def test_text_output_line_order_and_formatting_are_pinned(self):
        text = self.policy.text(
            800,
            600,
            50.0,
            "regional",
            30.0,
            True,
            {"rivers": True, "borders": True},
        )

        self.assertEqual(
            text.splitlines(),
            [
                "Render budget policy",
                "",
                "- state: over-budget",
                "- target: 33.33 ms/frame",
                "- current: 50.00 ms/frame",
                "- pressure: 1.50x",
                "- canvas: 1.00 MP",
                "- visible layer cost: 13",
                "- vector layer cost: 13",
                "- interaction active: True",
                "- defer vector overlays while dragging: True",
                "- prefer static/vector cache: True",
                "- vector camera quantum: 0.450 deg / zoom 0.0250",
                "- vector point stride: every 5 point(s)",
                "",
                "Rule: while dragging and over budget, keep the last vector overlay frame and recompute it after interaction settles.",
            ],
        )


if __name__ == "__main__":
    unittest.main()
