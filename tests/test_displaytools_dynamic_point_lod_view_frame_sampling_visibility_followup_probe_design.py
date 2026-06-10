"""Design fixture for the sampling / visibility / count follow-up probe."""

from __future__ import annotations

import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame sampling / visibility "
    "followup probe design gate. No new runtime execution, no probe script "
    "change, no production source change, no render_if_needed call, no "
    "controller instantiation, no renderer or GUI execution, no frame buffer "
    "read, no artifact generation, no formula or renderer behavior change, no "
    "correctness/readiness/leak-fix claim, and no push."
)


TOKENS_TO_OBSERVE_NEXT = [
    "sampled_visible_token",
    "visible_count_observation",
    "rendered_count_observation",
    "mask_visible_token",
    "source_lineage_integrity_token",
]


TOKENS_STILL_NOT_OBSERVED_NEXT = [
    "frame_visible_token",
    "transparent_globe_leak_behavior",
    "render_if_needed",
    "controller_renderer_path",
]


MINIMAL_SYNTHETIC_CASES = [
    {
        "case": "full_sample_case",
        "purpose": "baseline sampled token and count observation",
        "synthetic_only": True,
        "one_shot": True,
        "requires_render_if_needed": False,
        "requires_renderer": False,
        "artifact_write": False,
    },
    {
        "case": "reduced_sample_case",
        "purpose": "sampled versus rendered count reduction observation",
        "synthetic_only": True,
        "one_shot": True,
        "requires_render_if_needed": False,
        "requires_renderer": False,
        "artifact_write": False,
    },
    {
        "case": "mask_visible_true",
        "purpose": "mask-visible path preservation",
        "synthetic_only": True,
        "one_shot": True,
        "requires_render_if_needed": False,
        "requires_renderer": False,
        "artifact_write": False,
    },
    {
        "case": "mask_visible_false_synthetic",
        "purpose": "synthetic globe-mask suppression observation",
        "synthetic_only": True,
        "one_shot": True,
        "requires_render_if_needed": False,
        "requires_renderer": False,
        "artifact_write": False,
    },
    {
        "case": "source_lineage_guard_case",
        "purpose": "source lineage guard remains stable under sampling labels",
        "synthetic_only": True,
        "one_shot": True,
        "requires_render_if_needed": False,
        "requires_renderer": False,
        "artifact_write": False,
    },
]


PROBE_SCRIPT_UPDATE_DESIGN = {
    "future_script": "scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py",
    "this_gate_modifies_probe_script": False,
    "future_update_needed": True,
    "future_update_scope": [
        "add dry-planned sampling visibility cases",
        "emit sampled_visible_token from synthetic sampling case",
        "emit visible_count_observation from synthetic count case",
        "emit rendered_count_observation from synthetic count case",
        "preserve mask_visible_token observation",
        "preserve source_lineage_integrity_token observation",
    ],
    "future_update_must_not_include": [
        "render_if_needed call",
        "controller instantiation",
        "renderer execution",
        "frame buffer read",
        "artifact write",
        "formula mutation",
        "renderer behavior mutation",
        "compose order mutation",
    ],
}


ORACLE_DESIGN = [
    {
        "condition": "projected true + sampled false",
        "verdict": "sampling_responsibility_candidate",
    },
    {
        "condition": "visible_count > rendered_count",
        "verdict": "sampling_or_presentation_reduction_candidate",
    },
    {
        "condition": "overlay true + mask false",
        "verdict": "globe_mask_responsibility_candidate",
    },
    {
        "condition": "source lineage changed",
        "verdict": "source_lineage_pollution_fail",
    },
    {
        "condition": "source true + frame not observed",
        "verdict": "still_not_leak_evidence",
    },
]


