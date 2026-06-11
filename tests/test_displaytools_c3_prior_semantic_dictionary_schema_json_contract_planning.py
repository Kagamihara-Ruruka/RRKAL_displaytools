"""Docs/test-only planning for the c3 prior semantic dictionary JSON Schema contract."""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_contract as yaml_contract
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning as validator_planning
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_skeleton_planning as skeleton_planning


FUTURE_SCHEMA_TARGET = "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json"
FUTURE_YAML_TARGET = "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml"
FUTURE_VALIDATOR_TARGET = "scripts/validate_displaytools_c3_prior_semantic_dictionary.py"
FUTURE_DICTIONARY_CONTRACT_TEST = "tests/test_displaytools_c3_prior_semantic_dictionary_contract.py"

SCHEMA_IDENTITY_FIELDS = [
    "$schema",
    "$id",
    "title",
    "type",
    "required",
    "properties",
    "additionalProperties",
    "definitions",
]

PLANNED_TOP_LEVEL_REQUIRED_SECTIONS = list(skeleton_planning.YAML_TOP_LEVEL_SECTIONS)

REUSABLE_DEFINITIONS = [
    "evidence_ref",
    "authority_source_entry",
    "prior_term_entry",
    "view_family_entry",
    "layer_taxonomy_entry",
    "legacy_fossil_translation_entry",
    "stop_line_entry",
    "unknown_stop_line_entry",
    "validator_expectation_entry",
]

ENUM_FAMILIES = {
    "authority_family_values": list(yaml_contract.TERM_ENTRY_CONTRACT["authority_family_values"]),
    "confidence_values": list(yaml_contract.TERM_ENTRY_CONTRACT["confidence_values"]),
    "lifecycle_status_values": list(yaml_contract.TERM_ENTRY_CONTRACT["lifecycle_status_values"]),
    "entry_kind_values": ["mapping", "list"],
    "stop_line_status_values": [
        "blocked",
        "planned_only",
        "not_applicable_candidate_missing",
        "requires_resolution_gate",
    ],
}

FORBIDDEN_FIELD_FAMILIES = [
    "runtime_state",
    "renderer_state",
    "frame_buffer",
    "callable",
    "runtime_object",
    "dataframe",
    "raw_payload_contract",
    "c1_direct_dependency",
    "odoriba_bypass",
    "ui_state_as_truth",
    "legacy_runtime_patch_as_ideal_form",
    "implementation_authorized",
    "readiness_claimed",
]

SECTION_REQUIRED_FIELD_PLAN = {
    section: list(contract["required_fields"])
    for section, contract in yaml_contract.SECTION_CONTRACTS.items()
}

VALIDATOR_ALIGNMENT = {
    "missing_required_section": "root required sections and properties",
    "unknown_top_level_section": "root additionalProperties false",
    "missing_required_entry_field": "reusable entry definitions required fields",
    "bare_high_risk_term_id": "validator expectation entry plus prior term entry term_id rules",
    "unresolved_authority_ref": "authority source ref contract and evidence_ref definition",
    "legacy_fossil_direct_adoption": "legacy fossil translation entry and forbidden field families",
    "stop_line_authorizes_implementation": "stop_line_entry status enum and implementation_authorized rejection",
    "unknown_stop_line_without_resolution_gate": "unknown_stop_line_entry resolution gate fields",
    "recipe_truth_owned_by_ui": "recipe_authoring section and ui_state_as_truth rejection",
    "c4_mediation_bypassed": "c4_mediation section and odoriba_bypass rejection",
    "runtime_json_compilation_authorized": "validator_expectations plus runtime authorization rejection",
    "prototype_runtime_renderer_formula_authorized": "forbidden field families and stop line preservation",
}

SCHEMA_CONTRACT_PLANNING_MATRIX = {
    "schema_identity": {
        "future_schema_target": FUTURE_SCHEMA_TARGET,
        "identity_fields": SCHEMA_IDENTITY_FIELDS,
        "schema_file_creation_authorized": False,
    },
    "root_contract": {
        "type": "object",
        "required": PLANNED_TOP_LEVEL_REQUIRED_SECTIONS,
        "additionalProperties": False,
    },
    "definitions": {name: {"planned_only": True} for name in REUSABLE_DEFINITIONS},
    "enum_families": ENUM_FAMILIES,
    "forbidden_field_families": FORBIDDEN_FIELD_FAMILIES,
    "validator_alignment": VALIDATOR_ALIGNMENT,
}

