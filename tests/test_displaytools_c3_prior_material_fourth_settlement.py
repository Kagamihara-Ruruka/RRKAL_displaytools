"""Docs/test-only fourth settlement for c3 prior materials."""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_material_third_settlement as third_settlement
from tests import test_displaytools_c3_prior_semantic_dictionary_schema_json_contract as schema_contract
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning as validator_planning


LAB_REPORTS = {
    "a1_seed_term_compaction": Path(
        r"L:\RRKAL_lab\external_research\analysis\a1_c3_prior_seed_term_compaction_scout.zh-TW.md"
    ),
    "c4_dictionary_card_edge": Path(
        r"L:\RRKAL_lab\external_research\analysis\c4_c3_prior_dictionary_card_edge_scout.zh-TW.md"
    ),
    "c2_lod_hint_schema_pressure": Path(
        r"L:\RRKAL_lab\external_research\analysis\c2_c3_lod_hint_schema_pressure_scout.zh-TW.md"
    ),
    "c1_reference_envelope_schema_pressure": Path(
        r"L:\RRKAL_lab\external_research\analysis\c1_c3_reference_envelope_schema_pressure_scout.zh-TW.md"
    ),
}

SETTLEMENT_CATEGORIES = [
    "prior_dictionary_candidate",
    "schema_pressure_evidence",
    "schema_field_candidate",
    "validator_rule_candidate",
    "lab_evidence_reference",
    "caveat_required",
    "stop_line",
    "not_yet_allowed",
]

