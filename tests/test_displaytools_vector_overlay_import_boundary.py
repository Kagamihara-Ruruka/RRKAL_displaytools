import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_displaytools_vector_overlay_import_boundary import (
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_displaytools_vector_overlay_import_boundary.py"


class DisplaytoolsVectorOverlayImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_returns_json_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_vector_overlay_boundary.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_valid_pure_descriptor_candidate_passes(self):
        source = (
            "from __future__ import annotations\n"
            "\n"
            "def build_vector_overlay_descriptor():\n"
            "    return {\n"
            "        'projection': 'vector-specific projection label',\n"
            "        'mask': 'globe_mask clipping label',\n"
            "        'cache_status': 'cache_hit',\n"
            "        'source_kind': 'GeoJSON descriptor label only',\n"
            "        'runtime_merge_enabled': False,\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_import_fails(self):
        packet = validate_source("import taichi_global_bathymetry\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])

    def test_forbidden_from_import_fails(self):
        packet = validate_source("from PyQt6 import QtWidgets\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])

    def test_forbidden_direct_name_reference_fails(self):
        packet = validate_source("def f():\n    return alpha_compose\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])

    def test_forbidden_controller_runtime_name_fails(self):
        snippets = [
            "def f():\n    return HybridRenderController\n",
            "def f():\n    return GeoVectorLineOverlay\n",
            "def f():\n    return TaichiGlobeRenderer\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_forbidden_provider_cache_executable_name_fails(self):
        snippets = [
            "def f():\n    return load_natural_earth\n",
            "def f():\n    return load_hydrology\n",
            "def f():\n    return cache_hit\n",
            "from provider_cache_loader import cache_miss\n",
        ]
        for source in snippets:
            with self.subTest(source=source):
                packet = validate_source(source)
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])

    def test_forbidden_class_definition_fails(self):
        packet = validate_source("class GeoVectorLineOverlay:\n    pass\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("GeoVectorLineOverlay", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "class_definition")

    def test_forbidden_function_definition_fails(self):
        packet = validate_source("def load_hydrology():\n    return []\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("load_hydrology", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "function_definition")

    def test_forbidden_async_function_definition_fails(self):
        packet = validate_source("async def cache_hit():\n    return True\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("cache_hit", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "async_function_definition")

    def test_allowed_string_label_passes(self):
        source = (
            "def f():\n"
            "    return {\n"
            "        'cache_hit': 'string label only',\n"
            "        'GeoJSON': 'string label only',\n"
            "        'projection': 'string label only',\n"
            "        'mask': 'string label only',\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])

    def test_malformed_python_fails_with_json_shape(self):
        packet = validate_source("def broken(:\n")

        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])
        self.assertTrue(packet["violations"])
        self.assertIn("schema", packet)
        self.assertIn("checked_imports", packet)

    def test_cli_missing_target_output_shape_is_pinned(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "vector_overlay_boundary.py")],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertEqual(
            set(packet),
            {
                "schema",
                "target",
                "candidate_exists",
                "status",
                "boundary_passed",
                "violations",
                "checked_imports",
                "checked_names",
                "forbidden_families",
                "string_labels_allowed_as_data",
                "runtime_render_invoked",
                "runtime_merge_enabled",
                "boundary",
            },
        )
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_cli_forbidden_file_exits_nonzero_with_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_vector_overlay_boundary.py"
            target.write_text("from render_core.render_plan import alpha_compose\n", encoding="utf-8")
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
