import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_datashader_policy_import_boundary import validate_source, validate_target


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_datashader_policy_import_boundary.py"


class DatashaderPolicyImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_returns_json_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "datashader_sampling_policy.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_safe_source_passes(self):
        packet = validate_source("from __future__ import annotations\n")

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_direct_import_fails(self):
        packet = validate_source("import taichi as ti\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["module"], "taichi")

    def test_forbidden_from_import_name_fails(self):
        packet = validate_source("from taichi_global_bathymetry import HybridRenderController\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("HybridRenderController", packet["violations"][0]["names"])

    def test_cli_missing_candidate_output_is_json(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "datashader_sampling_policy.py")],
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
            target = Path(tmpdir) / "bad_datashader_policy.py"
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

    def test_pyais_import_fails(self):
        packet = validate_source("import pyais\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])

    def test_dataframe_and_datashader_imports_fail(self):
        snippets = [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import datashader as ds\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_parser_normalizer_provider_and_point_policy_imports_fail(self):
        snippets = [
            "from taichi_global_bathymetry import dataframe_from_text\n",
            "from render_core.dataframe_normalizers import normalize_ais_frame\n",
            "from ocean_condition_provider import OceanConditionProvider\n",
            "from render_core.point_overlay_budget_policy import PointOverlayBudgetPolicy\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
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
