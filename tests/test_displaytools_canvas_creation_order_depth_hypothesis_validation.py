import unittest


REQUIRED_LAYERS = {
    "light_sun_starfield",
    "world_frame_projection",
    "terrain_bathymetry",
    "vector_boundary_naming",
    "dynamic_point_creatures",
    "selection_card_governance",
}

ALIGNMENT_KEYS = {
    "layer_name",
    "creation_order_depth",
    "expected_lithology_bias",
    "known_lithology_or_gate_evidence",
    "known_strategy_evidence",
    "alignment_status",
    "supports_design_intent_hypothesis",
    "counterexample_flag",
    "evidence_limit",
    "confidence_level",
}


def build_displaytools_canvas_creation_order_depth_hypothesis_validation_packet():
    alignment_matrix = [
        {
            "layer_name": "light_sun_starfield",
            "creation_order_depth": 1,
            "expected_lithology_bias": "world_law_deep_frame_semantics",
            "known_lithology_or_gate_evidence": [
                "solar_lighting_frame_boundary_fixture_gate_blocks_compute_sun_direction",
                "lighting_shader_formula_and_starfield_frame_coupling_are_not_decoration",
            ],
            "known_strategy_evidence": "diagnostic_label_and_formula_stop_line_first",
            "alignment_status": "aligned_with_deep_frame_semantics",
            "supports_design_intent_hypothesis": True,
            "counterexample_flag": False,
            "evidence_limit": "solar_formula_and_renderer_lighting_not_executed",
            "confidence_level": "medium",
        },
        {
            "layer_name": "world_frame_projection",
            "creation_order_depth": 2,
            "expected_lithology_bias": "core_interface_only",
            "known_lithology_or_gate_evidence": [
                "projection_flip_mask_sync_current_lithology_core_interface_only",
                "projection_interface_shadow_gate_blocks_formula_movement",
            ],
            "known_strategy_evidence": "shadow_interface_not_formula_movement",
            "alignment_status": "aligned_with_core_interface_only",
            "supports_design_intent_hypothesis": True,
            "counterexample_flag": False,
            "evidence_limit": "coordinate_correctness_not_claimed",
            "confidence_level": "high",
        },
        {
            "layer_name": "terrain_bathymetry",
            "creation_order_depth": 3,
            "expected_lithology_bias": "world_body_high_coupling",
            "known_lithology_or_gate_evidence": [
                "terrain_bathymetry_boundary_fixture_blocks_shader_sampling_projection_flip_mask_lighting_formula",
                "terrain_bathymetry_boundary_keeps_provider_cache_and_visual_faults_unmoved",
            ],
            "known_strategy_evidence": "descriptor_shell_before_shader_sampling_or_visual_formula",
            "alignment_status": "aligned_with_world_body_high_coupling",
            "supports_design_intent_hypothesis": True,
            "counterexample_flag": False,
            "evidence_limit": "terrain_visual_quality_and_sampling_runtime_not_executed",
            "confidence_level": "medium",
        },
        {
            "layer_name": "vector_boundary_naming",
            "creation_order_depth": 4,
            "expected_lithology_bias": "semantic_geography_boundary_layer",
            "known_lithology_or_gate_evidence": [
                "vector_overlay_boundary_minimal_extraction_moved_descriptor_policy_ledger_only",
                "projection_mask_provider_controller_runtime_remain_blocked",
            ],
            "known_strategy_evidence": "descriptor_policy_ledger_when_runtime_and_formula_surfaces_are_excluded",
            "alignment_status": "aligned_with_semantic_geography_boundary_naming",
            "supports_design_intent_hypothesis": True,
            "counterexample_flag": False,
            "evidence_limit": "does_not_generalize_to_vector_provider_or_projection_runtime",
            "confidence_level": "medium_high",
        },
        {
            "layer_name": "dynamic_point_creatures",
            "creation_order_depth": 5,
            "expected_lithology_bias": "later_created_entities_with_reconstructable_semantics",
            "known_lithology_or_gate_evidence": [
                "dynamic_point_lithology_model_promoted_to_local_pattern_inside_dynamic_point_scope",
                "dynamic_point_ancient_sediment_correlation_supports_later_entity_semantics",
            ],
            "known_strategy_evidence": "semantic_reconstruction_and_ablation_before_runtime_channels",
            "alignment_status": "aligned_with_later_entity_semantic_reconstruction",
            "supports_design_intent_hypothesis": True,
            "counterexample_flag": False,
            "evidence_limit": "dynamic_point_local_pattern_does_not_generalize_to_all_canvas_layers",
            "confidence_level": "high",
        },
        {
            "layer_name": "selection_card_governance",
            "creation_order_depth": 6,
            "expected_lithology_bias": "governance_interface_cross_organ_semantics",
            "known_lithology_or_gate_evidence": [
                "metadata_artifact_schema_requires_schema_governance",
                "cross_organ_card_integration_requires_cross_organ_handoff",
            ],
            "known_strategy_evidence": "governance_review_or_cross_organ_handoff_not_c3_only_extraction",
            "alignment_status": "aligned_with_governance_cross_organ_strategy",
            "supports_design_intent_hypothesis": True,
            "counterexample_flag": False,
            "evidence_limit": "governance_requires_o1_or_cross_agent_context",
            "confidence_level": "medium_high",
        },
    ]

    return {
        "schema": "rrkal.displaytools.canvas_creation_order_depth_hypothesis_validation.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "design_intent_source": "e874ece",
        "hypothesis_validation_status": {
            "design_intent_hypothesis_supported": True,
            "previous_trust_level": "L1_design_intent_hypothesis",
            "maximum_trust_level": "L1_supported_design_intent_hypothesis",
            "l2_local_pattern_authorized": False,
            "universal_doctrine_authorized": False,
        },
        "alignment_matrix": alignment_matrix,
        "counterexample_summary": {
            "counterexamples_present": False,
            "counterexamples": [],
            "counterexample_limit": "absence_of_counterexample_is_not_proof_of_subconscious_design_intent",
        },
        "trust_level_recommendation": {
            "recommended_trust_level": "L1_supported_design_intent_hypothesis",
            "l2_local_pattern_authorized": False,
            "l3_reusable_method_authorized": False,
            "universal_doctrine_authorized": False,
            "reason": "alignment exists across known c3 lithology and strategy evidence, but this remains design-intent support only",
        },
        "use_in_future_lithology_work": {
            "allowed_use": "secondary_depth_bias_axis",
            "genesis_axis_replaces_git_history": False,
            "genesis_axis_replaces_dependency_scan": False,
            "genesis_axis_replaces_ablation_response": False,
            "genesis_axis_replaces_lithology_model": False,
            "extraction_authorized": False,
        },
        "evidence_limits": [
            "static_scan_only",
            "religious_correctness_not_claimed",
            "subconscious_design_intent_not_fully_proven",
            "does_not_replace_hard_evidence",
            "does_not_authorize_source_movement",
            "does_not_upgrade_to_l2_or_universal_doctrine",
        ],
        "decision_output": {
            "creation_order_depth_validation_gate_passed": True,
            "design_intent_hypothesis_supported": True,
            "maximum_trust_level": "L1_supported_design_intent_hypothesis",
            "l2_local_pattern_authorized": False,
            "universal_doctrine_authorized": False,
            "religious_correctness_claimed": False,
            "subconscious_design_intent_fully_proven": False,
            "genesis_axis_replaces_git_history": False,
            "genesis_axis_replaces_dependency_scan": False,
            "genesis_axis_replaces_ablation_response": False,
            "genesis_axis_replaces_lithology_model": False,
            "extraction_authorized": False,
            "source_movement_authorized": False,
            "runtime_merge_enabled": False,
            "readiness_claimed": False,
            "recommended_next_gate": "displaytools_canvas_creation_order_depth_cross_subsystem_counterexample_gate",
        },
        "boundary_statement": (
            "Docs/test-only displaytools canvas creation order depth hypothesis validation gate. "
            "No helper module creation, no source movement, no production source change, "
            "no checker script creation, no checker script change, no generic checker trust-level change, "
            "no generic checker blocking behavior change, no generic profile change, no monolith import, "
            "no runtime execution, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask/solar/lighting/terrain/vector/dynamic-point behavior change, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, "
            "no cross-organ integration implementation, no religious correctness claim, "
            "no subconscious design intent proof claim, no evidence replacement claim, "
            "no L2 local pattern or universal doctrine promotion, no runtime merge enablement, "
            "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DisplaytoolsCanvasCreationOrderDepthHypothesisValidationTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_displaytools_canvas_creation_order_depth_hypothesis_validation_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "base_camp_rollback_anchor",
                "design_intent_source",
                "hypothesis_validation_status",
                "alignment_matrix",
                "counterexample_summary",
                "trust_level_recommendation",
                "use_in_future_lithology_work",
                "evidence_limits",
                "decision_output",
                "boundary_statement",
            },
        )

    def test_base_and_design_intent_source(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["design_intent_source"], "e874ece")

    def test_all_required_layers_present(self):
        self.assertEqual(
            {row["layer_name"] for row in self.packet["alignment_matrix"]},
            REQUIRED_LAYERS,
        )
        for row in self.packet["alignment_matrix"]:
            self.assertEqual(set(row), ALIGNMENT_KEYS)

    def test_alignment_statuses_are_present(self):
        for row in self.packet["alignment_matrix"]:
            self.assertTrue(row["alignment_status"])
            self.assertIn(row["supports_design_intent_hypothesis"], {True, False})
            self.assertIn(row["counterexample_flag"], {True, False})

    def test_world_frame_projection_aligns_with_core_interface_only(self):
        row = self._row("world_frame_projection")
        self.assertEqual(row["expected_lithology_bias"], "core_interface_only")
        self.assertEqual(row["alignment_status"], "aligned_with_core_interface_only")
        self.assertIn("projection_interface_shadow_gate_blocks_formula_movement", row["known_lithology_or_gate_evidence"])

    def test_dynamic_point_creatures_align_with_semantic_reconstruction(self):
        row = self._row("dynamic_point_creatures")
        self.assertEqual(row["expected_lithology_bias"], "later_created_entities_with_reconstructable_semantics")
        self.assertEqual(row["alignment_status"], "aligned_with_later_entity_semantic_reconstruction")
        self.assertIn("semantic_reconstruction", row["known_strategy_evidence"])

    def test_selection_card_governance_aligns_with_governance_cross_organ(self):
        row = self._row("selection_card_governance")
        self.assertEqual(row["expected_lithology_bias"], "governance_interface_cross_organ_semantics")
        self.assertEqual(row["alignment_status"], "aligned_with_governance_cross_organ_strategy")

    def test_maximum_trust_level_is_l1_supported(self):
        status = self.packet["hypothesis_validation_status"]
        self.assertIs(status["design_intent_hypothesis_supported"], True)
        self.assertEqual(status["maximum_trust_level"], "L1_supported_design_intent_hypothesis")
        self.assertEqual(
            self.packet["trust_level_recommendation"]["recommended_trust_level"],
            "L1_supported_design_intent_hypothesis",
        )

    def test_no_l2_or_universal_doctrine_authorization(self):
        status = self.packet["hypothesis_validation_status"]
        trust = self.packet["trust_level_recommendation"]
        self.assertIs(status["l2_local_pattern_authorized"], False)
        self.assertIs(status["universal_doctrine_authorized"], False)
        self.assertIs(trust["l2_local_pattern_authorized"], False)
        self.assertIs(trust["l3_reusable_method_authorized"], False)
        self.assertIs(trust["universal_doctrine_authorized"], False)

    def test_religious_and_subconscious_claims_not_made(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["religious_correctness_claimed"], False)
        self.assertIs(decision["subconscious_design_intent_fully_proven"], False)

    def test_genesis_axis_does_not_replace_evidence(self):
        use = self.packet["use_in_future_lithology_work"]
        self.assertIs(use["genesis_axis_replaces_git_history"], False)
        self.assertIs(use["genesis_axis_replaces_dependency_scan"], False)
        self.assertIs(use["genesis_axis_replaces_ablation_response"], False)
        self.assertIs(use["genesis_axis_replaces_lithology_model"], False)
        decision = self.packet["decision_output"]
        self.assertIs(decision["genesis_axis_replaces_git_history"], False)
        self.assertIs(decision["genesis_axis_replaces_dependency_scan"], False)
        self.assertIs(decision["genesis_axis_replaces_ablation_response"], False)
        self.assertIs(decision["genesis_axis_replaces_lithology_model"], False)

    def test_no_extraction_source_movement_runtime_or_readiness(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["extraction_authorized"], False)
        self.assertIs(decision["source_movement_authorized"], False)
        self.assertIs(decision["runtime_merge_enabled"], False)
        self.assertIs(decision["readiness_claimed"], False)

    def test_recommended_next_gate(self):
        self.assertEqual(
            self.packet["decision_output"]["recommended_next_gate"],
            "displaytools_canvas_creation_order_depth_cross_subsystem_counterexample_gate",
        )

    def _row(self, layer_name):
        return next(row for row in self.packet["alignment_matrix"] if row["layer_name"] == layer_name)


if __name__ == "__main__":
    unittest.main()
