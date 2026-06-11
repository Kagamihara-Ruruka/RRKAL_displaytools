"""Docs/test-only second settlement for c3 parallel supply-chain materials."""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_semantic_dictionary_schema_json_contract_planning as schema_planning
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning as validator_planning


LAB_EVIDENCE_REFS = [
    "L:/RRKAL_lab/external_research/analysis/a1_c3_wysiwyg_recipe_authoring_authority_scout.zh-TW.md",
    "L:/RRKAL_lab/external_research/analysis/c4_c3_render_recipe_ingress_egress_mediation_scout.zh-TW.md",
    "L:/RRKAL_lab/external_research/analysis/c2_c3_spatiotemporal_lod_preaggregation_prior_scout.zh-TW.md",
    "L:/RRKAL_lab/external_research/analysis/c1_c3_asset_source_reference_shape_scout.zh-TW.md",
]

SETTLEMENT_CATEGORIES = [
    "prior_dictionary_candidate",
    "schema_field_candidate",
    "validator_rule_candidate",
    "authority_reference_only",
    "lab_evidence_reference",
    "caveat_required",
    "stop_line",
    "not_yet_allowed",
]

SECOND_SETTLEMENT_MATRIX = [
    {
        "source_agent": "a_1",
        "term_id": "stateless_render_recipe_document_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_recipe_document_prior",
        "caveat": "recipe document planning only; no render recipe implementation",
        "stop_line": "visual_parity_oracle_required_before_pixel_truth",
    },
    {
        "source_agent": "a_1",
        "term_id": "canvas_container_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "settlement": "accepted_as_canvas_container_prior",
        "caveat": "container vocabulary only; no renderer surface creation",
        "stop_line": "renderer_runtime_not_authorized",
    },
    {
        "source_agent": "a_1",
        "term_id": "viewport_coordinate_frame_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_viewport_coordinate_frame_prior",
        "caveat": "coordinate frame vocabulary only; no projection formula movement",
        "stop_line": "projection_formula_stop_line",
    },
    {
        "source_agent": "a_1",
        "term_id": "multiviewport_layout_recipe_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "settlement": "accepted_as_multiviewport_layout_recipe_prior",
        "caveat": "layout recipe vocabulary only; no host shell implementation",
        "stop_line": "prototype_authorization_stop_line",
    },
    {
        "source_agent": "a_1",
        "term_id": "custom_render_pipeline_extension_prior",
        "categories": ["prior_dictionary_candidate", "caveat_required", "stop_line"],
        "settlement": "extension_registry_candidate_only",
        "caveat": "extension registry vocabulary only; no shader or custom pipeline implementation",
        "stop_line": "shader_implementation_not_authorized",
    },
    {
        "source_agent": "a_1",
        "term_id": "pixel_visual_parity_oracle_requirement",
        "categories": ["validator_rule_candidate", "caveat_required", "stop_line"],
        "settlement": "oracle_requirement_preserved",
        "caveat": "visual parity remains externally judged and not claimed here",
        "stop_line": "visual_parity_claim_not_authorized",
    },
    {
        "source_agent": "c_4",
        "term_id": "c4_mediates_ingress_egress_for_render_recipe",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_governance_prior_candidate",
        "caveat": "mediation planning only; no c4 implementation change",
        "stop_line": "c4_implementation_change_not_authorized",
    },
    {
        "source_agent": "c_4",
        "term_id": "result_card_evidence_handoff",
        "categories": ["schema_field_candidate", "validator_rule_candidate"],
        "settlement": "future_schema_field_candidate",
        "caveat": "result card and evidence handoff are future dictionary fields only",
        "stop_line": "runtime_handoff_not_implemented",
    },
    {
        "source_agent": "c_4",
        "term_id": "raw_row_seam_temporary_modular_removable",
        "categories": ["caveat_required", "stop_line", "lab_evidence_reference"],
        "settlement": "temporary_seam_caveat_recorded",
        "caveat": "raw-row seam is temporary, modular, and removable; removal timing needs a future gate",
        "stop_line": "same_workflow_removal_not_forced",
    },
    {
        "source_agent": "c_2",
        "term_id": "lod_hint",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_safer_planning_evidence",
        "caveat": "display planning hint only; compression algorithm remains c_2-owned",
        "stop_line": "compression_algorithm_not_transferred",
    },
    {
        "source_agent": "c_2",
        "term_id": "bbox",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_safer_planning_evidence",
        "caveat": "extent planning field only; no geometry payload handoff",
        "stop_line": "raw_geometry_payload_not_authorized",
    },
    {
        "source_agent": "c_2",
        "term_id": "tile_ref",
        "categories": ["not_yet_allowed", "caveat_required"],
        "settlement": "requires_future_gate",
        "caveat": "tile reference stability and ownership need future review",
        "stop_line": "tile_contract_not_finalized",
    },
    {
        "source_agent": "c_2",
        "term_id": "time_window",
        "categories": ["not_yet_allowed", "caveat_required"],
        "settlement": "requires_future_gate",
        "caveat": "temporal slice semantics need future review",
        "stop_line": "time_window_contract_not_finalized",
    },
    {
        "source_agent": "c_2",
        "term_id": "sample_budget",
        "categories": ["not_yet_allowed", "caveat_required"],
        "settlement": "requires_future_gate",
        "caveat": "sampling budget risks runtime interpretation and needs future review",
        "stop_line": "sample_budget_contract_not_finalized",
    },
    {
        "source_agent": "c_2",
        "term_id": "aggregation_level",
        "categories": ["not_yet_allowed", "caveat_required"],
        "settlement": "requires_future_gate",
        "caveat": "aggregation algorithm remains c_2-owned and needs future review",
        "stop_line": "aggregation_algorithm_not_transferred",
    },
    {
        "source_agent": "c_2",
        "term_id": "density_hint",
        "categories": ["not_yet_allowed", "caveat_required"],
        "settlement": "requires_future_gate",
        "caveat": "density semantics need future validator and schema gate",
        "stop_line": "density_hint_contract_not_finalized",
    },
    {
        "source_agent": "c_2",
        "term_id": "preview_budget",
        "categories": ["not_yet_allowed", "caveat_required"],
        "settlement": "requires_future_gate",
        "caveat": "preview budget can drift into performance claim and needs future review",
        "stop_line": "performance_claim_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "asset_id",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "opaque identifier only; no payload locator",
        "stop_line": "payload_path_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "subject_ref",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "subject reference only; no geometry payload",
        "stop_line": "raw_geometry_payload_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "source_ref",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "source evidence reference only; no DB or path access",
        "stop_line": "database_query_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "dataset_kind",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "coarse planning enum only; no parser dispatch",
        "stop_line": "runtime_parser_dispatch_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "spatial_extent",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "bounded summary only; no feature collection",
        "stop_line": "raw_geometry_payload_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "temporal_extent",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "time summary only; no row-level timestamps",
        "stop_line": "raw_rows_not_authorized",
    },
    {
        "source_agent": "c_1",
        "term_id": "schema_ref",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "schema reference only; no schema ownership transfer",
        "stop_line": "api_schema_finalization_blocked",
    },
    {
        "source_agent": "c_1",
        "term_id": "sample_query_ref",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate", "caveat_required"],
        "settlement": "accepted_as_reference_envelope_planning_candidate",
        "caveat": "opaque sample reference only; no SQL, dataframe, or raw rows",
        "stop_line": "sample_query_execution_not_authorized",
    },
]

