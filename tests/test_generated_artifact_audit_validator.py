from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_generated_artifact_audit_packet.py"

spec = importlib.util.spec_from_file_location("validate_generated_artifact_audit_packet", VALIDATOR_PATH)
assert spec is not None
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class GeneratedArtifactAuditValidatorTest(unittest.TestCase):
    def test_reference_packet_passes(self) -> None:
        result = validator.build_validation_result(self_test_negative=False)

        self.assertEqual(result["schema"], "rrkal_displaytools.generated_artifact_audit_validation.v1")
        self.assertEqual(result["status"], "pass")
        self.assertTrue(result["contract_only"])
        self.assertEqual(result["errors"], [])

    def test_negative_self_test_detects_false_signals(self) -> None:
        result = validator.build_validation_result(self_test_negative=True)

        self.assertEqual(result["status"], "pass")
        self.assertTrue(result["negative_self_test_enabled"])
        cases = {case["id"]: case for case in result["negative_self_test_results"]}
        expected_ids = {
            "runtime_render_invoked_true",
            "runtime_merge_enabled_true",
            "visual_parity_ready_true",
            "interactive_fps_ready_true",
            "state_artifacts_staged_present",
            "png_artifacts_staged_present",
            "json_artifacts_staged_present",
            "state_artifacts_untracked_present",
            "png_artifacts_untracked_present",
            "json_artifacts_untracked_present",
        }
        self.assertEqual(set(cases), expected_ids)
        for case in cases.values():
            self.assertTrue(case["detected"], case)
            self.assertEqual(case["status"], "pass")


if __name__ == "__main__":
    unittest.main()
