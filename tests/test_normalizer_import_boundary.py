import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_normalizer_import_boundary import validate_source, validate_target


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_normalizer_import_boundary.py"


class NormalizerImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_returns_not_applicable_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_dataframe_normalizers.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_safe_source_passes(self):
        packet = validate_source("import pandas as pd\nimport numpy as np\nfrom typing import Iterable\n")

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_import_fails(self):
        packet = validate_source("import taichi as ti\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["module"], "taichi")

    def test_pyais_import_is_forbidden(self):
        packet = validate_source("import pyais\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["module"], "pyais")

    def test_from_import_forbidden_name_fails(self):
        packet = validate_source("from taichi_global_bathymetry import HybridRenderController\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("HybridRenderController", packet["violations"][0]["names"])

    def test_cli_missing_candidate_output_is_json(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_dataframe_normalizers.py")],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])

    def test_cli_forbidden_file_exits_nonzero_and_outputs_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_normalizer.py"
            target.write_text("from PyQt6 import QtWidgets\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), str(target)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=10,
            )

        self.assertNotEqual(result.returncode, 0)
        packet = json.loads(result.stdout)
        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])

    def test_self_test_negative_passes(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--self-test-negative"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertTrue(packet["negative_self_test_passed"])
        self.assertTrue(packet["all_forbidden_snippets_detected"])


if __name__ == "__main__":
    unittest.main()