ACCEPTED_A1_PRIORS = [
    "stateless_render_recipe_document_prior",
    "canvas_container_prior",
    "viewport_coordinate_frame_prior",
    "multiviewport_layout_recipe_prior",
]

C2_NOT_YET_STABLE_FIELDS = [
    "tile_ref",
    "time_window",
    "sample_budget",
    "aggregation_level",
    "density_hint",
    "preview_budget",
]

C1_REFERENCE_ENVELOPE_FIELDS = [
    "asset_id",
    "subject_ref",
    "source_ref",
    "dataset_kind",
    "spatial_extent",
    "temporal_extent",
    "schema_ref",
    "sample_query_ref",
]

DECISION_OUTPUT = {
    "parallel_supply_chain_second_settlement_passed": True,
    "yaml_dictionary_creation_authorized": False,
    "schema_json_creation_authorized": False,
    "validator_script_creation_authorized": False,
    "future_dictionary_contract_test_creation_authorized": False,
    "prototype_authorized": False,
    "runtime_renderer_behavior_authorized": False,
    "c4_c1_c2_integration_implemented": False,
    "readiness_claimed": False,
    "correctness_claimed": False,
    "visual_parity_claimed": False,
    "leak_fix_claimed": False,
    "performance_claimed": False,
    "runtime_replacement_authorized": False,
}

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 parallel supply-chain material second settlement gate. "
    "This gate classifies second-wave a_1, c_1, c_2, and c_4 lab materials into prior dictionary "
    "candidates, schema-field candidates, validator-rule candidates, evidence references, caveats, stop-lines, "
    "and not-yet-allowed fields. It does not create YAML dictionary files, schema files, validator scripts, "
    "future dictionary contract tests, prototype code, runtime behavior, renderer behavior, formula movement, "
    "c_4, c_1, or c_2 integration changes, readiness claims, correctness claims, visual parity claims, "
    "leak-fix claims, performance claims, or runtime replacement authorization."
)


def _row(term_id):
    for row in SECOND_SETTLEMENT_MATRIX:
        if row["term_id"] == term_id:
            return row
    raise AssertionError(f"missing term: {term_id}")


