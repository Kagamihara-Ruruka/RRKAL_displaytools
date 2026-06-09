import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_displaytools_dynamic_point_selection_render_policy_import_boundary import (
    DEFAULT_TARGET,
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py"


class DisplaytoolsDynamicPointSelectionRenderPolicyImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_cli_returns_json_pass(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_dynamic_point_selection_render_policy_boundary.py")],
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

    def test_default_target_is_selection_render_policy_boundary(self):
        self.assertEqual(DEFAULT_TARGET.as_posix(), "render_core/dynamic_point_selection_render_policy_boundary.py")
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertEqual(packet["target"], "render_core\\dynamic_point_selection_render_policy_boundary.py")
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertTrue(packet["boundary_passed"])

    def test_missing_candidate_function_returns_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_dynamic_point_selection_render_policy_boundary.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_clean_temporary_candidate_passes(self):
        source = (
            "from __future__ import annotations\n"
            "\n"
            "def build_selection_render_descriptor():\n"
            "    return {\n"
            "        'selected_vehicle': 'data label only',\n"
            "        'selected_layer': 'data label only',\n"
            "        'hit_state': 'data label only',\n"
            "        'picker_status': 'data label only',\n"
            "        'visible_count': 'data label only',\n"
            "        'rendered_count': 'data label only',\n"
            "        'render_cap': 'data label only',\n"
            "        'adaptive_sampling': 'data label only',\n"
            "        'controller_selection_runtime_dependency': 'blocked label only',\n"
            "        'picker_hit_test_runtime_dependency': 'blocked label only',\n"
            "        'datashader_sampling_runtime_dependency': 'blocked label only',\n"
            "        'renderer_host_runtime_dependency': 'blocked label only',\n"
            "        'runtime_dependency_allowed': False,\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_import_fails(self):
        packet = validate_source("import datashader\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["kind"], "import")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "runtime_sampling")

    def test_forbidden_import_from_fails(self):
        packet = validate_source("from PyQt6 import QtWidgets\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertEqual(packet["violations"][0]["kind"], "from_import")

    def test_forbidden_name_reference_fails(self):
        packet = validate_source("def f():\n    return selected_vehicle_runtime\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("selected_vehicle_runtime", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "name_reference")

    def test_forbidden_attribute_reference_fails(self):
        packet = validate_source("def f(obj):\n    return obj.picker\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("picker", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "attribute_reference")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "picker_hit_test")

    def test_forbidden_call_target_fails(self):
        packet = validate_source("def f():\n    return hit_test()\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("hit_test", packet["checked_names"])
        kinds = {violation["kind"] for violation in packet["violations"]}
        self.assertIn("call_target", kinds)

    def test_forbidden_class_definition_fails(self):
        packet = validate_source("class TaichiGlobeRenderer:\n    pass\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("TaichiGlobeRenderer", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "class_definition")

    def test_forbidden_function_definition_fails(self):
        packet = validate_source("def selected_vehicle_runtime():\n    return None\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("selected_vehicle_runtime", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "function_definition")

    def test_forbidden_async_function_definition_fails(self):
        packet = validate_source("async def legacy_pick():\n    return None\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("legacy_pick", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "async_function_definition")

    def test_syntax_error_returns_json_shape_and_nonpass(self):
        packet = validate_source("def broken(:\n")

        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])
        self.assertTrue(packet["violations"])
        self.assertIn("schema", packet)
        self.assertIn("checked_imports", packet)
        self.assertEqual(packet["violations"][0]["forbidden_family"], "syntax_error")

    def test_allowed_string_labels_pass(self):
        source = (
            "def f():\n"
            "    return {\n"
            "        'selected_vehicle': 'data label only',\n"
            "        'selected_layer': 'data label only',\n"
            "        'hit_state': 'data label only',\n"
            "        'picker_status': 'data label only',\n"
            "        'visible_count': 'data label only',\n"
            "        'rendered_count': 'data label only',\n"
            "        'render_cap': 'data label only',\n"
            "        'adaptive_sampling': 'data label only',\n"
            "        'selection_staleness_fault': 'data label only',\n"
            "        'hit_test_dependency_fault': 'data label only',\n"
            "        'render_policy_guard_flag': 'data label only',\n"
            "        'controller_selection_runtime_dependency': 'data label only',\n"
            "        'picker_hit_test_runtime_dependency': 'data label only',\n"
            "        'datashader_sampling_runtime_dependency': 'data label only',\n"
            "        'renderer_host_runtime_dependency': 'data label only',\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])

    def test_cli_forbidden_file_exits_nonzero_with_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_dynamic_point_selection_render_policy_boundary.py"
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

    def test_cli_json_shape_is_pinned_for_missing_candidate(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_dynamic_point_selection_render_policy_boundary.py")],
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
        self.assertEqual(packet["violations"], [])

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