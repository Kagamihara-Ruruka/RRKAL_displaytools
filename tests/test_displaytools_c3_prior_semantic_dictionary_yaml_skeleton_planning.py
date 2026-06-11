"""Docs/test-only YAML skeleton planning for the future c_3 prior dictionary.

This gate plans future topology, sections, entry shape, prior term families,
stop-lines, and validator expectations. It intentionally creates no YAML,
schema, validator, contract test, prototype, runtime, renderer, or formula code.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_law_material_settlement as settlement
from tests import test_displaytools_c3_prior_dictionary_international_law_registry as international_law


FUTURE_FILE_TOPOLOGY = [
    "docs/c3_prior_dictionary/README.zh-TW.md",
    "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml",
    "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
    "scripts/validate_displaytools_c3_prior_semantic_dictionary.py",
    "tests/test_displaytools_c3_prior_semantic_dictionary_contract.py",
]

YAML_TOP_LEVEL_SECTIONS = [
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

REQUIRED_PRIOR_TERM_FAMILIES = [
    "composition_stack_prior",
    "host_shell_docking_layout_prior",
    "rendered_viewport_ui_prior",
    "viewport_camera_transformation_prior",
    "interaction_state_dispatcher_prior",
    "temporal_playback_controller_prior",
    "tabular_data_inspector_prior",
    "plugin_extension_registry_prior",
    "globe_view",
    "map_projection_view",
    "time_series_view",
    "table_view",
    "multi_view_layout",
    "layered_occluding_body_visibility_contract",
    "recipe_owns_truth_prior",
    "c4_mediates_both_ingress_and_egress",
    "multispatial_coordinate_transform_prior",
    "declarative_alpha_compositing_policy",
    "multiresolution_data_lod_prior",
]

MINIMUM_ENTRY_SHAPE = [
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
]

PRESERVED_STOP_LINES = [
    "legacy_mask_direct_adoption_stop_line",
    "projection_formula_stop_line",
    "frame_buffer_truth_stop_line",
    "transparent_globe_leak_unresolved_stop_line",
    "render_if_needed_runtime_stop_line",
    "renderer_controller_runtime_stop_line",
    "prototype_authorization_stop_line",
    "runtime_replacement_stop_line",
    "host_shell_rendered_viewport_relation_stop_line",
]

YAML_GOVERNANCE_DECISION = {
    "yaml_is_human_agent_maintained_semantic_source": True,
    "runtime_json_may_be_compiled_later_not_now": True,
    "schema_validator_planned_not_created": True,
    "yaml_file_created_in_this_gate": False,
    "schema_file_created_in_this_gate": False,
    "validator_script_created_in_this_gate": False,
    "dictionary_contract_test_created_in_this_gate": False,
    "term_planning_is_implementation_authorization": False,
    "readiness_claimed": False,
    "correctness_claimed": False,
    "leak_fix_claimed": False,
    "runtime_replacement_authorized": False,
    "prototype_authorized": False,
}

PLANNING_DECISION = {
    "yaml_skeleton_planning_gate_passed": True,
    "allowed_only_after_prior_law_settlement": True,
    "settlement_passed": settlement.DECISION_OUTPUT["settlement_passed"],
    "graphics_geospatial_materials_incorporated": settlement.DECISION_OUTPUT["graphics_geospatial_materials_incorporated"],
    "yaml_dictionary_creation_authorized": False,
    "schema_creation_authorized": False,
    "prior_card_schema_creation_authorized": False,
    "prototype_authorized": False,
    "runtime_execution_authorized": False,
    "product_source_change_authorized": False,
    "formula_movement_authorized": False,
    "c4_implementation_change_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_yaml_contract_gate"

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 prior semantic dictionary YAML skeleton planning gate. "
    "This gate plans future dictionary topology, sections, entry shape, prior term families, stop-lines, and validator expectations. "
    "It does not create YAML dictionary, schema files, validator scripts, contract tests, prototype code, runtime behavior, "
    "renderer behavior, formula movement, repo topology change, readiness claim, correctness claim, leak-fix claim, "
    "or runtime replacement authorization."
)


class C3PriorSemanticDictionaryYamlSkeletonPlanningTest(unittest.TestCase):
    def test_settlement_gate_exists_and_passes_before_yaml_planning(self) -> None:
        self.assertTrue(settlement.DECISION_OUTPUT["settlement_passed"])
        self.assertTrue(settlement.DECISION_OUTPUT["graphics_geospatial_materials_incorporated"])
        self.assertFalse(settlement.DECISION_OUTPUT["yaml_skeleton_planning_active_before_settlement"])
        self.assertTrue(PLANNING_DECISION["allowed_only_after_prior_law_settlement"])
        self.assertFalse(international_law.DECISION_OUTPUT["yaml_dictionary_authorized"])

    def test_future_file_topology_is_recorded_but_not_created(self) -> None:
        self.assertEqual(
            FUTURE_FILE_TOPOLOGY,
            [
                "docs/c3_prior_dictionary/README.zh-TW.md",
                "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml",
                "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json",
                "scripts/validate_displaytools_c3_prior_semantic_dictionary.py",
                "tests/test_displaytools_c3_prior_semantic_dictionary_contract.py",
            ],
        )
        for future_path in FUTURE_FILE_TOPOLOGY:
            self.assertFalse(Path(future_path).exists(), future_path)

    def test_top_level_sections_are_complete(self) -> None:
        self.assertEqual(
            set(YAML_TOP_LEVEL_SECTIONS),
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

    def test_required_prior_term_families_are_included(self) -> None:
        expected = {
            "composition_stack_prior",
            "host_shell_docking_layout_prior",
            "rendered_viewport_ui_prior",
            "viewport_camera_transformation_prior",
            "interaction_state_dispatcher_prior",
            "temporal_playback_controller_prior",
            "tabular_data_inspector_prior",
            "plugin_extension_registry_prior",
            "globe_view",
            "map_projection_view",
            "time_series_view",
            "table_view",
            "multi_view_layout",
            "layered_occluding_body_visibility_contract",
            "recipe_owns_truth_prior",
            "c4_mediates_both_ingress_and_egress",
            "multispatial_coordinate_transform_prior",
            "declarative_alpha_compositing_policy",
            "multiresolution_data_lod_prior",
        }
        self.assertEqual(set(REQUIRED_PRIOR_TERM_FAMILIES), expected)

    def test_minimum_entry_shape_is_complete(self) -> None:
        self.assertEqual(
            set(MINIMUM_ENTRY_SHAPE),
            {
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
            },
        )

    def test_stop_lines_are_preserved(self) -> None:
        for stop_line in [
            "legacy_mask_direct_adoption_stop_line",
            "projection_formula_stop_line",
            "frame_buffer_truth_stop_line",
            "transparent_globe_leak_unresolved_stop_line",
            "render_if_needed_runtime_stop_line",
            "renderer_controller_runtime_stop_line",
            "prototype_authorization_stop_line",
            "runtime_replacement_stop_line",
            "host_shell_rendered_viewport_relation_stop_line",
        ]:
            self.assertIn(stop_line, PRESERVED_STOP_LINES)

    def test_no_yaml_schema_validator_or_contract_test_is_created(self) -> None:
        forbidden_suffixes = [".yaml", ".yml"]
        for future_path in FUTURE_FILE_TOPOLOGY:
            path = Path(future_path)
            if path.suffix in forbidden_suffixes or path.name.endswith(".schema.v0.json"):
                self.assertFalse(path.exists(), future_path)
        self.assertFalse(Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py").exists())
        self.assertFalse(Path("tests/test_displaytools_c3_prior_semantic_dictionary_contract.py").exists())

    def test_yaml_governance_decision_blocks_implementation_overread(self) -> None:
        self.assertTrue(YAML_GOVERNANCE_DECISION["yaml_is_human_agent_maintained_semantic_source"])
        self.assertTrue(YAML_GOVERNANCE_DECISION["runtime_json_may_be_compiled_later_not_now"])
        self.assertTrue(YAML_GOVERNANCE_DECISION["schema_validator_planned_not_created"])
        for key in [
            "yaml_file_created_in_this_gate",
            "schema_file_created_in_this_gate",
            "validator_script_created_in_this_gate",
            "dictionary_contract_test_created_in_this_gate",
            "term_planning_is_implementation_authorization",
            "readiness_claimed",
            "correctness_claimed",
            "leak_fix_claimed",
            "runtime_replacement_authorized",
            "prototype_authorized",
        ]:
            self.assertFalse(YAML_GOVERNANCE_DECISION[key], key)

    def test_planning_decision_forbids_runtime_source_formula_and_c4_changes(self) -> None:
        self.assertTrue(PLANNING_DECISION["yaml_skeleton_planning_gate_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_creation_authorized",
            "prior_card_schema_creation_authorized",
            "prototype_authorized",
            "runtime_execution_authorized",
            "product_source_change_authorized",
            "formula_movement_authorized",
            "c4_implementation_change_authorized",
        ]:
            self.assertFalse(PLANNING_DECISION[key], key)
        self.assertEqual(RECOMMENDED_NEXT_GATE, "c3_prior_semantic_dictionary_yaml_contract_gate")

    def test_boundary_statement_is_planning_only(self) -> None:
        self.assertIn("Docs/test-only c_3 prior semantic dictionary YAML skeleton planning gate", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary", BOUNDARY_STATEMENT)
        self.assertIn("does not create", BOUNDARY_STATEMENT)
        self.assertIn("runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()