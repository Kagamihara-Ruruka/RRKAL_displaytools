"""Tests for the dynamic point source-lineage guard import-boundary checker."""

from __future__ import annotations

import ast
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import validate_displaytools_dynamic_point_source_lineage_guard_import_boundary as checker
from tests import test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning as planning


class DynamicPointSourceLineageGuardImportBoundaryTest(unittest.TestCase):
    def test_default_target_is_source_lineage_guard_boundary(self) -> None:
        self.assertEqual(checker.DEFAULT_TARGET, Path("render_core/dynamic_point_source_lineage_guard_boundary.py"))

    def test_planning_gate_prerequisite(self) -> None:
        self.assertTrue(planning.PACKET["decision_output"]["source_lineage_guard_checker_planning_passed"])
        self.assertEqual(str(checker.DEFAULT_TARGET).replace("\\", "/"), planning.PACKET["future_helper_target"])
        self.assertEqual(
            "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py",
            planning.PACKET["future_checker_target"],
        )

    def test_missing_target_passes_as_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            packet = checker.validate_target(Path(temp_dir) / "missing.py")
        self.assertFalse(packet["candidate_exists"])
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])
        self.assertFalse(packet["target_imported"])
        self.assertFalse(packet["target_executed"])

    def test_clean_synthetic_candidate_passes(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_allowed_string_labels_pass(self) -> None:
        packet = checker.validate_source("LABELS = " + repr(sorted(checker.ALLOWED_STRING_LABELS)) + "\n")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])
        self.assertIn("controlled_raw_row_compatibility_seam", checker.ALLOWED_STRING_LABELS)

    def test_allowed_label_as_executable_reference_fails(self) -> None:
        snippets = [
            "def f():\n    return source_lineage_integrity_token\n",
            "def controlled_raw_row_compatibility_seam():\n    return None\n",
            "class future_c4_odoriba_handoff_material:\n    pass\n",
            "def f(obj):\n    return obj.direct_c1_integration_not_authorized\n",
            "def f():\n    return payload_identity_guard()\n",
        ]
        for snippet in snippets:
            packet = checker.validate_source(snippet)
            self.assertFalse(packet["boundary_passed"], snippet)
            self.assertIn("label_executable_reference", {row["forbidden_family"] for row in packet["violations"]})

    def test_forbidden_imports_fail(self) -> None:
        packet = checker.validate_source("import taichi_global_bathymetry\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["forbidden_family"], "monolith")
        packet = checker.validate_source("from taichi_global_bathymetry import render_if_needed\n")
        families = {row["forbidden_family"] for row in packet["violations"]}
        self.assertIn("monolith", families)
        self.assertIn("render_if_needed", families)
        packet = checker.validate_source("import numpy\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("dataframe_runtime", {row["forbidden_family"] for row in packet["violations"]})

    def test_forbidden_names_fail(self) -> None:
        snippets = {
            "runtime_probe": "value = runtime_probe_executed\n",
            "frame_buffer": "value = frame_rgba\n",
            "source_lineage_mutation": "value = source_lineage_mutated\n",
            "hidden_as_missing_interpretation": "value = hidden_as_missing\n",
            "reduced_count_as_source_loss_interpretation": "value = reduced_count_as_source_loss\n",
            "occluded_as_source_loss_interpretation": "value = occluded_as_source_loss\n",
            "direct_c1_integration": "value = direct_c1_integration\n",
            "c4_odoriba_bypass": "value = c4_odoriba_bypass\n",
            "transparent_globe_leak_inference": "value = transparent_globe_leak_inferred\n",
            "readiness_claim": "value = readiness_claimed\n",
        }
        for family, snippet in snippets.items():
            packet = checker.validate_source(snippet)
            self.assertFalse(packet["boundary_passed"], family)
            self.assertIn(family, {row["forbidden_family"] for row in packet["violations"]})

    def test_forbidden_attributes_fail(self) -> None:
        packet = checker.validate_source("def f(renderer):\n    return renderer.render(None)\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("renderer_runtime", {row["forbidden_family"] for row in packet["violations"]})
        packet = checker.validate_source("def f(Image):\n    return Image.fromarray(None).save('x.png')\n")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("artifact_writer", {row["forbidden_family"] for row in packet["violations"]})

    def test_forbidden_calls_fail(self) -> None:
        snippets = {
            "projection_formula": "def f():\n    return project_ais_to_screen(None)\n",
            "mask_formula": "def f():\n    return mask_overlay_to_globe(None, None)\n",
            "sampling_formula_movement": "def f():\n    return _sample_projected_frame(None, 'ais')\n",
            "alpha_compose_formula": "def f():\n    return alpha_compose(None, None)\n",
            "dataframe_runtime": "def f(pd, np):\n    return pd.DataFrame(np.asarray([]))\n",
            "live_source": "def f():\n    return AISSource()\n",
            "real_ais_adsb_source": "def f():\n    return live_ais()\n",
            "source_lineage_mutation": "def f():\n    return mutate_source_lineage()\n",
            "direct_c1_integration": "def f():\n    return connect_to_c1()\n",
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
        self.assertTrue(packet["allowed_string_label_distinction_preserved"])
        self.assertEqual({row["family"] for row in packet["results"]}, set(checker.FORBIDDEN_FAMILIES))

    def test_decision_output_fields_are_non_authorizing(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertTrue(packet["source_lineage_guard_import_boundary_checker_created"])
        self.assertFalse(packet["target_imported"])
        self.assertFalse(packet["target_executed"])
        self.assertTrue(packet["controlled_raw_row_compatibility_seam_label_allowed"])
        self.assertFalse(packet["controlled_raw_row_compatibility_seam_runtime_authorized"])
        self.assertFalse(packet["helper_creation_authorized"])
        self.assertFalse(packet["runtime_execution_authorized"])
        self.assertFalse(packet["source_lineage_mutation_authorized"])
        self.assertFalse(packet["direct_c1_integration_authorized"])
        self.assertFalse(packet["c4_odoriba_bypass_authorized"])

    def test_checker_does_not_import_target(self) -> None:
        source = Path(checker.__file__).read_text(encoding="utf-8")
        self.assertNotIn("__import__", source)
        self.assertNotIn("exec(", source)
        self.assertNotIn("eval(", source)
        tree = ast.parse(source)
        imported_modules = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_modules.add(node.module or "")
        self.assertNotIn("render_core.dynamic_point_source_lineage_guard_boundary", imported_modules)
        self.assertNotIn("dynamic_point_source_lineage_guard_boundary", imported_modules)

    def test_ast_node_coverage_is_declared(self) -> None:
        packet = checker.validate_source(checker.CLEAN_SYNTHETIC_CANDIDATE)
        self.assertEqual(
            set(packet["checked_node_types"]),
            {"ast.Import", "ast.ImportFrom", "ast.Name", "ast.Attribute", "ast.Call", "ast.FunctionDef", "ast.AsyncFunctionDef", "ast.ClassDef"},
        )

    def test_cli_missing_target_self_test_and_syntax_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "candidate.py"
            completed = subprocess.run(
                [sys.executable, "-B", "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py", str(missing)],
                check=True,
                capture_output=True,
                text=True,
            )
            syntax_error = Path(temp_dir) / "broken.py"
            syntax_error.write_text("def broken(:\n    pass\n", encoding="utf-8")
            failed = subprocess.run(
                [sys.executable, "-B", "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py", str(syntax_error)],
                capture_output=True,
                text=True,
            )
        packet = json.loads(completed.stdout)
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(packet["boundary_passed"])
        self.assertNotEqual(failed.returncode, 0)
        packet = json.loads(failed.stdout)
        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])

        completed = subprocess.run(
            [sys.executable, "-B", "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py", "--self-test-negative"],
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
            "source_lineage_guard_checker_safe_import",
            "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py",
        )
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(str(module.DEFAULT_TARGET), "render_core\\dynamic_point_source_lineage_guard_boundary.py")


if __name__ == "__main__":
    unittest.main()
