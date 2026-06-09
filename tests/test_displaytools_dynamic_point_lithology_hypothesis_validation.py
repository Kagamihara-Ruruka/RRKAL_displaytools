import unittest


SURFACE_NAMES = {
    "replay_live_lineage_deeper_runtime",
    "controller_selection_picker_hit_test",
    "datashader_runtime_sampling",
    "projection_flip_mask_sync",
    "metadata_artifact_schema",
    "cross_organ_card_integration",
}

TRUST_LEVELS = {
    "L1_hypothesis",
    "L1_supported_hypothesis",
    "L2_local_pattern_candidate",
    "L2_local_pattern",
    "blocked_insufficient_evidence",
}

SURFACE_VALIDATION_MATRIX = [
    {
        "surface_name": "replay_live_lineage_deeper_runtime",
        "lithology_from_recursive_gate": "andesite",
        "semantic_strategy_from_design_gate": "semantic_reconstruction_before_rebuild_or_wrapper_decision",
        "metamorphic_transition_from_inventory_gate": "sediment_to_andesite_bridge",
        "classification_stability": "reasonable_refinement_with_history_limit",
        "decision_reduction": "rebuild_or_wrapper_after_semantic_reconstruction",
        "risk_reduction": "prevents_direct_sql_websocket_cache_extraction",
        "confidence_level": "medium",
        "trust_level_recommendation": "L1_supported_hypothesis",
        "recommended_next_gate": "dynamic_point_replay_live_lineage_semantic_reconstruction_gate",
        "remaining_uncertainty": "history_query_limited_and_runtime_not_executed",
        "implementation_transplant_authorized": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "controller_selection_picker_hit_test",
        "lithology_from_recursive_gate": "late_hardened_granite",
        "semantic_strategy_from_design_gate": "interface_wrapper_design_not_direct_transplant",
        "metamorphic_transition_from_inventory_gate": "sediment_to_late_hardened_granite",
        "classification_stability": "stable_runtime_coupled",
        "decision_reduction": "wrapper_interface_not_transplant",
        "risk_reduction": "prevents_controller_picker_hit_test_runtime_movement",
        "confidence_level": "medium",
        "trust_level_recommendation": "L1_supported_hypothesis",
        "recommended_next_gate": "dynamic_point_controller_selection_interface_design_gate",
        "remaining_uncertainty": "picker_runtime_not_executed",
        "implementation_transplant_authorized": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "datashader_runtime_sampling",
        "lithology_from_recursive_gate": "late_hardened_granite",
        "semantic_strategy_from_design_gate": "runtime_sampling_contract_adapter_design",
        "metamorphic_transition_from_inventory_gate": "sediment_to_late_hardened_granite",
        "classification_stability": "stable_runtime_coupled",
        "decision_reduction": "adapter_contract_design",
        "risk_reduction": "prevents_datashader_pandas_numpy_runtime_extraction",
        "confidence_level": "medium",
        "trust_level_recommendation": "L2_local_pattern_candidate",
        "recommended_next_gate": "dynamic_point_runtime_sampling_contract_design_gate",
        "remaining_uncertainty": "visual_sampling_behavior_not_executed",
        "implementation_transplant_authorized": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "projection_flip_mask_sync",
        "lithology_from_recursive_gate": "core_interface_only",
        "semantic_strategy_from_design_gate": "core_interface_only_shadow_path",
        "metamorphic_transition_from_inventory_gate": "core_lineage_to_interface_only",
        "classification_stability": "stable_core_interface",
        "decision_reduction": "interface_only_shadow_path",
        "risk_reduction": "prevents_projection_flip_mask_formula_movement",
        "confidence_level": "high",
        "trust_level_recommendation": "L2_local_pattern_candidate",
        "recommended_next_gate": "dynamic_point_projection_interface_shadow_gate",
        "remaining_uncertainty": "formula_behavior_not_executed",
        "implementation_transplant_authorized": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "metadata_artifact_schema",
        "lithology_from_recursive_gate": "new_organ_surface",
        "semantic_strategy_from_design_gate": "schema_governance_o1_review",
        "metamorphic_transition_from_inventory_gate": "schema_surface_requires_governance",
        "classification_stability": "stable_schema_governance",
        "decision_reduction": "schema_governance_not_c3_implementation",
        "risk_reduction": "prevents_metadata_output_schema_change",
        "confidence_level": "high",
        "trust_level_recommendation": "L2_local_pattern_candidate",
        "recommended_next_gate": "o1_metadata_artifact_schema_review_gate",
        "remaining_uncertainty": "schema_governance_not_decided_by_c3",
        "implementation_transplant_authorized": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "cross_organ_card_integration",
        "lithology_from_recursive_gate": "new_organ_surface",
        "semantic_strategy_from_design_gate": "cross_organ_handoff_contract_discussion",
        "metamorphic_transition_from_inventory_gate": "new_organ_to_cross_organ_handoff",
        "classification_stability": "stable_cross_organ_handoff",
        "decision_reduction": "cross_organ_handoff_not_c3_only",
        "risk_reduction": "prevents_c3_only_cross_organ_implementation",
        "confidence_level": "high",
        "trust_level_recommendation": "L2_local_pattern_candidate",
        "recommended_next_gate": "o1_cross_organ_card_integration_review_gate",
        "remaining_uncertainty": "requires_cross_agent_context",
        "implementation_transplant_authorized": False,
        "source_movement_authorized": False,
    },
]


