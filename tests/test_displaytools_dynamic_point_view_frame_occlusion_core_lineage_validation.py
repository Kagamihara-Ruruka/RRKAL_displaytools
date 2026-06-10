import unittest


REQUIRED_SURFACES = {
    "zoom_rotation_view_state",
    "lod_policy",
    "globe_angle_frame_state",
    "projection_shadow",
    "occlusion_policy",
    "presentation_policy",
    "source_lineage_integrity",
    "computed_but_hidden_point",
    "transparent_globe_leak_fault",
}

ALLOWED_SEMANTIC_CLASSIFICATIONS = {
    "core_lineage_view_frame_semantics",
    "core_interface_only",
    "presentation_policy_surface",
    "source_lineage_guard",
    "unresolved_static_fault",
    "runtime_characterization_candidate",
    "not_enough_evidence",
}

SURFACE_KEYS = {
    "surface",
    "observed_role",
    "historical_pressure",
    "dependency_pressure",
    "ablation_response",
    "semantic_classification",
    "recommended_strategy",
    "extraction_authorized",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "dynamic_point_lithology_l2_local_pattern_source",
    "projection_shadow_source",
    "projection_shadow_planning",
    "view_frame_occlusion_monkey_matrix",
    "creation_order_counterexample_source",
    "optional_history_query",
    "evidence_dimensions",
    "surface_classification_matrix",
    "decision_output",
    "boundary_statement",
}


