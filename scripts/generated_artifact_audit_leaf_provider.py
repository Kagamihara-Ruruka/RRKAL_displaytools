from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from render_core.generated_artifact_audit import build_generated_artifact_audit_packet

GIT_TIMEOUT_SECONDS = 10


def _split_git_paths(stdout: str) -> list[str]:
    return [line.strip() for line in stdout.splitlines() if line.strip()]


def _git_paths(repo_root: Path, args: list[str]) -> list[str]:
    completed = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        capture_output=True,
        text=True,
        timeout=GIT_TIMEOUT_SECONDS,
    )
    return _split_git_paths(completed.stdout)


def collect_staged_paths(repo_root: Path = REPO_ROOT) -> list[str]:
    return _git_paths(repo_root, ["diff", "--cached", "--name-only"])


def collect_untracked_paths(repo_root: Path = REPO_ROOT) -> list[str]:
    return _git_paths(repo_root, ["ls-files", "--others", "--exclude-standard"])


def build_leaf_provider_packet(repo_root: Path = REPO_ROOT) -> dict[str, object]:
    return build_generated_artifact_audit_packet(
        staged_paths=collect_staged_paths(repo_root),
        untracked_paths=collect_untracked_paths(repo_root),
        source="scripts.generated_artifact_audit_leaf_provider.build_leaf_provider_packet",
    )


def main() -> int:
    packet = build_leaf_provider_packet()
    print(json.dumps(packet, ensure_ascii=False, indent=2))
    return 0 if packet.get("generated_artifact_audit_passed") is True else 1


if __name__ == "__main__":
    raise SystemExit(main())
