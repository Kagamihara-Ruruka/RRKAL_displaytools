import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_displaytools_import_boundary_from_profile import (
    load_profile,
    validate_source,
    validate_target,
)
from scripts.validate_displaytools_dynamic_point_payload_coordinate_quality_import_boundary import (
    validate_target as validate_handwritten_target,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_displaytools_import_boundary_from_profile.py"
PROFILE = REPO_ROOT / "tests" / "fixtures" / "import_boundary_profiles" / "dynamic_point_payload_coordinate_quality.profile.json"
HANDWRITTEN_SCRIPT = REPO_ROOT / "scripts" / "validate_displaytools_dynamic_point_payload_coordinate_quality_import_boundary.py"
TARGET = REPO_ROOT / "render_core" / "dynamic_point_payload_coordinate_quality_boundary.py"


class GenericImportBoundaryProfileTests(unittest.TestCase):
    def load_profile(self):
        return load_profile(PROFILE)

    def test_profile_shape_and_shadow_flags_are_pinned(self):
        profile = self.load_profile()

        self.assertEqual(profile["schema"], "rrkal.import_boundary_profile.v1")
        self.assertEqual(profile["capability"], "dynamic_point_payload_coordinate_quality")
        self.assertEqual(profile["target"], "render_core/dynamic_point_payload_coordinate_quality_boundary.py")
        self.assertEqual(profile["trust_level"], "L1_shadow")
        self.assertFalse(profile["blocking"])
        self.assertTrue(profile["handwritten_checker_is_source_of_truth"])
        self.assertFalse(profile["runtime_flags"]["runtime_render_invoked"])
        self.assertFalse(profile["runtime_flags"]["runtime_merge_enabled"])
        self.assertFalse(profile["runtime_flags"]["readiness_claimed"])
        self.assertEqual(
            set(profile["ast_nodes"]),
            {"Import", "ImportFrom", "Name", "Attribute", "Call", "FunctionDef", "AsyncFunctionDef", "ClassDef"},
        )

    def test_generic_checker_candidate_passes_with_shadow_metadata(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(PROFILE)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["trust_level"], "L1_shadow")
        self.assertFalse(packet["blocking"])
        self.assertTrue(packet["handwritten_checker_is_source_of_truth"])
        self.assertFalse(packet["replacement_authorized"])
        self.assertEqual(packet["violations"], [])

    def test_handwritten_checker_candidate_passes_as_source_of_truth(self):
        packet = validate_handwritten_target(TARGET)

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["candidate_exists"])
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_missing_target_behavior_matches_handwritten_semantics(self):
        profile = self.load_profile()
        missing = REPO_ROOT / "render_core" / "missing_profile_shadow_target.py"
        generic_packet = validate_target(profile, str(PROFILE), missing)

        self.assertEqual(generic_packet["status"], "not_applicable_candidate_missing")
        self.assertFalse(generic_packet["candidate_exists"])
        self.assertTrue(generic_packet["boundary_passed"])
        self.assertEqual(generic_packet["violations"], [])
        self.assertEqual(generic_packet["trust_level"], "L1_shadow")
        self.assertFalse(generic_packet["blocking"])

    def test_clean_temporary_candidate_passes(self):
        profile = self.load_profile()
        source = (
            "def build_payload_descriptor():\n"
            "    return {\n"
            "        'payload_shape': 'data label only',\n"
            "        'coordinate_quality': 'data label only',\n"
            "        'timestamp_quality': 'data label only',\n"
            "        'source_id_quality': 'data label only',\n"
            "        'speed_heading_quality': 'data label only',\n"
            "        'missing': 'data label only',\n"
            "        'invalid': 'data label only',\n"
            "        'stale': 'data label only',\n"
            "        'unknown': 'data label only',\n"
            "        'projection_dependency': 'string label only',\n"
            "        'controller_selection_dependency': 'string label only',\n"
            "    }\n"
        )
        packet = validate_source(profile, source, "<clean>", str(PROFILE))

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_forbidden_executable_references_fail(self):
        profile = self.load_profile()
        cases = {
            "import": "import pandas\n",
            "from_import": "from PyQt6 import QtWidgets\n",
            "name": "def f():\n    return DB_URL\n",
            "attribute": "def f(obj):\n    return obj.cache_read\n",
            "call": "def f():\n    return project_point()\n",
            "class_definition": "class TaichiGlobeRenderer:\n    pass\n",
            "function_definition": "def replay_query():\n    return None\n",
            "async_function_definition": "async def controller_mutation():\n    return None\n",
        }
        for name, source in cases.items():
            with self.subTest(name=name):
                packet = validate_source(profile, source, f"<{name}>", str(PROFILE))
                self.assertEqual(packet["status"], "fail")
                self.assertFalse(packet["boundary_passed"])
                self.assertTrue(packet["violations"])

    def test_syntax_error_returns_json_shape_and_nonpass(self):
        profile = self.load_profile()
        packet = validate_source(profile, "def broken(:\n", "<syntax>", str(PROFILE))

        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])
        self.assertTrue(packet["violations"])
        self.assertIn("profile", packet)
        self.assertIn("checked_imports", packet)
        self.assertIn("checked_names", packet)

    def test_allowed_string_labels_pass_as_data(self):
        profile = self.load_profile()
        labels = profile["allowed_string_labels"]
        body = ",\n".join(f"        '{label}': 'data label only'" for label in labels)
        source = "def f():\n    return {\n" + body + "\n    }\n"
        packet = validate_source(profile, source, "<labels>", str(PROFILE))

        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["boundary_passed"])
        self.assertEqual(packet["violations"], [])

    def test_generic_negative_self_test_passes(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(PROFILE), "--self-test-negative"],
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
        self.assertEqual(packet["trust_level"], "L1_shadow")
        self.assertFalse(packet["blocking"])

    def test_handwritten_negative_self_test_still_passes(self):
        result = subprocess.run(
            [sys.executable, "-B", str(HANDWRITTEN_SCRIPT), "--self-test-negative"],
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

    def test_cli_missing_target_override_returns_pass_json(self):
        missing = REPO_ROOT / "render_core" / "missing_profile_shadow_target.py"
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(PROFILE), "--target", str(missing)],
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

    def test_cli_syntax_error_file_exits_nonzero_with_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "bad_profile_shadow_target.py"
            target.write_text("def broken(:\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), str(PROFILE), "--target", str(target)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=10,
            )

        self.assertNotEqual(result.returncode, 0)
        packet = json.loads(result.stdout)
        self.assertEqual(packet["status"], "syntax_error")
        self.assertFalse(packet["boundary_passed"])

    def test_cli_json_shape_includes_shadow_fields(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(PROFILE)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        packet = json.loads(result.stdout)

        for key in [
            "schema",
            "profile",
            "target",
            "trust_level",
            "blocking",
            "handwritten_checker_is_source_of_truth",
            "replacement_authorized",
            "violations",
            "checked_imports",
            "checked_names",
            "forbidden_families",
            "runtime_render_invoked",
            "runtime_merge_enabled",
            "readiness_claimed",
        ]:
            self.assertIn(key, packet)


if __name__ == "__main__":
    unittest.main()
