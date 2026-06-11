"""Docs/test-only third settlement for c3 prior materials."""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_parallel_supply_chain_material_second_settlement as second_settlement
from tests import test_displaytools_c3_prior_law_material_settlement as law_settlement
from tests import test_displaytools_c3_prior_semantic_dictionary_schema_json_contract_planning as schema_planning
from tests import test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning as validator_planning


LAB_REPORTS = {
    "a1_python_template_export": Path(
        r"L:\RRKAL_lab\external_research\analysis\a1_c3_python_template_export_authority_scout.zh-TW.md"
    ),
    "c4_result_card_contract": Path(
        r"L:\RRKAL_lab\external_research\analysis\c4_c3_render_recipe_result_card_contract_scout.zh-TW.md"
    ),
    "c2_display_hint_negative_consumption": Path(
        r"L:\RRKAL_lab\external_research\analysis\c2_c3_display_hint_negative_consumption_matrix_scout.zh-TW.md"
    ),
    "c1_redaction_negative_matrix": Path(
        r"L:\RRKAL_lab\external_research\analysis\c1_c3_asset_reference_redaction_negative_matrix_scout.zh-TW.md"
    ),
}

C1_REDACTION_NEGATIVE_MATRIX_STATUS = (
    "observed"
    if LAB_REPORTS["c1_redaction_negative_matrix"].exists()
    else "c1_redaction_negative_matrix_not_observed"
)

SETTLEMENT_CATEGORIES = [
    "prior_dictionary_candidate",
    "schema_field_candidate",
    "validator_rule_candidate",
    "lab_evidence_reference",
    "caveat_required",
    "stop_line",
    "negative_consumption_guard",
    "not_yet_allowed",
]

