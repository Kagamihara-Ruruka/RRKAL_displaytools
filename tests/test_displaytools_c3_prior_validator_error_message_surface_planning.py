"""Docs/test-only planning for future validator error-message surfaces.

This gate plans error-code families, diagnostic wording, stderr/json surfaces,
and fixture filename alignment. It does not change validator behavior, schema,
fixtures, runtime behavior, or integration behavior.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_yaml_fixture_error_surface_material_settlement as error_settlement
from tests import test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture as fixture_gate


VALIDATOR_SCRIPT = Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py")
SCHEMA_JSON = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json")
FORMAL_DICTIONARY = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml")

ERROR_CODE_FAMILIES = {
    "parse_error": {
        "planned_error_codes": ["yaml_syntax_error", "yaml_root_not_mapping"],
        "source_evidence": "a1_error_message_readability_scout",
        "status": "future_error_code_family",
    },
    "schema_error": {
        "planned_error_codes": ["missing_required_section", "unknown_top_level_section", "schema_json_missing"],
        "source_evidence": "validator_current_surface_and_a1_scout",
        "status": "future_error_code_family",
    },
    "business_rule_error": {
        "planned_error_codes": [
            "bare_high_risk_term_id",
            "legacy_fossil_direct_adoption",
            "c4_mediation_bypassed",
            "forbidden_field_detected",
            "readiness_claim_rejected",
        ],
        "source_evidence": "current_fixture_gate_and_error_surface_settlement",
        "status": "future_error_code_family",
    },
    "reference_envelope_error": {
        "planned_error_codes": [
            "asset_id_pathlike_rejected",
            "subject_ref_payload_geometry_rejected",
            "source_ref_fetchable_rejected",
            "schema_ref_private_schema_rejected",
            "sample_query_ref_callable_rejected",
            "spatial_extent_payload_rejected",
            "temporal_extent_row_payload_rejected",
            "evidence_refs_unstructured_rejected",
            "redaction_context_ambiguous_rejected",
            "review_direct_use_signal_rejected",
        ],
        "source_evidence": "c1_reference_envelope_error_surface_scout",
        "status": "future_validator_rule_candidate",
    },
    "display_hint_error": {
        "planned_error_codes": [
            "display_hint_lod_unknown_value",
            "display_hint_bbox_invalid_geometry",
            "display_hint_coordref_missing_or_unknown",
            "display_hint_timewindow_invalid_interval",
            "display_hint_tile_ref_credential_leak",
            "display_hint_density_unit_missing",
            "display_hint_sample_budget_unit_missing",
            "display_hint_planning_only_false",
        ],
        "source_evidence": "c2_display_hint_error_surface_scout",
        "status": "future_validator_rule_candidate",
    },
}

DIAGNOSTIC_WORDING_STYLE = {
    "stderr_minimum_shape": "[ERROR] <error_code>: File \"<file_path>\", at <position> | <reason>",
    "json_surface_candidate": {
        "error_code": "stable snake_case code",
        "file_path": "fixture or dictionary path",
        "position": "YAML path or top-level surface",
        "reason": "short human-readable reason",
        "severity": "fail | warning | not_applicable | success",
        "boundary": "reference_only | planning_only | card_edge_only | validator_only",
    },
    "style_rules": {
        "snake_case_error_codes": True,
        "one_line_stderr": True,
        "avoid_raw_yaml_dump": True,
        "avoid_payload_echo": True,
        "neutral_pass_message": "Validation passed successfully.",
        "neutral_missing_message": "not_applicable_dictionary_missing",
        "no_readiness_or_usable_wording": True,
    },
}

FIXTURE_FILENAME_ALIGNMENT = {
    "invalid_missing_required_section.yaml": "missing_required_section",
    "invalid_bare_high_risk_term_id.yaml": "bare_high_risk_term_id",
    "invalid_forbidden_runtime_field.yaml": "forbidden_field_detected",
    "invalid_legacy_fossil_direct_adoption.yaml": "legacy_fossil_direct_adoption",
    "invalid_c4_mediation_bypass.yaml": "c4_mediation_bypassed",
    "invalid_readiness_claim.yaml": "readiness_claim_rejected",
}

PASS_FAIL_NOT_APPLICABLE_WORDING = {
    "pass_stdout": "Validation passed successfully.",
    "missing_dictionary_stdout": "not_applicable_dictionary_missing",
    "fail_stderr_required": True,
    "fail_stdout_required": False,
    "not_applicable_is_not_readiness": True,
}

UNKNOWN_STOP_LINES = {
    "structured_json_error_output": {
        "reason": "current validator emits stderr/stdout text only",
        "resolution_gate": "future_validator_error_json_surface_gate",
    },
    "display_hint_warning_vs_fail_runtime_policy": {
        "reason": "future display-hint policy must not imply runtime SLA",
        "resolution_gate": "future_display_hint_validator_policy_gate",
    },
}

DECISION_OUTPUT = {
    "validator_error_message_surface_planning_passed": True,
    "error_surface_settlement_passed": error_settlement.DECISION_OUTPUT[
        "yaml_fixture_error_surface_material_settlement_passed"
    ],
    "validator_script_modification_authorized": False,
    "schema_json_modification_authorized": False,
    "yaml_fixture_creation_authorized": False,
    "formal_dictionary_creation_authorized": False,
    "runtime_execution_authorized": False,
    "renderer_behavior_authorized": False,
    "formula_movement_authorized": False,
    "storage_sql_crawler_behavior_authorized": False,
    "cross_agent_integration_authorized": False,
    "readiness_claimed": False,
    "usable_dictionary_claimed": False,
    "correctness_claimed": False,
    "visual_parity_claimed": False,
    "performance_claimed": False,
    "runtime_replacement_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_validator_error_message_surface_contract_gate"


class C3PriorValidatorErrorMessageSurfacePlanningTest(unittest.TestCase):
    def test_error_surface_settlement_and_current_fixtures_are_source_evidence(self) -> None:
        self.assertTrue(DECISION_OUTPUT["error_surface_settlement_passed"])
        self.assertTrue(fixture_gate.VALID_FIXTURE.exists())
        self.assertFalse(FORMAL_DICTIONARY.exists())

    def test_planned_error_code_families_cover_core_surfaces(self) -> None:
        self.assertEqual(
            set(ERROR_CODE_FAMILIES),
            {
                "parse_error",
                "schema_error",
                "business_rule_error",
                "reference_envelope_error",
                "display_hint_error",
            },
        )
        self.assertIn("yaml_syntax_error", ERROR_CODE_FAMILIES["parse_error"]["planned_error_codes"])
        self.assertIn("missing_required_section", ERROR_CODE_FAMILIES["schema_error"]["planned_error_codes"])
        self.assertIn("legacy_fossil_direct_adoption", ERROR_CODE_FAMILIES["business_rule_error"]["planned_error_codes"])

    def test_reference_envelope_error_codes_are_planning_only(self) -> None:
        codes = set(ERROR_CODE_FAMILIES["reference_envelope_error"]["planned_error_codes"])
        for code in [
            "asset_id_pathlike_rejected",
            "source_ref_fetchable_rejected",
            "sample_query_ref_callable_rejected",
            "review_direct_use_signal_rejected",
        ]:
            self.assertIn(code, codes)
        self.assertEqual(ERROR_CODE_FAMILIES["reference_envelope_error"]["status"], "future_validator_rule_candidate")

    def test_display_hint_error_codes_preserve_planning_only_boundary(self) -> None:
        codes = set(ERROR_CODE_FAMILIES["display_hint_error"]["planned_error_codes"])
        for code in [
            "display_hint_lod_unknown_value",
            "display_hint_bbox_invalid_geometry",
            "display_hint_sample_budget_unit_missing",
            "display_hint_planning_only_false",
        ]:
            self.assertIn(code, codes)
        self.assertIn("display_hint_warning_vs_fail_runtime_policy", UNKNOWN_STOP_LINES)

    def test_diagnostic_wording_style_is_planned_without_validator_change(self) -> None:
        self.assertIn("<error_code>", DIAGNOSTIC_WORDING_STYLE["stderr_minimum_shape"])
        self.assertIn("<file_path>", DIAGNOSTIC_WORDING_STYLE["stderr_minimum_shape"])
        self.assertIn("<position>", DIAGNOSTIC_WORDING_STYLE["stderr_minimum_shape"])
        self.assertIn("<reason>", DIAGNOSTIC_WORDING_STYLE["stderr_minimum_shape"])
        self.assertTrue(DIAGNOSTIC_WORDING_STYLE["style_rules"]["one_line_stderr"])
        self.assertTrue(DIAGNOSTIC_WORDING_STYLE["style_rules"]["avoid_raw_yaml_dump"])
        self.assertTrue(DIAGNOSTIC_WORDING_STYLE["style_rules"]["no_readiness_or_usable_wording"])

    def test_fixture_filename_alignment_matches_existing_invalid_fixtures(self) -> None:
        self.assertEqual(set(FIXTURE_FILENAME_ALIGNMENT), set(fixture_gate.INVALID_FIXTURES))
        self.assertEqual(FIXTURE_FILENAME_ALIGNMENT["invalid_c4_mediation_bypass.yaml"], "c4_mediation_bypassed")
        self.assertEqual(
            FIXTURE_FILENAME_ALIGNMENT["invalid_legacy_fossil_direct_adoption.yaml"],
            "legacy_fossil_direct_adoption",
        )

    def test_pass_fail_and_not_applicable_wording_is_neutral(self) -> None:
        self.assertEqual(PASS_FAIL_NOT_APPLICABLE_WORDING["pass_stdout"], "Validation passed successfully.")
        self.assertEqual(
            PASS_FAIL_NOT_APPLICABLE_WORDING["missing_dictionary_stdout"],
            "not_applicable_dictionary_missing",
        )
        self.assertTrue(PASS_FAIL_NOT_APPLICABLE_WORDING["not_applicable_is_not_readiness"])

    def test_unknown_surfaces_are_stop_lines_not_forced_plans(self) -> None:
        self.assertEqual(
            UNKNOWN_STOP_LINES["structured_json_error_output"]["resolution_gate"],
            "future_validator_error_json_surface_gate",
        )
        self.assertEqual(
            UNKNOWN_STOP_LINES["display_hint_warning_vs_fail_runtime_policy"]["resolution_gate"],
            "future_display_hint_validator_policy_gate",
        )

    def test_decision_output_blocks_implementation_and_claims(self) -> None:
        self.assertTrue(DECISION_OUTPUT["validator_error_message_surface_planning_passed"])
        self.assertTrue(VALIDATOR_SCRIPT.exists())
        self.assertTrue(SCHEMA_JSON.exists())
        self.assertFalse(FORMAL_DICTIONARY.exists())
        for key in [
            "validator_script_modification_authorized",
            "schema_json_modification_authorized",
            "yaml_fixture_creation_authorized",
            "formal_dictionary_creation_authorized",
            "runtime_execution_authorized",
            "renderer_behavior_authorized",
            "formula_movement_authorized",
            "storage_sql_crawler_behavior_authorized",
            "cross_agent_integration_authorized",
            "readiness_claimed",
            "usable_dictionary_claimed",
            "correctness_claimed",
            "visual_parity_claimed",
            "performance_claimed",
            "runtime_replacement_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_recommended_next_gate_is_contract_gate_not_runtime_or_validator_change(self) -> None:
        self.assertEqual(RECOMMENDED_NEXT_GATE, "c3_prior_validator_error_message_surface_contract_gate")


if __name__ == "__main__":
    unittest.main()