def build_dynamic_point_lithology_hypothesis_validation_packet():
    return {
        "schema": "rrkal.displaytools.dynamic_point_lithology_hypothesis_validation.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "forward_camps": [
            "b29b79f",
            "71c7182",
        ],
        "hypothesis_status": {
            "method_useful": True,
            "hypothesis_status_label": "locally_supported_non_authorizing_hypothesis",
            "overall_trust_level_recommendation": "L2_local_pattern_candidate",
            "universal_doctrine_authorized": False,
            "historical_diff_is_not_lithology_verdict": True,
            "semantic_hypothesis_is_not_extraction_authorization": True,
            "generic_checker_upgrade_authorized": False,
        },
        "validated_inputs": [
            "recursive_historical_lithology_gate",
            "lithology_semantic_reconstruction_design_gate",
            "metamorphic_history_slice_inventory_gate",
        ],
        "surface_validation_matrix": SURFACE_VALIDATION_MATRIX,
        "validation_questions": {
            "classification_stability": "all six surfaces stay stable or receive a bounded refinement across the three gates",
            "decision_reduction": "each surface now maps to rebuild, wrapper, interface-only, schema governance, or cross-organ handoff",
            "risk_reduction": "the model prevents runtime, formula, schema, and cross-organ surfaces from being treated as sediment",
            "evidence_support": "history slices and dependency pressure strengthen projection, datashader, metadata, and cross-organ stop lines",
            "evidence_limit": "history query limits and no runtime execution keep replay, controller, and sampling claims below final doctrine",
            "operational_entropy_delta": "decision space is reduced from six ambiguous hard surfaces to typed non-extraction next gates",
            "trust_level_recommendation": "dynamic point local use may be treated as L2 local pattern candidate; universal doctrine is not authorized",
            "next_action": "dynamic_point_projection_interface_shadow_gate",
        },
        "trust_level_recommendations": {
            "supported_levels": sorted(TRUST_LEVELS),
            "overall_method": "L2_local_pattern_candidate",
            "not_universal_doctrine": True,
            "surfaces_remaining_l1_supported": [
                "replay_live_lineage_deeper_runtime",
                "controller_selection_picker_hit_test",
            ],
            "surfaces_l2_local_pattern_candidates": [
                "datashader_runtime_sampling",
                "projection_flip_mask_sync",
                "metadata_artifact_schema",
                "cross_organ_card_integration",
            ],
            "generic_checker_trust_level_unchanged": "L1_shadow",
        },
        "operational_entropy_assessment": {
            "baseline_without_hypothesis": "six_remaining_surfaces_ambiguous",
            "after_validation": "surfaces_partitioned_into_rebuild_wrapper_interface_schema_handoff",
            "decision_space_reduced": True,
            "ambiguous_surface_count_before": 6,
            "ambiguous_surface_count_after": 2,
            "entropy_delta": "reduced",
            "method_not_universal_doctrine": True,
        },
        "evidence_limits": [
            "historical_diff_is_not_lithology_verdict",
            "semantic_hypothesis_is_not_extraction_authorization",
            "history_query_limited",
            "runtime_not_executed",
            "schema_and_cross_organ_governance_not_decided_by_c3",
        ],
        "decision_output": {
            "hypothesis_validation_gate_passed": True,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "generic_checker_replacement_authorized": False,
            "readiness_claimed": False,
            "implementation_transplant_authorized": False,
            "universal_methodology_doctrine_promoted": False,
            "recommended_next_gate": "dynamic_point_projection_interface_shadow_gate",
            "next_gate_kind": "analysis_design_not_extraction",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point lithology hypothesis validation gate. "
            "No helper module creation, no source movement, no production source change, "
            "no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, "
            "no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, "
            "no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, "
            "no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, "
            "no cross-organ integration implementation, no runtime merge enablement, "
            "no universal methodology doctrine promotion, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointLithologyHypothesisValidationTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_lithology_hypothesis_validation_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "base_camp_rollback_anchor",
                "forward_camps",
                "hypothesis_status",
                "validated_inputs",
                "surface_validation_matrix",
                "validation_questions",
                "trust_level_recommendations",
                "operational_entropy_assessment",
                "evidence_limits",
                "decision_output",
                "boundary_statement",
            },
        )

    def test_base_and_forward_camps(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertIn("b29b79f", self.packet["forward_camps"])
        self.assertIn("71c7182", self.packet["forward_camps"])

    def test_all_six_surfaces_present(self):
        self.assertEqual(
            {row["surface_name"] for row in self.packet["surface_validation_matrix"]},
            SURFACE_NAMES,
        )

    def test_every_surface_has_validation_fields(self):
        required = {
            "surface_name",
            "lithology_from_recursive_gate",
            "semantic_strategy_from_design_gate",
            "metamorphic_transition_from_inventory_gate",
            "classification_stability",
            "decision_reduction",
            "risk_reduction",
            "confidence_level",
            "trust_level_recommendation",
            "recommended_next_gate",
            "remaining_uncertainty",
            "implementation_transplant_authorized",
            "source_movement_authorized",
        }
        for row in self.packet["surface_validation_matrix"]:
            self.assertEqual(set(row), required)
            self.assertTrue(row["classification_stability"])
            self.assertTrue(row["decision_reduction"])
            self.assertTrue(row["risk_reduction"])
            self.assertIn(row["trust_level_recommendation"], TRUST_LEVELS)

    def test_no_surface_grants_transplant_or_source_movement(self):
        for row in self.packet["surface_validation_matrix"]:
            self.assertIs(row["implementation_transplant_authorized"], False)
            self.assertIs(row["source_movement_authorized"], False)

    def test_hypothesis_not_universal_doctrine(self):
        status = self.packet["hypothesis_status"]
        self.assertIs(status["method_useful"], True)
        self.assertEqual(status["overall_trust_level_recommendation"], "L2_local_pattern_candidate")
        self.assertIs(status["universal_doctrine_authorized"], False)
        self.assertIs(self.packet["trust_level_recommendations"]["not_universal_doctrine"], True)
        used_levels = {row["trust_level_recommendation"] for row in self.packet["surface_validation_matrix"]}
        self.assertNotIn("L2_local_pattern", used_levels)

    def test_historical_and_semantic_evidence_are_not_authorization(self):
        status = self.packet["hypothesis_status"]
        self.assertIs(status["historical_diff_is_not_lithology_verdict"], True)
        self.assertIs(status["semantic_hypothesis_is_not_extraction_authorization"], True)

    def test_operational_entropy_reduced(self):
        entropy = self.packet["operational_entropy_assessment"]
        self.assertIs(entropy["decision_space_reduced"], True)
        self.assertLess(
            entropy["ambiguous_surface_count_after"],
            entropy["ambiguous_surface_count_before"],
        )
        self.assertEqual(entropy["entropy_delta"], "reduced")

    def test_guard_flags_remain_false(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["source_movement_authorized"], False)
        self.assertIs(decision["helper_module_creation_authorized"], False)
        self.assertIs(decision["runtime_merge_enabled"], False)
        self.assertIs(decision["generic_checker_blocking"], False)
        self.assertIs(decision["generic_checker_replacement_authorized"], False)
        self.assertIs(decision["readiness_claimed"], False)
        self.assertIs(decision["implementation_transplant_authorized"], False)
        self.assertIs(decision["universal_methodology_doctrine_promoted"], False)

    def test_recommended_next_gate_is_design_not_extraction(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_projection_interface_shadow_gate")
        self.assertEqual(decision["next_gate_kind"], "analysis_design_not_extraction")
        self.assertNotIn("extraction", decision["recommended_next_gate"])

    def test_boundary_statement_excludes_readiness_and_source_movement(self):
        statement = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", statement)
        self.assertIn("no source movement", statement)
        self.assertIn("no universal methodology doctrine promotion", statement)
        self.assertIn("no readiness/performance/visual parity/bug-fix/safe-to-extract claim", statement)


if __name__ == "__main__":
    unittest.main()
