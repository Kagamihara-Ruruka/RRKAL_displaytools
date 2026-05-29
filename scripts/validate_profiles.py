from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "profiles"
sys.path.insert(0, str(ROOT))

from profile_schema import load_profile_payload, profile_payload_errors  # noqa: E402


def validate_profile(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = load_profile_payload(path)
    except Exception as exc:
        return [f"{path.name}: invalid JSON: {exc}"]
    errors.extend(f"{path.name}: {error}" for error in profile_payload_errors(payload))
    return errors


def main() -> int:
    profile_paths = sorted(PROFILE_DIR.glob("*.json"))
    if not profile_paths:
        print("No profile templates found.", file=sys.stderr)
        return 1
    errors: list[str] = []
    for path in profile_paths:
        errors.extend(validate_profile(path))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Profile validation passed: {len(profile_paths)} templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
