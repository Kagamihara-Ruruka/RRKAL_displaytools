"""Docs/test-only settlement for c_3 YAML fixture expectation materials.

This gate settles expectation materials for the next fixture expansion. It
creates no YAML fixtures and does not modify schema JSON or the validator.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture as fixture_gate
from tests import test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture_planning as fixture_planning


FORMAL_DICTIONARY = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml")
SCHEMA_JSON = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json")
VALIDATOR_SCRIPT = Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py")

SETTLEMENT_CATEGORIES = {
    "fixture_style_rule",
    "validator_expectation_candidate",
    "schema_pressure_candidate",
    "card_edge_expectation_candidate",
    "reference_only_guard",
    "planning_only_guard",
    "negative_fixture_candidate",
    "stop_line",
    "not_yet_allowed",
}

MATERIAL_SETTLEMENT = {
    "a1_c3_yaml_fixture_readability_and_fixture_style_audit": {
        "categories": {
            "fixture_style_rule",
            "planning_only_guard",
            "stop_line",
        },
        "accepted": True,
        "settlement": "future_fixture_style_rule",
        "accepted_surfaces": {
            "yaml_fixture_naming_rule",
            "valid_fixture_filename_rule",
            "invalid_fixture_filename_rule",
            "field_order_recommendation",
            "single_error_per_negative_fixture_rule",
            "formal_dictionary_confusion_prevention",
        },
        "caveat": "lab prose is mojibake-heavy, so only stable coverage labels are settled",
        "stop_lines": {
            "no_yaml_fixture_creation_in_this_gate",
            "no_schema_or_validator_modification",
            "no_production_use_claim",
        },
    },
    "c1_c3_reference_envelope_fixture_validator_expectation_scout": {
        "categories": {
            "validator_expectation_candidate",
            "schema_pressure_candidate",
            "reference_only_guard",
            "planning_only_guard",
        },
        "accepted": True,
        "settlement": "future_fixture_material",
        "accepted_surfaces": {
            "asset_id",
            "subject_ref",
            "source_ref",
            "schema_ref",
            "sample_query_ref",
            "spatial_extent",
            "temporal_extent",
            "evidence_refs",
            "redaction",
            "review",
        },
        "stop_lines": {
            "no_payload",
            "no_db_query",
            "no_raw_row",
            "no_fetchable_source_ref",
            "no_callable_sample_query_ref",
            "no_c3_consumes_c1_claim",
        },
    },
    "c2_c3_display_hint_fixture_validator_expectation_scout": {
        "categories": {
            "validator_expectation_candidate",
            "schema_pressure_candidate",
            "negative_fixture_candidate",
            "planning_only_guard",
            "stop_line",
        },
        "accepted": True,
        "settlement": "future_fixture_material",
        "accepted_surfaces": {
            "lod_hint",
            "bbox",
            "coord_ref",
            "time_window",
            "tile_ref",
            "density_hint",
            "sample_budget",
            "planning_only",
        },
        "stop_lines": {
            "no_vizasset_schema_modification",
            "no_cli_modification",
            "no_compression_algorithm_transfer",
            "no_runtime_sla",
            "no_downstream_ready_claim",
        },
    },
    "c4_c3_yaml_fixture_validation_card_expectation_scout": {
        "categories": {
            "card_edge_expectation_candidate",
            "validator_expectation_candidate",
            "reference_only_guard",
            "stop_line",
        },
        "accepted": True,
        "settlement": "future_card_edge_fixture_material",
        "accepted_surfaces": {
            "validation_result_ref",
            "dictionary_ref",
            "schema_ref",
            "diagnostics_ref",
            "failed_rule_id",
            "error_code",
            "status",
            "producer",
            "schema_version",
            "evidence_refs",
            "output_card_ref",
        },
        "stop_lines": {
            "no_yaml_parse_by_c4",
            "no_validator_ownership_transfer",
            "no_fixture_repair_by_c4",
            "no_raw_payload_handoff",
            "no_c3_direct_c1_connection",
        },
    },
    "current_minimal_yaml_fixture_gate": {
        "categories": {
            "validator_expectation_candidate",
            "planning_only_guard",
            "stop_line",
        },
        "accepted": True,
        "settlement": "current_fixture_baseline",
        "accepted_surfaces": {
            "minimal_first_slice_valid",
            "invalid_missing_required_section",
            "invalid_bare_high_risk_term_id",
            "invalid_forbidden_runtime_field",
        },
        "stop_lines": {
            "formal_dictionary_not_authorized",
            "schema_json_not_modified",
            "validator_script_not_modified",
        },
    },
}

NEXT_INVALID_FIXTURE_RECOMMENDATION = [
    "invalid_legacy_fossil_direct_adoption.yaml",
    "invalid_c4_mediation_bypass.yaml",
    "invalid_readiness_claim.yaml",
]

DECISION_OUTPUT = {
    "yaml_fixture_expectation_material_settlement_passed": True,
    "a1_style_audit_accepted_as_future_fixture_style_rule": True,
    "c1_reference_envelope_expectation_accepted_as_future_fixture_material": True,
    "c2_display_hint_expectation_accepted_as_future_fixture_material": True,
    "c4_validation_card_expectation_accepted_as_future_card_edge_fixture_material": True,
    "next_invalid_fixture_recommendation": NEXT_INVALID_FIXTURE_RECOMMENDATION,
    "formal_dictionary_authorized": False,
    "additional_yaml_fixture_creation_authorized": False,
    "schema_json_modification_authorized": False,
    "validator_script_modification_authorized": False,
    "runtime_execution_authorized": False,
    "renderer_behavior_authorized": False,
    "formula_movement_authorized": False,
    "c1_c2_c4_real_integration_authorized": False,
    "dictionary_usable_claimed": False,
    "readiness_claimed": False,
    "correctness_claimed": False,
    "visual_parity_claimed": False,
    "runtime_replacement_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_yaml_invalid_fixture_expansion_gate"


class C3PriorYamlFixtureExpectationMaterialSettlementTest(unittest.TestCase):
    def test_material_inventory_is_complete(self) -> None:
        self.assertEqual(
            set(MATERIAL_SETTLEMENT),
            {
                "a1_c3_yaml_fixture_readability_and_fixture_style_audit",
                "c1_c3_reference_envelope_fixture_validator_expectation_scout",
                "c2_c3_display_hint_fixture_validator_expectation_scout",
                "c4_c3_yaml_fixture_validation_card_expectation_scout",
                "current_minimal_yaml_fixture_gate",
            },
        )

    def test_all_categories_are_known(self) -> None:
        for material in MATERIAL_SETTLEMENT.values():
            self.assertTrue(material["categories"])
            self.assertTrue(material["categories"].issubset(SETTLEMENT_CATEGORIES))

    def test_current_fixture_gate_and_planning_gate_remain_source_evidence(self) -> None:
        self.assertTrue(fixture_gate.VALID_FIXTURE.exists())
        self.assertFalse(fixture_gate.FORMAL_DICTIONARY.exists())
        self.assertTrue(fixture_planning.DECISION_OUTPUT["minimal_yaml_fixture_planning_gate_passed"])
        self.assertTrue(fixture_planning.DECISION_OUTPUT["planned_fixture_creation_completed"])

    def test_a1_style_audit_is_accepted_as_future_fixture_style_rule(self) -> None:
        material = MATERIAL_SETTLEMENT["a1_c3_yaml_fixture_readability_and_fixture_style_audit"]
        self.assertTrue(material["accepted"])
        self.assertIn("fixture_style_rule", material["categories"])
        self.assertIn("single_error_per_negative_fixture_rule", material["accepted_surfaces"])
        self.assertIn("formal_dictionary_confusion_prevention", material["accepted_surfaces"])
        self.assertIn("mojibake-heavy", material["caveat"])

    def test_c1_reference_envelope_expectation_is_future_fixture_material(self) -> None:
        material = MATERIAL_SETTLEMENT["c1_c3_reference_envelope_fixture_validator_expectation_scout"]
        self.assertTrue(material["accepted"])
        for surface in ["asset_id", "source_ref", "sample_query_ref", "redaction", "review"]:
            self.assertIn(surface, material["accepted_surfaces"])
        for stop_line in ["no_payload", "no_db_query", "no_fetchable_source_ref", "no_c3_consumes_c1_claim"]:
            self.assertIn(stop_line, material["stop_lines"])

    def test_c2_display_hint_expectation_is_future_fixture_material(self) -> None:
        material = MATERIAL_SETTLEMENT["c2_c3_display_hint_fixture_validator_expectation_scout"]
        self.assertTrue(material["accepted"])
        for surface in ["lod_hint", "bbox", "coord_ref", "time_window", "tile_ref", "sample_budget"]:
            self.assertIn(surface, material["accepted_surfaces"])
        for stop_line in ["no_compression_algorithm_transfer", "no_runtime_sla", "no_downstream_ready_claim"]:
            self.assertIn(stop_line, material["stop_lines"])

    def test_c4_validation_card_expectation_is_future_card_edge_fixture_material(self) -> None:
        material = MATERIAL_SETTLEMENT["c4_c3_yaml_fixture_validation_card_expectation_scout"]
        self.assertTrue(material["accepted"])
        for surface in ["validation_result_ref", "dictionary_ref", "schema_ref", "failed_rule_id", "error_code"]:
            self.assertIn(surface, material["accepted_surfaces"])
        for stop_line in ["no_yaml_parse_by_c4", "no_validator_ownership_transfer", "no_raw_payload_handoff"]:
            self.assertIn(stop_line, material["stop_lines"])

    def test_next_invalid_fixture_recommendation_order_is_fixed(self) -> None:
        self.assertEqual(
            NEXT_INVALID_FIXTURE_RECOMMENDATION,
            [
                "invalid_legacy_fossil_direct_adoption.yaml",
                "invalid_c4_mediation_bypass.yaml",
                "invalid_readiness_claim.yaml",
            ],
        )

    def test_formal_dictionary_schema_validator_and_runtime_remain_unauthorized(self) -> None:
        self.assertFalse(FORMAL_DICTIONARY.exists())
        self.assertTrue(SCHEMA_JSON.exists())
        self.assertTrue(VALIDATOR_SCRIPT.exists())
        for key in [
            "formal_dictionary_authorized",
            "additional_yaml_fixture_creation_authorized",
            "schema_json_modification_authorized",
            "validator_script_modification_authorized",
            "runtime_execution_authorized",
            "renderer_behavior_authorized",
            "formula_movement_authorized",
            "c1_c2_c4_real_integration_authorized",
            "dictionary_usable_claimed",
            "readiness_claimed",
            "correctness_claimed",
            "visual_parity_claimed",
            "runtime_replacement_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_recommended_next_gate_is_invalid_fixture_expansion_not_dictionary(self) -> None:
        self.assertEqual(
            RECOMMENDED_NEXT_GATE,
            "c3_prior_semantic_dictionary_yaml_invalid_fixture_expansion_gate",
        )


if __name__ == "__main__":
    unittest.main()
