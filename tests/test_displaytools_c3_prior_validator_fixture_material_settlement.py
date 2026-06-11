"""Docs/test-only settlement for c_3 prior validator fixture materials.

This gate classifies fixture-oriented lab materials before any formal YAML
dictionary entries are created. It does not modify schema JSON or the validator.
"""

from pathlib import Path
import unittest


VALIDATOR_SCRIPT = Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py")
SCHEMA_JSON = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json")
YAML_DICTIONARY = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml")

SETTLEMENT_CATEGORIES = {
    "prior_dictionary_candidate",
    "schema_field_candidate",
    "validator_rule_candidate",
    "authority_reference_only",
    "lab_evidence_reference",
    "caveat_required",
    "stop_line",
    "not_yet_allowed",
}

MATERIAL_INVENTORY = {
    "c4_c3_validator_failure_card_edge_scout": {
        "categories": {
            "schema_field_candidate",
            "validator_rule_candidate",
            "lab_evidence_reference",
            "caveat_required",
        },
        "accepted_fields": {
            "validation_result_ref",
            "failed_rule_id",
            "error_code",
            "diagnostics_ref",
            "dictionary_ref",
            "schema_ref",
            "evidence_refs",
            "status",
            "producer",
            "schema_version",
        },
        "validator_fixture_use": "failure_card_edge_fixture_candidate",
        "caveat": "failure card records validator result references only and does not hand off raw YAML payloads",
        "stop_lines": {
            "no_raw_yaml_payload",
            "no_dataframe",
            "no_framebuffer",
            "no_c4_validator_ownership",
            "no_runtime_handoff",
        },
    },
    "c2_c3_display_hint_validator_negative_fixture_scout": {
        "categories": {
            "validator_rule_candidate",
            "lab_evidence_reference",
            "caveat_required",
            "stop_line",
        },
        "accepted_negative_fixture_families": {
            "unknown_lod_hint",
            "bbox_axis_order_ambiguity",
            "bbox_without_coord_ref",
            "invalid_time_window",
            "credential_bearing_tile_ref",
            "unitless_density_hint",
            "unitless_sample_budget",
            "sample_budget_mistaken_as_sla",
        },
        "validator_fixture_use": "display_hint_negative_fixture_candidate",
        "caveat": "display hints remain planning evidence and do not transfer c2 compression or preaggregation ownership",
        "stop_lines": {
            "no_runtime_sla",
            "no_tile_secret",
            "no_compression_algorithm_transfer",
            "no_vizasset_schema_change",
        },
    },
    "c1_c3_reference_envelope_validator_positive_fixture_scout": {
        "categories": {
            "prior_dictionary_candidate",
            "schema_field_candidate",
            "validator_rule_candidate",
            "lab_evidence_reference",
            "caveat_required",
        },
        "accepted_positive_fixture_fields": {
            "asset_id",
            "subject_ref",
            "source_ref",
            "schema_ref",
            "sample_query_ref",
            "spatial_extent",
            "temporal_extent",
            "evidence_refs",
            "safety",
            "review",
        },
        "validator_fixture_use": "reference_envelope_positive_fixture_candidate",
        "caveat": "reference envelope is sealed, redacted, and non-fetchable; it is not a c1 consumption API",
        "stop_lines": {
            "no_payload",
            "no_dataframe",
            "no_db_query",
            "no_fetchable_source",
            "no_cleaning_transfer",
            "no_c3_consumes_c1_claim",
        },
    },
    "a1_c3_prior_dictionary_minimal_yaml_entry_shape_scout": {
        "categories": {
            "prior_dictionary_candidate",
            "schema_field_candidate",
            "validator_rule_candidate",
            "lab_evidence_reference",
            "caveat_required",
        },
        "accepted_entry_shape_surfaces": {
            "prior_terms",
            "view_families",
            "layer_taxonomy",
            "c4_mediation",
            "stop_lines",
            "unknown_stop_lines",
            "forbidden_fields",
        },
        "validator_fixture_use": "minimal_yaml_entry_shape_fixture_candidate",
        "caveat": "lab note has mojibake-heavy prose, so only stable token-level fixture surfaces are settled",
        "stop_lines": {
            "no_yaml_dictionary_creation",
            "no_schema_json_change",
            "no_validator_change",
            "no_runtime_state",
            "no_renderer_state",
            "no_raw_payload",
            "no_implementation_authorization",
        },
    },
    "current_validator_gate": {
        "categories": {
            "authority_reference_only",
            "validator_rule_candidate",
            "stop_line",
        },
        "accepted_validator_behaviors": {
            "schema_json_parse_pass",
            "missing_yaml_not_applicable",
            "missing_schema_fail",
            "malformed_schema_fail",
            "forbidden_family_detection",
        },
        "validator_fixture_use": "current_validator_behavior_reference",
        "caveat": "validator exists but formal YAML dictionary remains absent",
        "stop_lines": {
            "no_yaml_dictionary_creation",
            "no_schema_json_change",
            "no_runtime_execution",
            "no_readiness_claim",
        },
    },
}

