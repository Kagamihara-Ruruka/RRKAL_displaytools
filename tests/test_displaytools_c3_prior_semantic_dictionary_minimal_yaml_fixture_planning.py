"""Docs/test-only planning for future c_3 prior YAML fixtures.

This gate plans fixture topology and validation inputs, but creates no YAML or
YML fixture files and does not modify schema JSON or the validator.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_validator_fixture_material_settlement as fixture_settlement


FORMAL_DICTIONARY_TARGET = "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml"
SCHEMA_JSON_TARGET = "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json"
VALIDATOR_TARGET = "scripts/validate_displaytools_c3_prior_semantic_dictionary.py"

FUTURE_VALID_FIXTURE_TARGET = (
    "tests/fixtures/c3_prior_dictionary/minimal_first_slice.valid.v0.yaml"
)

FUTURE_INVALID_FIXTURE_TARGETS = [
    "tests/fixtures/c3_prior_dictionary/invalid_missing_required_section.yaml",
    "tests/fixtures/c3_prior_dictionary/invalid_bare_high_risk_term_id.yaml",
    "tests/fixtures/c3_prior_dictionary/invalid_forbidden_runtime_field.yaml",
    "tests/fixtures/c3_prior_dictionary/invalid_legacy_fossil_direct_adoption.yaml",
    "tests/fixtures/c3_prior_dictionary/invalid_c4_mediation_bypass.yaml",
    "tests/fixtures/c3_prior_dictionary/invalid_readiness_claim.yaml",
]

REQUIRED_TOP_LEVEL_SECTIONS = [
    "dictionary_metadata",
    "authority_sources",
    "phenomenon_translation_map",
    "prior_terms",
    "view_families",
    "layer_taxonomy",
    "recipe_authoring",
    "c4_mediation",
    "legacy_fossil_translation",
    "stop_lines",
    "unknown_stop_lines",
    "validator_expectations",
]

VALID_FIXTURE_MINIMUM_SHAPE = {
    "fixture_target": FUTURE_VALID_FIXTURE_TARGET,
    "top_level_sections_required": REQUIRED_TOP_LEVEL_SECTIONS,
    "dictionary_metadata_required_fields": [
        "dictionary_id",
        "version",
        "owner",
        "lifecycle_status",
        "source_commit",
    ],
    "minimal_prior_term_required_fields": [
        "term_id",
        "definition",
        "authority_family",
        "source_evidence_refs",
        "allowed_use",
        "forbidden_use",
        "example",
        "counterexample",
        "schema_field_candidate",
        "validator_rule_candidate",
        "prototype_behavior_candidate",
        "stop_line",
        "confidence",
        "lifecycle_status",
    ],
    "validator_input_contract": {
        "dictionary_path": FUTURE_VALID_FIXTURE_TARGET,
        "schema_path": SCHEMA_JSON_TARGET,
        "validator_path": VALIDATOR_TARGET,
    },
}

SEED_TERM_FIXTURE_MATERIAL = {
    "allowed_as_fixture_material": [
        "recipe_owns_truth_prior",
        "c4_mediates_ingress_egress_for_render_recipe",
        "reference_envelope_positive_fixture",
        "display_hint_negative_fixture",
        "validator_failure_card_edge",
    ],
    "lab_evidence_only": [
        "raw_yaml_payload",
        "dataframe_preview",
        "frame_buffer_truth",
        "runtime_sla",
        "prior_card_generation_readiness",
        "legacy_mask_direct_adoption",
    ],
}

INVALID_FIXTURE_FAMILY_PLAN = {
    "missing_required_section": {
        "future_target": "tests/fixtures/c3_prior_dictionary/invalid_missing_required_section.yaml",
        "expected_validator_surface": "missing_required_section",
        "source_material": "schema_json_contract",
    },
    "bare_high_risk_term_id": {
        "future_target": "tests/fixtures/c3_prior_dictionary/invalid_bare_high_risk_term_id.yaml",
        "expected_validator_surface": "bare_high_risk_term_id",
        "source_material": "validator_gate",
    },
    "forbidden_runtime_field": {
        "future_target": "tests/fixtures/c3_prior_dictionary/invalid_forbidden_runtime_field.yaml",
        "expected_validator_surface": "forbidden_field_family",
        "source_material": "minimal_yaml_entry_shape_scout",
    },
    "legacy_fossil_direct_adoption": {
        "future_target": "tests/fixtures/c3_prior_dictionary/invalid_legacy_fossil_direct_adoption.yaml",
        "expected_validator_surface": "legacy_fossil_direct_adoption",
        "source_material": "prior_law_settlement",
    },
    "c4_mediation_bypass": {
        "future_target": "tests/fixtures/c3_prior_dictionary/invalid_c4_mediation_bypass.yaml",
        "expected_validator_surface": "c4_mediation_bypassed",
        "source_material": "c4_fixture_scout",
    },
    "readiness_claim": {
        "future_target": "tests/fixtures/c3_prior_dictionary/invalid_readiness_claim.yaml",
        "expected_validator_surface": "readiness_claimed",
        "source_material": "validator_fixture_settlement",
    },
}

STOP_LINES_PRESERVED = {
    "no_yaml_fixture_creation",
    "no_formal_dictionary_creation",
    "no_schema_json_modification",
    "no_validator_modification",
    "no_runtime_behavior",
    "no_renderer_behavior",
    "no_formula_behavior",
    "no_dictionary_usable_claim",
    "no_readiness_claim",
    "no_correctness_claim",
    "no_visual_parity_claim",
    "no_runtime_replacement_claim",
}

VALIDATOR_MISSING_TARGET_BEHAVIOR = {
    "formal_dictionary_missing_status": "not_applicable_dictionary_missing",
    "future_fixture_missing_status": "not_applicable_dictionary_missing",
    "missing_yaml_target_passes": True,
    "missing_schema_target_fails": True,
    "validator_input_not_created_in_this_gate": True,
}

DECISION_OUTPUT = {
    "minimal_yaml_fixture_planning_gate_passed": True,
    "validator_fixture_settlement_passed": fixture_settlement.DECISION_OUTPUT[
        "validator_fixture_material_settlement_passed"
    ],
    "yaml_fixture_creation_authorized": False,
    "formal_dictionary_creation_authorized": False,
    "schema_json_modification_authorized": False,
    "validator_modification_authorized": False,
    "runtime_execution_authorized": False,
    "renderer_behavior_authorized": False,
    "formula_movement_authorized": False,
    "dictionary_usable_claimed": False,
    "readiness_claimed": False,
    "correctness_claimed": False,
    "visual_parity_claimed": False,
    "runtime_replacement_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_minimal_yaml_fixture_gate"


class C3PriorSemanticDictionaryMinimalYamlFixturePlanningTest(unittest.TestCase):
    def test_fixture_settlement_is_source_evidence(self) -> None:
        self.assertTrue(DECISION_OUTPUT["validator_fixture_settlement_passed"])
        self.assertEqual(
            fixture_settlement.RECOMMENDED_NEXT_GATE,
            "c3_prior_semantic_dictionary_minimal_yaml_fixture_planning_gate",
        )

    def test_future_fixture_topology_is_planned_but_absent(self) -> None:
        self.assertEqual(
            FUTURE_VALID_FIXTURE_TARGET,
            "tests/fixtures/c3_prior_dictionary/minimal_first_slice.valid.v0.yaml",
        )
        self.assertEqual(len(FUTURE_INVALID_FIXTURE_TARGETS), 6)
        for future_path in [FUTURE_VALID_FIXTURE_TARGET, *FUTURE_INVALID_FIXTURE_TARGETS]:
            self.assertTrue(future_path.endswith(".yaml"))
            self.assertFalse(Path(future_path).exists(), future_path)

    def test_formal_dictionary_remains_absent(self) -> None:
        self.assertFalse(Path(FORMAL_DICTIONARY_TARGET).exists())
        self.assertTrue(Path(SCHEMA_JSON_TARGET).exists())
        self.assertTrue(Path(VALIDATOR_TARGET).exists())

    def test_valid_fixture_minimum_shape_requires_all_twelve_top_level_sections(self) -> None:
        self.assertEqual(len(REQUIRED_TOP_LEVEL_SECTIONS), 12)
        self.assertEqual(
            VALID_FIXTURE_MINIMUM_SHAPE["top_level_sections_required"],
            REQUIRED_TOP_LEVEL_SECTIONS,
        )
        for section in [
            "dictionary_metadata",
            "authority_sources",
            "prior_terms",
            "c4_mediation",
            "validator_expectations",
        ]:
            self.assertIn(section, REQUIRED_TOP_LEVEL_SECTIONS)

    def test_valid_fixture_plans_validator_input_without_creating_input(self) -> None:
        contract = VALID_FIXTURE_MINIMUM_SHAPE["validator_input_contract"]
        self.assertEqual(contract["dictionary_path"], FUTURE_VALID_FIXTURE_TARGET)
        self.assertEqual(contract["schema_path"], SCHEMA_JSON_TARGET)
        self.assertEqual(contract["validator_path"], VALIDATOR_TARGET)
        self.assertFalse(Path(contract["dictionary_path"]).exists())

    def test_invalid_fixture_family_plan_is_complete(self) -> None:
        self.assertEqual(
            set(INVALID_FIXTURE_FAMILY_PLAN),
            {
                "missing_required_section",
                "bare_high_risk_term_id",
                "forbidden_runtime_field",
                "legacy_fossil_direct_adoption",
                "c4_mediation_bypass",
                "readiness_claim",
            },
        )
        for family in INVALID_FIXTURE_FAMILY_PLAN.values():
            self.assertIn(family["future_target"], FUTURE_INVALID_FIXTURE_TARGETS)
            self.assertFalse(Path(family["future_target"]).exists())

    def test_seed_terms_are_separated_from_lab_evidence_only_material(self) -> None:
        self.assertIn("recipe_owns_truth_prior", SEED_TERM_FIXTURE_MATERIAL["allowed_as_fixture_material"])
        self.assertIn(
            "reference_envelope_positive_fixture",
            SEED_TERM_FIXTURE_MATERIAL["allowed_as_fixture_material"],
        )
        for lab_only in [
            "prior_card_generation_readiness",
            "raw_yaml_payload",
            "frame_buffer_truth",
            "runtime_sla",
        ]:
            self.assertIn(lab_only, SEED_TERM_FIXTURE_MATERIAL["lab_evidence_only"])

    def test_missing_target_behavior_remains_not_applicable_for_yaml_inputs(self) -> None:
        self.assertEqual(
            VALIDATOR_MISSING_TARGET_BEHAVIOR["formal_dictionary_missing_status"],
            "not_applicable_dictionary_missing",
        )
        self.assertEqual(
            VALIDATOR_MISSING_TARGET_BEHAVIOR["future_fixture_missing_status"],
            "not_applicable_dictionary_missing",
        )
        self.assertTrue(VALIDATOR_MISSING_TARGET_BEHAVIOR["missing_yaml_target_passes"])
        self.assertTrue(VALIDATOR_MISSING_TARGET_BEHAVIOR["missing_schema_target_fails"])

    def test_stop_lines_and_decision_output_block_creation_and_claims(self) -> None:
        for stop_line in [
            "no_yaml_fixture_creation",
            "no_formal_dictionary_creation",
            "no_schema_json_modification",
            "no_validator_modification",
            "no_dictionary_usable_claim",
            "no_readiness_claim",
        ]:
            self.assertIn(stop_line, STOP_LINES_PRESERVED)
        self.assertTrue(DECISION_OUTPUT["minimal_yaml_fixture_planning_gate_passed"])
        for key in [
            "yaml_fixture_creation_authorized",
            "formal_dictionary_creation_authorized",
            "schema_json_modification_authorized",
            "validator_modification_authorized",
            "runtime_execution_authorized",
            "renderer_behavior_authorized",
            "formula_movement_authorized",
            "dictionary_usable_claimed",
            "readiness_claimed",
            "correctness_claimed",
            "visual_parity_claimed",
            "runtime_replacement_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_recommended_next_gate_is_fixture_creation_not_formal_dictionary(self) -> None:
        self.assertEqual(
            RECOMMENDED_NEXT_GATE,
            "c3_prior_semantic_dictionary_minimal_yaml_fixture_gate",
        )


if __name__ == "__main__":
    unittest.main()
