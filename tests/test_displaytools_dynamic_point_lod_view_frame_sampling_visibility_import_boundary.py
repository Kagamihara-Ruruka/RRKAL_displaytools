"""Tests for the dynamic point sampling visibility import-boundary checker."""

from __future__ import annotations

import ast
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import validate_displaytools_dynamic_point_sampling_visibility_import_boundary as checker


class DynamicPointSamplingVisibilityImportBoundaryTest(unittest.TestCase):
    def test_default_target_is_sampling_visibility_boundary(self) -> None:
        self.assertEqual(
            checker.DEFAULT_TARGET,
            Path("render_core/dynamic_point_sampling_visibility_boundary.py"),
        )

    def test_missing_target_passes_as_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing.py"
            packet = checker.validate_target(missing)
        self.assertFalse(packet["candidate_exists"])
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_clean_synthetic_candidate_passes(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_allowed_string_labels_pass(self) -> None:
        source = "LABELS = " + repr(sorted(checker.ALLOWED_STRING_LABELS)) + "\n"
        packet = checker.validate_source(source)
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_imports_fail(self) -> None:
        packet = checker.validate_source("import taichi_global_bathymetry\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["forbidden_family"], "monolith")
        packet = checker.validate_source("from taichi_global_bathymetry import render_if_needed\n")
        families = {row["forbidden_family"] for row in packet["violations"]}
        self.assertIn("monolith", families)
        self.assertIn("render_if_needed", families)

    def test_forbidden_names_fail(self) -> None:
        packet = checker.validate_source("value = frame_rgba\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["forbidden_family"], "frame_buffer")

    def test_forbidden_attributes_fail(self) -> None:
        packet = checker.validate_source("def f(renderer):\n    return renderer.render(None)\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn(
            "renderer_runtime",
            {row["forbidden_family"] for row in packet["violations"]},
        )

    def test_forbidden_calls_fail(self) -> None:
        snippets = {
            "projection_formula": "def f():\n    return project_ais_to_screen(None)\n",
            "mask_formula": "def f():\n    return mask_overlay_to_globe(None, None)\n",
            "artifact_writer": "def f(Image):\n    return Image.fromarray(None).save('x.png')\n",
            "dataframe_runtime": "def f(pd):\n    return pd.DataFrame([])\n",
        }
        for family, snippet in snippets.items():
            packet = checker.validate_source(snippet)
            self.assertFalse(packet["boundary_passed"], family)
            self.assertIn(family, {row["forbidden_family"] for row in packet["violations"]})

    def test_forbidden_function_and_class_declarations_fail(self) -> None:
        packet = checker.validate_source("def render_if_needed():\n    return None\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["forbidden_family"], "render_if_needed")
        packet = checker.validate_source("class HybridRenderController:\n    pass\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["forbidden_family"], "controller_runtime")

    def test_syntax_error_returns_json_fail(self) -> None:
        packet = checker.validate_source("def broken(:\n    pass\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["status"], "syntax_error")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "syntax_error")

    def test_negative_self_test_detects_all_forbidden_families(self) -> None:
        packet = checker.run_self_test_negative()
        self.assertTrue(packet["negative_self_test_passed"])
        self.assertTrue(packet["all_forbidden_snippets_detected"])
        self.assertTrue(packet["clean_synthetic_candidate_passed"])
        self.assertTrue(packet["allowed_string_labels_passed"])
        self.assertEqual(
            {row["family"] for row in packet["results"]},
            set(checker.FORBIDDEN_FAMILIES),
        )

    def test_checker_does_not_import_target(self) -> None:
        source = Path(checker.__file__).read_text(encoding="utf-8")
        self.assertNotIn("importlib", source)
        self.assertNotIn("__import__", source)
        self.assertNotIn("exec(", source)
        self.assertNotIn("eval(", source)

    def test_ast_node_coverage_is_declared(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertEqual(
            set(packet["checked_node_types"]),
            {
                "ast.Import",
                "ast.ImportFrom",
                "ast.Name",
                "ast.Attribute",
                "ast.Call",
                "ast.FunctionDef",
                "ast.AsyncFunctionDef",
                "ast.ClassDef",
            },
        )

    def test_cli_missing_target_and_self_test(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "candidate.py"
            completed = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    "scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py",
                    str(missing),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        packet = json.loads(completed.stdout)
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(packet["boundary_passed"])

        completed = subprocess.run(
            [
                sys.executable,
                "-B",
                "scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py",
                "--self-test-negative",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        packet = json.loads(completed.stdout)
        self.assertTrue(packet["negative_self_test_passed"])

    def test_imported_modules_are_standard_library_only(self) -> None:
        source = Path(checker.__file__).read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported.add((node.module or "").split(".", 1)[0])
        self.assertEqual(imported, {"__future__", "argparse", "ast", "json", "pathlib"})

    def test_module_can_import_safely(self) -> None:
        spec = importlib.util.spec_from_file_location(
            "sampling_visibility_checker_safe_import",
            "scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py",
        )
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(str(module.DEFAULT_TARGET), "render_core\\dynamic_point_sampling_visibility_boundary.py")


if __name__ == "__main__":
    unittest.main()