DECISION_OUTPUT = {
    "validator_fixture_material_settlement_passed": True,
    "fixture_materials_settled": True,
    "yaml_dictionary_creation_authorized": False,
    "schema_json_modification_authorized": False,
    "validator_script_modification_authorized": False,
    "runtime_execution_authorized": False,
    "renderer_behavior_authorized": False,
    "formula_movement_authorized": False,
    "c1_c2_c4_integration_authorized": False,
    "readiness_claimed": False,
    "visual_parity_claimed": False,
    "correctness_claimed": False,
    "runtime_replacement_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_minimal_yaml_fixture_planning_gate"


class C3PriorValidatorFixtureMaterialSettlementTest(unittest.TestCase):
    def test_required_material_inventory_is_complete(self) -> None:
        self.assertEqual(
            set(MATERIAL_INVENTORY),
            {
                "c4_c3_validator_failure_card_edge_scout",
                "c2_c3_display_hint_validator_negative_fixture_scout",
                "c1_c3_reference_envelope_validator_positive_fixture_scout",
                "a1_c3_prior_dictionary_minimal_yaml_entry_shape_scout",
                "current_validator_gate",
            },
        )

    def test_all_categories_are_known(self) -> None:
        for material in MATERIAL_INVENTORY.values():
            self.assertTrue(material["categories"])
            self.assertTrue(material["categories"].issubset(SETTLEMENT_CATEGORIES))

    def test_c4_failure_card_edges_are_settled_as_result_references_only(self) -> None:
        material = MATERIAL_INVENTORY["c4_c3_validator_failure_card_edge_scout"]
        self.assertIn("validation_result_ref", material["accepted_fields"])
        self.assertIn("failed_rule_id", material["accepted_fields"])
        self.assertIn("error_code", material["accepted_fields"])
        self.assertIn("no_raw_yaml_payload", material["stop_lines"])
        self.assertIn("no_c4_validator_ownership", material["stop_lines"])

    def test_c2_negative_fixtures_preserve_display_hint_stop_lines(self) -> None:
        material = MATERIAL_INVENTORY["c2_c3_display_hint_validator_negative_fixture_scout"]
        for fixture in [
            "unknown_lod_hint",
            "bbox_axis_order_ambiguity",
            "bbox_without_coord_ref",
            "credential_bearing_tile_ref",
            "sample_budget_mistaken_as_sla",
        ]:
            self.assertIn(fixture, material["accepted_negative_fixture_families"])
        self.assertIn("no_runtime_sla", material["stop_lines"])
        self.assertIn("no_compression_algorithm_transfer", material["stop_lines"])

    def test_c1_positive_reference_envelope_is_non_payload_and_non_fetchable(self) -> None:
        material = MATERIAL_INVENTORY["c1_c3_reference_envelope_validator_positive_fixture_scout"]
        for field in [
            "asset_id",
            "subject_ref",
            "source_ref",
            "schema_ref",
            "sample_query_ref",
            "spatial_extent",
            "temporal_extent",
            "evidence_refs",
        ]:
            self.assertIn(field, material["accepted_positive_fixture_fields"])
        for stop_line in ["no_payload", "no_dataframe", "no_db_query", "no_fetchable_source"]:
            self.assertIn(stop_line, material["stop_lines"])

    def test_a1_minimal_entry_shape_is_fixture_material_not_yaml_creation(self) -> None:
        material = MATERIAL_INVENTORY["a1_c3_prior_dictionary_minimal_yaml_entry_shape_scout"]
        for surface in ["prior_terms", "view_families", "layer_taxonomy", "c4_mediation"]:
            self.assertIn(surface, material["accepted_entry_shape_surfaces"])
        self.assertIn("no_yaml_dictionary_creation", material["stop_lines"])
        self.assertIn("no_implementation_authorization", material["stop_lines"])
        self.assertIn("mojibake-heavy prose", material["caveat"])

    def test_current_validator_gate_is_reference_not_modification_authorization(self) -> None:
        material = MATERIAL_INVENTORY["current_validator_gate"]
        self.assertTrue(VALIDATOR_SCRIPT.exists())
        self.assertTrue(SCHEMA_JSON.exists())
        self.assertFalse(YAML_DICTIONARY.exists())
        self.assertIn("missing_yaml_not_applicable", material["accepted_validator_behaviors"])
        self.assertIn("forbidden_family_detection", material["accepted_validator_behaviors"])

    def test_decision_output_blocks_yaml_schema_validator_runtime_and_claims(self) -> None:
        self.assertTrue(DECISION_OUTPUT["validator_fixture_material_settlement_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_json_modification_authorized",
            "validator_script_modification_authorized",
            "runtime_execution_authorized",
            "renderer_behavior_authorized",
            "formula_movement_authorized",
            "c1_c2_c4_integration_authorized",
            "readiness_claimed",
            "visual_parity_claimed",
            "correctness_claimed",
            "runtime_replacement_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_recommended_next_gate_remains_fixture_planning_not_dictionary_creation(self) -> None:
        self.assertEqual(
            RECOMMENDED_NEXT_GATE,
            "c3_prior_semantic_dictionary_minimal_yaml_fixture_planning_gate",
        )


if __name__ == "__main__":
    unittest.main()
