
import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame runtime probe authorization review gate. "
    "No helper module creation, no source movement, no production source change, no checker script change, "
    "no probe harness creation, no monolith import, no runtime execution, no runtime probe execution, "
    "no instrumentation, no monkey patch implementation, no __getattribute__ implementation, no sys.settrace, "
    "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
    "no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, "
    "no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, "
    "no renderer behavior change, no compose order change, no metadata/output schema change, "
    "no coordinate/visual correctness claim, no transparent-globe leak fix claim, "
    "no runtime characterization execution authorization, no global methodology promotion, "
    "no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
)


AUTHORIZATION_PREREQUISITE_PACKET = {
    "planning_gate_available": True,
    "representative_slice_strategy_available": True,
    "entrypoint_matrix_available": True,
    "monkey_condition_matrix_available": True,
    "contrast_token_matrix_available": True,
    "oracle_rules_available": True,
    "occlusion_responsibility_boundary_available": True,
    "grafting_path_minimal_evidence_available": True,
    "early_runtime_pipeline_characterization_available": True,
    "authorization_review_passed": True,
}


ENTRYPOINT_AUTHORIZATION_MATRIX = [
    {
        "entrypoint": "render_if_needed",
        "entrypoint_exists_in_evidence": True,
        "probe_scope": "current_21k_one_shot_synthetic_render_path_design",
        "synthetic_payload_possible": True,
        "one_shot_possible": True,
        "formula_mutation_required": False,
        "renderer_behavior_mutation_required": False,
        "source_lineage_mutation_required": False,
        "persistent_artifact_required": False,
        "authorization_recommendation": "candidate_for_future_probe_design",
    },
    {
        "entrypoint": "project_ais_to_screen",
        "entrypoint_exists_in_evidence": True,
        "probe_scope": "projection_horizon_and_screen_bounds_design",
        "synthetic_payload_possible": True,
        "one_shot_possible": True,
        "formula_mutation_required": False,
        "renderer_behavior_mutation_required": False,
        "source_lineage_mutation_required": False,
        "persistent_artifact_required": False,
        "authorization_recommendation": "candidate_for_future_probe_design",
    },
    {
        "entrypoint": "mask_overlay_to_globe",
        "entrypoint_exists_in_evidence": True,
        "probe_scope": "mask_alpha_gate_design",
        "synthetic_payload_possible": True,
        "one_shot_possible": True,
        "formula_mutation_required": False,
        "renderer_behavior_mutation_required": False,
        "source_lineage_mutation_required": False,
        "persistent_artifact_required": False,
        "authorization_recommendation": "candidate_for_future_probe_design",
    },
    {
        "entrypoint": "controller_fixed_one_shot_render_path",
        "entrypoint_exists_in_evidence": True,
        "probe_scope": "fixed_one_shot_controller_path_design_only",
        "synthetic_payload_possible": True,
        "one_shot_possible": True,
        "formula_mutation_required": False,
        "renderer_behavior_mutation_required": False,
        "source_lineage_mutation_required": False,
        "persistent_artifact_required": False,
        "authorization_recommendation": "candidate_for_future_probe_design",
    },
    {
        "entrypoint": "early_5_12_render_globe_baseline",
        "entrypoint_exists_in_evidence": True,
        "probe_scope": "core_globe_view_frame_reference_only",
        "synthetic_payload_possible": False,
        "one_shot_possible": True,
        "formula_mutation_required": False,
        "renderer_behavior_mutation_required": False,
        "source_lineage_mutation_required": False,
        "persistent_artifact_required": False,
        "authorization_recommendation": "reference_only",
    },
    {
        "entrypoint": "early_5_29_dynamic_point_grafting_reference",
        "entrypoint_exists_in_evidence": True,
        "probe_scope": "dynamic_point_grafting_reference_static_design_only",
        "synthetic_payload_possible": True,
        "one_shot_possible": True,
        "formula_mutation_required": False,
        "renderer_behavior_mutation_required": False,
        "source_lineage_mutation_required": False,
        "persistent_artifact_required": False,
        "authorization_recommendation": "reference_only",
    },
]


SYNTHETIC_ADAPTER_CONTRACT_REVIEW = {
    "synthetic_payload_minimal_fields": [
        "point_id",
        "source_label",
        "timestamp",
        "lat",
        "lon",
        "speed_or_altitude_label",
    ],
    "covers_ais_adsb_minimal_pipeline": True,
    "synthetic_adapter_replaces_sql_websocket_cache_live_source": True,
    "source_lineage_token_can_be_fixed": True,
    "deterministic_fixture_can_represent_point_id_coordinate_timestamp_source": True,
    "real_data_read_needed": False,
    "synthetic_data_only_sufficient": True,
    "real_source_required": False,
    "sql_required": False,
    "websocket_required": False,
    "cache_database_required": False,
}