THIRD_SETTLEMENT_MATRIX = [
    {
        "source_report": "a1_c3_python_template_export_authority_scout",
        "term_id": "python_template_export_reference_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "caveat_required"],
        "classification": "template_reference_prior_candidate",
        "settlement": "Python template export may be represented as reference or stencil vocabulary only",
        "forbidden_overread": "not executable Python export authorization",
        "stop_line": "prototype_code_generation_not_authorized",
    },
    {
        "source_report": "a1_c3_python_template_export_authority_scout",
        "term_id": "headless_export_oracle_candidate",
        "categories": ["validator_rule_candidate", "caveat_required", "stop_line"],
        "classification": "oracle_candidate_only",
        "settlement": "Headless export and structural oracle language may guide future validator planning",
        "forbidden_overread": "not pixel or visual parity proof",
        "stop_line": "visual_parity_claim_not_authorized",
    },
    {
        "source_report": "a1_c3_python_template_export_authority_scout",
        "term_id": "stateless_figure_dictionary_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate"],
        "classification": "stateless_reference_shape_candidate",
        "settlement": "Figure-like output should be dictionary or reference shaped, not live object shaped",
        "forbidden_overread": "no matplotlib plotly or GUI runtime object handoff",
        "stop_line": "runtime_object_not_authorized",
    },
    {
        "source_report": "a1_c3_python_template_export_authority_scout",
        "term_id": "environment_specific_magic_filter",
        "categories": ["validator_rule_candidate", "negative_consumption_guard", "stop_line"],
        "classification": "environment_lockin_guard",
        "settlement": "Notebook or environment-specific magic should be rejected or filtered before prior use",
        "forbidden_overread": "not notebook runtime support authorization",
        "stop_line": "environment_runtime_not_authorized",
    },
    {
        "source_report": "c4_c3_render_recipe_result_card_contract_scout",
        "term_id": "translation_result_card_contract_prior",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "classification": "result_card_contract_candidate",
        "settlement": "Result-card vocabulary may structure future c_4 to c_3 handoff evidence",
        "forbidden_overread": "not c_4 implementation change or live handoff",
        "stop_line": "c4_implementation_change_not_authorized",
    },
    {
        "source_report": "c4_c3_render_recipe_result_card_contract_scout",
        "term_id": "output_card_ref",
        "categories": ["schema_field_candidate", "validator_rule_candidate"],
        "classification": "reference_field_candidate",
        "settlement": "Output card reference may be planned as reference-only schema field",
        "forbidden_overread": "not dereference permission or artifact read permission",
        "stop_line": "artifact_read_not_authorized",
    },
    {
        "source_report": "c4_c3_render_recipe_result_card_contract_scout",
        "term_id": "diagnostics_and_evidence_refs",
        "categories": ["schema_field_candidate", "validator_rule_candidate"],
        "classification": "evidence_handoff_field_candidate",
        "settlement": "Diagnostics and evidence refs may preserve handoff state without raw payload",
        "forbidden_overread": "not readiness or integration proof",
        "stop_line": "readiness_claim_not_authorized",
    },
    {
        "source_report": "c4_c3_render_recipe_result_card_contract_scout",
        "term_id": "payload_framebuffer_dataframe_binary_rejection",
        "categories": ["validator_rule_candidate", "negative_consumption_guard", "stop_line"],
        "classification": "forbidden_payload_family_guard",
        "settlement": "Payload, framebuffer, dataframe, binary, and private path fields must be rejected",
        "forbidden_overread": "not raw payload or frame buffer authorization",
        "stop_line": "raw_payload_framebuffer_dataframe_not_authorized",
    },
    {
        "source_report": "c2_c3_display_hint_negative_consumption_matrix_scout",
        "term_id": "display_hint_negative_consumption_matrix",
        "categories": ["validator_rule_candidate", "negative_consumption_guard", "lab_evidence_reference"],
        "classification": "negative_consumption_matrix_candidate",
        "settlement": "Display hints may be planned as declared-only evidence with negative consumption guards",
        "forbidden_overread": "not cross-repo consumption-ready contract",
        "stop_line": "display_hint_consumption_not_authorized",
    },
    {
        "source_report": "c2_c3_display_hint_negative_consumption_matrix_scout",
        "term_id": "lod_hint_declared_only_guard",
        "categories": ["validator_rule_candidate", "schema_field_candidate", "caveat_required"],
        "classification": "safe_planning_field_guard",
        "settlement": "lod_hint remains planning-only and cannot become parser or runtime requirement",
        "forbidden_overread": "not c_3 parser or algorithm requirement",
        "stop_line": "runtime_consumption_not_authorized",
    },
    {
        "source_report": "c2_c3_display_hint_negative_consumption_matrix_scout",
        "term_id": "bbox_declared_only_guard",
        "categories": ["validator_rule_candidate", "schema_field_candidate", "caveat_required"],
        "classification": "safe_planning_field_guard",
        "settlement": "bbox remains extent planning evidence and cannot become authoritative geometry payload",
        "forbidden_overread": "not raw world-coordinate or geometry payload truth",
        "stop_line": "geometry_payload_not_authorized",
    },
    {
        "source_report": "c2_c3_display_hint_negative_consumption_matrix_scout",
        "term_id": "unstable_display_hint_fields",
        "categories": ["not_yet_allowed", "caveat_required", "stop_line"],
        "classification": "future_gate_required",
        "settlement": "tile_ref, time_window, sample_budget, aggregation_level, density_hint, preview_budget, trajectory_simplification_hint, and table_preview_limit need future gates",
        "forbidden_overread": "not schema required fields or runtime consumption fields",
        "stop_line": "unstable_hint_contract_not_finalized",
    },
    {
        "source_report": "c1_c3_asset_reference_redaction_negative_matrix_scout",
        "term_id": "c1_redaction_negative_matrix_observed",
        "categories": ["lab_evidence_reference", "validator_rule_candidate", "negative_consumption_guard"],
        "classification": C1_REDACTION_NEGATIVE_MATRIX_STATUS,
        "settlement": "Observed c_1 redaction negative matrix can inform future validator rules",
        "forbidden_overread": "not mature c_1 to c_3 interface authorization",
        "stop_line": "c1_direct_integration_not_authorized",
    },
    {
        "source_report": "c1_c3_asset_reference_redaction_negative_matrix_scout",
        "term_id": "private_path_sql_db_raw_rows_dataframe_redaction_guard",
        "categories": ["validator_rule_candidate", "negative_consumption_guard", "stop_line"],
        "classification": "redaction_guard_candidate" if C1_REDACTION_NEGATIVE_MATRIX_STATUS == "observed" else "not_observed",
        "settlement": "Private paths, SQL, DB connection strings, raw rows, dataframes, feature collections, cache paths, and cleaning hints must be rejected or made opaque",
        "forbidden_overread": "not payload, dataframe, DB query, or cleaning transfer authorization",
        "stop_line": "raw_payload_dataframe_db_query_not_authorized",
    },
]

