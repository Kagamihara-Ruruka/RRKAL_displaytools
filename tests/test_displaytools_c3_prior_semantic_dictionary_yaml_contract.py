"""Docs/test-only contract gate for the future c_3 prior YAML dictionary.

This gate fixes dictionary invariants before any YAML, schema JSON, validator,
contract test, prototype, runtime, renderer, or formula work is created.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_dictionary_international_law_registry as international_law
from tests import test_displaytools_c3_prior_law_material_settlement as settlement
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_skeleton_planning as skeleton


CONTRACT_LEVEL = "semantic_dictionary_contract_only"

FUTURE_ACTUAL_FILES = skeleton.FUTURE_FILE_TOPOLOGY

SECTION_CONTRACTS = {
    "dictionary_metadata": {
        "entry_kind": "mapping",
        "required_fields": ["dictionary_id", "version", "owner", "lifecycle_status", "source_commit"],
        "forbidden_fields": ["runtime_state", "renderer_state", "frame_buffer"],
    },
    "authority_sources": {
        "entry_kind": "list",
        "required_fields": ["source_id", "authority_family", "source_ref", "adoption_status", "forbidden_overread"],
        "forbidden_fields": ["import_module", "runtime_loader", "network_fetch"],
    },
    "phenomenon_translation_map": {
        "entry_kind": "list",
        "required_fields": ["naive_observed_phrase", "formal_engineering_term", "rrkal_prior_candidate", "stop_line"],
        "forbidden_fields": ["ui_widget_class", "renderer_object", "implementation_snippet"],
    },
    "prior_terms": {
        "entry_kind": "list",
        "required_fields": skeleton.MINIMUM_ENTRY_SHAPE,
        "forbidden_fields": ["callable", "runtime_object", "dataframe", "framebuffer"],
    },
    "view_families": {
        "entry_kind": "list",
        "required_fields": ["view_family_id", "view_kind", "input_contract", "output_contract", "non_goals"],
        "forbidden_fields": ["earth_only_assumption", "qt_widget_binding", "renderer_host"],
    },
    "layer_taxonomy": {
        "entry_kind": "list",
        "required_fields": ["layer_kind", "owns_truth", "consumer", "forbidden_confusion"],
        "forbidden_fields": ["bare_layer", "implicit_stack_order", "legacy_mask_direct_use"],
    },
    "recipe_authoring": {
        "entry_kind": "mapping",
        "required_fields": ["recipe_owns_truth", "preview_consumes_recipe", "export_consumes_recipe", "ui_does_not_own_truth"],
        "forbidden_fields": ["ui_state_as_truth", "viewport_state_as_export_contract"],
    },
    "c4_mediation": {
        "entry_kind": "mapping",
        "required_fields": ["ingress_mediated_by_c4", "egress_mediated_by_c4", "direct_c3_to_c1_forbidden"],
        "forbidden_fields": ["c1_direct_dependency", "odoriba_bypass", "raw_payload_contract"],
    },
    "legacy_fossil_translation": {
        "entry_kind": "list",
        "required_fields": ["legacy_term", "observed_need", "translated_ideal_candidate", "direct_adoption_forbidden"],
        "forbidden_fields": ["legacy_term_as_final_api", "legacy_runtime_patch_as_ideal_form"],
    },
    "stop_lines": {
        "entry_kind": "list",
        "required_fields": ["stop_line_id", "reason", "blocked_claims", "reopen_condition"],
        "forbidden_fields": ["implementation_authorized", "readiness_claimed"],
    },
    "unknown_stop_lines": {
        "entry_kind": "list",
        "required_fields": ["unknown_id", "why_unknown", "allowed_reference_use", "resolution_gate"],
        "forbidden_fields": ["silent_default", "implicit_prior_term"],
    },
    "validator_expectations": {
        "entry_kind": "list",
        "required_fields": ["rule_id", "checked_surface", "fail_condition", "error_code"],
        "forbidden_fields": ["runtime_execution", "monolith_import", "renderer_call"],
    },
}

TERM_ENTRY_CONTRACT = {
    "required_fields": skeleton.MINIMUM_ENTRY_SHAPE,
    "confidence_values": ["low", "medium", "high", "evidence_gap"],
    "lifecycle_status_values": [
        "planned",
        "accepted_candidate",
        "authority_reference_only",
        "legacy_fossil_evidence",
        "ideal_form_embryo",
        "stop_line",
        "unknown_stop_line",
    ],
    "authority_family_values": [
        "external_standard",
        "external_reference_implementation",
        "external_mature_tool_model",
        "rrkal_native_governance",
        "legacy_fossil_evidence",
        "local_semantic_evidence",
        "candidate_pending_review",
    ],
}

REQUIRED_INITIAL_TERM_CONTRACTS = {
    term_id: {
        "must_have_source_evidence_refs": True,
        "must_have_allowed_and_forbidden_use": True,
        "must_have_example_and_counterexample": True,
        "must_not_authorize_implementation": True,
    }
    for term_id in skeleton.REQUIRED_PRIOR_TERM_FAMILIES
}

VALIDATOR_RULE_CONTRACTS = [
    "top_level_sections_exact_match",
    "required_entry_fields_present",
    "no_unknown_top_level_sections",
    "no_bare_high_risk_term_ids",
    "authority_refs_must_be_known_or_local_ref",
    "legacy_fossils_must_require_translation",
    "stop_lines_must_not_authorize_implementation",
    "unknown_stop_lines_require_resolution_gate",
    "recipe_must_own_truth",
    "c4_mediation_required_for_ingress_and_egress",
    "runtime_json_compilation_not_authorized",
    "prototype_runtime_renderer_formula_changes_forbidden",
]

HIGH_RISK_BARE_TERM_RULE = {
    "bare_terms": settlement.HIGH_RISK_BARE_TERMS,
    "accepted_bare_term_count": settlement.HIGH_RISK_BARE_TERM_COUNT,
    "term_id_must_be_qualified": True,
}

STOP_LINE_CONTRACTS = sorted(
    set(skeleton.PRESERVED_STOP_LINES)
    | set(settlement.STOP_LINE_TERMS)
    | {
        "yaml_creation_stop_line",
        "schema_creation_stop_line",
        "validator_creation_stop_line",
        "dictionary_contract_test_creation_stop_line",
        "prior_card_schema_stop_line",
        "runtime_json_compilation_stop_line",
    }
)

DECISION_OUTPUT = {
    "yaml_contract_gate_passed": True,
    "skeleton_planning_gate_passed": skeleton.PLANNING_DECISION["yaml_skeleton_planning_gate_passed"],
    "settlement_passed": settlement.DECISION_OUTPUT["settlement_passed"],
    "international_law_registry_passed": international_law.DECISION_OUTPUT["international_law_registry_gate_passed"],
    "yaml_dictionary_creation_authorized": False,
    "schema_creation_authorized": False,
    "validator_script_creation_authorized": False,
    "future_dictionary_contract_test_creation_authorized": False,
    "prior_card_schema_creation_authorized": False,
    "prototype_authorized": False,
    "runtime_execution_authorized": False,
    "runtime_json_compilation_authorized": False,
    "renderer_behavior_change_authorized": False,
    "formula_movement_authorized": False,
    "c4_implementation_change_authorized": False,
    "repo_topology_change_authorized": False,
    "readiness_claimed": False,
    "correctness_claimed": False,
    "leak_fix_claimed": False,
    "runtime_replacement_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_yaml_schema_validator_planning_gate"

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 prior semantic dictionary YAML contract gate. "
    "This gate fixes section, entry, term, validator, stop-line, recipe, c_4 mediation, and legacy-fossil invariants "
    "for a future YAML dictionary. It does not create YAML dictionary files, schema files, validator scripts, "
    "future dictionary contract tests, prototype code, runtime behavior, renderer behavior, formula movement, "
    "repo topology change, readiness claim, correctness claim, leak-fix claim, or runtime replacement authorization."
)


class C3PriorSemanticDictionaryYamlContractTest(unittest.TestCase):
    def test_contract_depends_on_prior_law_settlement_and_skeleton_planning(self) -> None:
        self.assertTrue(DECISION_OUTPUT["settlement_passed"])
        self.assertTrue(DECISION_OUTPUT["international_law_registry_passed"])
        self.assertTrue(DECISION_OUTPUT["skeleton_planning_gate_passed"])
        self.assertEqual(CONTRACT_LEVEL, "semantic_dictionary_contract_only")

    def test_section_contracts_cover_exact_skeleton_sections(self) -> None:
        self.assertEqual(set(SECTION_CONTRACTS), set(skeleton.YAML_TOP_LEVEL_SECTIONS))
        for section, contract in SECTION_CONTRACTS.items():
            self.assertIn(contract["entry_kind"], {"mapping", "list"})
            self.assertTrue(contract["required_fields"], section)
            self.assertTrue(contract["forbidden_fields"], section)

    def test_prior_term_entry_contract_matches_planned_minimum_shape(self) -> None:
        self.assertEqual(TERM_ENTRY_CONTRACT["required_fields"], skeleton.MINIMUM_ENTRY_SHAPE)
        for required in [
            "term_id",
            "definition",
            "authority_family",
            "source_evidence_refs",
            "allowed_use",
            "forbidden_use",
            "example",
            "counterexample",
            "stop_line",
            "confidence",
            "lifecycle_status",
        ]:
            self.assertIn(required, TERM_ENTRY_CONTRACT["required_fields"])
        self.assertIn("evidence_gap", TERM_ENTRY_CONTRACT["confidence_values"])
        self.assertIn("unknown_stop_line", TERM_ENTRY_CONTRACT["lifecycle_status_values"])

    def test_initial_term_contracts_cover_every_required_family(self) -> None:
        self.assertEqual(set(REQUIRED_INITIAL_TERM_CONTRACTS), set(skeleton.REQUIRED_PRIOR_TERM_FAMILIES))
        for term_id, contract in REQUIRED_INITIAL_TERM_CONTRACTS.items():
            self.assertTrue(contract["must_have_source_evidence_refs"], term_id)
            self.assertTrue(contract["must_have_allowed_and_forbidden_use"], term_id)
            self.assertTrue(contract["must_have_example_and_counterexample"], term_id)
            self.assertTrue(contract["must_not_authorize_implementation"], term_id)

    def test_validator_rule_contracts_cover_core_invariants(self) -> None:
        for rule in [
            "top_level_sections_exact_match",
            "required_entry_fields_present",
            "no_bare_high_risk_term_ids",
            "legacy_fossils_must_require_translation",
            "recipe_must_own_truth",
            "c4_mediation_required_for_ingress_and_egress",
            "runtime_json_compilation_not_authorized",
            "prototype_runtime_renderer_formula_changes_forbidden",
        ]:
            self.assertIn(rule, VALIDATOR_RULE_CONTRACTS)

    def test_high_risk_bare_terms_remain_disallowed_as_term_ids(self) -> None:
        self.assertEqual(HIGH_RISK_BARE_TERM_RULE["accepted_bare_term_count"], 0)
        self.assertTrue(HIGH_RISK_BARE_TERM_RULE["term_id_must_be_qualified"])
        for bare_term in ["layer", "mask", "view", "projection", "frame", "render", "recipe"]:
            self.assertIn(bare_term, HIGH_RISK_BARE_TERM_RULE["bare_terms"])
            self.assertNotIn(bare_term, REQUIRED_INITIAL_TERM_CONTRACTS)

    def test_stop_line_contracts_preserve_existing_and_new_creation_stop_lines(self) -> None:
        for stop_line in [
            "legacy_mask_direct_adoption_stop_line",
            "projection_formula_stop_line",
            "frame_buffer_truth_stop_line",
            "transparent_globe_leak_unresolved_stop_line",
            "render_if_needed_runtime_stop_line",
            "renderer_controller_runtime_stop_line",
            "prototype_authorization_stop_line",
            "runtime_replacement_stop_line",
            "yaml_creation_stop_line",
            "schema_creation_stop_line",
            "validator_creation_stop_line",
            "dictionary_contract_test_creation_stop_line",
            "runtime_json_compilation_stop_line",
        ]:
            self.assertIn(stop_line, STOP_LINE_CONTRACTS)

    def test_future_actual_files_are_still_not_created(self) -> None:
        for future_path in FUTURE_ACTUAL_FILES:
            self.assertFalse(Path(future_path).exists(), future_path)
        self.assertFalse(Path("docs/c3_prior_dictionary").exists())
        self.assertFalse(Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py").exists())
        self.assertFalse(Path("tests/test_displaytools_c3_prior_semantic_dictionary_contract.py").exists())

    def test_decision_output_blocks_creation_runtime_claims_and_replacement(self) -> None:
        self.assertTrue(DECISION_OUTPUT["yaml_contract_gate_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_creation_authorized",
            "validator_script_creation_authorized",
            "future_dictionary_contract_test_creation_authorized",
            "prior_card_schema_creation_authorized",
            "prototype_authorized",
            "runtime_execution_authorized",
            "runtime_json_compilation_authorized",
            "renderer_behavior_change_authorized",
            "formula_movement_authorized",
            "c4_implementation_change_authorized",
            "repo_topology_change_authorized",
            "readiness_claimed",
            "correctness_claimed",
            "leak_fix_claimed",
            "runtime_replacement_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_next_gate_and_boundary_statement_are_contract_only(self) -> None:
        self.assertEqual(RECOMMENDED_NEXT_GATE, "c3_prior_semantic_dictionary_yaml_schema_validator_planning_gate")
        self.assertIn("Docs/test-only c_3 prior semantic dictionary YAML contract gate", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary files", BOUNDARY_STATEMENT)
        self.assertIn("does not create", BOUNDARY_STATEMENT)
        self.assertIn("runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
