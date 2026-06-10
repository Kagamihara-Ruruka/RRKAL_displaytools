"""Planning gate for computed-but-hidden minimal extraction."""

from __future__ import annotations

import unittest


FUTURE_HELPER_TARGET = "render_core/dynamic_point_computed_but_hidden_boundary.py"
REQUIRED_CHECKER = "scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py"

ALLOWED_OUTPUT_SHAPE = {
    "nested_dict": True,
    "list": True,
    "scalar": True,
    "callable": False,
    "runtime_object": False,
    "dataframe": False,
    "renderer_buffer": False,
}

ALLOWED_LABELS = [
    "source_present_token",
    "computed_point_token",
    "hidden_visibility_token",
    "frame_visible_not_observed",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "computed_but_hidden_contract",
    "transparent_globe_leak_not_inferred",
    "source_loss_not_inferred",
    "frame_buffer_read_blocked",
    "renderer_execution_blocked",
    "readiness_not_claimed",
]

FORBIDDEN_FIELDS = [
    "runtime_probe",
    "render_if_needed",
    "controller_runtime",
    "renderer_runtime",
    "frame_buffer",
    "artifact_writer",
    "projection_formula",
    "mask_formula",
    "sampling_formula_movement",
    "alpha_compose_formula",
    "dataframe_runtime",
    "live_source",
    "cache_database_io",
    "hidden_as_missing_interpretation",
    "source_lineage_loss_interpretation",
    "transparent_globe_leak_inference",
    "coordinate_correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "transparent_globe_leak_fix_claim",
]

PLANNED_HELPER_FAMILIES = [
    {
        "helper_family": "build_dynamic_point_computed_but_hidden_contract_descriptor",
        "intended_output_keys": [
            "contract_id",
            "source_present_token",
            "computed_point_token",
            "hidden_visibility_token",
            "hidden_is_not_missing",
            "computed_but_hidden_contract",
            "allowed_output_shape",
        ],
        "allowed_labels": [
            "source_present_token",
            "computed_point_token",
            "hidden_visibility_token",
            "hidden_is_not_missing",
            "computed_but_hidden_contract",
            "readiness_not_claimed",
        ],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "preserve_identity_only_no_mutation",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "computed_but_hidden_import_boundary_checker_blocks_runtime_formula_frame_and_claims",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_hidden_visibility_contract_descriptor",
        "intended_output_keys": [
            "contract_id",
            "hidden_visibility_token",
            "hidden_is_not_missing",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
        ],
        "allowed_labels": [
            "hidden_visibility_token",
            "hidden_is_not_missing",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
        ],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "hidden_visibility_does_not_delete_source",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "label_executable_reference_and_hidden_as_missing_are_blocked",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_computed_point_contract_descriptor",
        "intended_output_keys": [
            "contract_id",
            "computed_point_token",
            "source_present_token",
            "computed_but_hidden_contract",
            "coordinate_correctness_claimed",
        ],
        "allowed_labels": [
            "computed_point_token",
            "source_present_token",
            "computed_but_hidden_contract",
        ],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "computed_status_is_not_source_completeness_claim",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "correctness_and_runtime_probe_references_are_blocked",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor",
        "intended_output_keys": [
            "guard_id",
            "source_present_token",
            "occluded_is_not_source_lineage_loss",
            "source_loss_not_inferred",
            "source_lineage_mutation_allowed",
        ],
        "allowed_labels": [
            "source_present_token",
            "occluded_is_not_source_lineage_loss",
            "source_loss_not_inferred",
        ],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "guard_only_no_source_lineage_loss_interpretation",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "source_lineage_loss_interpretation_is_blocked",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "build_dynamic_point_computed_but_hidden_stop_line_ledger",
        "intended_output_keys": [
            "ledger_id",
            "frame_visible_not_observed",
            "frame_buffer_read_blocked",
            "renderer_execution_blocked",
            "transparent_globe_leak_not_inferred",
            "readiness_not_claimed",
        ],
        "allowed_labels": [
            "frame_visible_not_observed",
            "frame_buffer_read_blocked",
            "renderer_execution_blocked",
            "transparent_globe_leak_not_inferred",
            "readiness_not_claimed",
        ],
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "no_source_lineage_mutation_from_visibility_stop_line",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "frame_buffer_renderer_leak_inference_and_readiness_claims_are_blocked",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "dynamic_point_computed_but_hidden_boundary_descriptor",
        "intended_output_keys": [
            "boundary_id",
            "scope",
            "owned_contracts",
            "blocked_surfaces",
            "allowed_output_shape",
        ],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "descriptor_records_guard_no_mutation",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "all_forbidden_families_remain_negative_self_tested",
        "helper_creation_authorized": False,
    },
    {
        "helper_family": "dynamic_point_computed_but_hidden_planning_bundle",
        "intended_output_keys": [
            "minimal_extraction_planning_passed",
            "future_helper_target",
            "checker_available_for_future_helper",
            "helper_creation_authorized",
            "decision_output",
        ],
        "allowed_labels": ALLOWED_LABELS,
        "forbidden_fields": FORBIDDEN_FIELDS,
        "source_lineage_impact": "bundle_is_non_authorizing_planning_only",
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "checker_coverage_expectation": "future_helper_must_pass_dedicated_checker_before_creation_gate",
        "helper_creation_authorized": False,
    },
]

