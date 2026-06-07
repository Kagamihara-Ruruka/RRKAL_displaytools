import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_layer_render_plan_composition_dispatch_import_boundary import (
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_layer_render_plan_composition_dispatch_import_boundary.py"


class LayerRenderPlanCompositionDispatchImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_returns_not_applicable_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_layer_render_plan_composition_dispatch.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_current_candidate_passes_boundary(self):
        packet = validate_target(REPO_ROOT / "render_core" / "layer_render_plan_composition_dispatch.py")

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_safe_source_passes(self):
        source = (
            "from __future__ import annotations\n"
            "\n"
            "def build_action(step):\n"
            "    return {'kind': str(step.get('kind') or '')}\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_import_fails(self):
        packet = validate_source("import taichi_global_bathymetry\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["module"], "taichi_global_bathymetry")

    def test_forbidden_from_import_name_fails(self):
        packet = validate_source("from taichi_global_bathymetry import HybridRenderController\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("HybridRenderController", packet["violations"][0]["names"])

    def test_runtime_ui_gpu_and_ndarray_imports_fail(self):
        snippets = [
            "import taichi as ti\n",
            "from PyQt6 import QtWidgets\n",
            "import vispy\n",
            "import numpy as np\n",
            "import pandas as pd\n",
            "import datashader as ds\n",
            "import pyais\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_render_plan_alpha_and_compose_queue_imports_fail(self):
        snippets = [
            "from render_core.render_plan import build_layer_render_plan_composition_apply_action\n",
            "from render_core.render_plan import alpha_compose\n",
            "from render_core.render_plan import alpha_blend_compose\n",
            "from render_core.layer_render_plan_compose_queue import build_layer_render_plan_compose_runs\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_metadata_artifact_parser_normalizer_provider_and_policy_imports_fail(self):
        snippets = [
            "from render_core.metadata import build_renderer_output_metadata_payload\n",
            "from render_core.preview import write_preview_frame_png\n",
            "from taichi_global_bathymetry import write_compose_parity_artifacts\n",
            "from render_core.dataframe_normalizers import normalize_aircraft_frame\n",
            "from taichi_global_bathymetry import dataframe_from_json\n",
            "from provider_cache_loader import fetch_layer\n",
            "from render_core.datashader_sampling_policy import DatashaderSamplingPolicy\n",
            "from render_core.layer_render_budget_policy import LayerRenderBudgetPolicy\n",
            "from render_core.adaptive_render_quality_policy import AdaptiveRenderQualityPolicy\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_cli_missing_target_output_is_valid_json(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_layer_render_plan_composition_dispatch.py")],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_cli_forbidden_file_exits_nonzero_with_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_composition_dispatch.py"
            target.write_text("from render_core.preview import write_preview_frame_png\n", encoding="utf-8")
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

    def test_negative_self_test_passes(self):
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
