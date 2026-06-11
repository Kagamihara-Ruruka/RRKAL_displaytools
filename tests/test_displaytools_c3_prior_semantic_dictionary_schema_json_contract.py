"""Contract tests for the c3 prior semantic dictionary JSON Schema v0."""

from pathlib import Path
import json
import unittest

from tests import test_displaytools_c3_prior_semantic_dictionary_schema_json_contract_planning as planning
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_contract as yaml_contract
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning as validator_planning
from tests import test_displaytools_c3_prior_material_third_settlement as third_settlement


SCHEMA_PATH = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json")
README_PATH = Path("docs/c3_prior_dictionary/README.zh-TW.md")
YAML_DICTIONARY_PATH = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml")
VALIDATOR_PATH = Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py")


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


class C3PriorSemanticDictionarySchemaJsonContractTest(unittest.TestCase):
    def test_schema_and_readme_exist_and_yaml_is_still_absent(self):
        self.assertTrue(SCHEMA_PATH.exists())
        self.assertTrue(README_PATH.exists())
        self.assertFalse(YAML_DICTIONARY_PATH.exists())
        self.assertEqual(VALIDATOR_PATH.as_posix(), planning.FUTURE_VALIDATOR_TARGET)

    def test_schema_json_parses_and_has_identity_fields(self):
        schema = load_schema()
        for field in planning.SCHEMA_IDENTITY_FIELDS:
            self.assertIn(field, schema)
        self.assertEqual(schema["type"], "object")
        self.assertFalse(schema["additionalProperties"])

    def test_required_top_level_sections_match_planning_and_yaml_contract(self):
        schema = load_schema()
        self.assertEqual(schema["required"], planning.PLANNED_TOP_LEVEL_REQUIRED_SECTIONS)
        self.assertEqual(set(schema["properties"]), set(planning.PLANNED_TOP_LEVEL_REQUIRED_SECTIONS))
        self.assertEqual(set(schema["properties"]), set(yaml_contract.SECTION_CONTRACTS))

    def test_reusable_definitions_are_present(self):
        schema = load_schema()
        definitions = schema["$defs"]
        for definition in planning.REUSABLE_DEFINITIONS:
            self.assertIn(definition, definitions)
        self.assertIn("phenomenon_translation_entry", definitions)
        self.assertIn("dictionary_metadata", definitions)
        self.assertIn("recipe_authoring_contract", definitions)
        self.assertIn("c4_mediation_contract", definitions)

    def test_enum_families_match_planning_and_yaml_contract(self):
        definitions = load_schema()["$defs"]
        self.assertEqual(
            definitions["authority_family_values"]["enum"],
            yaml_contract.TERM_ENTRY_CONTRACT["authority_family_values"],
        )
        self.assertEqual(
            definitions["confidence_values"]["enum"],
            yaml_contract.TERM_ENTRY_CONTRACT["confidence_values"],
        )
        self.assertEqual(
            definitions["lifecycle_status_values"]["enum"],
            yaml_contract.TERM_ENTRY_CONTRACT["lifecycle_status_values"],
        )
        self.assertEqual(set(definitions["entry_kind_values"]["enum"]), {"mapping", "list"})

    def test_prior_term_entry_shape_matches_yaml_contract(self):
        prior_term = load_schema()["$defs"]["prior_term_entry"]
        self.assertFalse(prior_term["additionalProperties"])
        self.assertEqual(prior_term["required"], yaml_contract.TERM_ENTRY_CONTRACT["required_fields"])
        term_id = prior_term["properties"]["term_id"]
        self.assertEqual(set(term_id["not"]["enum"]), set(["layer", "mask", "view", "projection", "frame", "render", "recipe"]))

    def test_required_entry_definitions_use_additional_properties_false_where_reasonable(self):
        definitions = load_schema()["$defs"]
        for definition in [
            "evidence_ref",
            "dictionary_metadata",
            "authority_source_entry",
            "phenomenon_translation_entry",
            "prior_term_entry",
            "view_family_entry",
            "layer_taxonomy_entry",
            "recipe_authoring_contract",
            "c4_mediation_contract",
            "legacy_fossil_translation_entry",
            "stop_line_entry",
            "unknown_stop_line_entry",
            "validator_expectation_entry",
        ]:
            self.assertFalse(definitions[definition]["additionalProperties"], definition)

    def test_forbidden_runtime_field_families_are_encoded(self):
        schema = load_schema()
        self.assertEqual(
            set(schema["x-rrkal-forbidden-field-families"]),
            set(planning.FORBIDDEN_FIELD_FAMILIES),
        )
        self.assertEqual(
            set(schema["$defs"]["forbidden_field_family_values"]["enum"]),
            set(planning.FORBIDDEN_FIELD_FAMILIES),
        )

    def test_stop_line_fields_are_present(self):
        stop_line = load_schema()["$defs"]["stop_line_entry"]
        self.assertEqual(
            stop_line["required"],
            ["stop_line_id", "reason", "blocked_claims", "reopen_condition"],
        )
        self.assertIn("status", stop_line["properties"])
        unknown = load_schema()["$defs"]["unknown_stop_line_entry"]
        self.assertEqual(
            unknown["required"],
            ["unknown_id", "why_unknown", "allowed_reference_use", "resolution_gate"],
        )

    def test_validator_planning_and_third_settlement_evidence_remain_sources(self):
        self.assertTrue(validator_planning.DECISION_OUTPUT["schema_validator_planning_gate_passed"])
        self.assertTrue(third_settlement.DECISION_OUTPUT["third_settlement_gate_passed"])
        self.assertTrue(planning.DECISION_OUTPUT["schema_json_contract_planning_gate_passed"])

    def test_boundary_does_not_authorize_runtime_or_claims(self):
        boundary = load_schema()["x-rrkal-boundary"]
        for forbidden in [
            "No YAML dictionary",
            "validator script",
            "prototype",
            "runtime API",
            "renderer behavior",
            "formula movement",
            "readiness claim",
            "correctness claim",
            "visual parity claim",
            "runtime replacement authorization",
        ]:
            self.assertIn(forbidden, boundary)


if __name__ == "__main__":
    unittest.main()