def build_dynamic_point_view_frame_occlusion_core_lineage_validation_packet():
    surface_classification_matrix = [
        {
            "surface": "zoom_rotation_view_state",
            "observed_role": "viewer_state_changes_upstream_view_frame_and_lod_pressure",
            "historical_pressure": "view_camera_rotation_zoom_terms_present_in_static_monolith_and_canvas_evidence",
            "dependency_pressure": "adjacent_to_renderer_view_frame_and_projection_state",
            "ablation_response": "zoom_affects_lod_policy_and_rotation_affects_globe_angle_frame",
            "semantic_classification": "core_lineage_view_frame_semantics",
            "recommended_strategy": "shadow_interface_and_runtime_characterization_planning_only",
            "extraction_authorized": False,
        },
        {
            "surface": "lod_policy",
            "observed_role": "presentation_load_and_sampling_label_not_provider_lineage",
            "historical_pressure": "lod_level_scale_terms_exist_across_renderer_and_display_contract_surfaces",
            "dependency_pressure": "near_presentation_sampling_and_renderer_policy",
            "ablation_response": "lod_policy_affects_presentation_load_sampling_label_without_source_lineage_mutation",
            "semantic_classification": "presentation_policy_surface",
            "recommended_strategy": "runtime_characterization_candidate_without_runtime_authorization",
            "extraction_authorized": False,
        },
        {
            "surface": "globe_angle_frame_state",
            "observed_role": "view_frame_angle_upstream_of_occlusion_decision",
            "historical_pressure": "globe_angle_frame_view_camera_terms_align_with_early_world_frame_language",
            "dependency_pressure": "close_to_projection_frame_and_renderer_view_state",
            "ablation_response": "globe_angle_frame_affects_occlusion_decision",
            "semantic_classification": "core_lineage_view_frame_semantics",
            "recommended_strategy": "core_interface_shadow_not_formula_extraction",
            "extraction_authorized": False,
        },
        {
            "surface": "projection_shadow",
            "observed_role": "label_reference_ledger_boundary_for_projection_policy_refs",
            "historical_pressure": "projection_shadow_gate_classifies_projection_flip_mask_sync_as_core_interface_only",
            "dependency_pressure": "directly_adjacent_to_projection_flip_mask_formula_stop_lines",
            "ablation_response": "projection_shadow_allows_label_reference_ledger_only_and_blocks_formula",
            "semantic_classification": "core_interface_only",
            "recommended_strategy": "shadow_interface_only_with_checker_guard",
            "extraction_authorized": False,
        },
        {
            "surface": "occlusion_policy",
            "observed_role": "visibility_policy_for_hidden_or_visible_point_state",
            "historical_pressure": "visibility_hidden_occlusion_terms_align_with_view_frame_not_provider_lineage",
            "dependency_pressure": "between_globe_angle_projection_shadow_and_presentation",
            "ablation_response": "occlusion_affects_visibility_and_must_not_change_source_lineage",
            "semantic_classification": "runtime_characterization_candidate",
            "recommended_strategy": "runtime_characterization_planning_after_core_lineage_validation",
            "extraction_authorized": False,
        },
        {
            "surface": "presentation_policy",
            "observed_role": "rendered_visibility_and_presentation_label_surface",
            "historical_pressure": "presentation_rendered_visibility_terms_exist_in_renderer_contract_context",
            "dependency_pressure": "touches_renderer_presentation_without_provider_cache_database_authority",
            "ablation_response": "presentation_affects_rendered_visibility_not_provider_cache_database",
            "semantic_classification": "presentation_policy_surface",
            "recommended_strategy": "presentation_policy_characterization_without_runtime_merge",
            "extraction_authorized": False,
        },
        {
            "surface": "source_lineage_integrity",
            "observed_role": "guard_that_provider_lineage_survives_view_frame_and_occlusion_changes",
            "historical_pressure": "source_lineage_is_dynamic_point_data_axis_not_view_frame_law",
            "dependency_pressure": "separate_from_renderer_projection_and_occlusion_path",
            "ablation_response": "source_lineage_integrity_stable_under_lod_and_occlusion_labels",
            "semantic_classification": "source_lineage_guard",
            "recommended_strategy": "keep_guarded_against_lod_occlusion_mutation",
            "extraction_authorized": False,
        },
        {
            "surface": "computed_but_hidden_point",
            "observed_role": "point_computation_can_exist_while_current_presentation_hides_it",
            "historical_pressure": "computed_visibility_split_is_inferred_from_monkey_matrix_not_runtime_execution",
            "dependency_pressure": "bridges_source_identity_and_presentation_visibility",
            "ablation_response": "computed_existence_is_preserved_separately_from_hidden_visibility",
            "semantic_classification": "runtime_characterization_candidate",
            "recommended_strategy": "characterize_without_claiming_runtime_correctness",
            "extraction_authorized": False,
        },
        {
            "surface": "transparent_globe_leak_fault",
            "observed_role": "known_fault_label_for_backside_point_leak_through_globe",
            "historical_pressure": "fault_is_static_matrix_entry_not_verified_runtime_fix",
            "dependency_pressure": "touches_occlusion_projection_and_renderer_presentation_risk",
            "ablation_response": "leak_recorded_as_fault_not_fix",
            "semantic_classification": "unresolved_static_fault",
            "recommended_strategy": "record_fault_and_plan_observation_without_fix_claim",
            "extraction_authorized": False,
        },
    ]

    return {
        "schema": "rrkal.displaytools.dynamic_point_view_frame_occlusion_core_lineage_validation.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "dynamic_point_lithology_l2_local_pattern_source": "60cded8",
        "projection_shadow_source": "6289c60",
        "projection_shadow_planning": "a67a685",
        "view_frame_occlusion_monkey_matrix": "8b5cac7",
        "creation_order_counterexample_source": "53afb98",
        "optional_history_query": {
            "history_query_attempted": True,
            "history_query_limited": False,
            "history_query_interpretation": "history_terms_support_age_pressure_but_do_not_prove_lithology_alone",
            "runtime_execution_performed": False,
        },
        "evidence_dimensions": {
            "historical_age_pressure": {
                "summary": "rotation_zoom_lod_frame_angle_projection_mask_visibility_terms_are_not_unique_to_late_dynamic_point_descriptors",
                "supports_core_lineage": True,
                "evidence_limit": "static_history_and_scan_only",
            },
            "dependency_depth_pressure": {
                "summary": "chain_is_near_renderer_projection_frame_hot_path_and_presentation_surfaces",
                "supports_core_lineage": True,
                "evidence_limit": "no_runtime_or_formula_read",
            },
            "monkey_ablation_response": {
                "summary": "8b5cac7_separates_view_frame_lod_occlusion_presentation_from_source_lineage",
                "supports_core_lineage": True,
                "evidence_limit": "docs_test_only_matrix",
            },
            "semantic_reconstruction_pressure": {
                "summary": "dynamic_point_appears_to_attach_to_existing_view_frame_law_rather_than_owning_visibility_law",
                "supports_core_lineage": True,
                "evidence_limit": "hypothesis_supported_not_runtime_proven",
            },
        },
        "surface_classification_matrix": surface_classification_matrix,
        "decision_output": {
            "view_frame_occlusion_core_lineage_supported": True,
            "ordinary_helper_extraction_authorized": False,
            "shadow_interface_path_required": True,
            "runtime_characterization_candidate": True,
            "runtime_characterization_authorized": False,
            "formula_movement_authorized": False,
            "renderer_runtime_authorized": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "performance_claimed": False,
            "transparent_globe_leak_fix_claimed": False,
            "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point view-frame occlusion core-lineage validation gate. "
            "No helper module creation, no source movement, no production source change, no checker script change, "
            "no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, "
            "no monolith import, no runtime execution, no SQL/WebSocket/live-source execution, "
            "no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, "
            "no projection/flip/mask formula read/copy/movement/change, "
            "no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, "
            "no transparent-globe leak fix claim, no runtime characterization authorization, "
            "no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointViewFrameOcclusionCoreLineageValidationTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_view_frame_occlusion_core_lineage_validation_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_view_frame_occlusion_core_lineage_validation.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["dynamic_point_lithology_l2_local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["projection_shadow_source"], "6289c60")
        self.assertEqual(self.packet["projection_shadow_planning"], "a67a685")
        self.assertEqual(self.packet["view_frame_occlusion_monkey_matrix"], "8b5cac7")
        self.assertEqual(self.packet["creation_order_counterexample_source"], "53afb98")

    def test_optional_history_query_is_static_and_not_verdict(self):
        history = self.packet["optional_history_query"]
        self.assertTrue(history["history_query_attempted"])
        self.assertFalse(history["history_query_limited"])
        self.assertFalse(history["runtime_execution_performed"])
        self.assertIn("do_not_prove_lithology_alone", history["history_query_interpretation"])

    def test_required_evidence_dimensions_present(self):
        self.assertEqual(
            set(self.packet["evidence_dimensions"]),
            {
                "historical_age_pressure",
                "dependency_depth_pressure",
                "monkey_ablation_response",
                "semantic_reconstruction_pressure",
            },
        )
        for dimension in self.packet["evidence_dimensions"].values():
            self.assertTrue(dimension["supports_core_lineage"])
            self.assertTrue(dimension["summary"])
            self.assertTrue(dimension["evidence_limit"])

    def test_required_surfaces_classified_with_allowed_labels(self):
        rows = {row["surface"]: row for row in self.packet["surface_classification_matrix"]}
        self.assertEqual(set(rows), REQUIRED_SURFACES)
        for row in rows.values():
            self.assertEqual(set(row), SURFACE_KEYS)
            self.assertIn(row["semantic_classification"], ALLOWED_SEMANTIC_CLASSIFICATIONS)
            self.assertFalse(row["extraction_authorized"])
            self.assertTrue(row["recommended_strategy"])

    def test_expected_surface_classifications(self):
        rows = {row["surface"]: row for row in self.packet["surface_classification_matrix"]}
        self.assertEqual(rows["zoom_rotation_view_state"]["semantic_classification"], "core_lineage_view_frame_semantics")
        self.assertEqual(rows["globe_angle_frame_state"]["semantic_classification"], "core_lineage_view_frame_semantics")
        self.assertEqual(rows["projection_shadow"]["semantic_classification"], "core_interface_only")
        self.assertEqual(rows["lod_policy"]["semantic_classification"], "presentation_policy_surface")
        self.assertEqual(rows["presentation_policy"]["semantic_classification"], "presentation_policy_surface")
        self.assertEqual(rows["source_lineage_integrity"]["semantic_classification"], "source_lineage_guard")
        self.assertEqual(rows["computed_but_hidden_point"]["semantic_classification"], "runtime_characterization_candidate")
        self.assertEqual(rows["transparent_globe_leak_fault"]["semantic_classification"], "unresolved_static_fault")

    def test_decision_output_supports_core_lineage_but_blocks_extraction(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["view_frame_occlusion_core_lineage_supported"])
        self.assertFalse(decision["ordinary_helper_extraction_authorized"])
        self.assertTrue(decision["shadow_interface_path_required"])
        self.assertTrue(decision["runtime_characterization_candidate"])
        self.assertFalse(decision["runtime_characterization_authorized"])
        self.assertFalse(decision["formula_movement_authorized"])
        self.assertFalse(decision["renderer_runtime_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["performance_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        )

    def test_transparent_globe_fault_is_not_fix_claim(self):
        row = {
            item["surface"]: item for item in self.packet["surface_classification_matrix"]
        }["transparent_globe_leak_fault"]
        self.assertEqual(row["semantic_classification"], "unresolved_static_fault")
        self.assertIn("without_fix_claim", row["recommended_strategy"])
        self.assertFalse(self.packet["decision_output"]["transparent_globe_leak_fix_claimed"])

    def test_boundary_statement_contains_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no performance claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no runtime characterization authorization", boundary)


if __name__ == "__main__":
    unittest.main()
