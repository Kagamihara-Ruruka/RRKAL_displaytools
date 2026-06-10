"""Planning gate for dynamic point source-lineage guard import-boundary checker."""

from __future__ import annotations

import unittest

from tests import test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning as contract_planning
from tests import test_displaytools_dynamic_point_post_computed_but_hidden_next_bridge_selection as bridge_selection


FUTURE_HELPER_TARGET = "render_core/dynamic_point_source_lineage_guard_boundary.py"
FUTURE_CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py"

ALLOWED_STRING_LABELS = [
    "source_present_token",
    "source_label",
    "point_id",
    "source_lineage_integrity_token",
    "payload_identity_guard",
    "sampling_does_not_mutate_source",
    "presentation_count_does_not_mutate_source",
    "hidden_visibility_does_not_mutate_source",
    "mask_visibility_does_not_mutate_source",
    "occlusion_visibility_does_not_mutate_source",
    "reduced_count_is_not_source_loss",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "controlled_raw_row_compatibility_seam",
    "developmental_compensation_surface",
    "future_c4_odoriba_handoff_material",
    "direct_c1_integration_not_authorized",
]

FORBIDDEN_FAMILIES = [
    "monolith",
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
    "real_ais_adsb_source",
    "source_lineage_mutation",
    "hidden_as_missing_interpretation",
    "reduced_count_as_source_loss_interpretation",
    "occluded_as_source_loss_interpretation",
    "direct_c1_integration",
    "c4_odoriba_bypass",
    "transparent_globe_leak_inference",
    "correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "transparent_globe_leak_fix_claim",
    "label_executable_reference",
]

CHECKER_EXPECTATION = {
    "ast_only": True,
    "target_imported": False,
    "target_executed": False,
    "missing_target_passes": True,
    "missing_target_status": "not_applicable_candidate_missing",
    "syntax_error_json_fail": True,
    "inspected_ast_nodes": [
        "ast.Import",
        "ast.ImportFrom",
        "ast.Name",
        "ast.Attribute",
        "ast.Call",
        "ast.FunctionDef",
        "ast.AsyncFunctionDef",
        "ast.ClassDef",
    ],
    "allowed_labels_pass_only_as_data_strings": True,
    "executable_references_must_fail": True,
    "negative_self_test_covers_all_forbidden_families": True,
}

RAW_ROW_COMPATIBILITY_SEAM_TREATMENT = {
    "controlled_raw_row_compatibility_seam_recognized": True,
    "classification": "transitional_c3_developmental_compensation_surface",
    "may_exist_as_transitional_c3_surface": True,
    "raw_row_compatibility_seam_must_not_mutate_source_identity": True,
    "raw_row_compatibility_seam_must_not_become_direct_c1_integration": True,
    "raw_row_compatibility_seam_remains_future_c4_odoriba_handoff_material": True,
    "direct_c1_integration_authorized": False,
    "c4_odoriba_mediation_required_for_future_cross_organ_integration": True,
    "mature_architecture_claimed": False,
}

