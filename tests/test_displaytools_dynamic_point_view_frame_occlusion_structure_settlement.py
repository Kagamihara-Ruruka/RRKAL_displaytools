import unittest


SETTLEMENT_SURFACES = {
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

SETTLED_CLASSIFICATIONS = {
    "core_lineage_view_frame_semantics",
    "core_interface_only",
    "andesite_bridge_semantics",
    "presentation_contract_candidate",
    "source_lineage_guard",
    "computed_but_hidden_semantics",
    "unresolved_static_fault",
    "forbidden_pollution_path",
    "not_settled_evidence_gap",
}

NEXT_STRATEGIES = {
    "shadow_interface_only",
    "semantic_reconstruction_before_rebuild",
    "presentation_contract_planning",
    "source_lineage_guard_only",
    "runtime_characterization_planning",
    "forbidden_path_stop",
    "evidence_gap_review",
}

SURFACE_KEYS = {
    "surface",
    "primary_evidence",
    "auxiliary_creation_order_alignment",
    "settled_classification",
    "allowed_next_strategy",
    "forbidden_next_strategy",
    "runtime_characterization_needed",
    "helper_extraction_authorized",
    "formula_movement_authorized",
    "source_lineage_pollution_allowed",
    "coordinate_correctness_claimed",
    "visual_correctness_claimed",
    "settlement_confidence",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "dynamic_point_lithology_l2_local_pattern_source",
    "creation_order_auxiliary_source",
    "creation_order_counterexample_source",
    "projection_shadow_source",
    "evidence_streams",
    "settlement_matrix",
    "interpretation_rules",
    "creation_order_auxiliary_axis_rules",
    "decision_output",
    "boundary_statement",
}


def _surface(
    surface,
    evidence,
    creation_alignment,
    classification,
    allowed_strategy,
    forbidden_strategy,
    runtime_needed,
    confidence,
):
    return {
        "surface": surface,
        "primary_evidence": evidence,
        "auxiliary_creation_order_alignment": creation_alignment,
        "settled_classification": classification,
        "allowed_next_strategy": allowed_strategy,
        "forbidden_next_strategy": forbidden_strategy,
        "runtime_characterization_needed": runtime_needed,
        "helper_extraction_authorized": False,
        "formula_movement_authorized": False,
        "source_lineage_pollution_allowed": False,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "settlement_confidence": confidence,
    }


def build_dynamic_point_view_frame_occlusion_structure_settlement_packet():
    settlement_matrix = [
        _surface(
            "zoom_rotation_view_state",
            [
                "monkey_ablation_matrix_evidence",
                "core_lineage_validation_evidence",
                "token_trace_matrix_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "world_frame_projection_depth_aligns_as_auxiliary_not_primary",
            "core_lineage_view_frame_semantics",
            "runtime_characterization_planning",
            ["ordinary_helper_extraction", "source_lineage_mutation", "renderer_runtime_execution"],
            True,
            "high",
        ),
        _surface(
            "lod_policy",
            [
                "monkey_ablation_matrix_evidence",
                "token_trace_matrix_evidence",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "dynamic_point_creatures_depth_allows_later_presentation_bridge_as_auxiliary",
            "andesite_bridge_semantics",
            "semantic_reconstruction_before_rebuild",
            ["direct_code_transplant", "source_filter_reclassification", "provider_cache_database_mutation"],
            True,
            "medium_high",
        ),
        _surface(
            "globe_angle_frame_state",
            [
                "monkey_ablation_matrix_evidence",
                "core_lineage_validation_evidence",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "world_frame_projection_depth_supports_core_view_frame_bias_as_auxiliary",
            "core_lineage_view_frame_semantics",
            "runtime_characterization_planning",
            ["ordinary_helper_extraction", "coordinate_correctness_claim", "formula_movement"],
            True,
            "high",
        ),
        _surface(
            "projection_shadow",
            [
                "projection_shadow_source",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "world_frame_projection_aligns_with_core_interface_only_as_auxiliary",
            "core_interface_only",
            "shadow_interface_only",
            ["projection_formula_movement", "flip_formula_movement", "mask_formula_movement"],
            False,
            "high",
        ),
        _surface(
            "occlusion_policy",
            [
                "monkey_ablation_matrix_evidence",
                "core_lineage_validation_evidence",
                "token_trace_matrix_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "dynamic_point_creatures_depth_supports_visibility_policy_as_auxiliary",
            "andesite_bridge_semantics",
            "semantic_reconstruction_before_rebuild",
            ["source_lineage_mutation", "source_filter_reclassification", "visual_correctness_claim"],
            True,
            "medium_high",
        ),
        _surface(
            "presentation_policy",
            [
                "monkey_ablation_matrix_evidence",
                "token_trace_matrix_evidence",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "selection_card_governance_depth_supports_contract_planning_as_auxiliary",
            "presentation_contract_candidate",
            "presentation_contract_planning",
            ["provider_data_mutation", "source_lineage_pollution", "performance_claim"],
            True,
            "medium_high",
        ),
        _surface(
            "source_lineage_integrity",
            [
                "monkey_ablation_matrix_evidence",
                "token_trace_matrix_evidence",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "dynamic_point_creatures_depth_does_not_override_source_identity_guard",
            "source_lineage_guard",
            "source_lineage_guard_only",
            ["lod_reverse_pollution", "occlusion_reverse_pollution", "presentation_reverse_pollution"],
            False,
            "high",
        ),
        _surface(
            "computed_but_hidden_point",
            [
                "monkey_ablation_matrix_evidence",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "dynamic_point_creatures_depth_supports_hidden_visibility_as_later_entity_state",
            "computed_but_hidden_semantics",
            "presentation_contract_planning",
            ["hidden_to_missing_source", "occlusion_as_source_filter", "source_lineage_mutation"],
            True,
            "high",
        ),
        _surface(
            "transparent_globe_leak_fault",
            [
                "monkey_ablation_matrix_evidence",
                "core_lineage_validation_evidence",
                "token_trace_lithology_transition_evidence",
                "ablation_conditioned_token_trace_evidence",
            ],
            "world_frame_projection_depth_supports_fault_near_core_view_frame_as_auxiliary",
            "unresolved_static_fault",
            "evidence_gap_review",
            ["visual_correctness_claim", "transparent_globe_leak_fix_claim", "runtime_probe_authorization"],
            False,
            "medium",
        ),
    ]

    return {
        "schema": "rrkal.displaytools.dynamic_point_view_frame_occlusion_structure_settlement.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "dynamic_point_lithology_l2_local_pattern_source": "60cded8",
        "creation_order_auxiliary_source": "f1213c1",
        "creation_order_counterexample_source": "53afb98",
        "projection_shadow_source": "6289c60",
        "evidence_streams": {
            "monkey_ablation_matrix_evidence": "8b5cac7",
            "core_lineage_validation_evidence": "bbd978d",
            "token_trace_matrix_evidence": "373da1e",
            "token_trace_lithology_transition_evidence": "9c0a40e",
            "ablation_conditioned_token_trace_evidence": "c7d329c",
            "creation_order_auxiliary_axis": ["f1213c1", "53afb98"],
        },
        "settlement_matrix": settlement_matrix,
        "interpretation_rules": {
            "core_lineage_view_frame_semantics": {
                "allowed": ["shadow_interface_only", "runtime_characterization_planning"],
                "ordinary_helper_extraction_authorized": False,
            },
            "core_interface_only": {
                "formula_movement_authorized": False,
                "allowed": ["reference", "ledger", "shadow_interface"],
            },
            "andesite_bridge_semantics": {
                "semantic_reconstruction_required": True,
                "direct_old_code_transplant_authorized": False,
            },
            "presentation_contract_candidate": {
                "presentation_contract_planning_allowed": True,
                "source_lineage_pollution_allowed": False,
            },
            "source_lineage_guard": {
                "identity_guard_only": True,
                "lod_occlusion_presentation_reverse_mutation_allowed": False,
            },
            "computed_but_hidden_semantics": {
                "hidden_equals_missing": False,
                "occlusion_is_source_filter": False,
            },
            "unresolved_static_fault": {
                "transparent_globe_leak_fix_claimed": False,
            },
            "forbidden_pollution_path": {
                "runtime_probe_allowed": False,
                "required_strategy": "forbidden_path_stop",
            },
        },
        "creation_order_auxiliary_axis_rules": {
            "can_align_layer_depth_with_token_path": True,
            "creation_order_is_primary_evidence": False,
            "implementation_authorized_by_creation_order": False,
            "religious_correctness_claimed": False,
            "subconscious_design_intent_fully_proven": False,
        },
        "decision_output": {
            "structure_settlement_gate_passed": True,
            "view_frame_occlusion_structure_settled": True,
            "ordinary_helper_extraction_authorized": False,
            "shadow_interface_path_required": True,
            "semantic_reconstruction_required_for_andesite": True,
            "presentation_contract_candidate_present": True,
            "source_lineage_guard_required": True,
            "runtime_characterization_planning_candidate": True,
            "runtime_characterization_authorized": False,
            "instrumentation_authorized": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "renderer_runtime_authorized": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "performance_claimed": False,
            "transparent_globe_leak_fix_claimed": False,
            "semantic_seismic_tomography_local_pattern_supported": True,
            "semantic_seismic_tomography_global_methodology_authorized": False,
            "creation_order_auxiliary_axis_aligned": True,
            "creation_order_is_primary_evidence": False,
            "implementation_authorized_by_creation_order": False,
            "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point view-frame occlusion structure settlement gate. "
            "No helper module creation, no source movement, no production source change, "
            "no existing monkey/token/lithology/core-lineage gate change, no checker script change, "
            "no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, "
            "no monolith import, no runtime execution, no instrumentation, no sys.settrace, no debugger/IDE automation, "
            "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, "
            "no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, "
            "no transparent-globe leak fix claim, no runtime characterization authorization, "
            "no token-trace global methodology authorization, no semantic-seismic-tomography global methodology authorization, "
            "no creation-order primary-evidence/religious-correctness claim, no runtime merge enablement, "
            "and no readiness/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointViewFrameOcclusionStructureSettlementTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_view_frame_occlusion_structure_settlement_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_view_frame_occlusion_structure_settlement.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["dynamic_point_lithology_l2_local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["creation_order_auxiliary_source"], "f1213c1")
        self.assertEqual(self.packet["creation_order_counterexample_source"], "53afb98")
        self.assertEqual(self.packet["projection_shadow_source"], "6289c60")

    def test_required_evidence_streams_integrated(self):
        streams = self.packet["evidence_streams"]
        self.assertEqual(streams["monkey_ablation_matrix_evidence"], "8b5cac7")
        self.assertEqual(streams["core_lineage_validation_evidence"], "bbd978d")
        self.assertEqual(streams["token_trace_matrix_evidence"], "373da1e")
        self.assertEqual(streams["token_trace_lithology_transition_evidence"], "9c0a40e")
        self.assertEqual(streams["ablation_conditioned_token_trace_evidence"], "c7d329c")
        self.assertEqual(streams["creation_order_auxiliary_axis"], ["f1213c1", "53afb98"])

    def test_required_surfaces_are_settled(self):
        surfaces = {row["surface"] for row in self.packet["settlement_matrix"]}
        self.assertEqual(surfaces, SETTLEMENT_SURFACES)
        for row in self.packet["settlement_matrix"]:
            self.assertEqual(set(row), SURFACE_KEYS)
            self.assertIn(row["settled_classification"], SETTLED_CLASSIFICATIONS)
            self.assertIn(row["allowed_next_strategy"], NEXT_STRATEGIES)
            self.assertFalse(row["helper_extraction_authorized"])
            self.assertFalse(row["formula_movement_authorized"])
            self.assertFalse(row["source_lineage_pollution_allowed"])
            self.assertFalse(row["coordinate_correctness_claimed"])
            self.assertFalse(row["visual_correctness_claimed"])

    def test_final_settled_classifications(self):
        rows = self._rows()
        self.assertEqual(rows["zoom_rotation_view_state"]["settled_classification"], "core_lineage_view_frame_semantics")
        self.assertEqual(rows["globe_angle_frame_state"]["settled_classification"], "core_lineage_view_frame_semantics")
        self.assertEqual(rows["projection_shadow"]["settled_classification"], "core_interface_only")
        self.assertEqual(rows["lod_policy"]["settled_classification"], "andesite_bridge_semantics")
        self.assertEqual(rows["occlusion_policy"]["settled_classification"], "andesite_bridge_semantics")
        self.assertEqual(rows["presentation_policy"]["settled_classification"], "presentation_contract_candidate")
        self.assertEqual(rows["source_lineage_integrity"]["settled_classification"], "source_lineage_guard")
        self.assertEqual(rows["computed_but_hidden_point"]["settled_classification"], "computed_but_hidden_semantics")
        self.assertEqual(rows["transparent_globe_leak_fault"]["settled_classification"], "unresolved_static_fault")

    def test_allowed_and_forbidden_strategies(self):
        rows = self._rows()
        self.assertEqual(rows["projection_shadow"]["allowed_next_strategy"], "shadow_interface_only")
        self.assertIn("projection_formula_movement", rows["projection_shadow"]["forbidden_next_strategy"])
        self.assertEqual(rows["lod_policy"]["allowed_next_strategy"], "semantic_reconstruction_before_rebuild")
        self.assertIn("direct_code_transplant", rows["lod_policy"]["forbidden_next_strategy"])
        self.assertEqual(rows["presentation_policy"]["allowed_next_strategy"], "presentation_contract_planning")
        self.assertIn("source_lineage_pollution", rows["presentation_policy"]["forbidden_next_strategy"])
        self.assertEqual(rows["source_lineage_integrity"]["allowed_next_strategy"], "source_lineage_guard_only")
        self.assertEqual(rows["transparent_globe_leak_fault"]["allowed_next_strategy"], "evidence_gap_review")

    def test_interpretation_rules_enforce_stop_lines(self):
        rules = self.packet["interpretation_rules"]
        self.assertFalse(rules["core_lineage_view_frame_semantics"]["ordinary_helper_extraction_authorized"])
        self.assertFalse(rules["core_interface_only"]["formula_movement_authorized"])
        self.assertTrue(rules["andesite_bridge_semantics"]["semantic_reconstruction_required"])
        self.assertFalse(rules["andesite_bridge_semantics"]["direct_old_code_transplant_authorized"])
        self.assertTrue(rules["presentation_contract_candidate"]["presentation_contract_planning_allowed"])
        self.assertFalse(rules["presentation_contract_candidate"]["source_lineage_pollution_allowed"])
        self.assertTrue(rules["source_lineage_guard"]["identity_guard_only"])
        self.assertFalse(rules["computed_but_hidden_semantics"]["hidden_equals_missing"])
        self.assertFalse(rules["computed_but_hidden_semantics"]["occlusion_is_source_filter"])
        self.assertFalse(rules["unresolved_static_fault"]["transparent_globe_leak_fix_claimed"])
        self.assertFalse(rules["forbidden_pollution_path"]["runtime_probe_allowed"])

    def test_creation_order_is_auxiliary_only(self):
        rules = self.packet["creation_order_auxiliary_axis_rules"]
        self.assertTrue(rules["can_align_layer_depth_with_token_path"])
        self.assertFalse(rules["creation_order_is_primary_evidence"])
        self.assertFalse(rules["implementation_authorized_by_creation_order"])
        self.assertFalse(rules["religious_correctness_claimed"])
        self.assertFalse(rules["subconscious_design_intent_fully_proven"])
        decision = self.packet["decision_output"]
        self.assertTrue(decision["creation_order_auxiliary_axis_aligned"])
        self.assertFalse(decision["creation_order_is_primary_evidence"])
        self.assertFalse(decision["implementation_authorized_by_creation_order"])

    def test_decision_output_settles_structure_without_authorization(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["structure_settlement_gate_passed"])
        self.assertTrue(decision["view_frame_occlusion_structure_settled"])
        self.assertFalse(decision["ordinary_helper_extraction_authorized"])
        self.assertTrue(decision["shadow_interface_path_required"])
        self.assertTrue(decision["semantic_reconstruction_required_for_andesite"])
        self.assertTrue(decision["presentation_contract_candidate_present"])
        self.assertTrue(decision["source_lineage_guard_required"])
        self.assertTrue(decision["runtime_characterization_planning_candidate"])
        self.assertFalse(decision["runtime_characterization_authorized"])
        self.assertFalse(decision["instrumentation_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["formula_movement_authorized"])
        self.assertFalse(decision["renderer_runtime_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["performance_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertTrue(decision["semantic_seismic_tomography_local_pattern_supported"])
        self.assertFalse(decision["semantic_seismic_tomography_global_methodology_authorized"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        )

    def test_runtime_characterization_rows_are_planning_only(self):
        rows = self._rows()
        runtime_surfaces = {
            surface for surface, row in rows.items() if row["runtime_characterization_needed"]
        }
        self.assertIn("zoom_rotation_view_state", runtime_surfaces)
        self.assertIn("globe_angle_frame_state", runtime_surfaces)
        self.assertIn("occlusion_policy", runtime_surfaces)
        self.assertIn("presentation_policy", runtime_surfaces)
        self.assertFalse(self.packet["decision_output"]["runtime_characterization_authorized"])

    def test_transparent_globe_fault_remains_unresolved(self):
        row = self._rows()["transparent_globe_leak_fault"]
        self.assertEqual(row["settled_classification"], "unresolved_static_fault")
        self.assertIn("transparent_globe_leak_fix_claim", row["forbidden_next_strategy"])
        self.assertFalse(self.packet["decision_output"]["transparent_globe_leak_fix_claimed"])

    def test_boundary_statement_contains_required_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no existing monkey/token/lithology/core-lineage gate change", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no instrumentation", boundary)
        self.assertIn("no sys.settrace", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no runtime characterization authorization", boundary)
        self.assertIn("no creation-order primary-evidence/religious-correctness claim", boundary)

    def _rows(self):
        return {row["surface"]: row for row in self.packet["settlement_matrix"]}


if __name__ == "__main__":
    unittest.main()
