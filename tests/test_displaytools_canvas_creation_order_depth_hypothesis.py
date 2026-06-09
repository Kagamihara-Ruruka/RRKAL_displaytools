import unittest


REQUIRED_LAYERS = [
    "chaos_or_raw_data",
    "light_sun_starfield",
    "world_frame_projection",
    "terrain_bathymetry",
    "vector_boundary_naming",
    "dynamic_point_creatures",
    "selection_card_governance",
]

LAYER_KEYS = {
    "layer_name",
    "creation_order_depth",
    "canvas_role",
    "representative_c3_surfaces",
    "expected_lithology_bias",
    "interface_strategy_bias",
    "evidence_refs",
    "confidence_level",
    "evidence_limit",
}

HYPOTHESIS_BOUNDARY_FLAGS = {
    "genesis_hypothesis_is_design_intent_axis": True,
    "genesis_hypothesis_is_not_religious_claim": True,
    "genesis_hypothesis_is_not_extraction_authorization": True,
    "genesis_hypothesis_does_not_replace_git_history": True,
    "genesis_hypothesis_does_not_replace_dependency_scan": True,
    "genesis_hypothesis_does_not_replace_ablation_response": True,
    "genesis_hypothesis_does_not_replace_lithology_model": True,
    "greek_cosmology_not_intended_source_model": True,
    "generic_cosmology_not_intended_source_model": True,
}