FOURTH_SETTLEMENT_MATRIX = [
    {
        "source_report": "a1_c3_prior_seed_term_compaction_scout",
        "term_id": "seed_term_compaction_candidate_set",
        "categories": ["prior_dictionary_candidate", "lab_evidence_reference", "caveat_required"],
        "settlement": "Seed terms may guide future YAML dictionary entries after o1 review",
        "forbidden_overread": "not final schema enum and not YAML creation authorization",
        "stop_line": "yaml_dictionary_not_authorized",
    },
    {
        "source_report": "a1_c3_prior_seed_term_compaction_scout",
        "term_id": "headless_render_oracle_candidate",
        "categories": ["validator_rule_candidate", "caveat_required", "stop_line"],
        "settlement": "Oracle language can inform future validator planning only",
        "forbidden_overread": "not visual parity proof and not renderer readiness",
        "stop_line": "visual_parity_readiness_not_authorized",
    },
    {
        "source_report": "a1_c3_prior_seed_term_compaction_scout",
        "term_id": "layered_occluding_body_visibility_contract",
        "categories": ["prior_dictionary_candidate", "schema_pressure_evidence", "caveat_required"],
        "settlement": "Ideal-form visibility term remains candidate vocabulary only",
        "forbidden_overread": "not mask implementation and not frame buffer truth",
        "stop_line": "runtime_occlusion_not_authorized",
    },
    {
        "source_report": "c4_c3_prior_dictionary_card_edge_scout",
        "term_id": "recipe_template_preview_ref_edges",
        "categories": ["schema_field_candidate", "validator_rule_candidate", "caveat_required"],
        "settlement": "recipe_ref, template_ref, and preview_ref may be future reference fields",
        "forbidden_overread": "not artifact dereference or runtime handoff",
        "stop_line": "artifact_runtime_handoff_not_authorized",
    },
    {
        "source_report": "c4_c3_prior_dictionary_card_edge_scout",
        "term_id": "view_card_translation_result_card_edge",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "ViewCard and TranslationResultCard edges can shape future dictionary cards",
        "forbidden_overread": "not c4 implementation change and not c1 runtime bridge",
        "stop_line": "c4_c1_integration_not_authorized",
    },
    {
        "source_report": "c4_c3_prior_dictionary_card_edge_scout",
        "term_id": "raw_payload_edge_rejection",
        "categories": ["validator_rule_candidate", "stop_line"],
        "settlement": "raw payload, framebuffer, dataframe, private path, and binary fields stay rejected",
        "forbidden_overread": "not payload allowance",
        "stop_line": "raw_payload_framebuffer_dataframe_not_authorized",
    },
    {
        "source_report": "c2_c3_lod_hint_schema_pressure_scout",
        "term_id": "lod_hint_schema_pressure",
        "categories": ["schema_pressure_evidence", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "lod_hint may pressure future schema shape but remains planning-only",
        "forbidden_overread": "not parser requirement and not runtime LOD algorithm",
        "stop_line": "lod_runtime_consumption_not_authorized",
    },
    {
        "source_report": "c2_c3_lod_hint_schema_pressure_scout",
        "term_id": "bbox_schema_pressure",
        "categories": ["schema_pressure_evidence", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "bbox may pressure future schema shape with planning-only extent semantics",
        "forbidden_overread": "not geometry payload and not query predicate",
        "stop_line": "geometry_payload_not_authorized",
    },
    {
        "source_report": "c2_c3_lod_hint_schema_pressure_scout",
        "term_id": "time_window_tile_ref_density_sample_pressure",
        "categories": ["schema_pressure_evidence", "not_yet_allowed", "caveat_required"],
        "settlement": "time_window, tile_ref, density_hint, and sample_budget require future gates",
        "forbidden_overread": "not stable required schema fields",
        "stop_line": "future_schema_pressure_gate_required",
    },
    {
        "source_report": "c1_c3_reference_envelope_schema_pressure_scout",
        "term_id": "reference_envelope_reference_only_contract",
        "categories": ["schema_pressure_evidence", "validator_rule_candidate", "caveat_required"],
        "settlement": "Reference envelope fields must stay opaque or summary-only",
        "forbidden_overread": "not direct c1 consumption and not raw cargo handoff",
        "stop_line": "direct_c1_consumption_not_authorized",
    },
    {
        "source_report": "c1_c3_reference_envelope_schema_pressure_scout",
        "term_id": "reference_envelope_redaction_safety_block",
        "categories": ["schema_field_candidate", "validator_rule_candidate", "stop_line"],
        "settlement": "Safety and redaction diagnostics should become future schema pressure",
        "forbidden_overread": "not c3 redaction responsibility and not payload acceptance",
        "stop_line": "c3_redaction_responsibility_not_authorized",
    },
    {
        "source_report": "c1_c3_reference_envelope_schema_pressure_scout",
        "term_id": "sample_query_ref_noncallable_guard",
        "categories": ["validator_rule_candidate", "stop_line"],
        "settlement": "sample_query_ref must remain opaque and non-callable",
        "forbidden_overread": "not DB query or sample dereference permission",
        "stop_line": "db_query_not_authorized",
    },
]

DECISION_OUTPUT = {
    "fourth_settlement_gate_passed": True,
    "yaml_dictionary_creation_authorized": False,
    "schema_json_modification_authorized": False,
    "validator_script_creation_authorized": False,
    "prototype_authorized": False,
    "runtime_renderer_formula_authorized": False,
    "lab_scout_final_schema_authorized": False,
    "readiness_claimed": False,
    "visual_parity_claimed": False,
    "correctness_claimed": False,
}

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 prior material fourth settlement gate. This gate classifies fourth-wave lab "
    "materials into prior dictionary candidates, schema-pressure evidence, schema-field candidates, "
    "validator-rule candidates, caveats, and stop-lines. It does not create YAML dictionary files, "
    "validator scripts, prototype code, runtime behavior, renderer behavior, formula movement, schema JSON changes, "
    "readiness claims, visual parity claims, correctness claims, or final-schema adoption of lab scouts."
)


def _row(term_id):
    for row in FOURTH_SETTLEMENT_MATRIX:
        if row["term_id"] == term_id:
            return row
    raise AssertionError(f"missing term: {term_id}")


class C3PriorMaterialFourthSettlementTest(unittest.TestCase):
    def test_required_lab_reports_are_observed(self):
        for name, path in LAB_REPORTS.items():
            self.assertTrue(path.exists(), name)
            self.assertGreater(path.stat().st_size, 100, name)

    def test_current_schema_and_validator_planning_remain_source_evidence(self):
        self.assertTrue(third_settlement.DECISION_OUTPUT["third_settlement_gate_passed"])
        self.assertTrue(validator_planning.DECISION_OUTPUT["schema_validator_planning_gate_passed"])
        self.assertTrue(schema_contract.SCHEMA_PATH.exists())
        self.assertFalse(schema_contract.YAML_DICTIONARY_PATH.exists())
        self.assertFalse(schema_contract.VALIDATOR_PATH.exists())

    def test_categories_are_complete(self):
        self.assertEqual(
            set(SETTLEMENT_CATEGORIES),
            {
                "prior_dictionary_candidate",
                "schema_pressure_evidence",
                "schema_field_candidate",
                "validator_rule_candidate",
                "lab_evidence_reference",
                "caveat_required",
                "stop_line",
                "not_yet_allowed",
            },
        )

    def test_a1_seed_terms_are_candidates_not_final_schema(self):
        seed = _row("seed_term_compaction_candidate_set")
        self.assertIn("prior_dictionary_candidate", seed["categories"])
        self.assertEqual(seed["stop_line"], "yaml_dictionary_not_authorized")
        oracle = _row("headless_render_oracle_candidate")
        self.assertEqual(oracle["stop_line"], "visual_parity_readiness_not_authorized")
        visibility = _row("layered_occluding_body_visibility_contract")
        self.assertIn("schema_pressure_evidence", visibility["categories"])

    def test_c4_card_edges_are_reference_fields_not_runtime_handoff(self):
        refs = _row("recipe_template_preview_ref_edges")
        self.assertIn("schema_field_candidate", refs["categories"])
        self.assertEqual(refs["stop_line"], "artifact_runtime_handoff_not_authorized")
        cards = _row("view_card_translation_result_card_edge")
        self.assertIn("validator_rule_candidate", cards["categories"])
        rejection = _row("raw_payload_edge_rejection")
        self.assertEqual(rejection["stop_line"], "raw_payload_framebuffer_dataframe_not_authorized")

    def test_c2_lod_schema_pressure_does_not_authorize_runtime_consumption(self):
        self.assertIn("schema_field_candidate", _row("lod_hint_schema_pressure")["categories"])
        self.assertEqual(_row("lod_hint_schema_pressure")["stop_line"], "lod_runtime_consumption_not_authorized")
        self.assertEqual(_row("bbox_schema_pressure")["stop_line"], "geometry_payload_not_authorized")
        unstable = _row("time_window_tile_ref_density_sample_pressure")
        self.assertIn("not_yet_allowed", unstable["categories"])
        self.assertEqual(unstable["stop_line"], "future_schema_pressure_gate_required")

    def test_c1_reference_envelope_pressure_preserves_reference_only_boundary(self):
        envelope = _row("reference_envelope_reference_only_contract")
        self.assertIn("validator_rule_candidate", envelope["categories"])
        self.assertEqual(envelope["stop_line"], "direct_c1_consumption_not_authorized")
        safety = _row("reference_envelope_redaction_safety_block")
        self.assertIn("schema_field_candidate", safety["categories"])
        self.assertEqual(safety["stop_line"], "c3_redaction_responsibility_not_authorized")
        self.assertEqual(_row("sample_query_ref_noncallable_guard")["stop_line"], "db_query_not_authorized")

    def test_every_row_has_valid_category_forbidden_overread_and_stop_line(self):
        allowed = set(SETTLEMENT_CATEGORIES)
        for row in FOURTH_SETTLEMENT_MATRIX:
            self.assertTrue(set(row["categories"]).issubset(allowed), row["term_id"])
            self.assertTrue(row["forbidden_overread"], row["term_id"])
            self.assertTrue(row["stop_line"], row["term_id"])

    def test_forbidden_scope_remains_blocked(self):
        self.assertTrue(DECISION_OUTPUT["fourth_settlement_gate_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_json_modification_authorized",
            "validator_script_creation_authorized",
            "prototype_authorized",
            "runtime_renderer_formula_authorized",
            "lab_scout_final_schema_authorized",
            "readiness_claimed",
            "visual_parity_claimed",
            "correctness_claimed",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_schema_json_file_is_not_modified_by_this_settlement(self):
        schema = schema_contract.load_schema()
        self.assertEqual(schema["title"], "RRKAL c3 prior semantic dictionary v0")
        self.assertIn("x-rrkal-boundary", schema)
        self.assertFalse(schema_contract.YAML_DICTIONARY_PATH.exists())
        self.assertFalse(schema_contract.VALIDATOR_PATH.exists())

    def test_boundary_statement_is_docs_test_only(self):
        self.assertIn("Docs/test-only", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary files", BOUNDARY_STATEMENT)
        self.assertIn("schema JSON changes", BOUNDARY_STATEMENT)
        self.assertIn("final-schema adoption of lab scouts", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()