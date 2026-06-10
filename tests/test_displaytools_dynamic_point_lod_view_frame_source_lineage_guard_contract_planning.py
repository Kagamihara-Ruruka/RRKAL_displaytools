"""Planning gate for dynamic point source-lineage guard contract."""

from __future__ import annotations

import unittest

from tests import test_displaytools_dynamic_point_post_computed_but_hidden_next_bridge_selection as selection


FUTURE_HELPER_TARGET = "render_core/dynamic_point_source_lineage_guard_boundary.py"
FUTURE_CHECKER_TARGET = "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py"

PLANNED_HELPER_FAMILIES = [
    "build_dynamic_point_source_identity_contract_descriptor",
    "build_dynamic_point_source_lineage_integrity_descriptor",
    "build_dynamic_point_sampling_source_guard_descriptor",
    "build_dynamic_point_presentation_count_source_guard_descriptor",
    "build_dynamic_point_hidden_visibility_source_guard_descriptor",
    "build_dynamic_point_mask_occlusion_source_guard_descriptor",
    "build_dynamic_point_source_lineage_guard_stop_line_ledger",
    "dynamic_point_source_lineage_guard_boundary_descriptor",
    "dynamic_point_source_lineage_guard_planning_bundle",
]

GUARD_SURFACES = [
    {
        "surface": "source_present_token",
        "contract_role": "source_presence_contract_label",
        "evidence_refs": ["computed_but_hidden_boundary", "runtime_probe_result_interpretation"],
        "allowed_state": "may_be_true_before_visibility_or_presentation_judgement",
        "forbidden_interpretation": "source_present_token_is_not_frame_visibility_truth",
        "protected_existing_surface": ["computed_but_hidden_boundary"],
        "dependency_cycle_risk": "low_primary_anchor",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_source_identity_contract_descriptor",
        "checker_need": "future_source_lineage_guard_import_boundary_checker",
        "stop_condition": "stop if source presence is treated as visual correctness",
    },
    {
        "surface": "source_label",
        "contract_role": "source_identity_label",
        "evidence_refs": ["grafting_path_minimal_evidence", "one_shot_runtime_probe_output_interpretation"],
        "allowed_state": "synthetic_or_declared_label_only",
        "forbidden_interpretation": "source_label_must_not_trigger_real_source_read",
        "protected_existing_surface": ["sampling_visibility_boundary", "computed_but_hidden_boundary"],
        "dependency_cycle_risk": "medium_near_provider_lineage",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_source_identity_contract_descriptor",
        "checker_need": "future_checker_must_block_live_source_and_cache_io",
        "stop_condition": "stop if real AIS ADS-B SQL WebSocket cache or DB read is required",
    },
    {
        "surface": "point_id",
        "contract_role": "stable_payload_identity_label",
        "evidence_refs": ["one_shot_runtime_probe_output_interpretation", "computed_but_hidden_boundary"],
        "allowed_state": "identity_marker_only",
        "forbidden_interpretation": "point_id_is_not_coordinate_correctness",
        "protected_existing_surface": ["computed_but_hidden_boundary", "sampling_visibility_boundary"],
        "dependency_cycle_risk": "medium_identity_shared_by_multiple_contracts",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_source_identity_contract_descriptor",
        "checker_need": "future_checker_must_allow_string_labels_only",
        "stop_condition": "stop if point identity requires runtime id trace or source mutation",
    },
    {
        "surface": "source_lineage_integrity_token",
        "contract_role": "lineage_integrity_guard_token",
        "evidence_refs": ["sampling_visibility_boundary", "presentation_count_boundary", "computed_but_hidden_boundary"],
        "allowed_state": "guard_true_when_visibility_contracts_do_not_mutate_source",
        "forbidden_interpretation": "visibility_state_cannot_rewrite_source_lineage",
        "protected_existing_surface": [
            "sampling_visibility_boundary",
            "presentation_count_boundary",
            "computed_but_hidden_boundary",
        ],
        "dependency_cycle_risk": "reduces_cycle_risk_across_extracted_surfaces",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_source_lineage_integrity_descriptor",
        "checker_need": "future_checker_must_block_source_lineage_mutation",
        "stop_condition": "stop if any protected surface is allowed to mutate lineage",
    },
    {
        "surface": "payload_identity_guard",
        "contract_role": "payload_identity_guard_contract",
        "evidence_refs": ["grafting_path_minimal_evidence", "one_shot_runtime_probe_output_interpretation"],
        "allowed_state": "descriptor_guard_for_payload_identity",
        "forbidden_interpretation": "payload_guard_is_not_schema_or_runtime_readiness",
        "protected_existing_surface": ["source_lineage_guard_contract"],
        "dependency_cycle_risk": "medium_payload_identity_touches_multiple_surfaces",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_source_identity_contract_descriptor",
        "checker_need": "future_checker_must_block_runtime_probe_and_dataframe_runtime",
        "stop_condition": "stop if payload guard needs runtime object or dataframe",
    },
    {
        "surface": "sampling_does_not_mutate_source",
        "contract_role": "sampling_source_guard",
        "evidence_refs": ["sampling_visibility_boundary", "sampling_visibility_runtime_probe_result_interpretation"],
        "allowed_state": "sampled_or_unsampled_is_visibility_sampling_state_only",
        "forbidden_interpretation": "sampled_false_is_not_missing_source",
        "protected_existing_surface": ["sampling_visibility_boundary"],
        "dependency_cycle_risk": "medium_sampling_visibility_overlap",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_sampling_source_guard_descriptor",
        "checker_need": "future_checker_must_block_sampling_formula_movement",
        "stop_condition": "stop if sampling formula movement or source deletion is required",
    },
    {
        "surface": "presentation_count_does_not_mutate_source",
        "contract_role": "presentation_count_source_guard",
        "evidence_refs": ["presentation_count_boundary", "sampling_visibility_boundary"],
        "allowed_state": "visible_or_rendered_count_is_count_contract_only",
        "forbidden_interpretation": "rendered_count_lower_than_visible_is_not_source_loss",
        "protected_existing_surface": ["presentation_count_boundary"],
        "dependency_cycle_risk": "low_already_cooled_count_contract",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_presentation_count_source_guard_descriptor",
        "checker_need": "future_checker_must_block_reduced_count_as_source_loss",
        "stop_condition": "stop if reduced count is treated as source loss",
    },
    {
        "surface": "hidden_visibility_does_not_mutate_source",
        "contract_role": "hidden_visibility_source_guard",
        "evidence_refs": ["computed_but_hidden_boundary"],
        "allowed_state": "hidden_is_visibility_or_presentation_hidden_only",
        "forbidden_interpretation": "hidden_is_not_missing",
        "protected_existing_surface": ["computed_but_hidden_boundary"],
        "dependency_cycle_risk": "medium_hidden_contract_depends_on_lineage_guard",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_hidden_visibility_source_guard_descriptor",
        "checker_need": "future_checker_must_block_hidden_as_missing",
        "stop_condition": "stop if hidden is treated as missing",
    },
    {
        "surface": "mask_visibility_does_not_mutate_source",
        "contract_role": "mask_visibility_source_guard",
        "evidence_refs": ["sampling_visibility_boundary", "occlusion_responsibility_boundary"],
        "allowed_state": "mask_visible_or_hidden_is_occlusion_visibility_state_only",
        "forbidden_interpretation": "mask_hidden_is_not_source_deletion",
        "protected_existing_surface": ["sampling_visibility_boundary", "future_mask_visibility_contract"],
        "dependency_cycle_risk": "medium_mask_occlusion_overlap",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_mask_occlusion_source_guard_descriptor",
        "checker_need": "future_checker_must_block_mask_formula_movement",
        "stop_condition": "stop if mask formula call or source deletion is required",
    },
    {
        "surface": "occlusion_visibility_does_not_mutate_source",
        "contract_role": "occlusion_source_guard",
        "evidence_refs": ["occlusion_responsibility_boundary", "computed_but_hidden_boundary"],
        "allowed_state": "occlusion_can_hide_without_deleting_source_identity",
        "forbidden_interpretation": "occluded_as_source_lineage_loss",
        "protected_existing_surface": ["computed_but_hidden_boundary", "future_occlusion_responsibility_contract"],
        "dependency_cycle_risk": "medium_occlusion_hidden_overlap",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_mask_occlusion_source_guard_descriptor",
        "checker_need": "future_checker_must_block_occluded_as_source_loss",
        "stop_condition": "stop if occlusion is treated as lineage loss",
    },
    {
        "surface": "reduced_count_is_not_source_loss",
        "contract_role": "reduction_source_loss_guard",
        "evidence_refs": ["presentation_count_boundary", "sampling_visibility_runtime_probe_result_interpretation"],
        "allowed_state": "reduced_count_is_sampling_or_presentation_reduction_candidate",
        "forbidden_interpretation": "reduced_count_as_source_loss",
        "protected_existing_surface": ["presentation_count_boundary"],
        "dependency_cycle_risk": "low_count_contract_guard",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_presentation_count_source_guard_descriptor",
        "checker_need": "future_checker_must_block_reduced_count_as_source_loss",
        "stop_condition": "stop if count reduction becomes source loss",
    },
    {
        "surface": "hidden_is_not_missing",
        "contract_role": "hidden_missing_guard",
        "evidence_refs": ["computed_but_hidden_boundary", "occlusion_responsibility_boundary"],
        "allowed_state": "hidden_state_remains_visibility_or_presentation_state",
        "forbidden_interpretation": "hidden_as_missing_interpretation",
        "protected_existing_surface": ["computed_but_hidden_boundary"],
        "dependency_cycle_risk": "medium_shared_with_computed_hidden_contract",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_hidden_visibility_source_guard_descriptor",
        "checker_need": "future_checker_must_block_hidden_as_missing",
        "stop_condition": "stop if hidden is treated as missing",
    },
    {
        "surface": "occluded_is_not_source_lineage_loss",
        "contract_role": "occluded_lineage_loss_guard",
        "evidence_refs": ["computed_but_hidden_boundary", "occlusion_responsibility_boundary"],
        "allowed_state": "occluded_state_remains_visibility_or_mask_state",
        "forbidden_interpretation": "occluded_as_source_lineage_loss",
        "protected_existing_surface": ["computed_but_hidden_boundary", "occlusion_responsibility_contract"],
        "dependency_cycle_risk": "medium_shared_with_occlusion_contract",
        "runtime_dependency": False,
        "frame_renderer_dependency": False,
        "formula_dependency": False,
        "helper_candidate": "build_dynamic_point_mask_occlusion_source_guard_descriptor",
        "checker_need": "future_checker_must_block_source_lineage_loss_interpretation",
        "stop_condition": "stop if occluded is treated as lineage loss",
    },
]


