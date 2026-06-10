from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import validate_displaytools_dynamic_point_presentation_reduction_import_boundary as checker


class DynamicPointPresentationReductionImportBoundaryCheckerTest(unittest.TestCase):
    def test_default_target_is_presentation_reduction_boundary(self) -> None:
        self.assertEqual(
            checker.DEFAULT_TARGET,
            Path("render_core/dynamic_point_presentation_reduction_boundary.py"),
        )

    def test_missing_target_passes_as_not_applicable(self) -> None:
        packet = checker.validate_target(Path("render_core/dynamic_point_presentation_reduction_boundary.py"))
        self.assertFalse(packet["candidate_exists"])
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])
        self.assertFalse(packet["target_imported"])
        self.assertFalse(packet["target_executed"])

    def test_clean_synthetic_candidate_passes(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_allowed_string_labels_pass_only_as_data(self) -> None:
        source = "LABELS = " + repr(sorted(checker.ALLOWED_STRING_LABELS)) + "\n"
        packet = checker.validate_source(source)
        self.assertTrue(packet["boundary_passed"])
        executable_packet = checker.validate_source("def f():\n    return rendered_lower_than_visible\n")
        self.assertFalse(executable_packet["boundary_passed"])
        self.assertEqual(executable_packet["violations"][0]["forbidden_family"], "label_executable_reference")

    def test_forbidden_imports_fail(self) -> None:
        cases = {
            "monolith": "import taichi_global_bathymetry\n",
            "runtime_probe": "from scripts.dynamic_point_lod_view_frame_one_shot_runtime_probe import run_probe\n",
            "renderer_runtime": "import taichi\n",
            "dataframe_runtime": "import numpy\n",
            "cache_database_io": "import sqlite3\n",
        }
        for family, source in cases.items():
            with self.subTest(family=family):
                packet = checker.validate_source(source)
                self.assertFalse(packet["boundary_passed"])
                self.assertIn(family, {violation["forbidden_family"] for violation in packet["violations"]})

    def test_forbidden_names_attributes_calls_and_defs_fail(self) -> None:
        cases = {
            "render_if_needed": "def f():\n    return render_if_needed()\n",
            "controller_runtime": "class HybridRenderController:\n    pass\n",
            "renderer_runtime": "def f(renderer):\n    return renderer.render(None)\n",
            "frame_buffer": "def f():\n    return frame_rgba\n",
            "artifact_writer": "def f(Image):\n    return Image.fromarray(None).save('x.png')\n",
            "projection_formula": "def f():\n    return project_ais_to_screen(None)\n",
            "mask_formula": "def f():\n    return mask_overlay_to_globe(None, None)\n",
            "sampling_formula_movement": "def f():\n    return _sample_projected_frame(None, 'ais')\n",
            "alpha_compose_formula": "def f():\n    return alpha_compose(None, None)\n",
            "source_lineage_mutation": "def f():\n    return mutate_source_lineage()\n",
            "source_loss_interpretation": "rendered_lower_than_visible_means_source_loss = True\n",
            "frame_truth_claim": "frame_truth_claimed = True\n",
            "transparent_globe_leak_inference": "transparent_globe_leak_inferred = True\n",
            "correctness_claim": "visual_correctness_claimed = True\n",
            "visual_parity_claim": "visual_parity_claimed = True\n",
            "readiness_claim": "readiness_claimed = True\n",
            "performance_claim": "performance_claimed = True\n",
            "transparent_globe_leak_fix_claim": "transparent_globe_leak_fix_claimed = True\n",
            "c4_odoriba_bypass": "c4_odoriba_bypass = True\n",
        }
        for family, source in cases.items():
            with self.subTest(family=family):
                packet = checker.validate_source(source)
                self.assertFalse(packet["boundary_passed"])
                self.assertIn(family, {violation["forbidden_family"] for violation in packet["violations"]})

    def test_syntax_error_json_fail_with_nonzero_exit(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as handle:
            handle.write("def broken(:\n")
            path = Path(handle.name)
        try:
            completed = subprocess.run(
                [sys.executable, "-B", "scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(completed.returncode, 0)
            packet = json.loads(completed.stdout)
            self.assertEqual(packet["status"], "syntax_error")
            self.assertFalse(packet["boundary_passed"])
        finally:
            path.unlink(missing_ok=True)

    def test_self_test_negative_covers_all_forbidden_families(self) -> None:
        packet = checker.run_self_test_negative()
        self.assertTrue(packet["negative_self_test_passed"])
        self.assertTrue(packet["all_forbidden_snippets_detected"])
        self.assertTrue(packet["clean_synthetic_candidate_passed"])
        self.assertTrue(packet["allowed_string_labels_passed"])
        self.assertTrue(packet["allowed_string_label_distinction_preserved"])
        families = {row["family"] for row in packet["results"]}
        self.assertEqual(families, set(checker.FORBIDDEN_FAMILIES))

    def test_decision_packet_closes_runtime_and_claim_authorizations(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertTrue(packet["presentation_reduction_import_boundary_checker_created"])
        self.assertFalse(packet["helper_creation_authorized"])
        self.assertFalse(packet["runtime_execution_authorized"])
        self.assertFalse(packet["source_loss_interpretation_authorized"])
        self.assertFalse(packet["frame_truth_claim_authorized"])
        self.assertFalse(packet["transparent_globe_leak_inferred"])
        self.assertFalse(packet["readiness_claimed"])
        self.assertFalse(packet["performance_claimed"])
        self.assertFalse(packet["c4_odoriba_bypass_authorized"])


if __name__ == "__main__":
    unittest.main()
