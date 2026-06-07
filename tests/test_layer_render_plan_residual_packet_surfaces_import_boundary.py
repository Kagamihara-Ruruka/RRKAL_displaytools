import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_layer_render_plan_residual_packet_surfaces_import_boundary import (
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "scripts"
    / "validate_layer_render_plan_residual_packet_surfaces_import_boundary.py"
)


class LayerRenderPlanResidualPacketSurfacesImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_returns_not_applicable_pass(self):
        packet = validate_target(
            REPO_ROOT / "render_core" / "missing_layer_render_plan_residual_packet_surfaces.py"
        )

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])
        self.assertTrue(packet["alpha_helpers_excluded"])
        self.assertTrue(packet["apply_path_excluded"])

    def test_safe_source_passes_with_preserved_string_labels(self):
        source = (
            "from __future__ import annotations\n"
            "\n"
            "def build_layer_render_plan_style_postprocess_packet(style_profile):\n"
            "    return {\n"
            "        'apply_helper': 'apply_style_profile',\n"
            "        'composition_helper': 'HybridRenderController.apply_layer_render_plan_composition',\n"
            "        'kind': 'alpha_blend',\n"
            "        'single_pass_target': 'future_unified_taichi_render_plan',\n"
            "        'runtime_optimization_applied': False,\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_runtime_and_data_imports_fail(self):
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

    def test_render_plan_alpha_and_apply_path_imports_or_names_fail(self):
        snippets = [
            "from render_core.render_plan import build_layer_render_plan_runtime_snapshot\n",
            "from render_core.render_plan import alpha_compose\n",
            "def f():\n    return alpha_blend_compose\n",
            "from render_core.render_plan import build_layer_render_plan_apply_path\n",
            "def f():\n    return build_layer_render_plan_apply_path\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_controller_method_names_fail(self):
        snippets = [
            "from taichi_global_bathymetry import HybridRenderController\n",
            "def f(controller):\n    return controller.apply_layer_render_plan_composition\n",
            "def f():\n    return merge_alpha_compose_overlay_run\n",
            "def f():\n    return apply_layer_render_plan_merged_candidate_composition\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_sibling_helper_imports_fail(self):
        snippets = [
            "from render_core.layer_render_plan_compose_queue import build_layer_render_plan_compose_runs\n",
            "from render_core.layer_render_plan_composition_dispatch import build_layer_render_plan_composition_dispatch_packet\n",
            "from render_core.layer_render_plan_cache_diagnostics import build_layer_render_plan_cache_key\n",
            "from render_core.layer_render_plan_execution_phase_timing import build_layer_render_plan_execution_summary\n",
            "from render_core.layer_render_plan_adapter_preflight import build_layer_render_plan_adapter_payload\n",
            "from render_core.layer_render_plan_compiled_reused_packets import build_compiled_layer_render_plan_packet\n",
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
            "def f():\n    return write_runtime_metadata_payload\n",
            "def f():\n    return write_runtime_artifact_packet\n",
            "from metadata_sidecar_writer import write_sidecar\n",
            "from render_core.dataframe_normalizers import normalize_aircraft_frame\n",
            "from taichi_global_bathymetry import dataframe_from_json\n",
            "from render_core.point_overlay_budget_policy import PointOverlayBudgetPolicy\n",
            "from render_core.datashader_sampling_policy import DatashaderSamplingPolicy\n",
            "from render_core.layer_render_budget_policy import LayerRenderBudgetPolicy\n",
            "from render_core.adaptive_render_quality_policy import AdaptiveRenderQualityPolicy\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_provider_source_loader_download_cache_lifecycle_imports_fail(self):
        snippets = [
            "from provider_loader import load_provider\n",
            "from source_loader import load_source\n",
            "from rrkal_download_source import fetch_remote_source\n",
            "from layer_cache_loader import load_cache\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_cli_missing_target_output_is_valid_json(self):
        result = subprocess.run(
            [
                sys.executable,
                "-B",
                str(SCRIPT),
                str(REPO_ROOT / "render_core" / "missing_layer_render_plan_residual_packet_surfaces.py"),
            ],
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
            target = Path(tmpdir) / "bad_residual_packet_surfaces.py"
            target.write_text(
                "from render_core.render_plan import build_layer_render_plan_apply_path\n",
                encoding="utf-8",
            )
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
