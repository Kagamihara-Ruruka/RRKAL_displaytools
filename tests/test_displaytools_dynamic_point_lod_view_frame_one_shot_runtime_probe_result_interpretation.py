"""Interpretation gate for the first one-shot synthetic runtime probe result."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame one-shot runtime probe result "
    "interpretation gate. No production source change, no probe expansion, no "
    "renderer execution, no controller instantiation, no artifact generation, "
    "no formula or renderer behavior change, no correctness/readiness/fix "
    "claim, and no push."
)


def run_probe_packet() -> dict:
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


def build_interpretation_packet(probe_packet: dict) -> dict:
    decision = probe_packet["decision_output"]
    token_packet = probe_packet["token_packet"]
    seam_summary = probe_packet["seam_call_summary"]
    import_safety = probe_packet["import_safety"]
    observed = {
        "runtime_probe_executed": probe_packet["runtime_probe_executed"],
        "project_ais_to_screen_called": seam_summary["project_ais_to_screen_called"],
        "project_aircraft_to_screen_called": seam_summary[
            "project_aircraft_to_screen_called"
        ],
        "mask_overlay_to_globe_called": seam_summary["mask_overlay_to_globe_called"],
        "render_if_needed_called": seam_summary["render_if_needed_called"],
        "controller_instantiated": decision["controller_instantiated"],
        "renderer_executed": decision["renderer_executed"],
        "artifact_written": decision["artifact_written"],
        "stdout_only": decision["stdout_only"],
        "import_stdout_suppressed": import_safety["import_stdout_suppressed"],
        "source_present_token": token_packet["source_present_token"],
        "projected_visible_token": token_packet["projected_visible_token"],
        "overlay_rendered_token": token_packet["overlay_rendered_token"],
        "mask_visible_token": token_packet["mask_visible_token"],
        "source_lineage_integrity_token": token_packet[
            "source_lineage_integrity_token"
        ],
    }
    unobserved = {
        "sampled_visible_token": token_packet["sampled_visible_token"],
        "frame_visible_token": token_packet["frame_visible_token"],
        "visible_count_observation": token_packet["visible_count_observation"],
        "rendered_count_observation": token_packet["rendered_count_observation"],
    }
    decision_output = {
        "interpretation_gate_passed": True,
        "projection_seams_callable_by_synthetic_one_shot": True,
        "source_lineage_pollution_observed": False,
        "mask_visible_path_observed": True,
        "sampling_observed": False,
        "frame_visibility_observed": False,
        "rendered_count_observed": False,
        "transparent_globe_leak_observed": False,
        "probe_expansion_authorized": False,
        "render_if_needed_authorized": False,
        "controller_instantiation_authorized": False,
        "renderer_execution_authorized": False,
        "artifact_generation_authorized": False,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
        "readiness_claimed": False,
        "recommended_next_gate": (
            "dynamic_point_lod_view_frame_sampling_visibility_followup_planning_gate"
        ),
    }
    return {
        "schema": (
            "rrkal.displaytools.dynamic_point_lod_view_frame_one_shot_runtime_"
            "probe_result_interpretation.v1"
        ),
        "probe_status": probe_packet["status"],
        "observed_result": observed,
        "not_observed_result": unobserved,
        "oracle_result": probe_packet["oracle"]["oracle_result"],
        "supported_decisions": [
            "projection_aircraft_projection_and_globe_mask_seams_callable",
            "source_lineage_not_observed_polluted",
            "mask_visible_path_exists",
        ],
        "unsupported_decisions": [
            "sampling_visibility",
            "frame_visibility",
            "rendered_count",
            "transparent_globe_leak",
            "coordinate_correctness",
            "visual_correctness",
            "readiness",
            "leak_fix",
        ],
        "decision_output": decision_output,
        "boundary_statement": BOUNDARY_STATEMENT,
    }


class DynamicPointRuntimeProbeResultInterpretationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.probe_packet = run_probe_packet()
        cls.packet = build_interpretation_packet(cls.probe_packet)

    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "probe_status",
                "observed_result",
                "not_observed_result",
                "oracle_result",
                "supported_decisions",
                "unsupported_decisions",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_one_shot_runtime_"
            "probe_result_interpretation.v1",
        )

    def test_runtime_probe_stdout_was_full_json(self) -> None:
        self.assertEqual(self.probe_packet["status"], "runtime_probe_stdout_packet")
        self.assertTrue(self.probe_packet["runtime_probe_executed"])

    def test_required_observed_points(self) -> None:
        observed = self.packet["observed_result"]
        for key in (
            "runtime_probe_executed",
            "project_ais_to_screen_called",
            "project_aircraft_to_screen_called",
            "mask_overlay_to_globe_called",
            "stdout_only",
            "import_stdout_suppressed",
            "source_present_token",
            "projected_visible_token",
            "overlay_rendered_token",
            "mask_visible_token",
            "source_lineage_integrity_token",
        ):
            self.assertIs(observed[key], True, key)
        for key in (
            "render_if_needed_called",
            "controller_instantiated",
            "renderer_executed",
            "artifact_written",
        ):
            self.assertIs(observed[key], False, key)

    def test_required_not_observed_points(self) -> None:
        unobserved = self.packet["not_observed_result"]
        self.assertEqual(
            unobserved,
            {
                "sampled_visible_token": "not_observed",
                "frame_visible_token": "not_observed",
                "visible_count_observation": "not_observed",
                "rendered_count_observation": "not_observed",
            },
        )

    def test_interpretation_supported_and_unsupported_decisions(self) -> None:
        self.assertEqual(
            set(self.packet["supported_decisions"]),
            {
                "projection_aircraft_projection_and_globe_mask_seams_callable",
                "source_lineage_not_observed_polluted",
                "mask_visible_path_exists",
            },
        )
        self.assertIn("sampling_visibility", self.packet["unsupported_decisions"])
        self.assertIn("frame_visibility", self.packet["unsupported_decisions"])
        self.assertIn("rendered_count", self.packet["unsupported_decisions"])
        self.assertIn("transparent_globe_leak", self.packet["unsupported_decisions"])

    def test_decision_output_boundaries_and_next_gate(self) -> None:
        decision = self.packet["decision_output"]
        self.assertTrue(decision["interpretation_gate_passed"])
        self.assertTrue(decision["projection_seams_callable_by_synthetic_one_shot"])
        self.assertFalse(decision["source_lineage_pollution_observed"])
        self.assertTrue(decision["mask_visible_path_observed"])
        self.assertFalse(decision["sampling_observed"])
        self.assertFalse(decision["frame_visibility_observed"])
        self.assertFalse(decision["rendered_count_observed"])
        self.assertFalse(decision["transparent_globe_leak_observed"])
        for key in (
            "probe_expansion_authorized",
            "render_if_needed_authorized",
            "controller_instantiation_authorized",
            "renderer_execution_authorized",
            "artifact_generation_authorized",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "transparent_globe_leak_fix_claimed",
            "readiness_claimed",
        ):
            self.assertIs(decision[key], False, key)
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_sampling_visibility_followup_planning_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("No production source change", BOUNDARY_STATEMENT)
        self.assertIn("no probe expansion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
