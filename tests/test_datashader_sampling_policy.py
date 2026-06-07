import unittest

import taichi_global_bathymetry as tgb


class DatashaderSamplingPolicyFixtureTests(unittest.TestCase):
    def setUp(self):
        self.policy = tgb.DatashaderSamplingPolicy()

    def test_records_below_budget_aggregate_all(self):
        decision = self.policy.decision(199_999, "regional", 1.0, True)

        self.assertEqual(decision["records"], 199_999)
        self.assertEqual(decision["base_budget"], 900_000)
        self.assertEqual(decision["effective_budget"], 900_000)
        self.assertEqual(decision["sample_fraction"], 1.0)
        self.assertEqual(decision["strategy"], "aggregate-all")

    def test_records_at_200k_still_under_regional_budget(self):
        decision = self.policy.decision(200_000, "regional", 1.0, True)

        self.assertEqual(decision["records"], 200_000)
        self.assertEqual(decision["sample_fraction"], 1.0)
        self.assertEqual(decision["strategy"], "aggregate-all")

    def test_records_at_800k_with_half_scale_presamples(self):
        decision = self.policy.decision(800_000, "regional", 0.5, True)

        self.assertEqual(decision["effective_budget"], 450_000)
        self.assertAlmostEqual(decision["sample_fraction"], 0.5625)
        self.assertEqual(decision["strategy"], "pre-sample-then-aggregate")

    def test_records_at_2m_global_presamples(self):
        decision = self.policy.decision(2_000_000, "global", 1.0, True)

        self.assertEqual(decision["base_budget"], 250_000)
        self.assertEqual(decision["effective_budget"], 250_000)
        self.assertEqual(decision["sample_fraction"], 0.125)
        self.assertEqual(decision["strategy"], "pre-sample-then-aggregate")

    def test_lod_unknown_uses_global_budget(self):
        decision = self.policy.decision(500_000, "unknown", 1.0, True)

        self.assertEqual(decision["lod"], "unknown")
        self.assertEqual(decision["base_budget"], 250_000)
        self.assertEqual(decision["effective_budget"], 250_000)
        self.assertEqual(decision["sample_fraction"], 0.5)

    def test_continental_and_local_lod_budgets_are_pinned(self):
        continental = self.policy.decision(500_000, "continental", 1.0, True)
        local = self.policy.decision(1_250_000, "local", 1.0, True)

        self.assertEqual(continental["base_budget"], 500_000)
        self.assertEqual(continental["effective_budget"], 500_000)
        self.assertEqual(continental["sample_fraction"], 1.0)
        self.assertEqual(local["base_budget"], 1_250_000)
        self.assertEqual(local["effective_budget"], 1_250_000)
        self.assertEqual(local["sample_fraction"], 1.0)

    def test_offline_mode_raises_effective_budget_to_records(self):
        decision = self.policy.decision(2_000_000, "global", 0.5, False)

        self.assertFalse(decision["realtime"])
        self.assertEqual(decision["effective_budget"], 2_000_000)
        self.assertEqual(decision["sample_fraction"], 1.0)
        self.assertEqual(decision["strategy"], "aggregate-all")

    def test_user_scale_floor_is_pinned(self):
        decision = self.policy.decision(100_000, "global", 0.0, True)

        self.assertEqual(decision["effective_budget"], 12_500)
        self.assertEqual(decision["sample_fraction"], 0.125)
        self.assertEqual(decision["strategy"], "pre-sample-then-aggregate")

    def test_negative_records_coerce_to_zero(self):
        decision = self.policy.decision(-10, "global", 1.0, True)

        self.assertEqual(decision["records"], 0)
        self.assertEqual(decision["sample_fraction"], 1.0)
        self.assertEqual(decision["strategy"], "aggregate-all")

    def test_decision_output_keys_are_pinned(self):
        decision = self.policy.decision(1, "global", 1.0, True)

        self.assertEqual(
            set(decision),
            {
                "lod",
                "records",
                "base_budget",
                "effective_budget",
                "sample_fraction",
                "strategy",
                "realtime",
            },
        )

    def test_deterministic_repeat_call_returns_same_output(self):
        args = (800_000, "regional", 0.5, True)

        self.assertEqual(self.policy.decision(*args), self.policy.decision(*args))

    def test_text_output_line_order_and_formatting_are_pinned(self):
        text = self.policy.text(
            ais_records=800_000,
            aircraft_records=2_000_000,
            lod="global",
            ais_scale=0.5,
            aircraft_scale=1.0,
            mode="realtime",
        )

        self.assertEqual(
            text.splitlines(),
            [
                "Datashader sampling policy",
                "",
                "- mode: realtime",
                "- lod: global",
                "",
                "AIS:",
                "- records: 800000",
                "- effective budget: 125000",
                "- sample fraction: 0.1562",
                "- strategy: pre-sample-then-aggregate",
                "",
                "ADS-B:",
                "- records: 2000000",
                "- effective budget: 250000",
                "- sample fraction: 0.1250",
                "- strategy: pre-sample-then-aggregate",
                "",
                "Rule: Datashader should aggregate all points when affordable; sampling is a realtime FPS valve.",
            ],
        )

    def test_text_offline_mode_wording_and_budget_are_pinned(self):
        text = self.policy.text(
            ais_records=800_000,
            aircraft_records=2_000_000,
            lod="global",
            ais_scale=0.5,
            aircraft_scale=1.0,
            mode="offline",
        )

        self.assertIn("- mode: offline", text)
        self.assertIn("- effective budget: 800000", text)
        self.assertIn("- effective budget: 2000000", text)
        self.assertIn("- sample fraction: 1.0000", text)


if __name__ == "__main__":
    unittest.main()
