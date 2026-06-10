"""Tests for the bounded one-shot synthetic runtime probe shell."""

from __future__ import annotations

import ast
import inspect
import json
import subprocess
import sys
import unittest

from scripts import dynamic_point_lod_view_frame_one_shot_runtime_probe as probe


class DynamicPointLodViewFrameOneShotRuntimeProbeTest(unittest.TestCase):
    def test_allowed_runtime_seams_are_exact(self) -> None:
        self.assertEqual(
            set(probe.ALLOWED_RUNTIME_SEAMS),
            {
                "project_ais_to_screen",
                "project_aircraft_to_screen",
                "mask_overlay_to_globe",
            },
        )

    def test_self_test_does_not_execute_runtime_probe(self) -> None:
        packet = probe.build_self_test_packet()
        self.assertEqual(packet["status"], "self_test_passed")
        self.assertFalse(packet["runtime_probe_executed"])
        self.assertFalse(packet["monolith_imported"])
        self.assertTrue(packet["dry_self_test_passed"])
        decision = packet["decision_output"]
        self.assertFalse(decision["runtime_probe_executed"])
        self.assertFalse(decision["import_safety_passed"])
        self.assertFalse(decision["project_ais_to_screen_called"])
        self.assertFalse(decision["project_aircraft_to_screen_called"])
        self.assertFalse(decision["mask_overlay_to_globe_called"])
        self.assertFalse(decision["render_if_needed_called"])

    def test_blocked_packet_shape_and_boundaries(self) -> None:
        packet = probe.blocked_packet("blocked_import_safety", "fixture")
        self.assertEqual(packet["status"], "blocked_import_safety")
        self.assertFalse(packet["runtime_probe_executed"])
        self.assertEqual(packet["token_packet"]["source_present_token"], "not_observed")
        self.assertEqual(packet["oracle"]["oracle_result"], "not_observed")
        self.assertFalse(packet["oracle"]["transparent_globe_leak_fix_claimed"])
        self.assertFalse(packet["oracle"]["coordinate_correctness_claimed"])
        self.assertFalse(packet["oracle"]["visual_correctness_claimed"])
        self.assertFalse(packet["oracle"]["readiness_claimed"])
        self.assertEqual(
            packet["recommended_next_gate"],
            "dynamic_point_lod_view_frame_one_shot_runtime_probe_blocker_closure_gate",
        )

    def test_oracle_preserves_unknown_downstream_tokens(self) -> None:
        token_packet = probe.build_token_packet(
            source_present_token=True,
            projected_visible_token=True,
            sampled_visible_token="not_observed",
            overlay_rendered_token=True,
            mask_visible_token=True,
            frame_visible_token="not_observed",
            source_lineage_integrity_token=True,
            visible_count_observation="not_observed",
            rendered_count_observation="not_observed",
        )
        result = probe.evaluate_runtime_oracle(token_packet)
        self.assertEqual(result["oracle_result"], "path_preserved_or_not_enough_evidence")

    def test_oracle_classifies_projection_drop_and_mask_hide(self) -> None:
        projection_drop = probe.build_token_packet(
            source_present_token=True,
            projected_visible_token=False,
            sampled_visible_token="not_observed",
            overlay_rendered_token="not_observed",
            mask_visible_token="not_observed",
            frame_visible_token="not_observed",
            source_lineage_integrity_token=True,
            visible_count_observation="not_observed",
            rendered_count_observation="not_observed",
        )
        self.assertEqual(
            probe.evaluate_runtime_oracle(projection_drop)["oracle_result"],
            "projection_or_horizon_responsibility",
        )
        mask_hide = probe.build_token_packet(
            source_present_token=True,
            projected_visible_token=True,
            sampled_visible_token="not_observed",
            overlay_rendered_token=True,
            mask_visible_token=False,
            frame_visible_token="not_observed",
            source_lineage_integrity_token=True,
            visible_count_observation="not_observed",
            rendered_count_observation="not_observed",
        )
        self.assertEqual(
            probe.evaluate_runtime_oracle(mask_hide)["oracle_result"],
            "globe_mask_responsibility",
        )

    def test_decision_output_has_required_false_boundaries(self) -> None:
        decision = probe._decision()
        self.assertTrue(decision["runtime_probe_execution_gate_passed"])
        self.assertFalse(decision["render_if_needed_called"])
        self.assertFalse(decision["controller_instantiated"])
        self.assertFalse(decision["renderer_executed"])
        self.assertFalse(decision["artifact_written"])
        self.assertFalse(decision["live_source_used"])
        self.assertFalse(decision["db_cache_used"])
        self.assertTrue(decision["stdout_only"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])

    def test_signature_expectations_cover_selected_functions_only(self) -> None:
        self.assertEqual(set(probe.EXPECTED_SIGNATURES), set(probe.ALLOWED_RUNTIME_SEAMS))
        self.assertEqual(
            probe.EXPECTED_SIGNATURES["mask_overlay_to_globe"],
            ("overlay", "globe_mask"),
        )
        self.assertNotIn("render_if_needed", probe.EXPECTED_SIGNATURES)

    def test_source_has_no_forbidden_runtime_helpers_or_artifact_writes(self) -> None:
        source = inspect.getsource(probe)
        self.assertNotIn(".save(", source)
        self.assertNotIn("write_preview_frame_png(", source)
        self.assertNotIn("sys.settrace", source)
        self.assertNotIn("__getattribute__", source.replace("no __getattribute__", ""))
        self.assertNotIn("__array__", source)
        self.assertNotIn("subprocess", source)
        self.assertNotIn("requests", source)
        self.assertNotIn("socket", source)

    def test_ast_imports_are_limited(self) -> None:
        source = inspect.getsource(probe)
        tree = ast.parse(source)
        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_roots.add((node.module or "").split(".", 1)[0])
        self.assertEqual(imported_roots, {"__future__", "contextlib", "importlib", "inspect", "io", "json", "pathlib", "sys", "typing", "scripts"})

    def test_run_probe_stdout_is_single_json_packet(self) -> None:
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
        packet = json.loads(completed.stdout)
        self.assertEqual(packet["status"], "runtime_probe_stdout_packet")
        self.assertTrue(packet["import_safety"]["import_stdout_suppressed"])
        self.assertGreaterEqual(packet["import_safety"]["import_stdout_line_count"], 1)
        self.assertNotIn("[Taichi]", completed.stdout)
        self.assertIn("import_stderr_suppressed", packet["import_safety"])


if __name__ == "__main__":
    unittest.main()
