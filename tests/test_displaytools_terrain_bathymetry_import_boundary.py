import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_displaytools_terrain_bathymetry_import_boundary import (
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_displaytools_terrain_bathymetry_import_boundary.py"


class DisplaytoolsTerrainBathymetryImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_cli_returns_json_pass(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "terrain_bathymetry_boundary.py")],
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
        self.assertEqual(packet["violations"], [])

    def test_missing_candidate_function_returns_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_terrain_bathymetry_boundary.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_valid_descriptor_only_candidate_passes(self):
        source = (
            "from __future__ import annotations\n"
            "\n"
            "def build_terrain_descriptor():\n"
            "    return {\n"
            "        'cache_status': 'cache_hit',\n"
            "        'lod': 'resolution label',\n"
            "        'bump': 'string label only',\n"
            "        'lighting': 'consumer label only',\n"
            "        'palette': 'style label only',\n"
            "        'projection': 'string label only',\n"
            "        'flip': 'string label only',\n"
            "        'runtime_dependency_allowed': False,\n"
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
        self.assertEqual(packet["violations"][0]["kind"], "import")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "monolith")

    def test_forbidden_import_from_fails(self):
        packet = validate_source("from PyQt6 import QtWidgets\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["kind"], "from_import")

    def test_forbidden_name_reference_fails(self):
        packet = validate_source("def f():\n    return load_topography\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("load_topography", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "name_reference")

    def test_forbidden_attribute_reference_fails(self):
        packet = validate_source("def f(obj):\n    return obj.light_dir\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("light_dir", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "attribute_reference")

    def test_forbidden_call_target_fails(self):
        packet = validate_source("def f():\n    return compute_sun_direction()\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("compute_sun_direction", packet["checked_names"])
        kinds = {violation["kind"] for violation in packet["violations"]}
        self.assertIn("call_target", kinds)

    def test_forbidden_class_definition_fails(self):
        packet = validate_source("class TaichiGlobeRenderer:\n    pass\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("TaichiGlobeRenderer", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "class_definition")

    def test_forbidden_function_definition_fails(self):
        packet = validate_source("def load_topography():\n    return {}\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("load_topography", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "function_definition")

    def test_forbidden_async_function_definition_fails(self):
        packet = validate_source("async def cache_hit():\n    return True\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("cache_hit", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "async_function_definition")

    def test_allowed_string_labels_pass(self):
        source = (
            "def f():\n"
            "    return {\n"
            "        'cache_hit': 'label only',\n"
            "        'cache_miss': 'label only',\n"
            "        'lod': 'label only',\n"
            "        'resolution': 'label only',\n"
            "        'bump': 'label only',\n"
            "        'lighting': 'label only',\n"
            "        'palette': 'label only',\n"
            "        'fallback': 'label only',\n"
            "        'known_fault': 'label only',\n"
            "        'projection': 'label only',\n"
            "        'flip': 'label only',\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])

    def test_syntax_error_returns_json_shape_and_nonpass(self):
        packet = validate_source("def broken(:\n")

        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])
        self.assertTrue(packet["violations"])
        self.assertIn("schema", packet)
        self.assertIn("checked_imports", packet)
        self.assertEqual(packet["violations"][0]["forbidden_family"], "syntax_error")

    def test_cli_forbidden_file_exits_nonzero_with_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_terrain_bathymetry_boundary.py"
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
        self.assertTrue(packet["violations"])

    def test_cli_json_shape_is_pinned(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "terrain_bathymetry_boundary.py")],
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

    def test_negative_self_test_passes_and_detects_all_snippets(self):
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
        self.assertTrue(packet["boundary_passed"])


if __name__ == "__main__":
    unittest.main()
