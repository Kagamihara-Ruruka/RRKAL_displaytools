"""Interpretation gate for the sampling / visibility runtime probe result."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from typing import Any


EXPECTED_RECOMMENDED_NEXT_GATE = (
    "dynamic_point_lod_view_frame_frame_visibility_stop_line_planning_gate"
)


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame sampling / visibility runtime "
    "probe result interpretation gate. No probe script change, no new runtime "
    "execution, no render_if_needed, no controller, no renderer, no frame "
    "buffer read, no artifact generation, no formula or renderer behavior "
    "change, no correctness/readiness/leak-fix claim, and no push."
)


EXPECTED_RUNTIME_FIELDS = {
    "runtime_probe_executed": True,
    "project_ais_to_screen_called": True,
    "project_aircraft_to_screen_called": True,
    "mask_overlay_to_globe_called": True,
    "render_if_needed_called": False,
    "controller_instantiated": False,
    "renderer_executed": False,
    "frame_buffer_read": False,
    "artifact_written": False,
}


EXPECTED_TOKEN_FIELDS = {
    "source_lineage_integrity_token": True,
    "sampled_visible_token": True,
    "visible_count_observation": 2,
    "rendered_count_observation": 1,
    "frame_visible_token": "not_observed",
}


EXPECTED_CASE_INTERPRETATIONS = [
    {
        "case": "full_sample_case",
        "observed": "projected_sampled_rendered_preserved",
        "interpretation": "projected, sampled, and rendered synthetic counts are preserved",
        "supports": "sampling_observed",
        "does_not_support": "frame_visibility_or_visual_correctness",
    },
    {
        "case": "reduced_sample_case",
        "observed": "rendered_lower_than_visible",
        "interpretation": "rendered count lower than visible count supports reduction model",
        "supports": "count_surface_observed",
        "does_not_support": "renderer_or_frame_behavior",
    },
    {
        "case": "mask_visible_true",
        "observed": "mask_visible_path_preserved",
        "interpretation": "mask-visible path is observable in the synthetic packet",
        "supports": "mask_visible_path_observed",
        "does_not_support": "coordinate_correctness",
    },
    {
        "case": "mask_visible_false_synthetic",
        "observed": "overlay_hidden_by_synthetic_mask",
        "interpretation": "globe mask can hide overlay without deleting source lineage",
        "supports": "mask_false_path_observed",
        "does_not_support": "transparent_globe_leak_fix",
    },
    {
        "case": "source_lineage_guard_case",
        "observed": "source_lineage_preserved",
        "interpretation": "sampling and mask labels do not pollute source identity",
        "supports": "source_lineage_guard_supported",
        "does_not_support": "source_mutation_authorization",
    },
    {
        "case": "frame_remains_not_observed",
        "observed": "frame_not_observed",
        "interpretation": "frame visibility remains outside this probe result",
        "supports": "frame_stop_line_needed",
        "does_not_support": "transparent_globe_leak_inference",
    },
]


DECISION_OUTPUT = {
    "sampling_visibility_interpretation_passed": True,
    "sampling_observed": True,
    "count_surface_observed": True,
    "mask_false_path_observed": True,
    "source_lineage_guard_supported": True,
    "frame_visibility_observed": False,
    "transparent_globe_leak_inferred": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "readiness_claimed": False,
    "recommended_next_gate": EXPECTED_RECOMMENDED_NEXT_GATE,
}


INTERPRETATION_PACKET = {
    "schema": (
        "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_"
        "runtime_probe_result_interpretation.v1"
    ),
    "expected_runtime_fields": EXPECTED_RUNTIME_FIELDS,
    "expected_token_fields": EXPECTED_TOKEN_FIELDS,
    "case_interpretations": EXPECTED_CASE_INTERPRETATIONS,
    "key_conclusion": {
        "sampling_count_synthetic_observed": True,
        "mask_can_hide_overlay_without_source_loss": True,
        "rendered_lower_than_visible_model_supported": True,
        "frame_renderer_leak_still_blocked": True,
        "andesite_segment_narrowed": True,
    },
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


def run_probe_packet() -> dict[str, Any]:
    completed = subprocess.run(
        [
            sys.executable,
            "-B",
            "scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py",
            "--run-probe",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


class DynamicPointSamplingVisibilityRuntimeProbeResultInterpretationTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(INTERPRETATION_PACKET),
            {
                "schema",
                "expected_runtime_fields",
                "expected_token_fields",
                "case_interpretations",
                "key_conclusion",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            INTERPRETATION_PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_"
            "runtime_probe_result_interpretation.v1",
        )

    def test_required_probe_fields_are_observed(self) -> None:
        packet = run_probe_packet()
        decision = packet["decision_output"]
        seam = packet["seam_call_summary"]
        token = packet["token_packet"]
        self.assertIs(packet["runtime_probe_executed"], True)
        for key, expected in EXPECTED_RUNTIME_FIELDS.items():
            if key in seam:
                self.assertIs(seam[key], expected, key)
            elif key in decision:
                self.assertIs(decision[key], expected, key)
            else:
                self.fail(f"missing runtime field {key}")
        for key, expected in EXPECTED_TOKEN_FIELDS.items():
            self.assertEqual(token[key], expected, key)

    def test_required_case_interpretations_match_probe_json(self) -> None:
        packet = run_probe_packet()
        cases = {
            row["case"]: row for row in packet["sampling_visibility_case_results"]
        }
        oracles = {
            row["case"]: row["oracle_result"]
            for row in packet["sampling_visibility_oracle_results"]
        }
        self.assertEqual(
            set(cases),
            {row["case"] for row in EXPECTED_CASE_INTERPRETATIONS},
        )
        self.assertEqual(oracles["full_sample_case"], "full_sample_path_preserved")
        self.assertEqual(
            oracles["reduced_sample_case"],
            "sampling_or_presentation_reduction_candidate",
        )
        self.assertEqual(oracles["mask_visible_true"], "mask_visible_path_preserved")
        self.assertEqual(
            oracles["mask_visible_false_synthetic"],
            "globe_mask_responsibility_candidate",
        )
        self.assertEqual(
            oracles["source_lineage_guard_case"],
            "source_lineage_guard_preserved",
        )
        self.assertEqual(oracles["frame_remains_not_observed"], "still_not_leak_evidence")

    def test_decision_output_boundaries_and_recommendation(self) -> None:
        decision = INTERPRETATION_PACKET["decision_output"]
        self.assertTrue(decision["sampling_visibility_interpretation_passed"])
        self.assertTrue(decision["sampling_observed"])
        self.assertTrue(decision["count_surface_observed"])
        self.assertTrue(decision["mask_false_path_observed"])
        self.assertTrue(decision["source_lineage_guard_supported"])
        self.assertFalse(decision["frame_visibility_observed"])
        self.assertFalse(decision["transparent_globe_leak_inferred"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(decision["recommended_next_gate"], EXPECTED_RECOMMENDED_NEXT_GATE)

    def test_key_conclusion_keeps_frame_and_leak_blocked(self) -> None:
        conclusion = INTERPRETATION_PACKET["key_conclusion"]
        self.assertTrue(conclusion["sampling_count_synthetic_observed"])
        self.assertTrue(conclusion["mask_can_hide_overlay_without_source_loss"])
        self.assertTrue(conclusion["rendered_lower_than_visible_model_supported"])
        self.assertTrue(conclusion["andesite_segment_narrowed"])
        self.assertTrue(conclusion["frame_renderer_leak_still_blocked"])

    def test_boundary_statement(self) -> None:
        self.assertIn("No probe script change", BOUNDARY_STATEMENT)
        self.assertIn("no renderer", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
