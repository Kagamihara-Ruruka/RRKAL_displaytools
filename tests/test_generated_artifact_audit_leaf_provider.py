from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
PROVIDER_PATH = REPO_ROOT / "scripts" / "generated_artifact_audit_leaf_provider.py"

spec = importlib.util.spec_from_file_location("generated_artifact_audit_leaf_provider", PROVIDER_PATH)
assert spec is not None
provider = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(provider)


class GeneratedArtifactAuditLeafProviderTest(unittest.TestCase):
    def test_split_git_paths_ignores_blank_lines(self) -> None:
        self.assertEqual(provider._split_git_paths("a\n\n b \n"), ["a", "b"])

    def test_build_leaf_provider_packet_uses_path_collectors(self) -> None:
        original_staged = provider.collect_staged_paths
        original_untracked = provider.collect_untracked_paths
        try:
            provider.collect_staged_paths = lambda repo_root=provider.REPO_ROOT: ["docs/example.md"]
            provider.collect_untracked_paths = lambda repo_root=provider.REPO_ROOT: ["scripts/new_tool.py"]
            packet = provider.build_leaf_provider_packet()
        finally:
            provider.collect_staged_paths = original_staged
            provider.collect_untracked_paths = original_untracked

        self.assertEqual(packet["schema"], "rrkal_displaytools.generated_artifact_audit.v1")
        self.assertEqual(packet["status"], "pass")
        self.assertTrue(packet["generated_artifact_audit_passed"])
        self.assertFalse(packet["runtime_render_invoked"])
        self.assertFalse(packet["runtime_merge_enabled"])
        self.assertFalse(packet["visual_parity_ready"])
        self.assertFalse(packet["interactive_fps_ready"])


if __name__ == "__main__":
    unittest.main()
