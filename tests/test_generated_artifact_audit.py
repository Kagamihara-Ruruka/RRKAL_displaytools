from __future__ import annotations

import unittest

from render_core.generated_artifact_audit import build_generated_artifact_audit_packet


class GeneratedArtifactAuditPacketTest(unittest.TestCase):
    def test_clean_lists_pass_without_readiness_claims(self) -> None:
        packet = build_generated_artifact_audit_packet(
            staged_paths=["docs/C3_FIRST_HELPER_EXTRACTION_PREIMPLEMENTATION_GATE.zh-TW.md"],
            untracked_paths=["render_core/generated_artifact_audit.py"],
        )

        self.assertEqual(packet["schema"], "rrkal_displaytools.generated_artifact_audit.v1")
        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["contract_only"])
        self.assertTrue(packet["generated_artifact_audit_passed"])
        self.assertFalse(packet["runtime_render_invoked"])
        self.assertFalse(packet["runtime_merge_enabled"])
        self.assertFalse(packet["visual_parity_ready"])
        self.assertFalse(packet["interactive_fps_ready"])

    def test_state_png_json_paths_fail(self) -> None:
        packet = build_generated_artifact_audit_packet(
            staged_paths=[
                "state/compose_parity/frame.png",
                "reports/generated.json",
            ],
            untracked_paths=[
                "state/showcase/preview.png",
                "state/showcase/summary.json",
            ],
        )

        self.assertEqual(packet["status"], "fail")
        self.assertFalse(packet["generated_artifact_audit_passed"])
        self.assertEqual(packet["state_artifacts_staged"], ["state/compose_parity/frame.png"])
        self.assertEqual(packet["png_artifacts_staged"], ["state/compose_parity/frame.png"])
        self.assertEqual(packet["json_artifacts_staged"], ["reports/generated.json"])
        self.assertEqual(
            packet["state_artifacts_untracked"],
            ["state/showcase/preview.png", "state/showcase/summary.json"],
        )
        self.assertEqual(packet["png_artifacts_untracked"], ["state/showcase/preview.png"])
        self.assertEqual(packet["json_artifacts_untracked"], ["state/showcase/summary.json"])


if __name__ == "__main__":
    unittest.main()
