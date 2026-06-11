"""Docs/test-only planning for the future c_3 prior YAML validator.

This gate plans validator phases, error-code families, missing-target behavior,
and future CLI expectations. It creates no YAML dictionary, schema JSON,
validator script, contract test, prototype, runtime, renderer, or formula code.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_law_material_settlement as settlement
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_contract as contract
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_skeleton_planning as skeleton


FUTURE_VALIDATOR_TARGET = "scripts/validate_displaytools_c3_prior_semantic_dictionary.py"
FUTURE_VALIDATED_TARGETS = [
    "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml",
    "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
]

PLANNED_VALIDATOR_PHASES = [
    "file_presence_mode",
    "yaml_parse_mode",
    "top_level_section_contract",
    "term_entry_shape_contract",
    "authority_source_ref_contract",
    "bare_term_rejection_contract",
    "legacy_fossil_translation_contract",
    "stop_line_preservation_contract",
    "recipe_truth_contract",
    "c4_mediation_contract",
    "runtime_authorization_rejection_contract",
]

PLANNED_ERROR_CODE_FAMILIES = [
    "missing_required_section",
    "unknown_top_level_section",
    "missing_required_entry_field",
    "bare_high_risk_term_id",
    "unresolved_authority_ref",
    "legacy_fossil_direct_adoption",
    "stop_line_authorizes_implementation",
    "unknown_stop_line_without_resolution_gate",
    "recipe_truth_owned_by_ui",
    "c4_mediation_bypassed",
    "runtime_json_compilation_authorized",
    "prototype_runtime_renderer_formula_authorized",
]

MISSING_TARGET_BEHAVIOR = {
    "actual_yaml_created": False,
    "actual_schema_created": False,
    "actual_validator_created": False,
    "missing_future_target_status": "not_applicable_candidate_missing",
    "planning_gate_must_not_fail_on_missing_future_targets": True,
    "future_targets_planned_only": True,
}

FUTURE_CLI_EXPECTATION = {
    "command": (
        "py -3 -B scripts\\validate_displaytools_c3_prior_semantic_dictionary.py "
        "docs\\c3_prior_dictionary\\c3_prior_semantic_dictionary.v0.yaml"
    ),
    "created_in_this_gate": False,
    "executed_in_this_gate": False,
}

VALIDATOR_PLANNING_MATRIX = [
    {
        "phase": "file_presence_mode",
        "checks": ["dictionary_file_exists", "schema_file_exists", "missing_target_can_be_not_applicable"],
        "error_codes": ["missing_required_section"],
        "stop_line": "missing future target remains planned-only in this gate",
    },
    {
        "phase": "yaml_parse_mode",
        "checks": ["yaml_can_parse_when_future_file_exists", "mapping_root_expected"],
        "error_codes": ["unknown_top_level_section"],
        "stop_line": "no YAML file is parsed or created in this gate",
    },
    {
        "phase": "top_level_section_contract",
        "checks": list(skeleton.YAML_TOP_LEVEL_SECTIONS),
        "error_codes": ["missing_required_section", "unknown_top_level_section"],
        "stop_line": "section planning does not create schema JSON",
    },
    {
        "phase": "term_entry_shape_contract",
        "checks": list(skeleton.MINIMUM_ENTRY_SHAPE),
        "error_codes": ["missing_required_entry_field"],
        "stop_line": "entry shape planning is not implementation authorization",
    },
    {
        "phase": "authority_source_ref_contract",
        "checks": ["known_external_source", "known_local_ref", "candidate_pending_review_allowed_only_with_status"],
        "error_codes": ["unresolved_authority_ref"],
        "stop_line": "authority reference is not source adoption",
    },
    {
        "phase": "bare_term_rejection_contract",
        "checks": list(settlement.HIGH_RISK_BARE_TERMS),
        "error_codes": ["bare_high_risk_term_id"],
        "stop_line": "bare term cannot be prior id",
    },
    {
        "phase": "legacy_fossil_translation_contract",
        "checks": ["legacy_mask_requires_translation", "legacy_21k_not_final_api"],
        "error_codes": ["legacy_fossil_direct_adoption"],
        "stop_line": "legacy fossil is not implementation interface",
    },
    {
        "phase": "stop_line_preservation_contract",
        "checks": list(contract.STOP_LINE_CONTRACTS),
        "error_codes": ["stop_line_authorizes_implementation", "unknown_stop_line_without_resolution_gate"],
        "stop_line": "stop-line cannot authorize implementation",
    },
    {
        "phase": "recipe_truth_contract",
        "checks": ["recipe_owns_truth", "ui_does_not_own_truth"],
        "error_codes": ["recipe_truth_owned_by_ui"],
        "stop_line": "recipe planning is not prototype authorization",
    },
    {
        "phase": "c4_mediation_contract",
        "checks": ["ingress_mediated_by_c4", "egress_mediated_by_c4", "direct_c3_to_c1_forbidden"],
        "error_codes": ["c4_mediation_bypassed"],
        "stop_line": "no c4 implementation change",
    },
    {
        "phase": "runtime_authorization_rejection_contract",
        "checks": ["runtime_json_not_compiled", "prototype_not_authorized", "renderer_not_authorized", "formula_not_moved"],
        "error_codes": ["runtime_json_compilation_authorized", "prototype_runtime_renderer_formula_authorized"],
        "stop_line": "no runtime, renderer, prototype, or formula behavior",
    },
]

DECISION_OUTPUT = {
    "schema_validator_planning_gate_passed": True,
    "contract_gate_passed": contract.DECISION_OUTPUT["yaml_contract_gate_passed"],
    "skeleton_planning_gate_passed": skeleton.PLANNING_DECISION["yaml_skeleton_planning_gate_passed"],
    "settlement_gate_passed": settlement.DECISION_OUTPUT["settlement_passed"],
    "yaml_dictionary_creation_authorized": False,
    "schema_json_creation_authorized": False,
    "validator_script_creation_authorized": False,
    "future_contract_test_creation_authorized": False,
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
    "Docs/test-only c_3 prior semantic dictionary YAML schema validator planning gate. "
    "This gate plans validator phases, error-code families, missing-target behavior, future CLI expectations, "
    "and stop-line checks for a future YAML dictionary validator. It does not create YAML dictionary files, "
    "schema files, validator scripts, future dictionary contract tests, prototype code, runtime behavior, renderer behavior, "
    "formula movement, c_4 implementation changes, readiness claims, correctness claims, leak-fix claims, "
    "or runtime replacement authorization."
)


class C3PriorSemanticDictionaryYamlSchemaValidatorPlanningTest(unittest.TestCase):
    def test_contract_skeleton_and_settlement_gates_are_source_evidence(self) -> None:
        self.assertTrue(DECISION_OUTPUT["contract_gate_passed"])
        self.assertTrue(DECISION_OUTPUT["skeleton_planning_gate_passed"])
        self.assertTrue(DECISION_OUTPUT["settlement_gate_passed"])
        self.assertEqual(contract.RECOMMENDED_NEXT_GATE, "c3_prior_semantic_dictionary_yaml_schema_validator_planning_gate")

    def test_future_validator_and_validated_targets_are_planned_only(self) -> None:
        self.assertEqual(FUTURE_VALIDATOR_TARGET, "scripts/validate_displaytools_c3_prior_semantic_dictionary.py")
        self.assertEqual(
            FUTURE_VALIDATED_TARGETS,
            [
                "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml",
                "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
            ],
        )
        self.assertFalse(Path(FUTURE_VALIDATOR_TARGET).exists())
        self.assertFalse(Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml").exists())
        self.assertEqual(
            Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json").as_posix(),
            "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
        )

    def test_validator_phases_are_complete(self) -> None:
        self.assertEqual(
            set(PLANNED_VALIDATOR_PHASES),
            {
                "file_presence_mode",
                "yaml_parse_mode",
                "top_level_section_contract",
                "term_entry_shape_contract",
                "authority_source_ref_contract",
                "bare_term_rejection_contract",
                "legacy_fossil_translation_contract",
                "stop_line_preservation_contract",
                "recipe_truth_contract",
                "c4_mediation_contract",
                "runtime_authorization_rejection_contract",
            },
        )
        self.assertEqual({row["phase"] for row in VALIDATOR_PLANNING_MATRIX}, set(PLANNED_VALIDATOR_PHASES))

    def test_error_code_families_are_complete(self) -> None:
        self.assertEqual(
            set(PLANNED_ERROR_CODE_FAMILIES),
            {
                "missing_required_section",
                "unknown_top_level_section",
                "missing_required_entry_field",
                "bare_high_risk_term_id",
                "unresolved_authority_ref",
                "legacy_fossil_direct_adoption",
                "stop_line_authorizes_implementation",
                "unknown_stop_line_without_resolution_gate",
                "recipe_truth_owned_by_ui",
                "c4_mediation_bypassed",
                "runtime_json_compilation_authorized",
                "prototype_runtime_renderer_formula_authorized",
            },
        )

    def test_matrix_uses_known_sections_entry_shape_stop_lines_and_bare_terms(self) -> None:
        top_level = next(row for row in VALIDATOR_PLANNING_MATRIX if row["phase"] == "top_level_section_contract")
        entry_shape = next(row for row in VALIDATOR_PLANNING_MATRIX if row["phase"] == "term_entry_shape_contract")
        bare_terms = next(row for row in VALIDATOR_PLANNING_MATRIX if row["phase"] == "bare_term_rejection_contract")
        stop_lines = next(row for row in VALIDATOR_PLANNING_MATRIX if row["phase"] == "stop_line_preservation_contract")
        self.assertEqual(set(top_level["checks"]), set(skeleton.YAML_TOP_LEVEL_SECTIONS))
        self.assertEqual(set(entry_shape["checks"]), set(skeleton.MINIMUM_ENTRY_SHAPE))
        self.assertEqual(set(bare_terms["checks"]), set(settlement.HIGH_RISK_BARE_TERMS))
        self.assertTrue(set(skeleton.PRESERVED_STOP_LINES).issubset(set(stop_lines["checks"])))

    def test_missing_target_behavior_is_not_applicable_candidate_missing(self) -> None:
        self.assertFalse(MISSING_TARGET_BEHAVIOR["actual_yaml_created"])
        self.assertFalse(MISSING_TARGET_BEHAVIOR["actual_schema_created"])
        self.assertFalse(MISSING_TARGET_BEHAVIOR["actual_validator_created"])
        self.assertEqual(MISSING_TARGET_BEHAVIOR["missing_future_target_status"], "not_applicable_candidate_missing")
        self.assertTrue(MISSING_TARGET_BEHAVIOR["planning_gate_must_not_fail_on_missing_future_targets"])
        self.assertTrue(MISSING_TARGET_BEHAVIOR["future_targets_planned_only"])

    def test_future_cli_expectation_is_not_created_or_executed(self) -> None:
        self.assertEqual(
            FUTURE_CLI_EXPECTATION["command"],
            "py -3 -B scripts\\validate_displaytools_c3_prior_semantic_dictionary.py docs\\c3_prior_dictionary\\c3_prior_semantic_dictionary.v0.yaml",
        )
        self.assertFalse(FUTURE_CLI_EXPECTATION["created_in_this_gate"])
        self.assertFalse(FUTURE_CLI_EXPECTATION["executed_in_this_gate"])

    def test_forbidden_creation_targets_are_absent_or_preexisting_evidence_only(self) -> None:
        self.assertFalse(Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml").exists())
        self.assertEqual(
            Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json").as_posix(),
            "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
        )
        self.assertFalse(Path(FUTURE_VALIDATOR_TARGET).exists())
        self.assertTrue(Path("tests/test_displaytools_c3_prior_semantic_dictionary_yaml_contract.py").exists())
        self.assertFalse(DECISION_OUTPUT["future_contract_test_creation_authorized"])

    def test_decision_output_blocks_runtime_prototype_renderer_formula_and_claims(self) -> None:
        self.assertTrue(DECISION_OUTPUT["schema_validator_planning_gate_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_json_creation_authorized",
            "validator_script_creation_authorized",
            "future_contract_test_creation_authorized",
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
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_boundary_statement_is_planning_only(self) -> None:
        self.assertIn("Docs/test-only c_3 prior semantic dictionary YAML schema validator planning gate", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary files", BOUNDARY_STATEMENT)
        self.assertIn("validator scripts", BOUNDARY_STATEMENT)
        self.assertIn("runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
