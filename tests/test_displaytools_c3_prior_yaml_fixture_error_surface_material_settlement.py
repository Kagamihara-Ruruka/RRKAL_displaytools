"""Docs/test-only settlement for c_3 YAML fixture error-surface materials.

This gate classifies lab-only error-surface materials as future fixture,
validator, diagnostic, and card-edge planning evidence. It creates no YAML
fixtures and does not modify schema JSON or validator behavior.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture as fixture_gate
from tests import test_displaytools_c3_prior_yaml_fixture_expectation_material_settlement as expectation_settlement


FORMAL_DICTIONARY = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml")
SCHEMA_JSON = Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json")
VALIDATOR_SCRIPT = Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py")

SETTLEMENT_CATEGORIES = {
    "error_message_style_candidate",
    "validator_error_code_candidate",
    "diagnostic_phrase_candidate",
    "fixture_error_surface_candidate",
    "card_edge_error_surface_candidate",
    "reference_only_guard",
    "planning_only_guard",
    "future_validator_rule_candidate",
    "not_yet_allowed",
    "stop_line",
}

MATERIAL_SETTLEMENT = {
    "a1_c3_yaml_fixture_error_message_readability_scout": {
        "categories": {
            "error_message_style_candidate",
            "validator_error_code_candidate",
            "diagnostic_phrase_candidate",
            "planning_only_guard",
            "stop_line",
        },
        "settled_surfaces": {
            "parse_error",
            "schema_error",
            "business_rule_error",
            "missing_fixture_not_applicable",
            "valid_fixture_pass",
        },
        "guard": "readability guidance only; no product integration boundary",
        "future_use": "future_diagnostic_candidate",
    },
    "c1_c3_reference_envelope_fixture_error_surface_scout": {
        "categories": {
            "fixture_error_surface_candidate",
            "validator_error_code_candidate",
            "diagnostic_phrase_candidate",
            "reference_only_guard",
            "future_validator_rule_candidate",
        },
        "settled_surfaces": {
            "path_like_asset_id",
            "geometry_bearing_subject_ref",
            "fetchable_source_ref",
            "private_schema_ref",
            "callable_sample_query_ref",
            "raw_spatial_extent",
            "row_level_temporal_extent",
            "fake_or_free_text_evidence_refs",
            "ambiguous_redaction",
            "approval_like_review",
        },
        "guard": "c_1 reference-only boundary",
        "future_use": "future_fixture_candidate",
    },
    "c2_c3_display_hint_fixture_error_surface_scout": {
        "categories": {
            "fixture_error_surface_candidate",
            "validator_error_code_candidate",
            "diagnostic_phrase_candidate",
            "planning_only_guard",
            "future_validator_rule_candidate",
        },
        "settled_surfaces": {
            "unknown_lod_hint",
            "invalid_bbox",
            "missing_or_unknown_coord_ref",
            "invalid_time_window",
            "credential_bearing_tile_ref",
            "unitless_density_hint",
            "unitless_sample_budget",
            "planning_only_false",
        },
        "guard": "c_2 planning-only and no runtime SLA boundary",
        "future_use": "future_error_code_candidate",
    },
    "c4_c3_yaml_fixture_error_card_surface_scout": {
        "categories": {
            "card_edge_error_surface_candidate",
            "validator_error_code_candidate",
            "diagnostic_phrase_candidate",
            "reference_only_guard",
            "stop_line",
        },
        "settled_surfaces": {
            "parse_error",
            "schema_error",
            "business_rule_error",
            "missing_fixture_not_applicable",
            "valid_fixture_pass",
        },
        "guard": "c_4 card-edge only and no parser-validator-renderer boundary",
        "future_use": "future_card_edge_expectation",
    },
    "current_product_fixture_and_validator_evidence": {
        "categories": {
            "fixture_error_surface_candidate",
            "planning_only_guard",
            "stop_line",
        },
        "settled_surfaces": set(fixture_gate.INVALID_FIXTURES.values()) | {"valid_fixture_pass"},
        "guard": "not_current_validator_change",
        "future_use": "not_current_validator_change",
    },
}

REQUIRED_ERROR_SURFACES = {
    "parse_error",
    "schema_error",
    "business_rule_error",
    "missing_fixture_not_applicable",
    "valid_fixture_pass",
    "path_like_asset_id",
    "geometry_bearing_subject_ref",
    "fetchable_source_ref",
    "private_schema_ref",
    "callable_sample_query_ref",
    "raw_spatial_extent",
    "row_level_temporal_extent",
    "fake_or_free_text_evidence_refs",
    "ambiguous_redaction",
    "approval_like_review",
    "unknown_lod_hint",
    "invalid_bbox",
    "missing_or_unknown_coord_ref",
    "invalid_time_window",
    "credential_bearing_tile_ref",
    "unitless_density_hint",
    "unitless_sample_budget",
    "planning_only_false",
}

CONSERVATIVE_FUTURE_USES = {
    "future_fixture_candidate",
    "future_error_code_candidate",
    "future_diagnostic_candidate",
    "future_card_edge_expectation",
    "not_current_validator_change",
}

GUARDS_PRESERVED = {
    "c_1 reference-only boundary",
    "c_2 planning-only and no runtime SLA boundary",
    "c_4 card-edge only and no parser-validator-renderer boundary",
    "readability guidance only; no product integration boundary",
}

DECISION_OUTPUT = {
    "yaml_fixture_error_surface_material_settlement_passed": True,
    "minimal_fixture_gate_available": True,
    "expectation_material_settlement_available": True,
    "formal_dictionary_creation_authorized": False,
    "yaml_fixture_creation_authorized": False,
    "schema_json_modification_authorized": False,
    "validator_script_modification_authorized": False,
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

RECOMMENDED_NEXT_GATE = "c3_prior_yaml_fixture_error_message_planning_gate"


class C3PriorYamlFixtureErrorSurfaceMaterialSettlementTest(unittest.TestCase):
    def test_material_inventory_is_complete(self) -> None:
        self.assertEqual(
            set(MATERIAL_SETTLEMENT),
            {
                "a1_c3_yaml_fixture_error_message_readability_scout",
                "c1_c3_reference_envelope_fixture_error_surface_scout",
                "c2_c3_display_hint_fixture_error_surface_scout",
                "c4_c3_yaml_fixture_error_card_surface_scout",
                "current_product_fixture_and_validator_evidence",
            },
        )

    def test_all_categories_are_known(self) -> None:
        for material in MATERIAL_SETTLEMENT.values():
            self.assertTrue(material["categories"])
            self.assertTrue(material["categories"].issubset(SETTLEMENT_CATEGORIES))

    def test_required_error_surface_coverage_is_complete(self) -> None:
        covered = set()
        for material in MATERIAL_SETTLEMENT.values():
            covered.update(material["settled_surfaces"])
        self.assertTrue(REQUIRED_ERROR_SURFACES.issubset(covered))

    def test_future_uses_are_conservative(self) -> None:
        for material in MATERIAL_SETTLEMENT.values():
            self.assertIn(material["future_use"], CONSERVATIVE_FUTURE_USES)

    def test_required_guards_are_preserved(self) -> None:
        guards = {material["guard"] for material in MATERIAL_SETTLEMENT.values()}
        self.assertTrue(GUARDS_PRESERVED.issubset(guards))

    def test_a1_error_message_style_material_is_readability_only(self) -> None:
        material = MATERIAL_SETTLEMENT["a1_c3_yaml_fixture_error_message_readability_scout"]
        self.assertIn("error_message_style_candidate", material["categories"])
        self.assertIn("parse_error", material["settled_surfaces"])
        self.assertIn("valid_fixture_pass", material["settled_surfaces"])
        self.assertEqual(material["future_use"], "future_diagnostic_candidate")

    def test_c1_reference_error_surfaces_are_reference_only(self) -> None:
        material = MATERIAL_SETTLEMENT["c1_c3_reference_envelope_fixture_error_surface_scout"]
        for surface in [
            "path_like_asset_id",
            "geometry_bearing_subject_ref",
            "fetchable_source_ref",
            "callable_sample_query_ref",
            "approval_like_review",
        ]:
            self.assertIn(surface, material["settled_surfaces"])
        self.assertEqual(material["guard"], "c_1 reference-only boundary")

    def test_c2_display_hint_surfaces_remain_planning_only(self) -> None:
        material = MATERIAL_SETTLEMENT["c2_c3_display_hint_fixture_error_surface_scout"]
        for surface in [
            "unknown_lod_hint",
            "invalid_bbox",
            "missing_or_unknown_coord_ref",
            "credential_bearing_tile_ref",
            "planning_only_false",
        ]:
            self.assertIn(surface, material["settled_surfaces"])
        self.assertEqual(material["guard"], "c_2 planning-only and no runtime SLA boundary")

    def test_c4_card_edge_surfaces_do_not_authorize_parser_validator_renderer(self) -> None:
        material = MATERIAL_SETTLEMENT["c4_c3_yaml_fixture_error_card_surface_scout"]
        self.assertIn("card_edge_error_surface_candidate", material["categories"])
        self.assertIn("business_rule_error", material["settled_surfaces"])
        self.assertEqual(material["guard"], "c_4 card-edge only and no parser-validator-renderer boundary")

    def test_product_fixture_and_expectation_evidence_remain_available(self) -> None:
        self.assertTrue(fixture_gate.VALID_FIXTURE.exists())
        self.assertFalse(fixture_gate.FORMAL_DICTIONARY.exists())
        self.assertTrue(expectation_settlement.DECISION_OUTPUT["yaml_fixture_expectation_material_settlement_passed"])

    def test_decision_output_blocks_implementation_and_claims(self) -> None:
        self.assertTrue(DECISION_OUTPUT["yaml_fixture_error_surface_material_settlement_passed"])
        self.assertTrue(SCHEMA_JSON.exists())
        self.assertTrue(VALIDATOR_SCRIPT.exists())
        self.assertFalse(FORMAL_DICTIONARY.exists())
        for key in [
            "formal_dictionary_creation_authorized",
            "yaml_fixture_creation_authorized",
            "schema_json_modification_authorized",
            "validator_script_modification_authorized",
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

    def test_recommended_next_gate_is_planning_not_validator_or_fixture_change(self) -> None:
        self.assertEqual(RECOMMENDED_NEXT_GATE, "c3_prior_yaml_fixture_error_message_planning_gate")


if __name__ == "__main__":
    unittest.main()