DECISION_OUTPUT = {
    "source_lineage_guard_checker_planning_passed": True,
    "dedicated_checker_required": True,
    "existing_checker_reusable": False,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "runtime_execution_authorized": False,
    "source_lineage_mutation_authorized": False,
    "controlled_raw_row_compatibility_seam_recognized": True,
    "direct_c1_integration_authorized": False,
    "c4_odoriba_mediation_required_for_future_cross_organ_integration": True,
    "transparent_globe_leak_inferred": False,
    "dependency_cycle_watch_enabled": True,
    "render_core_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "real_source_read_authorized": False,
    "hidden_as_missing_interpretation_authorized": False,
    "reduced_count_as_source_loss_interpretation_authorized": False,
    "occluded_as_source_loss_interpretation_authorized": False,
    "raw_row_compatibility_seam_promoted_to_mature_c1_integration": False,
    "direct_c3_to_c1_dependency_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_gate",
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame source-lineage guard import-boundary checker planning gate. "
    "No checker creation, no helper creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry.py change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/"
    "WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, "
    "no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, "
    "no raw-row compatibility seam promotion to mature c_1 integration, no direct c_3-to-c_1 "
    "dependency authorization, no c_4/Odoriba bypass, no transparent-globe leak inference, "
    "no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide "
    "methodology promotion, and no push."
)

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning.v1",
    "evidence_sources": {
        "source_lineage_guard_contract_planning": "f87d93c",
        "post_computed_but_hidden_next_bridge_selection": "27d6980",
        "post_computed_but_hidden_cartography_update": "a357bbe",
        "computed_but_hidden_boundary": "b7b11a5",
        "presentation_count_boundary": "d25e94c_lineage",
        "sampling_visibility_boundary": "76abda8_lineage",
        "occlusion_responsibility_boundary": "44356e9",
        "grafting_path_minimal_evidence": "87cb579",
        "previous_import_boundary_checker_patterns": "computed_but_hidden_and_presentation_count_checkers",
        "runtime_executed_by_this_gate": False,
    },
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "allowed_string_labels": ALLOWED_STRING_LABELS,
    "forbidden_families": FORBIDDEN_FAMILIES,
    "checker_expectation": CHECKER_EXPECTATION,
    "raw_row_compatibility_seam_treatment": RAW_ROW_COMPATIBILITY_SEAM_TREATMENT,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSourceLineageGuardImportBoundaryCheckerPlanningTest(unittest.TestCase):
    def test_packet_schema_and_evidence(self) -> None:
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])
        self.assertEqual(
            bridge_selection.PACKET["decision_output"]["selected_next_bridge_candidate"],
            "source_lineage_guard_contract",
        )
        self.assertTrue(
            contract_planning.PACKET["decision_output"]["source_lineage_guard_contract_planning_passed"]
        )

    def test_future_targets_are_planned_only(self) -> None:
        self.assertEqual(PACKET["future_helper_target"], FUTURE_HELPER_TARGET)
        self.assertEqual(PACKET["future_checker_target"], FUTURE_CHECKER_TARGET)
        self.assertFalse(PACKET["decision_output"]["helper_creation_authorized"])
        self.assertFalse(PACKET["decision_output"]["checker_creation_authorized"])

    def test_allowed_string_labels_are_exact(self) -> None:
        self.assertEqual(
            PACKET["allowed_string_labels"],
            [
                "source_present_token",
                "source_label",
                "point_id",
                "source_lineage_integrity_token",
                "payload_identity_guard",
                "sampling_does_not_mutate_source",
                "presentation_count_does_not_mutate_source",
                "hidden_visibility_does_not_mutate_source",
                "mask_visibility_does_not_mutate_source",
                "occlusion_visibility_does_not_mutate_source",
                "reduced_count_is_not_source_loss",
                "hidden_is_not_missing",
                "occluded_is_not_source_lineage_loss",
                "controlled_raw_row_compatibility_seam",
                "developmental_compensation_surface",
                "future_c4_odoriba_handoff_material",
                "direct_c1_integration_not_authorized",
            ],
        )

    def test_forbidden_families_are_exact(self) -> None:
        self.assertEqual(
            PACKET["forbidden_families"],
            [
                "monolith",
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
                "real_ais_adsb_source",
                "source_lineage_mutation",
                "hidden_as_missing_interpretation",
                "reduced_count_as_source_loss_interpretation",
                "occluded_as_source_loss_interpretation",
                "direct_c1_integration",
                "c4_odoriba_bypass",
                "transparent_globe_leak_inference",
                "correctness_claim",
                "visual_parity_claim",
                "readiness_claim",
                "transparent_globe_leak_fix_claim",
                "label_executable_reference",
            ],
        )

    def test_checker_expectation(self) -> None:
        expectation = PACKET["checker_expectation"]
        self.assertTrue(expectation["ast_only"])
        self.assertFalse(expectation["target_imported"])
        self.assertFalse(expectation["target_executed"])
        self.assertTrue(expectation["missing_target_passes"])
        self.assertEqual(expectation["missing_target_status"], "not_applicable_candidate_missing")
        self.assertTrue(expectation["syntax_error_json_fail"])
        self.assertEqual(
            expectation["inspected_ast_nodes"],
            [
                "ast.Import",
                "ast.ImportFrom",
                "ast.Name",
                "ast.Attribute",
                "ast.Call",
                "ast.FunctionDef",
                "ast.AsyncFunctionDef",
                "ast.ClassDef",
            ],
        )
        self.assertTrue(expectation["allowed_labels_pass_only_as_data_strings"])
        self.assertTrue(expectation["executable_references_must_fail"])
        self.assertTrue(expectation["negative_self_test_covers_all_forbidden_families"])

    def test_controlled_raw_row_compatibility_seam_treatment(self) -> None:
        seam = PACKET["raw_row_compatibility_seam_treatment"]
        self.assertTrue(seam["controlled_raw_row_compatibility_seam_recognized"])
        self.assertEqual(seam["classification"], "transitional_c3_developmental_compensation_surface")
        self.assertTrue(seam["may_exist_as_transitional_c3_surface"])
        self.assertTrue(seam["raw_row_compatibility_seam_must_not_mutate_source_identity"])
        self.assertTrue(seam["raw_row_compatibility_seam_must_not_become_direct_c1_integration"])
        self.assertTrue(seam["raw_row_compatibility_seam_remains_future_c4_odoriba_handoff_material"])
        self.assertFalse(seam["direct_c1_integration_authorized"])
        self.assertTrue(seam["c4_odoriba_mediation_required_for_future_cross_organ_integration"])
        self.assertFalse(seam["mature_architecture_claimed"])

    def test_decision_output_required_flags(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["source_lineage_guard_checker_planning_passed"])
        self.assertTrue(decision["dedicated_checker_required"])
        self.assertFalse(decision["existing_checker_reusable"])
        self.assertFalse(decision["helper_creation_authorized"])
        self.assertFalse(decision["checker_creation_authorized"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["source_lineage_mutation_authorized"])
        self.assertTrue(decision["controlled_raw_row_compatibility_seam_recognized"])
        self.assertFalse(decision["direct_c1_integration_authorized"])
        self.assertTrue(decision["c4_odoriba_mediation_required_for_future_cross_organ_integration"])
        self.assertFalse(decision["transparent_globe_leak_inferred"])
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_gate",
        )

    def test_decision_output_blocks_runtime_claim_and_cross_organ_shortcuts(self) -> None:
        decision = PACKET["decision_output"]
        for key in (
            "render_core_change_authorized",
            "runtime_probe_change_authorized",
            "taichi_global_bathymetry_change_authorized",
            "render_if_needed_authorized",
            "controller_renderer_frame_buffer_authorized",
            "artifact_generation_authorized",
            "formula_movement_authorized",
            "real_source_read_authorized",
            "hidden_as_missing_interpretation_authorized",
            "reduced_count_as_source_loss_interpretation_authorized",
            "occluded_as_source_loss_interpretation_authorized",
            "raw_row_compatibility_seam_promoted_to_mature_c1_integration",
            "direct_c3_to_c1_dependency_authorized",
            "c4_odoriba_bypass_authorized",
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_boundary_statement(self) -> None:
        self.assertIn("No checker creation", BOUNDARY_STATEMENT)
        self.assertIn("no helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no real AIS/ADS-B/SQL/WebSocket/cache/database read", BOUNDARY_STATEMENT)
        self.assertIn("no source-lineage mutation", BOUNDARY_STATEMENT)
        self.assertIn("no hidden-as-missing interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no reduced-count-as-source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no occluded-as-source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no raw-row compatibility seam promotion", BOUNDARY_STATEMENT)
        self.assertIn("no direct c_3-to-c_1 dependency authorization", BOUNDARY_STATEMENT)
        self.assertIn("no c_4/Odoriba bypass", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