class C3ParallelSupplyChainMaterialSecondSettlementTest(unittest.TestCase):
    def test_evidence_refs_exist_and_current_planning_gates_pass(self):
        for ref in LAB_EVIDENCE_REFS:
            self.assertTrue(Path(ref).exists(), ref)
        self.assertTrue(schema_planning.DECISION_OUTPUT["schema_json_contract_planning_gate_passed"])
        self.assertTrue(validator_planning.DECISION_OUTPUT["schema_validator_planning_gate_passed"])

    def test_required_settlement_categories_are_available(self):
        self.assertEqual(
            set(SETTLEMENT_CATEGORIES),
            {
                "prior_dictionary_candidate",
                "schema_field_candidate",
                "validator_rule_candidate",
                "authority_reference_only",
                "lab_evidence_reference",
                "caveat_required",
                "stop_line",
                "not_yet_allowed",
            },
        )

    def test_a1_wysiwyg_priors_are_accepted_with_oracle_and_extension_caveat(self):
        for term_id in ACCEPTED_A1_PRIORS:
            row = _row(term_id)
            self.assertIn("prior_dictionary_candidate", row["categories"])
            self.assertNotIn("not_yet_allowed", row["categories"])
        extension = _row("custom_render_pipeline_extension_prior")
        self.assertEqual(extension["settlement"], "extension_registry_candidate_only")
        self.assertIn("shader", extension["caveat"])
        oracle = _row("pixel_visual_parity_oracle_requirement")
        self.assertIn("validator_rule_candidate", oracle["categories"])
        self.assertEqual(oracle["stop_line"], "visual_parity_claim_not_authorized")

    def test_c4_mediation_accepts_governance_prior_and_preserves_raw_row_caveat(self):
        mediation = _row("c4_mediates_ingress_egress_for_render_recipe")
        self.assertIn("prior_dictionary_candidate", mediation["categories"])
        self.assertIn("validator_rule_candidate", mediation["categories"])
        result_card = _row("result_card_evidence_handoff")
        self.assertIn("schema_field_candidate", result_card["categories"])
        seam = _row("raw_row_seam_temporary_modular_removable")
        self.assertIn("caveat_required", seam["categories"])
        self.assertIn("temporary", seam["caveat"])
        self.assertEqual(seam["stop_line"], "same_workflow_removal_not_forced")

    def test_c2_lod_accepts_lod_hint_and_bbox_but_defers_unstable_fields(self):
        for term_id in ["lod_hint", "bbox"]:
            row = _row(term_id)
            self.assertIn("prior_dictionary_candidate", row["categories"])
            self.assertIn("schema_field_candidate", row["categories"])
        for term_id in C2_NOT_YET_STABLE_FIELDS:
            row = _row(term_id)
            self.assertIn("not_yet_allowed", row["categories"])
            self.assertIn("future", row["caveat"])
        self.assertEqual(_row("aggregation_level")["stop_line"], "aggregation_algorithm_not_transferred")

    def test_c1_reference_envelope_fields_are_accepted_without_payload_transfer(self):
        for term_id in C1_REFERENCE_ENVELOPE_FIELDS:
            row = _row(term_id)
            self.assertIn("prior_dictionary_candidate", row["categories"])
            self.assertIn("schema_field_candidate", row["categories"])
            self.assertNotIn("dataframe", row["caveat"] if term_id != "sample_query_ref" else "")
        self.assertEqual(_row("source_ref")["stop_line"], "database_query_not_authorized")
        self.assertEqual(_row("schema_ref")["stop_line"], "api_schema_finalization_blocked")
        self.assertEqual(_row("sample_query_ref")["stop_line"], "sample_query_execution_not_authorized")

    def test_every_row_has_required_categories_caveat_and_stop_line(self):
        allowed = set(SETTLEMENT_CATEGORIES)
        for row in SECOND_SETTLEMENT_MATRIX:
            self.assertTrue(set(row["categories"]).issubset(allowed), row["term_id"])
            self.assertTrue(row["caveat"], row["term_id"])
            self.assertTrue(row["stop_line"], row["term_id"])

    def test_forbidden_creation_runtime_integration_and_claims_are_blocked(self):
        self.assertTrue(DECISION_OUTPUT["parallel_supply_chain_second_settlement_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_json_creation_authorized",
            "validator_script_creation_authorized",
            "future_dictionary_contract_test_creation_authorized",
            "prototype_authorized",
            "runtime_renderer_behavior_authorized",
            "c4_c1_c2_integration_implemented",
            "readiness_claimed",
            "correctness_claimed",
            "visual_parity_claimed",
            "leak_fix_claimed",
            "performance_claimed",
            "runtime_replacement_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_no_future_dictionary_schema_validator_or_contract_targets_are_created(self):
        self.assertFalse(Path("docs/c3_prior_dictionary").exists())
        self.assertFalse(Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml").exists())
        self.assertFalse(Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json").exists())
        self.assertFalse(Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py").exists())
        self.assertFalse(Path("tests/test_displaytools_c3_prior_semantic_dictionary_contract.py").exists())

    def test_boundary_statement_blocks_runtime_readiness_and_replacement(self):
        self.assertIn("Docs/test-only", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary files", BOUNDARY_STATEMENT)
        self.assertIn("runtime behavior", BOUNDARY_STATEMENT)
        self.assertIn("runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