DECISION_OUTPUT = {
    "source_lineage_guard_contract_planning_passed": True,
    "source_lineage_guard_helper_candidate_supported": True,
    "descriptor_contract_ledger_candidate": True,
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "helper_creation_authorized": False,
    "checker_creation_authorized": False,
    "runtime_execution_authorized": False,
    "source_lineage_mutation_authorized": False,
    "hidden_as_missing_authorized": False,
    "reduced_count_as_source_loss_authorized": False,
    "occluded_as_source_loss_authorized": False,
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
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning_gate",
}


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame source-lineage guard contract planning gate. "
    "No helper creation, no checker creation, no render_core change, no runtime probe change, "
    "no taichi_global_bathymetry.py change, no render_if_needed, no controller, no renderer, "
    "no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/"
    "WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, "
    "no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, "
    "no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, "
    "no leak-fix claim, no RRKAL-wide methodology promotion, and no push."
)


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_source_lineage_guard_contract_planning.v1",
    "evidence_sources": {
        "post_computed_but_hidden_next_bridge_selection": "27d6980",
        "post_computed_but_hidden_cartography_update": "a357bbe",
        "computed_but_hidden_boundary": "b7b11a5",
        "presentation_count_boundary": "d25e94c_lineage",
        "sampling_visibility_boundary": "76abda8_lineage",
        "grafting_path_minimal_evidence": "87cb579",
        "occlusion_responsibility_boundary": "44356e9",
        "sampling_visibility_runtime_probe_result_interpretation": "5503eb0",
        "one_shot_runtime_probe_output_interpretation": "4b55302",
        "runtime_executed_by_this_gate": False,
    },
    "future_helper_target": FUTURE_HELPER_TARGET,
    "future_checker_target": FUTURE_CHECKER_TARGET,
    "planned_helper_families": PLANNED_HELPER_FAMILIES,
    "guard_surface_matrix": GUARD_SURFACES,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointSourceLineageGuardContractPlanningTest(unittest.TestCase):
    def test_packet_shape_and_schema(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "future_helper_target",
                "future_checker_target",
                "planned_helper_families",
                "guard_surface_matrix",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_source_lineage_guard_contract_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_previous_selection_chose_source_lineage_guard(self) -> None:
        self.assertEqual(
            selection.PACKET["decision_output"]["selected_next_bridge_candidate"],
            "source_lineage_guard_contract",
        )
        self.assertTrue(selection.PACKET["decision_output"]["dependency_cycle_watch_enabled"])

    def test_future_targets_are_planned_only(self) -> None:
        self.assertEqual(PACKET["future_helper_target"], "render_core/dynamic_point_source_lineage_guard_boundary.py")
        self.assertEqual(
            PACKET["future_checker_target"],
            "scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py",
        )
        self.assertFalse(PACKET["decision_output"]["helper_creation_authorized"])
        self.assertFalse(PACKET["decision_output"]["checker_creation_authorized"])

    def test_planned_helper_families(self) -> None:
        self.assertEqual(
            PACKET["planned_helper_families"],
            [
                "build_dynamic_point_source_identity_contract_descriptor",
                "build_dynamic_point_source_lineage_integrity_descriptor",
                "build_dynamic_point_sampling_source_guard_descriptor",
                "build_dynamic_point_presentation_count_source_guard_descriptor",
                "build_dynamic_point_hidden_visibility_source_guard_descriptor",
                "build_dynamic_point_mask_occlusion_source_guard_descriptor",
                "build_dynamic_point_source_lineage_guard_stop_line_ledger",
                "dynamic_point_source_lineage_guard_boundary_descriptor",
                "dynamic_point_source_lineage_guard_planning_bundle",
            ],
        )

    def test_guard_surfaces_are_complete_and_have_required_fields(self) -> None:
        rows = {row["surface"]: row for row in PACKET["guard_surface_matrix"]}
        self.assertEqual(
            set(rows),
            {
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
            },
        )
        required = {
            "surface",
            "contract_role",
            "evidence_refs",
            "allowed_state",
            "forbidden_interpretation",
            "protected_existing_surface",
            "dependency_cycle_risk",
            "runtime_dependency",
            "frame_renderer_dependency",
            "formula_dependency",
            "helper_candidate",
            "checker_need",
            "stop_condition",
        }
        for row in rows.values():
            self.assertEqual(set(row), required)
            self.assertTrue(row["evidence_refs"])
            self.assertTrue(row["protected_existing_surface"])
            self.assertFalse(row["runtime_dependency"])
            self.assertFalse(row["frame_renderer_dependency"])
            self.assertFalse(row["formula_dependency"])

    def test_guard_surfaces_protect_existing_extracted_surfaces(self) -> None:
        rows = {row["surface"]: row for row in PACKET["guard_surface_matrix"]}
        self.assertIn("sampling_visibility_boundary", rows["source_lineage_integrity_token"]["protected_existing_surface"])
        self.assertIn("presentation_count_boundary", rows["source_lineage_integrity_token"]["protected_existing_surface"])
        self.assertIn("computed_but_hidden_boundary", rows["source_lineage_integrity_token"]["protected_existing_surface"])
        self.assertIn("sampling_visibility_boundary", rows["sampling_does_not_mutate_source"]["protected_existing_surface"])
        self.assertIn("presentation_count_boundary", rows["presentation_count_does_not_mutate_source"]["protected_existing_surface"])
        self.assertIn("computed_but_hidden_boundary", rows["hidden_visibility_does_not_mutate_source"]["protected_existing_surface"])

    def test_forbidden_interpretations_are_explicit(self) -> None:
        rows = {row["surface"]: row for row in PACKET["guard_surface_matrix"]}
        self.assertEqual(rows["hidden_is_not_missing"]["forbidden_interpretation"], "hidden_as_missing_interpretation")
        self.assertEqual(rows["occluded_is_not_source_lineage_loss"]["forbidden_interpretation"], "occluded_as_source_lineage_loss")
        self.assertEqual(
            rows["presentation_count_does_not_mutate_source"]["forbidden_interpretation"],
            "rendered_count_lower_than_visible_is_not_source_loss",
        )
        self.assertEqual(rows["mask_visibility_does_not_mutate_source"]["forbidden_interpretation"], "mask_hidden_is_not_source_deletion")

    def test_dependency_cycle_watch_focuses_on_cross_surface_guard(self) -> None:
        rows = {row["surface"]: row for row in PACKET["guard_surface_matrix"]}
        self.assertEqual(
            rows["source_lineage_integrity_token"]["dependency_cycle_risk"],
            "reduces_cycle_risk_across_extracted_surfaces",
        )
        self.assertIn("overlap", rows["mask_visibility_does_not_mutate_source"]["dependency_cycle_risk"])
        self.assertIn("overlap", rows["occlusion_visibility_does_not_mutate_source"]["dependency_cycle_risk"])
        self.assertTrue(PACKET["decision_output"]["dependency_cycle_watch_enabled"])

    def test_decision_output_required_flags(self) -> None:
        decision = PACKET["decision_output"]
        self.assertTrue(decision["source_lineage_guard_contract_planning_passed"])
        self.assertTrue(decision["source_lineage_guard_helper_candidate_supported"])
        self.assertTrue(decision["descriptor_contract_ledger_candidate"])
        self.assertFalse(decision["helper_creation_authorized"])
        self.assertFalse(decision["checker_creation_authorized"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["source_lineage_mutation_authorized"])
        self.assertFalse(decision["hidden_as_missing_authorized"])
        self.assertFalse(decision["reduced_count_as_source_loss_authorized"])
        self.assertFalse(decision["occluded_as_source_loss_authorized"])
        self.assertFalse(decision["transparent_globe_leak_inferred"])
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning_gate",
        )

    def test_decision_output_blocks_all_forbidden_runtime_and_claim_surfaces(self) -> None:
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
            "coordinate_correctness_claimed",
            "visual_parity_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertIs(decision[key], False, key)

    def test_boundary_statement(self) -> None:
        self.assertIn("No helper creation", BOUNDARY_STATEMENT)
        self.assertIn("no checker creation", BOUNDARY_STATEMENT)
        self.assertIn("no real AIS/ADS-B/SQL/WebSocket/cache/database read", BOUNDARY_STATEMENT)
        self.assertIn("no source-lineage mutation", BOUNDARY_STATEMENT)
        self.assertIn("no hidden-as-missing interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no reduced-count-as-source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no occluded-as-source-loss interpretation", BOUNDARY_STATEMENT)
        self.assertIn("no RRKAL-wide methodology promotion", BOUNDARY_STATEMENT)
        self.assertIn("no push", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