def build_displaytools_canvas_creation_order_depth_hypothesis_packet():
    creation_order_matrix = [
        {
            "layer_name": "chaos_or_raw_data",
            "creation_order_depth": 0,
            "canvas_role": "pre_canvas_disorder_unshaped_data",
            "representative_c3_surfaces": [
                "real_provider_payloads",
                "raw_cache_database_or_file_inputs",
                "unshaped_dynamic_point_payload",
            ],
            "expected_lithology_bias": "outside_canvas_or_raw_source_pressure",
            "interface_strategy_bias": "do_not_infer_canvas_semantics_without_source_boundary",
            "evidence_refs": ["normalizer_and_provider_boundary_gates", "dynamic_point_source_lineage_gates"],
            "confidence_level": "medium",
            "evidence_limit": "design_intent_axis_only_not_runtime_evidence",
        },
        {
            "layer_name": "light_sun_starfield",
            "creation_order_depth": 1,
            "canvas_role": "light_stars_solar_time_orientation",
            "representative_c3_surfaces": [
                "solar_lighting_frame",
                "sun_direction_descriptor",
                "starfield_frame_dependency",
            ],
            "expected_lithology_bias": "world_law_deep_frame_semantics",
            "interface_strategy_bias": "diagnostic_label_and_formula_stop_line_first",
            "evidence_refs": ["solar_lighting_frame_boundary_fixture_gate"],
            "confidence_level": "medium",
            "evidence_limit": "does_not_prove_solar_formula_ownership",
        },
        {
            "layer_name": "world_frame_projection",
            "creation_order_depth": 2,
            "canvas_role": "world_visibility_coordinate_frame_observer_law",
            "representative_c3_surfaces": [
                "projection_flip_mask_sync",
                "globe_coordinate_ownership",
                "dynamic_point_projection_interface_shadow",
            ],
            "expected_lithology_bias": "core_interface_only",
            "interface_strategy_bias": "shadow_interface_not_formula_movement",
            "evidence_refs": [
                "dynamic_point_projection_interface_shadow_gate",
                "coordinate_ownership_diagnostic_gate",
            ],
            "confidence_level": "high",
            "evidence_limit": "coordinate_correctness_not_claimed",
        },
        {
            "layer_name": "terrain_bathymetry",
            "creation_order_depth": 3,
            "canvas_role": "earth_sea_shape_world_body",
            "representative_c3_surfaces": [
                "terrain_bathymetry_boundary",
                "height_field_descriptor",
                "bump_normal_consumer",
            ],
            "expected_lithology_bias": "world_body_high_coupling",
            "interface_strategy_bias": "descriptor_shell_before_shader_or_sampling_formula",
            "evidence_refs": ["terrain_bathymetry_boundary_fixture_gate"],
            "confidence_level": "medium",
            "evidence_limit": "terrain_sampling_and_visual_quality_not_proven",
        },
        {
            "layer_name": "vector_boundary_naming",
            "creation_order_depth": 4,
            "canvas_role": "boundary_naming_separation_semantic_geography",
            "representative_c3_surfaces": [
                "vector_overlay_boundary",
                "boundary_specs_descriptor",
                "hydrology_specs_descriptor",
            ],
            "expected_lithology_bias": "semantic_geography_boundary_layer",
            "interface_strategy_bias": "descriptor_policy_ledger_extraction_possible_when_runtime_is_excluded",
            "evidence_refs": ["vector_overlay_boundary_minimal_extraction_gate"],
            "confidence_level": "medium_high",
            "evidence_limit": "does_not_generalize_to_projection_or_provider_runtime",
        },
        {
            "layer_name": "dynamic_point_creatures",
            "creation_order_depth": 5,
            "canvas_role": "ais_adsb_moving_entities_created_creatures",
            "representative_c3_surfaces": [
                "dynamic_point_boundary",
                "source_lineage_boundary",
                "payload_coordinate_quality_boundary",
                "render_cap_adaptive_sampling_boundary",
            ],
            "expected_lithology_bias": "later_created_entities_with_reconstructable_semantics",
            "interface_strategy_bias": "semantic_reconstruction_and_ablation_before_runtime_channels",
            "evidence_refs": [
                "dynamic_point_boundary_minimal_extraction_gate",
                "dynamic_point_stratified_ancient_sediment_ablation_correlation_gate",
            ],
            "confidence_level": "high",
            "evidence_limit": "dynamic_point_local_pattern_only",
        },
        {
            "layer_name": "selection_card_governance",
            "creation_order_depth": 6,
            "canvas_role": "human_agent_viewing_selection_governance_card_semantics",
            "representative_c3_surfaces": [
                "selection_render_policy",
                "metadata_artifact_schema",
                "cross_organ_card_integration",
            ],
            "expected_lithology_bias": "governance_interface_cross_organ_semantics",
            "interface_strategy_bias": "schema_governance_or_cross_organ_handoff_not_c3_only_extraction",
            "evidence_refs": [
                "dynamic_point_lithology_hypothesis_validation_gate",
                "projection_interface_shadow_import_boundary_planning_gate",
            ],
            "confidence_level": "medium_high",
            "evidence_limit": "governance_requires_o1_or_cross_agent_context",
        },
    ]

    return {
        "schema": "rrkal.displaytools.canvas_creation_order_depth_hypothesis.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "local_pattern_source": "60cded8",
        "hypothesis_status": "L1_design_intent_hypothesis",
        "creation_order_matrix": creation_order_matrix,
        "design_intent_axis": {
            **HYPOTHESIS_BOUNDARY_FLAGS,
            "source_context": "u_o_supplied_genesis_like_canvas_creation_order",
            "scope": "c3_canvas_depth_bias_only",
        },
        "c3_layer_depth_bias": {
            "light_sun_starfield": "world_law_deep_frame_semantics_not_decoration",
            "world_frame_projection": "core_interface_only",
            "terrain_bathymetry": "world_body_high_coupling",
            "vector_boundary_naming": "boundary_semantic_geography",
            "dynamic_point_creatures": "later_created_entities_with_reconstructable_semantics",
            "selection_card_governance": "governance_interface_cross_organ_semantics",
        },
        "genesis_vs_generic_cosmology_boundary": {
            "u_o_design_context_recorded": True,
            "religious_correctness_claimed": False,
            "greek_cosmology_not_intended_source_model": True,
            "generic_cosmology_not_intended_source_model": True,
            "thales_anaximander_model_excluded": True,
        },
        "use_in_lithology_analysis": {
            "allowed_use": "secondary_design_intent_axis_for_depth_bias",
            "does_not_replace_git_history": True,
            "does_not_replace_dependency_scan": True,
            "does_not_replace_ablation_response": True,
            "does_not_replace_lithology_model": True,
            "does_not_authorize_extraction": True,
        },
        "evidence_limits": [
            "design_intent_axis_only",
            "not_religious_interpretation_correctness",
            "not_generic_cosmology_model",
            "does_not_prove_implementation_history",
            "does_not_prove_coordinate_or_visual_correctness",
        ],
        "decision_output": {
            "creation_order_depth_gate_passed": True,
            "hypothesis_status": "L1_design_intent_hypothesis",
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "readiness_claimed": False,
            "religious_claim_made": False,
            "extraction_authorized": False,
            "recommended_next_gate": "displaytools_canvas_creation_order_depth_hypothesis_validation_gate",
        },
        "boundary_statement": (
            "Docs/test-only displaytools canvas creation order depth hypothesis gate. "
            "No helper module creation, no source movement, no production source change, "
            "no checker script creation, no checker script change, no generic checker trust-level change, "
            "no generic checker blocking behavior change, no generic profile change, no monolith import, "
            "no runtime execution, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask/solar/lighting/terrain/vector/dynamic-point behavior change, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, "
            "no cross-organ integration implementation, no religious correctness claim, no evidence replacement claim, "
            "no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DisplaytoolsCanvasCreationOrderDepthHypothesisTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_displaytools_canvas_creation_order_depth_hypothesis_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "base_camp_rollback_anchor",
                "local_pattern_source",
                "hypothesis_status",
                "creation_order_matrix",
                "design_intent_axis",
                "c3_layer_depth_bias",
                "genesis_vs_generic_cosmology_boundary",
                "use_in_lithology_analysis",
                "evidence_limits",
                "decision_output",
                "boundary_statement",
            },
        )

    def test_hypothesis_status_is_l1_design_intent(self):
        self.assertEqual(self.packet["hypothesis_status"], "L1_design_intent_hypothesis")
        self.assertEqual(self.packet["decision_output"]["hypothesis_status"], "L1_design_intent_hypothesis")

    def test_all_required_creation_order_layers_present(self):
        self.assertEqual(
            [row["layer_name"] for row in self.packet["creation_order_matrix"]],
            REQUIRED_LAYERS,
        )
        for row in self.packet["creation_order_matrix"]:
            self.assertEqual(set(row), LAYER_KEYS)

    def test_creation_order_depth_is_strictly_increasing(self):
        depths = [row["creation_order_depth"] for row in self.packet["creation_order_matrix"]]
        self.assertEqual(depths, sorted(depths))
        self.assertEqual(len(depths), len(set(depths)))

    def test_genesis_boundary_flags_are_correct(self):
        axis = self.packet["design_intent_axis"]
        for key, value in HYPOTHESIS_BOUNDARY_FLAGS.items():
            self.assertIs(axis[key], value)

    def test_greek_and_generic_cosmology_are_excluded(self):
        boundary = self.packet["genesis_vs_generic_cosmology_boundary"]
        self.assertIs(boundary["greek_cosmology_not_intended_source_model"], True)
        self.assertIs(boundary["generic_cosmology_not_intended_source_model"], True)
        self.assertIs(boundary["thales_anaximander_model_excluded"], True)
        self.assertIs(boundary["religious_correctness_claimed"], False)

    def test_expected_layer_biases(self):
        bias = self.packet["c3_layer_depth_bias"]
        self.assertEqual(bias["light_sun_starfield"], "world_law_deep_frame_semantics_not_decoration")
        self.assertEqual(bias["world_frame_projection"], "core_interface_only")
        self.assertEqual(
            bias["dynamic_point_creatures"],
            "later_created_entities_with_reconstructable_semantics",
        )
        self.assertEqual(
            bias["selection_card_governance"],
            "governance_interface_cross_organ_semantics",
        )

    def test_hypothesis_does_not_replace_evidence_axes(self):
        use = self.packet["use_in_lithology_analysis"]
        self.assertIs(use["does_not_replace_git_history"], True)
        self.assertIs(use["does_not_replace_dependency_scan"], True)
        self.assertIs(use["does_not_replace_ablation_response"], True)
        self.assertIs(use["does_not_replace_lithology_model"], True)
        self.assertIs(use["does_not_authorize_extraction"], True)

    def test_guard_flags_remain_false(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["source_movement_authorized"], False)
        self.assertIs(decision["helper_module_creation_authorized"], False)
        self.assertIs(decision["runtime_merge_enabled"], False)
        self.assertIs(decision["generic_checker_blocking"], False)
        self.assertIs(decision["readiness_claimed"], False)
        self.assertIs(decision["religious_claim_made"], False)
        self.assertIs(decision["extraction_authorized"], False)

    def test_base_and_local_pattern_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["local_pattern_source"], "60cded8")

    def test_recommended_next_gate(self):
        self.assertEqual(
            self.packet["decision_output"]["recommended_next_gate"],
            "displaytools_canvas_creation_order_depth_hypothesis_validation_gate",
        )


if __name__ == "__main__":
    unittest.main()