ONE_SHOT_EXECUTION_REVIEW = {
    "fixed_zoom_rotation_lod_horizon_mask_compose_labels_possible": True,
    "single_projection_masking_composition_characterization_possible": True,
    "one_shot_sufficient": True,
    "long_running_gui_required": False,
    "human_gui_interaction_required": False,
    "persistent_runtime_state_required": False,
    "persistent_artifact_required": False,
}


MUTATION_AND_CLAIM_STOP_LINE_REVIEW = {
    "formula_mutation_required": False,
    "renderer_behavior_mutation_required": False,
    "compose_order_mutation_required": False,
    "frame_semantics_mutation_required": False,
    "coordinate_correctness_claim_allowed": False,
    "visual_correctness_claim_allowed": False,
    "transparent_globe_leak_fix_claim_allowed": False,
    "readiness_claim_allowed": False,
    "performance_claim_allowed": False,
}


ORACLE_SUFFICIENCY_REVIEW = {
    "covered_oracle_rules": {
        "source token changed": "source_lineage_pollution_fail",
        "source absent": "invalid_probe",
        "projected dropped while source present": "projection_or_horizon_responsibility",
        "sampled dropped while projected present": "sampling_responsibility",
        "overlay absent while sampled present": "overlay_or_presentation_responsibility",
        "mask hidden while overlay present": "globe_mask_responsibility",
        "frame visible while mask invisible": "transparent_globe_leak_candidate",
        "source present while frame hidden": "computed_but_hidden_supported",
    },
    "oracle_rules_sufficient_for_probe_design": True,
    "transparent_globe_leak_kept_as_candidate": True,
    "computed_but_hidden_rule_preserved": True,
    "source_lineage_pollution_guard_preserved": True,
}


