import unittest

import taichi_global_bathymetry as tgb


class PointOverlayBudgetPolicyFixtureTests(unittest.TestCase):
    def setUp(self):
        self.policy = tgb.PointOverlayBudgetPolicy()

    def test_low_record_count_under_budget_uses_full_quality(self):
        decision = self.policy.decision(
            layer="ais",
            point_count=12_000,
            width=1280,
            height=720,
            render_ms=20.0,
            lod="regional",
            target_fps=30.0,
            interaction_active=False,
        )

        self.assertEqual(decision["layer"], "ais")
        self.assertEqual(decision["point_count"], 12_000)
        self.assertFalse(decision["over_budget"])
        self.assertFalse(decision["dense"])
        self.assertFalse(decision["very_dense"])
        self.assertEqual(decision["sample_ratio_cap"], 1.0)
        self.assertEqual(decision["reason"], "full-quality")

    def test_medium_record_count_drag_over_budget_caps_sample_ratio(self):
        decision = self.policy.decision(
            layer="ais",
            point_count=75_000,
            width=1280,
            height=720,
            render_ms=40.0,
            lod="regional",
            target_fps=30.0,
            interaction_active=True,
        )

        self.assertTrue(decision["over_budget"])
        self.assertTrue(decision["dense"])
        self.assertFalse(decision["very_dense"])
        self.assertEqual(decision["sample_ratio_cap"], 0.18)
        self.assertEqual(decision["reason"], "drag-over-budget")

    def test_sparse_record_count_drag_over_budget_caps_sample_ratio(self):
        decision = self.policy.decision(
            layer="ais",
            point_count=12_000,
            width=1280,
            height=720,
            render_ms=40.0,
            lod="regional",
            target_fps=30.0,
            interaction_active=True,
        )

        self.assertTrue(decision["over_budget"])
        self.assertFalse(decision["dense"])
        self.assertFalse(decision["very_dense"])
        self.assertEqual(decision["sample_ratio_cap"], 0.35)
        self.assertEqual(decision["reason"], "drag-over-budget")

    def test_high_record_count_drag_over_budget_caps_more_aggressively(self):
        decision = self.policy.decision(
            layer="aircraft",
            point_count=250_000,
            width=1280,
            height=720,
            render_ms=40.0,
            lod="regional",
            target_fps=30.0,
            interaction_active=True,
        )

        self.assertEqual(decision["layer"], "aircraft")
        self.assertTrue(decision["very_dense"])
        self.assertEqual(decision["sample_ratio_cap"], 0.10)
        self.assertEqual(decision["reason"], "drag-over-budget")

    def test_over_budget_steady_dense_paths_are_pinned(self):
        dense = self.policy.decision(
            "ais", 75_000, 1280, 720, 40.0, "regional", 30.0, False
        )
        very_dense = self.policy.decision(
            "ais", 250_000, 1280, 720, 40.0, "regional", 30.0, False
        )

        self.assertEqual(dense["sample_ratio_cap"], 0.35)
        self.assertEqual(dense["reason"], "steady-over-budget-dense")
        self.assertEqual(very_dense["sample_ratio_cap"], 0.22)
        self.assertEqual(very_dense["reason"], "steady-over-budget-very-dense")

    def test_lod_global_large_canvas_affects_dense_under_budget(self):
        global_decision = self.policy.decision(
            "ais", 75_000, 2500, 1600, 20.0, "global", 30.0, False
        )
        regional_decision = self.policy.decision(
            "ais", 75_000, 2500, 1600, 20.0, "regional", 30.0, False
        )

        self.assertEqual(global_decision["megapixels"], 4.0)
        self.assertEqual(global_decision["sample_ratio_cap"], 0.55)
        self.assertEqual(global_decision["reason"], "global-large-canvas")
        self.assertEqual(regional_decision["sample_ratio_cap"], 1.0)
        self.assertEqual(regional_decision["reason"], "full-quality")

    def test_interaction_large_canvas_under_budget_paths_are_pinned(self):
        sparse = self.policy.decision(
            "ais", 12_000, 2500, 1600, 20.0, "regional", 30.0, True
        )
        dense = self.policy.decision(
            "ais", 75_000, 2500, 1600, 20.0, "regional", 30.0, True
        )

        self.assertEqual(sparse["megapixels"], 4.0)
        self.assertEqual(sparse["sample_ratio_cap"], 0.65)
        self.assertEqual(sparse["reason"], "drag-large-canvas")
        self.assertEqual(dense["sample_ratio_cap"], 0.40)
        self.assertEqual(dense["reason"], "drag-large-canvas")

    def test_boundary_equality_is_not_over_budget(self):
        target_ms = 1000.0 / 30.0
        equality_ms = target_ms * 1.08
        decision = self.policy.decision(
            "ais", 75_000, 1280, 720, equality_ms, "regional", 30.0, True
        )

        self.assertFalse(decision["over_budget"])
        self.assertEqual(decision["reason"], "full-quality")
        self.assertEqual(decision["sample_ratio_cap"], 1.0)

    def test_warming_up_render_ms_none_is_under_budget_full_quality(self):
        decision = self.policy.decision(
            "ais", -10, 640, 480, None, "global", 30.0, False
        )

        self.assertEqual(decision["point_count"], 0)
        self.assertEqual(decision["current_ms"], 0.0)
        self.assertEqual(decision["pressure"], 0.0)
        self.assertFalse(decision["over_budget"])
        self.assertEqual(decision["sample_ratio_cap"], 1.0)

    def test_deterministic_repeat_call_returns_same_output(self):
        args = ("ais", 80_000, 1280, 720, 40.0, "regional", 30.0, True)

        self.assertEqual(self.policy.decision(*args), self.policy.decision(*args))

    def test_decision_output_keys_are_pinned(self):
        decision = self.policy.decision(
            "ais", 1, 1, 1, 0.0, "global", 30.0, False
        )

        self.assertEqual(
            set(decision),
            {
                "layer",
                "point_count",
                "target_ms",
                "current_ms",
                "pressure",
                "megapixels",
                "interaction_active",
                "over_budget",
                "dense",
                "very_dense",
                "sample_ratio_cap",
                "reason",
                "lod",
            },
        )

    def test_text_output_wording_and_numeric_fields_are_pinned(self):
        decisions = {
            "ais": self.policy.decision("ais", 75_000, 1280, 720, 40.0, "regional", 30.0, True),
            "aircraft": self.policy.decision(
                "aircraft", 12_000, 1280, 720, 20.0, "regional", 30.0, False
            ),
        }

        self.assertEqual(
            self.policy.text(decisions).splitlines(),
            [
                "Point overlay budget policy",
                "",
                "Rule: AIS/ADS-B stay screen-space correct while interaction lowers sample ratio under pressure.",
                "",
                "[ais]",
                "- points: 75,000",
                "- reason: drag-over-budget",
                "- pressure: 1.20x",
                "- sample ratio cap: 0.18",
                "- interaction active: True",
                "",
                "[aircraft]",
                "- points: 12,000",
                "- reason: full-quality",
                "- pressure: 0.60x",
                "- sample ratio cap: 1.00",
                "- interaction active: False",
            ],
        )


if __name__ == "__main__":
    unittest.main()
