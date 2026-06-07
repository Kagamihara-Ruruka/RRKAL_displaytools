import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_layer_render_plan_cache_diagnostics_import_boundary import (
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_layer_render_plan_cache_diagnostics_import_boundary.py"


class LayerRenderPlanCacheDiagnosticsImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_returns_not_applicable_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_layer_render_plan_cache_diagnostics.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])
        self.assertTrue(packet["cache_word_allowed_in_helper_names"])
        self.assertTrue(packet["cache_lifecycle_modules_forbidden"])

    def test_current_candidate_passes_boundary(self):
        packet = validate_target(REPO_ROOT / "render_core" / "layer_render_plan_cache_diagnostics.py")

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_safe_cache_diagnostics_source_passes(self):
        source = (
            "from __future__ import annotations\n"
            "import json\n"
            "\n"
            "def build_layer_render_plan_cache_key(runtime_snapshot):\n"
            "    return json.dumps({'cache_key': runtime_snapshot}, sort_keys=True)\n"
            "\n"
            "def build_layer_render_plan_cache_invalidation_reasons():\n"
            "    return ['cache_key_match']\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_direct_imports_fail(self):
        snippets = [
            "import taichi_global_bathymetry\n",
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

    def test_render_plan_queue_dispatch_and_alpha_imports_fail(self):
        snippets = [
            "from render_core.render_plan import build_layer_render_plan_cache_key\n",
            "from render_core.layer_render_plan_compose_queue import build_layer_render_plan_compose_runs\n",
            "from render_core.layer_render_plan_composition_dispatch import build_layer_render_plan_composition_dispatch_packet\n",
            "from render_core.render_plan import alpha_compose\n",
            "def f():\n    return alpha_compose_transparent\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_metadata_artifact_parser_normalizer_policy_imports_fail(self):
        snippets = [
            "from render_core.metadata import build_renderer_output_metadata_payload\n",
            "from render_core.preview import write_preview_frame_png\n",
            "from taichi_global_bathymetry import write_compose_parity_artifacts\n",
            "from render_core.dataframe_normalizers import normalize_aircraft_frame\n",
            "from taichi_global_bathymetry import dataframe_from_json\n",
            "from render_core.datashader_sampling_policy import DatashaderSamplingPolicy\n",
            "from render_core.layer_render_budget_policy import LayerRenderBudgetPolicy\n",
            "from render_core.adaptive_render_quality_policy import AdaptiveRenderQualityPolicy\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_cache_word_allowed_but_cache_lifecycle_modules_fail(self):
        safe_source = (
            "def build_cache_key(cache_key):\n"
            "    local_cache_status = 'cache_key_match'\n"
            "    return {'cache_key': cache_key, 'cache_status': local_cache_status}\n"
        )
        self.assertTrue(validate_source(safe_source)["boundary_passed"])

        snippets = [
            "from provider_cache_loader import load_cache\n",
            "from layer_cache_store import write_cache\n",
            "from source_download_cache import fetch_remote\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_cli_missing_target_output_is_valid_json(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_layer_render_plan_cache_diagnostics.py")],
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
            target = Path(tmpdir) / "bad_cache_diagnostics.py"
            target.write_text("from render_core.metadata import build_renderer_output_metadata_payload\n", encoding="utf-8")
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