DESIGN_DECISION_OUTPUT = {
    "probe_design_gate_passed": True,
    "tokens_to_observe_next_defined": True,
    "tokens_still_not_observed_next_defined": True,
    "minimal_synthetic_cases_defined": True,
    "oracle_design_defined": True,
    "probe_script_update_needed_next": True,
    "this_gate_modifies_probe_script": False,
    "new_runtime_execution_authorized": False,
    "production_source_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_instantiation_authorized": False,
    "renderer_execution_authorized": False,
    "frame_buffer_read_authorized": False,
    "artifact_generation_authorized": False,
    "formula_change_authorized": False,
    "renderer_behavior_change_authorized": False,
    "compose_order_change_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
    "recommended_next_gate": (
        "dynamic_point_lod_view_frame_sampling_visibility_probe_script_update_gate"
    ),
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design.v1",
    "tokens_to_observe_next": TOKENS_TO_OBSERVE_NEXT,
    "tokens_still_not_observed_next": TOKENS_STILL_NOT_OBSERVED_NEXT,
    "minimal_synthetic_cases": MINIMAL_SYNTHETIC_CASES,
    "probe_script_update_design": PROBE_SCRIPT_UPDATE_DESIGN,
    "oracle_design": ORACLE_DESIGN,
    "design_decision_output": DESIGN_DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSamplingVisibilityFollowupProbeDesignTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "tokens_to_observe_next",
                "tokens_still_not_observed_next",
                "minimal_synthetic_cases",
                "probe_script_update_design",
                "oracle_design",
                "design_decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design.v1",
        )

    def test_next_tokens_and_still_unobserved_tokens(self) -> None:
        self.assertEqual(
            PACKET["tokens_to_observe_next"],
            [
                "sampled_visible_token",
                "visible_count_observation",
                "rendered_count_observation",
                "mask_visible_token",
                "source_lineage_integrity_token",
            ],
        )
        self.assertEqual(
            PACKET["tokens_still_not_observed_next"],
            [
                "frame_visible_token",
                "transparent_globe_leak_behavior",
                "render_if_needed",
                "controller_renderer_path",
            ],
        )

    def test_minimal_synthetic_cases(self) -> None:
        cases = {row["case"]: row for row in PACKET["minimal_synthetic_cases"]}
        self.assertEqual(
            set(cases),
            {
                "full_sample_case",
                "reduced_sample_case",
                "mask_visible_true",
                "mask_visible_false_synthetic",
                "source_lineage_guard_case",
            },
        )
        for row in cases.values():
            self.assertTrue(row["synthetic_only"])
            self.assertTrue(row["one_shot"])
            self.assertFalse(row["requires_render_if_needed"])
            self.assertFalse(row["requires_renderer"])
            self.assertFalse(row["artifact_write"])

    def test_oracle_design(self) -> None:
        verdicts = {row["verdict"] for row in PACKET["oracle_design"]}
        self.assertEqual(
            verdicts,
            {
                "sampling_responsibility_candidate",
                "sampling_or_presentation_reduction_candidate",
                "globe_mask_responsibility_candidate",
                "source_lineage_pollution_fail",
                "still_not_leak_evidence",
            },
        )

    def test_probe_script_update_is_future_only(self) -> None:
        design = PACKET["probe_script_update_design"]
        self.assertEqual(
            design["future_script"],
            "scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py",
        )
        self.assertFalse(design["this_gate_modifies_probe_script"])
        self.assertTrue(design["future_update_needed"])
        forbidden = set(design["future_update_must_not_include"])
        self.assertIn("render_if_needed call", forbidden)
        self.assertIn("controller instantiation", forbidden)
        self.assertIn("renderer execution", forbidden)
        self.assertIn("artifact write", forbidden)

    def test_decision_output_boundaries(self) -> None:
        decision = PACKET["design_decision_output"]
        self.assertTrue(decision["probe_design_gate_passed"])
        self.assertTrue(decision["tokens_to_observe_next_defined"])
        self.assertTrue(decision["minimal_synthetic_cases_defined"])
        self.assertTrue(decision["oracle_design_defined"])
        self.assertTrue(decision["probe_script_update_needed_next"])
        for key in (
            "this_gate_modifies_probe_script",
            "new_runtime_execution_authorized",
            "production_source_change_authorized",
            "render_if_needed_authorized",
            "controller_instantiation_authorized",
            "renderer_execution_authorized",
            "frame_buffer_read_authorized",
            "artifact_generation_authorized",
            "formula_change_authorized",
            "renderer_behavior_change_authorized",
            "compose_order_change_authorized",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "transparent_globe_leak_fix_claimed",
            "readiness_claimed",
        ):
            self.assertIs(decision[key], False, key)
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_probe_script_update_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("No new runtime execution", BOUNDARY_STATEMENT)
        self.assertIn("no probe script change", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
