"""Gate fixture for the sampling / visibility probe script update."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest


EXPECTED_NEXT_GATE = (
    "dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation_gate"
)


BOUNDARY_STATEMENT = (
    "Tooling/test/docs dynamic point LOD view-frame sampling / visibility "
    "probe script update gate. Synthetic-only sampling/count observation added "
    "to existing one-shot runtime probe; no render_if_needed, no controller, "
    "no renderer, no frame buffer read, no artifact generation, no production "
    "source change, no formula or renderer behavior change, no "
    "correctness/readiness/leak-fix claim, and no push."
)


SCRIPT_UPDATE_PACKET = {
    "schema": (
        "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_probe_"
        "script_update.v1"
    ),
    "script_updated": "scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py",
    "json_stdout_packet_additions": [
        "sampled_visible_token",
        "visible_count_observation",
        "rendered_count_observation",
        "sampling_visibility_case_results",
        "sampling_visibility_oracle_results",
    ],
    "synthetic_case_coverage": [
        "full_sample_case",
        "reduced_sample_case",
        "mask_visible_true",
        "mask_visible_false_synthetic",
        "source_lineage_guard_case",
        "frame_remains_not_observed",
    ],
    "required_oracle_results": [
        "full_sample_path_preserved",
        "sampling_or_presentation_reduction_candidate",
        "mask_visible_path_preserved",
        "globe_mask_responsibility_candidate",
        "source_lineage_guard_preserved",
        "still_not_leak_evidence",
    ],
    "required_runtime_boundaries": {
        "render_if_needed_called": False,
        "controller_instantiated": False,
        "renderer_executed": False,
        "frame_buffer_read": False,
        "artifact_written": False,
        "source_lineage_integrity_token": True,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
        "readiness_claimed": False,
    },
    "recommended_next_gate": EXPECTED_NEXT_GATE,
    "boundary_statement": BOUNDARY_STATEMENT,
}


def run_probe_packet() -> dict[str, object]:
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


class DynamicPointSamplingVisibilityProbeScriptUpdateTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(SCRIPT_UPDATE_PACKET),
            {
                "schema",
                "script_updated",
                "json_stdout_packet_additions",
                "synthetic_case_coverage",
                "required_oracle_results",
                "required_runtime_boundaries",
                "recommended_next_gate",
                "boundary_statement",
            },
        )
        self.assertEqual(
            SCRIPT_UPDATE_PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_sampling_visibility_probe_"
            "script_update.v1",
        )

    def test_runtime_probe_stdout_has_sampling_visibility_additions(self) -> None:
        packet = run_probe_packet()
        self.assertEqual(packet["status"], "runtime_probe_stdout_packet")
        self.assertTrue(packet["runtime_probe_executed"])
        self.assertIn("sampling_visibility_case_results", packet)
        self.assertIn("sampling_visibility_oracle_results", packet)
        token_packet = packet["token_packet"]
        self.assertIs(token_packet["sampled_visible_token"], True)
        self.assertIsInstance(token_packet["visible_count_observation"], int)
        self.assertIsInstance(token_packet["rendered_count_observation"], int)

    def test_synthetic_case_coverage(self) -> None:
        packet = run_probe_packet()
        cases = {
            row["case"]: row for row in packet["sampling_visibility_case_results"]
        }
        self.assertEqual(
            set(cases),
            set(SCRIPT_UPDATE_PACKET["synthetic_case_coverage"]),
        )
        full = cases["full_sample_case"]
        self.assertEqual(full["projected_count"], full["sampled_count"])
        self.assertEqual(full["sampled_count"], full["rendered_count_observation"])
        reduced = cases["reduced_sample_case"]
        self.assertLess(
            reduced["rendered_count_observation"],
            reduced["visible_count_observation"],
        )
        self.assertTrue(cases["mask_visible_true"]["mask_visible_token"])
        self.assertFalse(cases["mask_visible_false_synthetic"]["mask_visible_token"])
        self.assertTrue(cases["source_lineage_guard_case"]["source_lineage_integrity_token"])
        self.assertEqual(cases["frame_remains_not_observed"]["frame_visible_token"], "not_observed")

    def test_sampling_visibility_oracle_results(self) -> None:
        packet = run_probe_packet()
        observed = {
            row["oracle_result"] for row in packet["sampling_visibility_oracle_results"]
        }
        self.assertEqual(observed, set(SCRIPT_UPDATE_PACKET["required_oracle_results"]))
        main_oracle = packet["oracle"]
        self.assertNotEqual(
            main_oracle["oracle_result"],
            "transparent_globe_leak_candidate",
        )
        self.assertFalse(main_oracle["transparent_globe_leak_fix_claimed"])

    def test_runtime_boundaries_remain_false(self) -> None:
        packet = run_probe_packet()
        decision = packet["decision_output"]
        for key, expected in SCRIPT_UPDATE_PACKET["required_runtime_boundaries"].items():
            if key == "source_lineage_integrity_token":
                self.assertIs(packet["token_packet"][key], expected)
            else:
                self.assertIs(decision[key], expected, key)
        self.assertTrue(decision["runtime_probe_executed"])
        self.assertEqual(packet["recommended_next_gate"], EXPECTED_NEXT_GATE)

    def test_boundary_statement(self) -> None:
        self.assertIn("Synthetic-only sampling/count", BOUNDARY_STATEMENT)
        self.assertIn("no renderer", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
