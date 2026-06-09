import unittest


REQUIRED_PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "design_intent_source",
    "validation_source",
    "hypothesis_status_before",
    "counterexample_search_matrix",
    "counterexample_summary",
    "model_limitations",
    "trust_level_after_counterexample_search",
    "use_in_future_lithology_work",
    "decision_output",
    "boundary_statement",
}

REQUIRED_COUNTEREXAMPLE_TYPES = {
    "early_layer_low_coupling_counterexample",
    "late_layer_core_coupling_counterexample",
    "world_law_as_decoration_counterexample",
    "creature_layer_core_law_counterexample",
    "governance_layer_not_cross_organ_counterexample",
    "terrain_not_world_body_counterexample",
    "boundary_not_naming_counterexample",
}

COUNTEREXAMPLE_KEYS = {
    "counterexample_type",
    "searched_subsystems",
    "evidence_observed",
    "counterexample_status",
    "impact_on_hypothesis",
    "recommended_adjustment",
    "evidence_limit",
}

VALID_COUNTEREXAMPLE_STATUSES = {
    "not_observed",
    "possible",
    "observed",
    "insufficient_evidence",
}


def build_displaytools_canvas_creation_order_depth_cross_subsystem_counterexample_packet():
    counterexample_search_matrix = [
        {
            "counterexample_type": "early_layer_low_coupling_counterexample",
            "searched_subsystems": [
                "solar_lighting_frame",
                "terrain_bathymetry_boundary",
            ],
            "evidence_observed": [
                "solar_lighting_descriptor_shells_are_static_only",
                "solar_boundary_still_blocks_compute_sun_direction_shader_formula_and_starfield_runtime",
                "terrain_boundary_has_descriptor_fixture_but_blocks_shader_sampling_projection_flip_mask_lighting_formula",
            ],
            "counterexample_status": "possible",
            "impact_on_hypothesis": (
                "early canvas layers can expose descriptor shells, so creation depth cannot be treated "
                "as a coupling verdict"
            ),
            "recommended_adjustment": (
                "keep L1 supported design intent status and record descriptor-shell exceptions for early layers"
            ),
            "evidence_limit": "static docs and tests only; solar and terrain runtime behavior not executed",
        },
        {
            "counterexample_type": "late_layer_core_coupling_counterexample",
            "searched_subsystems": [
                "dynamic_point_projection_interface_shadow",
                "dynamic_point_selection_render_policy",
                "dynamic_point_lithology_gates",
            ],
            "evidence_observed": [
                "dynamic_point_creatures_have_descriptor_sediment",
                "projection_flip_mask_sync_remains_core_interface_only",
                "controller_selection_picker_hit_test_remains_blocked_runtime_or_interface_pressure",
            ],
            "counterexample_status": "possible",
            "impact_on_hypothesis": (
                "later entity layers can attach to core seams, so the depth axis cannot override "
                "dependency pressure or lithology evidence"
            ),
            "recommended_adjustment": (
                "limit the axis to semantic bias and keep projection/controller seams governed by hard evidence"
            ),
            "evidence_limit": "static shadow and lithology gates only; projection and controller runtime not executed",
        },
        {
            "counterexample_type": "world_law_as_decoration_counterexample",
            "searched_subsystems": [
                "solar_lighting_frame",
                "projection_interface_shadow",
            ],
            "evidence_observed": [
                "solar_lighting_frame_blocks_formula_and_runtime_surfaces",
                "projection_interface_shadow_treats_world_frame_projection_as_core_interface_only",
                "no evidence that light_sun_starfield_is_only_decoration_in_existing_gates",
            ],
            "counterexample_status": "not_observed",
            "impact_on_hypothesis": (
                "current c3 gates still align light and world-frame surfaces with deep-frame semantics"
            ),
            "recommended_adjustment": "none; keep the decoration counterexample open as a future scout item",
            "evidence_limit": "absence of observed counterexample is not proof of design intent",
        },
        {
            "counterexample_type": "creature_layer_core_law_counterexample",
            "searched_subsystems": [
                "dynamic_point_boundary",
                "dynamic_point_projection_interface_shadow",
                "dynamic_point_recursive_lithology",
            ],
            "evidence_observed": [
                "dynamic_point_descriptor_helpers_support_later_entity_semantics",
                "dynamic_point_projection_seam_is_core_interface_only",
                "runtime_lineage_and_controller_surfaces_remain_blocked",
            ],
            "counterexample_status": "possible",
            "impact_on_hypothesis": (
                "moving entities can carry reconstructable descriptors while still depending on core laws at "
                "projection and runtime seams"
            ),
            "recommended_adjustment": (
                "split dynamic point semantic surfaces from projection/runtime seams before using the axis"
            ),
            "evidence_limit": "static helper and shadow evidence only; no live AIS or ADS-B runtime evidence",
        },
        {
            "counterexample_type": "governance_layer_not_cross_organ_counterexample",
            "searched_subsystems": [
                "selection_card_governance",
                "metadata_artifact_schema",
                "cross_organ_card_integration",
            ],
            "evidence_observed": [
                "metadata_artifact_schema_is_classified_as_schema_governance",
                "cross_organ_card_integration_is_classified_as_cross_organ_handoff",
                "selection_card_governance_remains_not_c3_only_extraction",
            ],
            "counterexample_status": "not_observed",
            "impact_on_hypothesis": (
                "current evidence continues to align governance and card surfaces with handoff or interface strategy"
            ),
            "recommended_adjustment": "none; keep o1 or cross-agent review as the governing path",
            "evidence_limit": "schema and cross-organ implementation not inspected or changed",
        },
        {
            "counterexample_type": "terrain_not_world_body_counterexample",
            "searched_subsystems": [
                "terrain_bathymetry_boundary",
                "terrain_bathymetry_fixture_gate",
            ],
            "evidence_observed": [
                "terrain_bathymetry_boundary_blocks_shader_sampling_projection_flip_mask_lighting_formula",
                "terrain_provider_cache_and_visual_faults_remain_unmoved",
                "no current fixture treats terrain_as_low_coupling_world_decoration_only",
            ],
            "counterexample_status": "not_observed",
            "impact_on_hypothesis": "terrain still fits world-body or high-coupling bias in current c3 evidence",
            "recommended_adjustment": "none; keep terrain high-coupling evidence as static-only",
            "evidence_limit": "terrain rendering and visual quality not executed",
        },
        {
            "counterexample_type": "boundary_not_naming_counterexample",
            "searched_subsystems": [
                "vector_overlay_boundary",
                "vector_boundary_naming",
            ],
            "evidence_observed": [
                "vector_overlay_minimal_extraction_keeps_descriptor_policy_ledger_only",
                "provider_cache_projection_mask_controller_runtime_stay_blocked",
                "boundary_specs_and_hydrology_specs_remain_semantic_geography_descriptors",
            ],
            "counterexample_status": "not_observed",
            "impact_on_hypothesis": (
                "current vector overlay evidence still aligns boundary layers with semantic geography and naming"
            ),
            "recommended_adjustment": "none; do not generalize vector descriptor success to runtime or projection",
            "evidence_limit": "vector provider and projection runtime not executed",
        },
    ]

    direct_counterexample_observed = any(
        row["counterexample_status"] == "observed" for row in counterexample_search_matrix
    )
    possible_counterexample_count = sum(
        1 for row in counterexample_search_matrix if row["counterexample_status"] == "possible"
    )
    trust_after = (
        "L1_design_intent_hypothesis_with_counterexamples"
        if direct_counterexample_observed
        else "L1_supported_design_intent_hypothesis"
    )

    return {
        "schema": "rrkal.displaytools.canvas_creation_order_depth_cross_subsystem_counterexample.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "design_intent_source": "e874ece",
        "validation_source": "f1213c1",
        "hypothesis_status_before": "L1_supported_design_intent_hypothesis",
        "counterexample_search_matrix": counterexample_search_matrix,
        "counterexample_summary": {
            "direct_counterexample_observed": direct_counterexample_observed,
            "possible_counterexample_count": possible_counterexample_count,
            "not_observed_counterexample_count": sum(
                1 for row in counterexample_search_matrix if row["counterexample_status"] == "not_observed"
            ),
            "counterexample_search_is_not_reinforcement_only": True,
            "trust_behavior": (
                "direct observed counterexample would downgrade; possible counterexamples add limitations only"
            ),
        },
        "model_limitations": [
            "early layers can expose descriptor shells without proving low coupling",
            "late dynamic point surfaces can still attach to projection or controller core seams",
            "absence of observed counterexample is not proof of subconscious design intent",
            "creation order depth is secondary to git history dependency pressure ablation and lithology gates",
            "static scan does not execute renderer runtime or data sources",
        ],
        "trust_level_after_counterexample_search": trust_after,
        "use_in_future_lithology_work": {
            "allowed_use": "secondary_design_intent_axis_with_counterexample_limitations",
            "does_not_replace_git_history": True,
            "does_not_replace_dependency_scan": True,
            "does_not_replace_ablation_response": True,
            "does_not_replace_lithology_model": True,
            "does_not_authorize_extraction": True,
        },
        "decision_output": {
            "counterexample_gate_passed": True,
            "trust_level_before": "L1_supported_design_intent_hypothesis",
            "trust_level_after": trust_after,
            "l2_local_pattern_authorized": False,
            "universal_doctrine_authorized": False,
            "religious_correctness_claimed": False,
            "subconscious_design_intent_fully_proven": False,
            "evidence_replacement_claimed": False,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "readiness_claimed": False,
            "recommended_next_gate": "dynamic_point_projection_interface_shadow_import_boundary_checker_gate",
        },
        "boundary_statement": (
            "Docs/test-only displaytools canvas creation order depth cross-subsystem counterexample gate. "
            "No helper module creation, no source movement, no production source change, no checker script creation, "
            "no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, "
            "no generic profile change, no monolith import, no runtime execution, no SQL/WebSocket/live-source execution, "
            "no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, "
            "no projection/flip/mask/solar/lighting/terrain/vector/dynamic-point behavior change, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, "
            "no cross-organ integration implementation, no religious correctness claim, "
            "no subconscious design intent proof claim, no evidence replacement claim, "
            "no L2 local pattern or universal doctrine promotion, no runtime merge enablement, "
            "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class CanvasCreationOrderDepthCrossSubsystemCounterexampleTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_displaytools_canvas_creation_order_depth_cross_subsystem_counterexample_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), REQUIRED_PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.canvas_creation_order_depth_cross_subsystem_counterexample.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["design_intent_source"], "e874ece")
        self.assertEqual(self.packet["validation_source"], "f1213c1")

    def test_all_required_counterexample_classes_present(self):
        observed = {
            row["counterexample_type"] for row in self.packet["counterexample_search_matrix"]
        }
        self.assertEqual(observed, REQUIRED_COUNTEREXAMPLE_TYPES)

    def test_counterexample_rows_have_required_shape(self):
        for row in self.packet["counterexample_search_matrix"]:
            self.assertEqual(set(row), COUNTEREXAMPLE_KEYS)
            self.assertIn(row["counterexample_status"], VALID_COUNTEREXAMPLE_STATUSES)
            self.assertTrue(row["searched_subsystems"])
            self.assertTrue(row["evidence_observed"])
            self.assertTrue(row["impact_on_hypothesis"])
            self.assertTrue(row["recommended_adjustment"])
            self.assertTrue(row["evidence_limit"])

    def test_trust_behavior_follows_counterexample_results(self):
        statuses = {
            row["counterexample_status"] for row in self.packet["counterexample_search_matrix"]
        }
        decision = self.packet["decision_output"]
        if "observed" in statuses:
            self.assertEqual(
                self.packet["trust_level_after_counterexample_search"],
                "L1_design_intent_hypothesis_with_counterexamples",
            )
        else:
            self.assertEqual(
                self.packet["trust_level_after_counterexample_search"],
                "L1_supported_design_intent_hypothesis",
            )
        self.assertEqual(
            self.packet["trust_level_after_counterexample_search"],
            decision["trust_level_after"],
        )

    def test_possible_counterexamples_remain_limitations(self):
        possible = [
            row
            for row in self.packet["counterexample_search_matrix"]
            if row["counterexample_status"] == "possible"
        ]
        self.assertGreaterEqual(len(possible), 1)
        self.assertEqual(
            self.packet["trust_level_after_counterexample_search"],
            "L1_supported_design_intent_hypothesis",
        )
        self.assertIn("early layers can expose descriptor shells without proving low coupling", self.packet["model_limitations"])
        self.assertIn(
            "late dynamic point surfaces can still attach to projection or controller core seams",
            self.packet["model_limitations"],
        )

    def test_decision_output_blocks_l2_universal_and_implementation_claims(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["counterexample_gate_passed"])
        self.assertEqual(decision["trust_level_before"], "L1_supported_design_intent_hypothesis")
        self.assertFalse(decision["l2_local_pattern_authorized"])
        self.assertFalse(decision["universal_doctrine_authorized"])
        self.assertFalse(decision["religious_correctness_claimed"])
        self.assertFalse(decision["subconscious_design_intent_fully_proven"])
        self.assertFalse(decision["evidence_replacement_claimed"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["generic_checker_blocking"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_projection_interface_shadow_import_boundary_checker_gate",
        )

    def test_future_use_does_not_replace_hard_evidence(self):
        future_use = self.packet["use_in_future_lithology_work"]
        self.assertEqual(
            future_use["allowed_use"],
            "secondary_design_intent_axis_with_counterexample_limitations",
        )
        self.assertTrue(future_use["does_not_replace_git_history"])
        self.assertTrue(future_use["does_not_replace_dependency_scan"])
        self.assertTrue(future_use["does_not_replace_ablation_response"])
        self.assertTrue(future_use["does_not_replace_lithology_model"])
        self.assertTrue(future_use["does_not_authorize_extraction"])


if __name__ == "__main__":
    unittest.main()