DECISION_OUTPUT = {
    "third_settlement_gate_passed": True,
    "c1_redaction_negative_matrix_status": C1_REDACTION_NEGATIVE_MATRIX_STATUS,
    "yaml_dictionary_creation_authorized": False,
    "schema_json_creation_authorized": False,
    "validator_script_creation_authorized": False,
    "prototype_authorized": False,
    "runtime_renderer_formula_authorized": False,
    "raw_payload_authorized": False,
    "frame_buffer_authorized": False,
    "dataframe_authorized": False,
    "db_query_authorized": False,
    "c4_bypass_authorized": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "performance_claimed": False,
}

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 prior material third settlement gate. This gate classifies third-wave lab "
    "materials for Python template export, render recipe result cards, display hint negative consumption, "
    "and optional c_1 redaction negative matrix evidence before any YAML, schema, validator, prototype, "
    "runtime, renderer, or formula work. It does not authorize raw payloads, frame buffers, dataframes, "
    "DB queries, c_4 bypass, visual parity claims, readiness claims, performance claims, or push."
)


def _row(term_id):
    for row in THIRD_SETTLEMENT_MATRIX:
        if row["term_id"] == term_id:
            return row
    raise AssertionError(f"missing term: {term_id}")


class C3PriorMaterialThirdSettlementTest(unittest.TestCase):
    def test_required_lab_reports_are_observed_with_optional_c1_status(self):
        for key in [
            "a1_python_template_export",
            "c4_result_card_contract",
            "c2_display_hint_negative_consumption",
        ]:
            self.assertTrue(LAB_REPORTS[key].exists(), key)
        self.assertIn(
            C1_REDACTION_NEGATIVE_MATRIX_STATUS,
            {"observed", "c1_redaction_negative_matrix_not_observed"},
        )
        if C1_REDACTION_NEGATIVE_MATRIX_STATUS == "observed":
            self.assertTrue(LAB_REPORTS["c1_redaction_negative_matrix"].exists())

    def test_prior_settlement_evidence_remains_passed(self):
        self.assertTrue(second_settlement.DECISION_OUTPUT["parallel_supply_chain_second_settlement_passed"])
        self.assertTrue(law_settlement.DECISION_OUTPUT["settlement_passed"])
        self.assertTrue(schema_planning.DECISION_OUTPUT["schema_json_contract_planning_gate_passed"])
        self.assertTrue(validator_planning.DECISION_OUTPUT["schema_validator_planning_gate_passed"])

    def test_categories_are_complete(self):
        self.assertEqual(
            set(SETTLEMENT_CATEGORIES),
            {
                "prior_dictionary_candidate",
                "schema_field_candidate",
                "validator_rule_candidate",
                "lab_evidence_reference",
                "caveat_required",
                "stop_line",
                "negative_consumption_guard",
                "not_yet_allowed",
            },
        )

    def test_a1_python_template_export_is_reference_and_oracle_planning_only(self):
        self.assertIn("prior_dictionary_candidate", _row("python_template_export_reference_prior")["categories"])
        self.assertEqual(
            _row("python_template_export_reference_prior")["stop_line"],
            "prototype_code_generation_not_authorized",
        )
        self.assertEqual(_row("headless_export_oracle_candidate")["stop_line"], "visual_parity_claim_not_authorized")
        self.assertEqual(_row("stateless_figure_dictionary_prior")["stop_line"], "runtime_object_not_authorized")
        self.assertEqual(_row("environment_specific_magic_filter")["classification"], "environment_lockin_guard")

    def test_c4_result_card_contract_is_reference_only_with_payload_rejection(self):
        self.assertIn("prior_dictionary_candidate", _row("translation_result_card_contract_prior")["categories"])
        self.assertIn("schema_field_candidate", _row("output_card_ref")["categories"])
        self.assertIn("validator_rule_candidate", _row("diagnostics_and_evidence_refs")["categories"])
        rejection = _row("payload_framebuffer_dataframe_binary_rejection")
        self.assertIn("negative_consumption_guard", rejection["categories"])
        self.assertEqual(rejection["stop_line"], "raw_payload_framebuffer_dataframe_not_authorized")

    def test_c2_negative_consumption_matrix_blocks_runtime_consumption(self):
        matrix = _row("display_hint_negative_consumption_matrix")
        self.assertIn("negative_consumption_guard", matrix["categories"])
        self.assertEqual(matrix["stop_line"], "display_hint_consumption_not_authorized")
        self.assertEqual(_row("lod_hint_declared_only_guard")["stop_line"], "runtime_consumption_not_authorized")
        self.assertEqual(_row("bbox_declared_only_guard")["stop_line"], "geometry_payload_not_authorized")
        self.assertIn("not_yet_allowed", _row("unstable_display_hint_fields")["categories"])

    def test_optional_c1_redaction_matrix_is_settled_without_blocking_gate(self):
        c1_status = _row("c1_redaction_negative_matrix_observed")
        self.assertEqual(c1_status["classification"], C1_REDACTION_NEGATIVE_MATRIX_STATUS)
        if C1_REDACTION_NEGATIVE_MATRIX_STATUS == "observed":
            self.assertIn("validator_rule_candidate", c1_status["categories"])
            self.assertEqual(
                _row("private_path_sql_db_raw_rows_dataframe_redaction_guard")["classification"],
                "redaction_guard_candidate",
            )
        else:
            self.assertEqual(C1_REDACTION_NEGATIVE_MATRIX_STATUS, "c1_redaction_negative_matrix_not_observed")

    def test_every_row_has_valid_category_caveat_and_stop_line(self):
        allowed = set(SETTLEMENT_CATEGORIES)
        for row in THIRD_SETTLEMENT_MATRIX:
            self.assertTrue(set(row["categories"]).issubset(allowed), row["term_id"])
            self.assertTrue(row["forbidden_overread"], row["term_id"])
            self.assertTrue(row["stop_line"], row["term_id"])

    def test_forbidden_creation_runtime_payload_and_claims_are_blocked(self):
        self.assertTrue(DECISION_OUTPUT["third_settlement_gate_passed"])
        for key in [
            "yaml_dictionary_creation_authorized",
            "schema_json_creation_authorized",
            "validator_script_creation_authorized",
            "prototype_authorized",
            "runtime_renderer_formula_authorized",
            "raw_payload_authorized",
            "frame_buffer_authorized",
            "dataframe_authorized",
            "db_query_authorized",
            "c4_bypass_authorized",
            "visual_parity_claimed",
            "readiness_claimed",
            "performance_claimed",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_no_future_dictionary_schema_validator_or_prototype_targets_created(self):
        self.assertFalse(Path("docs/c3_prior_dictionary").exists())
        self.assertFalse(Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml").exists())
        self.assertFalse(Path("docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json").exists())
        self.assertFalse(Path("scripts/validate_displaytools_c3_prior_semantic_dictionary.py").exists())
        self.assertFalse(Path("tests/test_displaytools_c3_prior_semantic_dictionary_contract.py").exists())

    def test_boundary_statement_is_docs_test_only(self):
        self.assertIn("Docs/test-only", BOUNDARY_STATEMENT)
        self.assertIn("does not authorize raw payloads", BOUNDARY_STATEMENT)
        self.assertIn("visual parity claims", BOUNDARY_STATEMENT)
        self.assertIn("performance claims", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()