MISSING_TARGET_BEHAVIOR = {
    "future_schema_target": FUTURE_SCHEMA_TARGET,
    "future_yaml_target": FUTURE_YAML_TARGET,
    "future_validator_target": FUTURE_VALIDATOR_TARGET,
    "status": "not_applicable_candidate_missing",
    "schema_file_created": False,
    "yaml_dictionary_created": False,
    "validator_script_created": False,
}

DECISION_OUTPUT = {
    "schema_json_contract_planning_gate_passed": True,
    "future_schema_target": FUTURE_SCHEMA_TARGET,
    "yaml_contract_gate_passed": yaml_contract.DECISION_OUTPUT["yaml_contract_gate_passed"],
    "schema_validator_planning_gate_passed": validator_planning.DECISION_OUTPUT[
        "schema_validator_planning_gate_passed"
    ],
    "yaml_skeleton_planning_gate_passed": skeleton_planning.PLANNING_DECISION[
        "yaml_skeleton_planning_gate_passed"
    ],
    "schema_file_creation_authorized": False,
    "yaml_dictionary_creation_authorized": False,
    "validator_script_creation_authorized": False,
    "future_dictionary_contract_test_creation_authorized": False,
    "prototype_authorized": False,
    "runtime_execution_authorized": False,
    "renderer_behavior_authorized": False,
    "formula_movement_authorized": False,
    "c4_implementation_change_authorized": False,
    "readiness_claimed": False,
    "correctness_claimed": False,
    "visual_parity_claimed": False,
    "leak_fix_claimed": False,
    "runtime_replacement_authorized": False,
}

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 prior semantic dictionary schema JSON contract planning gate. "
    "This gate plans the future JSON Schema identity, top-level required sections, "
    "reusable definitions, enum families, forbidden field families, and validator alignment "
    "for a future c_3 prior semantic dictionary. It does not create YAML dictionary files, "
    "schema files, validator scripts, future dictionary contract tests, prototype code, "
    "runtime behavior, renderer behavior, formula movement, c_4 implementation changes, "
    "readiness claims, correctness claims, leak-fix claims, or runtime replacement authorization."
)


