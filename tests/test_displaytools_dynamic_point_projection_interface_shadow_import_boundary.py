import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary import (
    DEFAULT_TARGET,
    FORBIDDEN_FAMILIES,
    validate_source,
    validate_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py"


class DisplaytoolsDynamicPointProjectionInterfaceShadowImportBoundaryTests(unittest.TestCase):
    def test_missing_candidate_cli_returns_json_pass(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_dynamic_point_projection_interface_shadow_boundary.py")],
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

    def test_default_target_is_projection_interface_shadow_boundary(self):
        self.assertEqual(DEFAULT_TARGET.as_posix(), "render_core/dynamic_point_projection_interface_shadow_boundary.py")
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertEqual(packet["target"], "render_core\\dynamic_point_projection_interface_shadow_boundary.py")
        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_missing_candidate_function_returns_pass(self):
        packet = validate_target(REPO_ROOT / "render_core" / "missing_dynamic_point_projection_interface_shadow_boundary.py")

        self.assertEqual(packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])

    def test_clean_temporary_candidate_passes(self):
        source = (
            "from __future__ import annotations\n"
            "\n"
            "def build_shadow_contract_descriptor():\n"
            "    return {\n"
            "        'source_coordinate_space': 'data label only',\n"
            "        'target_coordinate_space': 'data label only',\n"
            "        'projection_policy_ref': 'data label only',\n"
            "        'flip_policy_ref': 'data label only',\n"
            "        'mask_policy_ref': 'data label only',\n"
            "        'frame_sync_ref': 'data label only',\n"
            "        'consumer_surface': 'data label only',\n"
            "        'uncertainty_label': 'data label only',\n"
            "        'evidence_refs': ['data label only'],\n"
            "        'formula_behavior_not_executed': True,\n"
            "        'coordinate_correctness_not_claimed': True,\n"
            "        'visual_correctness_not_claimed': True,\n"
            "        'core_interface_only': True,\n"
            "        'shadow_contract': 'data label only',\n"
            "        'stop_condition_ledger': [],\n"
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
        self.assertEqual(packet["violations"][0]["forbidden_family"], "runtime_renderer_host")

    def test_forbidden_name_reference_fails(self):
        packet = validate_source("def f():\n    return project_point\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("project_point", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "name_reference")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "projection_formula")

    def test_forbidden_attribute_reference_fails(self):
        packet = validate_source("def f(obj):\n    return obj.renderer_frame_transform\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("renderer_frame_transform", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "attribute_reference")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "renderer_frame_transform")

    def test_forbidden_call_target_fails(self):
        packet = validate_source("def f():\n    return lon_lat_to_screen()\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("lon_lat_to_screen", packet["checked_names"])
        kinds = {violation["kind"] for violation in packet["violations"]}
        self.assertIn("call_target", kinds)

    def test_forbidden_class_definition_fails(self):
        packet = validate_source("class TaichiGlobeRenderer:\n    pass\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("TaichiGlobeRenderer", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "class_definition")

    def test_forbidden_function_definition_fails(self):
        packet = validate_source("def mask_formula():\n    return None\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("mask_formula", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "function_definition")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "mask_formula")

    def test_forbidden_async_function_definition_fails(self):
        packet = validate_source("async def visual_correctness():\n    return None\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("visual_correctness", packet["checked_names"])
        self.assertEqual(packet["violations"][0]["kind"], "async_function_definition")
        self.assertEqual(packet["violations"][0]["forbidden_family"], "visual_correctness_claim")

    def test_syntax_error_returns_json_shape_and_nonpass(self):
        packet = validate_source("def broken(:\n")

        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])
        self.assertTrue(packet["violations"])
        self.assertIn("schema", packet)
        self.assertIn("checked_imports", packet)
        self.assertIn("checked_names", packet)
        self.assertEqual(packet["violations"][0]["forbidden_family"], "syntax_error")

    def test_allowed_string_labels_pass(self):
        source = (
            "def f():\n"
            "    return {\n"
            "        'source_coordinate_space': 'data label only',\n"
            "        'target_coordinate_space': 'data label only',\n"
            "        'projection_policy_ref': 'data label only',\n"
            "        'flip_policy_ref': 'data label only',\n"
            "        'mask_policy_ref': 'data label only',\n"
            "        'frame_sync_ref': 'data label only',\n"
            "        'consumer_surface': 'data label only',\n"
            "        'uncertainty_label': 'data label only',\n"
            "        'evidence_refs': ['data label only'],\n"
            "        'formula_behavior_not_executed': True,\n"
            "        'coordinate_correctness_not_claimed': True,\n"
            "        'visual_correctness_not_claimed': True,\n"
            "        'core_interface_only': True,\n"
            "        'shadow_contract': 'data label only',\n"
            "        'stop_condition_ledger': [],\n"
            "    }\n"
        )
        packet = validate_source(source)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])

    def test_allowed_label_as_executable_reference_fails(self):
        packet = validate_source("def f():\n    return projection_policy_ref()\n")

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["boundary_passed"])
        self.assertIn("projection_policy_ref", packet["checked_names"])
        self.assertTrue(packet["violations"])

    def test_cli_forbidden_file_exits_nonzero_with_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_dynamic_point_projection_interface_shadow_boundary.py"
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
            [sys.executable, "-B", str(SCRIPT), str(REPO_ROOT / "render_core" / "missing_dynamic_point_projection_interface_shadow_boundary.py")],
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
        self.assertTrue(packet["allowed_string_labels_passed"])

    def test_forbidden_family_coverage_is_complete(self):
        self.assertEqual(
            set(FORBIDDEN_FAMILIES),
            {
                "monolith",
                "projection_formula",
                "longitude_flip_formula",
                "latitude_flip_formula",
                "mask_formula",
                "renderer_frame_transform",
                "runtime_renderer_host",
                "dynamic_point_screen_projection_execution",
                "hot_path_alpha_apply_composition",
                "controller_selection",
                "dataframe_runtime",
                "live_source",
                "artifact_metadata",
                "coordinate_correctness_claim",
                "visual_correctness_claim",
            },
        )


if __name__ == "__main__":
    unittest.main()
