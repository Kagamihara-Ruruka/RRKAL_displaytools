from __future__ import annotations

from typing import Iterable


def _normalize_path(path: str) -> str:
    return str(path).replace("\\", "/").lstrip("./")


def _is_state_artifact(path: str) -> bool:
    normalized = _normalize_path(path)
    return normalized == "state" or normalized.startswith("state/")


def _has_suffix(path: str, suffix: str) -> bool:
    return _normalize_path(path).lower().endswith(suffix)


def _matching_paths(paths: Iterable[str], predicate) -> list[str]:
    return sorted(_normalize_path(path) for path in paths if predicate(str(path)))


def build_generated_artifact_audit_packet(
    *,
    staged_paths: Iterable[str],
    untracked_paths: Iterable[str],
    source: str = "render_core.generated_artifact_audit.build_generated_artifact_audit_packet",
) -> dict[str, object]:
    staged = [_normalize_path(path) for path in staged_paths]
    untracked = [_normalize_path(path) for path in untracked_paths]

    state_staged = _matching_paths(staged, _is_state_artifact)
    png_staged = _matching_paths(staged, lambda path: _has_suffix(path, ".png"))
    json_staged = _matching_paths(staged, lambda path: _has_suffix(path, ".json"))
    state_untracked = _matching_paths(untracked, _is_state_artifact)
    png_untracked = _matching_paths(untracked, lambda path: _has_suffix(path, ".png"))
    json_untracked = _matching_paths(untracked, lambda path: _has_suffix(path, ".json"))

    generated_artifact_audit_passed = not any(
        (
            state_staged,
            png_staged,
            json_staged,
            state_untracked,
            png_untracked,
            json_untracked,
        )
    )

    return {
        "schema": "rrkal_displaytools.generated_artifact_audit.v1",
        "source": source,
        "status": "pass" if generated_artifact_audit_passed else "fail",
        "contract_only": True,
        "state_artifacts_staged": state_staged,
        "png_artifacts_staged": png_staged,
        "json_artifacts_staged": json_staged,
        "state_artifacts_untracked": state_untracked,
        "png_artifacts_untracked": png_untracked,
        "json_artifacts_untracked": json_untracked,
        "generated_artifact_audit_passed": generated_artifact_audit_passed,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "interactive_fps_ready": False,
        "boundary": (
            "Generated artifact audit packet only; does not run renderer, launch Qt, read baseline/candidate "
            "artifacts, write state files, create PNG/JSON artifacts, change metadata schema, change output "
            "behavior, enable runtime merge, claim visual parity, or claim interactive FPS readiness."
        ),
    }