class C3PriorSemanticDictionarySchemaJsonContractPlanningTest(unittest.TestCase):
    def test_source_gates_pass_and_future_schema_target_is_planned_only(self):
        self.assertTrue(DECISION_OUTPUT["yaml_contract_gate_passed"])
        self.assertTrue(DECISION_OUTPUT["schema_validator_planning_gate_passed"])
        self.assertTrue(DECISION_OUTPUT["yaml_skeleton_planning_gate_passed"])
        self.assertEqual(
            FUTURE_SCHEMA_TARGET,
            "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
        )
        self.assertEqual(Path(FUTURE_SCHEMA_TARGET).as_posix(), FUTURE_SCHEMA_TARGET)
        self.assertFalse(Path(FUTURE_YAML_TARGET).exists())
        self.assertEqual(Path(FUTURE_VALIDATOR_TARGET).as_posix(), FUTURE_VALIDATOR_TARGET)

    def test_schema_identity_fields_are_complete(self):
        self.assertEqual(
            set(SCHEMA_IDENTITY_FIELDS),
            {
                "$schema",
                "$id",
                "title",
                "type",
                "required",
                "properties",
                "additionalProperties",
                "definitions",
            },
        )

    def test_top_level_required_sections_match_yaml_skeleton(self):
        self.assertEqual(
            PLANNED_TOP_LEVEL_REQUIRED_SECTIONS,
            skeleton_planning.YAML_TOP_LEVEL_SECTIONS,
        )
        self.assertEqual(
            set(PLANNED_TOP_LEVEL_REQUIRED_SECTIONS),
            {
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
            },
        )

    def test_reusable_definitions_are_complete(self):
        self.assertEqual(
            set(REUSABLE_DEFINITIONS),
            {
                "evidence_ref",
                "authority_source_entry",
                "prior_term_entry",
                "view_family_entry",
                "layer_taxonomy_entry",
                "legacy_fossil_translation_entry",
                "stop_line_entry",
                "unknown_stop_line_entry",
                "validator_expectation_entry",
            },
        )

    def test_enum_families_align_with_yaml_contract(self):
        self.assertEqual(
            ENUM_FAMILIES["authority_family_values"],
            yaml_contract.TERM_ENTRY_CONTRACT["authority_family_values"],
        )
        self.assertEqual(
            ENUM_FAMILIES["confidence_values"],
            yaml_contract.TERM_ENTRY_CONTRACT["confidence_values"],
        )
        self.assertEqual(
            ENUM_FAMILIES["lifecycle_status_values"],
            yaml_contract.TERM_ENTRY_CONTRACT["lifecycle_status_values"],
        )
        self.assertEqual(set(ENUM_FAMILIES["entry_kind_values"]), {"mapping", "list"})
        section_entry_kinds = {
            contract["entry_kind"] for contract in yaml_contract.SECTION_CONTRACTS.values()
        }
        self.assertLessEqual(section_entry_kinds, set(ENUM_FAMILIES["entry_kind_values"]))

    def test_required_fields_align_with_yaml_contract(self):
        self.assertEqual(
            set(SECTION_REQUIRED_FIELD_PLAN),
            set(yaml_contract.SECTION_CONTRACTS),
        )
        for section, contract in yaml_contract.SECTION_CONTRACTS.items():
            self.assertEqual(
                SECTION_REQUIRED_FIELD_PLAN[section],
                contract["required_fields"],
            )
        self.assertEqual(
            yaml_contract.TERM_ENTRY_CONTRACT["required_fields"],
            skeleton_planning.MINIMUM_ENTRY_SHAPE,
        )

    def test_forbidden_field_families_are_complete(self):
        self.assertEqual(
            set(FORBIDDEN_FIELD_FAMILIES),
            {
                "runtime_state",
                "renderer_state",
                "frame_buffer",
                "callable",
                "runtime_object",
                "dataframe",
                "raw_payload_contract",
                "c1_direct_dependency",
                "odoriba_bypass",
                "ui_state_as_truth",
                "legacy_runtime_patch_as_ideal_form",
                "implementation_authorized",
                "readiness_claimed",
            },
        )
        yaml_forbidden = set(FORBIDDEN_FIELD_FAMILIES)
        for contract in yaml_contract.SECTION_CONTRACTS.values():
            yaml_forbidden.update(contract["forbidden_fields"])
        self.assertIn("runtime_state", yaml_forbidden)
        self.assertIn("implementation_authorized", yaml_forbidden)
        self.assertIn("readiness_claimed", yaml_forbidden)

    def test_validator_alignment_covers_all_planned_error_code_families(self):
        self.assertEqual(
            set(VALIDATOR_ALIGNMENT),
            set(validator_planning.PLANNED_ERROR_CODE_FAMILIES),
        )
        self.assertIn("additionalProperties false", VALIDATOR_ALIGNMENT["unknown_top_level_section"])
        self.assertIn("forbidden field families", VALIDATOR_ALIGNMENT["prototype_runtime_renderer_formula_authorized"])

    def test_missing_targets_remain_missing_and_planned_only(self):
        self.assertEqual(MISSING_TARGET_BEHAVIOR["status"], "not_applicable_candidate_missing")
        self.assertFalse(Path(FUTURE_YAML_TARGET).exists())
        self.assertEqual(Path(FUTURE_SCHEMA_TARGET).as_posix(), FUTURE_SCHEMA_TARGET)
        self.assertEqual(Path(FUTURE_VALIDATOR_TARGET).as_posix(), FUTURE_VALIDATOR_TARGET)
        self.assertFalse(Path(FUTURE_DICTIONARY_CONTRACT_TEST).exists())
        self.assertFalse(MISSING_TARGET_BEHAVIOR["schema_file_created"])
        self.assertFalse(MISSING_TARGET_BEHAVIOR["yaml_dictionary_created"])
        self.assertFalse(MISSING_TARGET_BEHAVIOR["validator_script_created"])

    def test_decision_output_blocks_creation_runtime_claims_and_replacement(self):
        self.assertTrue(DECISION_OUTPUT["schema_json_contract_planning_gate_passed"])
        blocked_flags = [
            "schema_file_creation_authorized",
            "yaml_dictionary_creation_authorized",
            "validator_script_creation_authorized",
            "future_dictionary_contract_test_creation_authorized",
            "prototype_authorized",
            "runtime_execution_authorized",
            "renderer_behavior_authorized",
            "formula_movement_authorized",
            "c4_implementation_change_authorized",
            "readiness_claimed",
            "correctness_claimed",
            "visual_parity_claimed",
            "leak_fix_claimed",
            "runtime_replacement_authorized",
        ]
        for flag in blocked_flags:
            self.assertFalse(DECISION_OUTPUT[flag], flag)

    def test_boundary_statement_is_docs_only_planning(self):
        self.assertIn("Docs/test-only", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary files", BOUNDARY_STATEMENT)
        self.assertIn("does not create", BOUNDARY_STATEMENT)
        self.assertIn("runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