AUTHORIZATION_REVIEW_DECISION = {
    "authorization_review_passed": True,
    "runtime_probe_design_authorized": True,
    "runtime_probe_execution_authorized": False,
    "runtime_execution_authorized": False,
    "probe_harness_creation_authorized": False,
    "production_source_change_authorized": False,
    "formula_mutation_authorized": False,
    "renderer_behavior_mutation_authorized": False,
    "persistent_artifact_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
    "global_methodology_promotion_authorized": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_one_shot_synthetic_probe_design_gate",
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_runtime_probe_authorization_review.v1",
    "planning_source": "aa1ff89",
    "authorization_prerequisite_packet": AUTHORIZATION_PREREQUISITE_PACKET,
    "entrypoint_authorization_matrix": ENTRYPOINT_AUTHORIZATION_MATRIX,
    "synthetic_adapter_contract_review": SYNTHETIC_ADAPTER_CONTRACT_REVIEW,
    "one_shot_execution_review": ONE_SHOT_EXECUTION_REVIEW,
    "mutation_and_claim_stop_line_review": MUTATION_AND_CLAIM_STOP_LINE_REVIEW,
    "oracle_sufficiency_review": ORACLE_SUFFICIENCY_REVIEW,
    "authorization_review_decision": AUTHORIZATION_REVIEW_DECISION,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointLodViewFrameRuntimeProbeAuthorizationReviewTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "planning_source",
                "authorization_prerequisite_packet",
                "entrypoint_authorization_matrix",
                "synthetic_adapter_contract_review",
                "one_shot_execution_review",
                "mutation_and_claim_stop_line_review",
                "oracle_sufficiency_review",
                "authorization_review_decision",
                "boundary_statement",
            },
        )
        self.assertEqual(PACKET["schema"], "rrkal.displaytools.dynamic_point_lod_view_frame_runtime_probe_authorization_review.v1")
        self.assertEqual(PACKET["planning_source"], "aa1ff89")

    def test_authorization_prerequisites_are_available(self):
        prereq = PACKET["authorization_prerequisite_packet"]
        for key, value in prereq.items():
            self.assertTrue(value, key)

    def test_entrypoint_authorization_matrix(self):
        rows = {row["entrypoint"]: row for row in PACKET["entrypoint_authorization_matrix"]}
        self.assertEqual(
            set(rows),
            {
                "render_if_needed",
                "project_ais_to_screen",
                "mask_overlay_to_globe",
                "controller_fixed_one_shot_render_path",
                "early_5_12_render_globe_baseline",
                "early_5_29_dynamic_point_grafting_reference",
            },
        )
        allowed_recommendations = {
            "candidate_for_future_probe_design",
            "reference_only",
            "excluded_for_dynamic_point_probe",
            "blocked_pending_evidence",
        }
        for row in rows.values():
            self.assertTrue(row["entrypoint_exists_in_evidence"])
            self.assertIn(row["authorization_recommendation"], allowed_recommendations)
            self.assertFalse(row["formula_mutation_required"])
            self.assertFalse(row["renderer_behavior_mutation_required"])
            self.assertFalse(row["source_lineage_mutation_required"])
            self.assertFalse(row["persistent_artifact_required"])
        self.assertEqual(rows["early_5_12_render_globe_baseline"]["authorization_recommendation"], "reference_only")
        self.assertEqual(rows["early_5_29_dynamic_point_grafting_reference"]["authorization_recommendation"], "reference_only")

    def test_synthetic_adapter_contract_review(self):
        review = PACKET["synthetic_adapter_contract_review"]
        self.assertTrue(review["covers_ais_adsb_minimal_pipeline"])
        self.assertTrue(review["synthetic_adapter_replaces_sql_websocket_cache_live_source"])
        self.assertTrue(review["source_lineage_token_can_be_fixed"])
        self.assertTrue(review["deterministic_fixture_can_represent_point_id_coordinate_timestamp_source"])
        self.assertFalse(review["real_data_read_needed"])
        self.assertTrue(review["synthetic_data_only_sufficient"])
        self.assertFalse(review["real_source_required"])
        self.assertFalse(review["sql_required"])
        self.assertFalse(review["websocket_required"])
        self.assertFalse(review["cache_database_required"])
        self.assertIn("point_id", review["synthetic_payload_minimal_fields"])
        self.assertIn("source_label", review["synthetic_payload_minimal_fields"])

    def test_one_shot_execution_review(self):
        review = PACKET["one_shot_execution_review"]
        self.assertTrue(review["fixed_zoom_rotation_lod_horizon_mask_compose_labels_possible"])
        self.assertTrue(review["single_projection_masking_composition_characterization_possible"])
        self.assertTrue(review["one_shot_sufficient"])
        self.assertFalse(review["long_running_gui_required"])
        self.assertFalse(review["human_gui_interaction_required"])
        self.assertFalse(review["persistent_runtime_state_required"])
        self.assertFalse(review["persistent_artifact_required"])

    def test_mutation_and_claim_stop_lines(self):
        review = PACKET["mutation_and_claim_stop_line_review"]
        for key, value in review.items():
            self.assertFalse(value, key)

    def test_oracle_sufficiency_review(self):
        review = PACKET["oracle_sufficiency_review"]
        self.assertEqual(
            review["covered_oracle_rules"],
            {
                "source token changed": "source_lineage_pollution_fail",
                "source absent": "invalid_probe",
                "projected dropped while source present": "projection_or_horizon_responsibility",
                "sampled dropped while projected present": "sampling_responsibility",
                "overlay absent while sampled present": "overlay_or_presentation_responsibility",
                "mask hidden while overlay present": "globe_mask_responsibility",
                "frame visible while mask invisible": "transparent_globe_leak_candidate",
                "source present while frame hidden": "computed_but_hidden_supported",
            },
        )
        self.assertTrue(review["oracle_rules_sufficient_for_probe_design"])
        self.assertTrue(review["transparent_globe_leak_kept_as_candidate"])
        self.assertTrue(review["computed_but_hidden_rule_preserved"])
        self.assertTrue(review["source_lineage_pollution_guard_preserved"])

    def test_authorization_review_decision_allows_design_only(self):
        decision = PACKET["authorization_review_decision"]
        self.assertTrue(decision["authorization_review_passed"])
        self.assertTrue(decision["runtime_probe_design_authorized"])
        self.assertFalse(decision["runtime_probe_execution_authorized"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["probe_harness_creation_authorized"])
        self.assertFalse(decision["production_source_change_authorized"])
        self.assertFalse(decision["formula_mutation_authorized"])
        self.assertFalse(decision["renderer_behavior_mutation_authorized"])
        self.assertFalse(decision["persistent_artifact_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertFalse(decision["global_methodology_promotion_authorized"])
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_lod_view_frame_one_shot_synthetic_probe_design_gate")

    def test_boundary_statement_blocks_forbidden_actions(self):
        statement = PACKET["boundary_statement"]
        self.assertIn("No helper module creation", statement)
        self.assertIn("no probe harness creation", statement)
        self.assertIn("no runtime probe execution", statement)
        self.assertIn("no instrumentation", statement)
        self.assertIn("no monkey patch implementation", statement)
        self.assertIn("no __getattribute__ implementation", statement)
        self.assertIn("no sys.settrace", statement)
        self.assertIn("no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change", statement)
        self.assertIn("no coordinate/visual correctness claim", statement)
        self.assertIn("no transparent-globe leak fix claim", statement)
        self.assertIn("no runtime characterization execution authorization", statement)
        self.assertIn("no global methodology promotion", statement)


if __name__ == "__main__":
    unittest.main()
