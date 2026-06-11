"""Validator-backed tests for c_3 prior minimal YAML fixtures."""

import subprocess
import sys
import unittest
from pathlib import Path


VALIDATOR = Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py")
SCHEMA = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json")
FORMAL_DICTIONARY = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml")
FIXTURE_DIR = Path("tests/fixtures/c3_prior_dictionary")

VALID_FIXTURE = FIXTURE_DIR / "minimal_first_slice.valid.v0.yaml"
INVALID_FIXTURES = {
    "invalid_missing_required_section.yaml": "missing_required_section",
    "invalid_bare_high_risk_term_id.yaml": "bare_high_risk_term_id",
    "invalid_forbidden_runtime_field.yaml": "Forbidden key detected",
    "invalid_legacy_fossil_direct_adoption.yaml": "legacy_fossil_direct_adoption",
    "invalid_c4_mediation_bypass.yaml": "c4_mediation_bypassed",
    "invalid_readiness_claim.yaml": "Forbidden key detected",
}


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path), str(SCHEMA)],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


class C3PriorSemanticDictionaryMinimalYamlFixtureTest(unittest.TestCase):
    def test_fixture_files_exist_but_formal_dictionary_does_not(self) -> None:
        self.assertTrue(VALID_FIXTURE.exists())
        for name in INVALID_FIXTURES:
            self.assertTrue((FIXTURE_DIR / name).exists(), name)
        self.assertFalse(FORMAL_DICTIONARY.exists())

    def test_valid_minimal_first_slice_fixture_passes_validator(self) -> None:
        result = run_validator(VALID_FIXTURE)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validation passed successfully", result.stdout)

    def test_invalid_fixtures_fail_with_expected_surfaces(self) -> None:
        for name, expected in INVALID_FIXTURES.items():
            with self.subTest(name=name):
                result = run_validator(FIXTURE_DIR / name)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn(expected, result.stderr)

    def test_fixture_gate_does_not_modify_schema_or_validator_contract(self) -> None:
        self.assertTrue(SCHEMA.exists())
        self.assertTrue(VALIDATOR.exists())
        self.assertFalse(FORMAL_DICTIONARY.exists())


if __name__ == "__main__":
    unittest.main()
