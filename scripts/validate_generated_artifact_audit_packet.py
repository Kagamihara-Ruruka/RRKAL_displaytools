from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from render_core.generated_artifact_audit import build_generated_artifact_audit_packet


REQUIRED_EMPTY_LIST_FIELDS = (
    "state_artifacts_staged",
    "png_artifacts_staged",
    "json_artifacts_staged",
    "state_artifacts_untracked",
    "png_artifacts_untracked",
    "json_artifacts_untracked",
)


def build_reference_packet() -> dict[str, Any]:
    return build_generated_artifact_audit_packet(
        staged_paths=["docs/C3_FIRST_HELPER_EXTRACTION_PREIMPLEMENTATION_GATE.zh-TW.md"],
        untracked_paths=["scripts/validate_generated_artifact_audit_packet.py"],
        source="scripts.validate_generated_artifact_audit_packet.build_reference_packet",
    )


def validate_packet(packet: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    expected_values = {
        "schema": "rrkal_displaytools.generated_artifact_audit.v1",
        "contract_only": True,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "interactive_fps_ready": False,
        "generated_artifact_audit_passed": True,
        "status": "pass",
    }
    for field, expected in expected_values.items():
        if packet.get(field) != expected:
            errors.append(f"{field} expected {expected!r} but got {packet.get(field)!r}")

    for field in REQUIRED_EMPTY_LIST_FIELDS:
        value = packet.get(field)
        if value != []:
            errors.append(f"{field} expected [] but got {value!r}")

    return errors


def run_negative_self_test(reference_packet: dict[str, Any]) -> list[dict[str, Any]]:
    cases: list[tuple[str, str, Any]] = [
        ("runtime_render_invoked_true", "runtime_render_invoked", True),
        ("runtime_merge_enabled_true", "runtime_merge_enabled", True),
        ("visual_parity_ready_true", "visual_parity_ready", True),
        ("interactive_fps_ready_true", "interactive_fps_ready", True),
        ("state_artifacts_staged_present", "state_artifacts_staged", ["state/generated/frame.tmp"]),
        ("png_artifacts_staged_present", "png_artifacts_staged", ["reports/frame.png"]),
        ("json_artifacts_staged_present", "json_artifacts_staged", ["reports/summary.json"]),
        ("state_artifacts_untracked_present", "state_artifacts_untracked", ["state/showcase/output.tmp"]),
        ("png_artifacts_untracked_present", "png_artifacts_untracked", ["state/showcase/frame.png"]),
        ("json_artifacts_untracked_present", "json_artifacts_untracked", ["state/showcase/summary.json"]),
    ]

    results: list[dict[str, Any]] = []
    for case_id, field, value in cases:
        mutated = copy.deepcopy(reference_packet)
        mutated[field] = value
        case_errors = validate_packet(mutated)
        detected = bool(case_errors)
        results.append(
            {
                "id": case_id,
                "mutated_field": field,
                "expected_detection": True,
                "detected": detected,
                "status": "pass" if detected else "fail",
                "errors": case_errors,
            }
        )
    return results


def build_validation_result(*, self_test_negative: bool) -> dict[str, Any]:
    packet = build_reference_packet()
    errors = validate_packet(packet)
    negative_results: list[dict[str, Any]] = []

    if self_test_negative:
        negative_results = run_negative_self_test(packet)
        for result in negative_results:
            if not result["detected"]:
                errors.append(f"negative self-test failed to detect {result['id']}")

    passed = not errors
    return {
        "schema": "rrkal_displaytools.generated_artifact_audit_validation.v1",
        "source": "scripts/validate_generated_artifact_audit_packet.py",
        "status": "pass" if passed else "fail",
        "contract_only": True,
        "validated_packet_schema": packet.get("schema"),
        "checked_fields": [
            "contract_only",
            "runtime_render_invoked",
            "runtime_merge_enabled",
            "visual_parity_ready",
            "interactive_fps_ready",
            "generated_artifact_audit_passed",
            "state_artifacts_staged",
            "png_artifacts_staged",
            "json_artifacts_staged",
            "state_artifacts_untracked",
            "png_artifacts_untracked",
            "json_artifacts_untracked",
        ],
        "negative_self_test_enabled": bool(self_test_negative),
        "negative_self_test_results": negative_results,
        "errors": errors,
        "boundary": (
            "Generated artifact audit validator only; uses in-memory packets and does not run renderer, "
            "launch Qt, read or write runtime artifacts, change metadata schema, change output behavior, "
            "enable runtime merge, or assert image-equivalence / interactive-loop readiness."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    result = build_validation_result(self_test_negative=args.self_test_negative)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