DECISION_OUTPUT = {
    "minimal_extraction_planning_passed": True,
    "future_helper_target": FUTURE_HELPER_TARGET,
    "checker_available_for_future_helper": True,
    "dict_list_scalar_output_only": True,
    "computed_but_hidden_contract_candidate": True,
    "hidden_is_not_missing_contract": True,
    "occluded_is_not_source_lineage_loss_contract": True,
    "helper_creation_authorized": False,
    "checker_modification_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_core_change_authorized": False,
    "hidden_as_missing_authorized": False,
    "source_lineage_loss_interpretation_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "frame_truth_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "formula_movement_authorized": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_computed_but_hidden_minimal_extraction_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame computed-but-hidden minimal extraction planning gate. "
    "No helper creation, no render_core/dynamic_point_computed_but_hidden_boundary.py creation, "
    "no checker modification, no runtime probe change, no taichi_global_bathymetry change, "
    "no render_if_needed, no controller, no renderer, no frame buffer read, no artifact generation, "
    "no formula movement, no hidden-as-missing interpretation, no source-lineage-loss interpretation, "
    "no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, "
    "no RRKAL-wide methodology promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_computed_but_hidden_minimal_extraction_planning.v1",
    "evidence_sources": {
        "computed_but_hidden_import_boundary_checker": "ad48d63",
        "computed_but_hidden_import_boundary_checker_planning": "39bdb2c",
        "computed_but_hidden_contract_planning": "3c86eea",
        "post_presentation_count_next_bridge_selection": "d25e94c",
        "presentation_count_cartography_update": "a5fe556",
        "sampling_visibility_minimal_boundary": "76abda8",
        "occlusion_responsibility_boundary": "44356e9",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "runtime_executed_by_this_gate": False,
    },
    "future_helper_target": FUTURE_HELPER_TARGET,
    "required_checker": REQUIRED_CHECKER,
    "allowed_output_shape": ALLOWED_OUTPUT_SHAPE,
    "allowed_labels": ALLOWED_LABELS,
    "forbidden_fields": FORBIDDEN_FIELDS,
    "planned_helper_families": PLANNED_HELPER_FAMILIES,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointComputedButHiddenMinimalExtractionPlanningTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "future_helper_target",
                "required_checker",
                "allowed_output_shape",
                "allowed_labels",
                "forbidden_fields",
                "planned_helper_families",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_computed_but_hidden_minimal_extraction_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_future_helper_target_and_checker_are_defined_without_creation_authorization(self) -> None:
        self.assertEqual(PACKET["future_helper_target"], "render_core/dynamic_point_computed_but_hidden_boundary.py")
        self.assertEqual(PACKET["required_checker"], "scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py")
        self.assertFalse(PACKET["decision_output"]["helper_creation_authorized"])
        self.assertFalse(PACKET["decision_output"]["checker_modification_authorized"])
        self.assertFalse(PACKET["decision_output"]["render_core_change_authorized"])

    def test_allowed_output_shape_is_dict_list_scalar_only(self) -> None:
        shape = PACKET["allowed_output_shape"]
        self.assertTrue(shape["nested_dict"])
        self.assertTrue(shape["list"])
        self.assertTrue(shape["scalar"])
        self.assertFalse(shape["callable"])
        self.assertFalse(shape["runtime_object"])
        self.assertFalse(shape["dataframe"])
        self.assertFalse(shape["renderer_buffer"])

    def test_allowed_labels_are_exact(self) -> None:
        self.assertEqual(
            set(PACKET["allowed_labels"]),
            {
                "source_present_token",
                "computed_point_token",
                "hidden_visibility_token",
                "frame_visible_not_observed",
                "hidden_is_not_missing",
                "occluded_is_not_source_lineage_loss",
                "computed_but_hidden_contract",
                "transparent_globe_leak_not_inferred",
                "source_loss_not_inferred",
                "frame_buffer_read_blocked",
                "renderer_execution_blocked",
                "readiness_not_claimed",
            },
        )

    def test_forbidden_fields_are_exact(self) -> None:
        self.assertEqual(
            set(PACKET["forbidden_fields"]),
            {
                "runtime_probe",
                "render_if_needed",
                "controller_runtime",
                "renderer_runtime",
                "frame_buffer",
                "artifact_writer",
                "projection_formula",
                "mask_formula",
                "sampling_formula_movement",
                "alpha_compose_formula",
                "dataframe_runtime",
                "live_source",
                "cache_database_io",
                "hidden_as_missing_interpretation",
                "source_lineage_loss_interpretation",
                "transparent_globe_leak_inference",
                "coordinate_correctness_claim",
                "visual_parity_claim",
                "readiness_claim",
                "transparent_globe_leak_fix_claim",
            },
        )

    def test_planned_helper_families_are_complete(self) -> None:
        self.assertEqual(
            {row["helper_family"] for row in PACKET["planned_helper_families"]},
            {
                "build_dynamic_point_computed_but_hidden_contract_descriptor",
                "build_dynamic_point_hidden_visibility_contract_descriptor",
                "build_dynamic_point_computed_point_contract_descriptor",
                "build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor",
                "build_dynamic_point_computed_but_hidden_stop_line_ledger",
                "dynamic_point_computed_but_hidden_boundary_descriptor",
                "dynamic_point_computed_but_hidden_planning_bundle",
            },
        )

    def test_each_helper_family_has_required_planning_fields_and_blocks_runtime(self) -> None:
        required_keys = {
            "helper_family",
            "intended_output_keys",
            "allowed_labels",
            "forbidden_fields",
            "source_lineage_impact",
            "frame_renderer_dependency",
            "formula_dependency",
            "checker_coverage_expectation",
            "helper_creation_authorized",
        }
        allowed = set(PACKET["allowed_labels"])
        forbidden = set(PACKET["forbidden_fields"])
        for row in PACKET["planned_helper_families"]:
            self.assertEqual(set(row), required_keys)
            self.assertTrue(row["intended_output_keys"])
            self.assertTrue(set(row["allowed_labels"]).issubset(allowed))
            self.assertEqual(set(row["forbidden_fields"]), forbidden)
            self.assertIn("no", row["source_lineage_impact"])
            self.assertFalse(row["frame_renderer_dependency"])
            self.assertFalse(row["formula_dependency"])
            self.assertTrue(row["checker_coverage_expectation"])
            self.assertFalse(row["helper_creation_authorized"])

    def test_semantic_guard_helpers_are_planned(self) -> None:
        rows = {row["helper_family"]: row for row in PACKET["planned_helper_families"]}
        self.assertIn("hidden_is_not_missing", rows["build_dynamic_point_hidden_visibility_contract_descriptor"]["allowed_labels"])
        self.assertIn(
            "occluded_is_not_source_lineage_loss",
            rows["build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor"]["allowed_labels"],
        )
        self.assertIn(
            "transparent_globe_leak_not_inferred",
            rows["build_dynamic_point_computed_but_hidden_stop_line_ledger"]["allowed_labels"],
        )

    def test_decision_output_matches_required_non_authorizing_flags(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["minimal_extraction_planning_passed"])
        self.assertEqual(decision["future_helper_target"], FUTURE_HELPER_TARGET)
        self.assertTrue(decision["checker_available_for_future_helper"])
        self.assertTrue(decision["dict_list_scalar_output_only"])
        self.assertTrue(decision["computed_but_hidden_contract_candidate"])
        self.assertTrue(decision["hidden_is_not_missing_contract"])
        self.assertTrue(decision["occluded_is_not_source_lineage_loss_contract"])
        for key in (
            "helper_creation_authorized",
            "checker_modification_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_core_change_authorized",
            "hidden_as_missing_authorized",
            "source_lineage_loss_interpretation_authorized",
            "transparent_globe_leak_inference_authorized",
            "frame_truth_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "formula_movement_authorized",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_recommended_next_gate_is_minimal_extraction(self) -> None:
        self.assertEqual(
            PACKET["decision_output"]["recommended_next_gate"],
            "dynamic_point_lod_view_frame_computed_but_hidden_minimal_extraction_gate",
        )

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker modification", BOUNDARY_STATEMENT)
        self.assertIn("no frame buffer read", BOUNDARY_STATEMENT)
        self.assertIn("no hidden-as-missing interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no source-lineage-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no transparent-globe leak inference", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
