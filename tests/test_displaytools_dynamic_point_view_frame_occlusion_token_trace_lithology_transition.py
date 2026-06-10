import unittest


REQUIRED_LITHOLOGY_LABELS = {
    "core_lineage",
    "core_interface_only",
    "andesite_bridge",
    "presentation_policy",
    "source_lineage_guard",
    "computed_but_hidden",
    "unresolved_static_fault",
    "forbidden_pollution",
    "not_enough_evidence",
}

REQUIRED_TRANSITIONS = {
    "core_lineage_to_core_lineage",
    "core_lineage_to_core_interface",
    "core_lineage_to_andesite_bridge",
    "andesite_to_presentation_policy",
    "presentation_to_source_lineage_forbidden",
    "payload_to_core_formula_forbidden",
    "source_lineage_preserved",
    "computed_to_hidden_visibility",
    "fault_remains_unresolved",
    "not_enough_evidence",
}

REQUIRED_SEMANTIC_AGE_LABELS = {
    "deep_core_semantics",
    "core_interface_semantics",
    "older_bridge_semantics",
    "presentation_surface_semantics",
    "source_lineage_identity_preserved",
    "visibility_not_existence_semantics",
    "forbidden_reverse_pollution",
    "unresolved_fault_semantics",
    "not_enough_evidence",
}

RECOMMENDED_STRATEGIES = {
    "shadow_interface_only",
    "semantic_reconstruction_candidate",
    "presentation_contract_candidate",
    "source_lineage_guard_only",
    "runtime_characterization_candidate",
    "forbidden_path_stop",
    "evidence_gap_review",
}

REQUIRED_COMBOS = {
    ("zoom_entry", "zoom_token"),
    ("rotation_entry", "rotation_token"),
    ("lod_policy_entry", "lod_token"),
    ("globe_angle_frame_entry", "globe_angle_token"),
    ("projection_shadow_entry", "projection_policy_ref_token"),
    ("point_payload_entry", "point_id_token"),
    ("point_payload_entry", "coordinate_payload_token"),
    ("occlusion_policy_entry", "occlusion_visibility_token"),
    ("presentation_policy_entry", "presentation_visibility_token"),
    ("source_lineage_entry", "source_lineage_token"),
}

ROW_KEYS = {
    "entrypoint",
    "token",
    "mode",
    "expected_path",
    "lithology_sequence",
    "lithology_transition",
    "semantic_age_inference",
    "recommended_strategy",
    "runtime_probe_needed",
    "source_lineage_pollution_allowed",
    "coordinate_correctness_claimed",
    "visual_correctness_claimed",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "dynamic_point_lithology_l2_local_pattern_source",
    "projection_shadow_source",
    "view_frame_occlusion_monkey_matrix",
    "core_lineage_validation_source",
    "token_trace_matrix_source",
    "prior_gate_inputs",
    "lithology_labels",
    "lithology_transitions",
    "semantic_age_inference_labels",
    "transition_rules",
    "transition_matrix",
    "decision_output",
    "boundary_statement",
}


def _transition_rows():
    return [
        {
            "entrypoint": "zoom_entry",
            "token": "zoom_token",
            "mode": "token_trace_mode",
            "expected_path": ["zoom_state", "lod_policy", "view_frame_label"],
            "lithology_sequence": ["core_lineage", "andesite_bridge"],
            "lithology_transition": "core_lineage_to_andesite_bridge",
            "semantic_age_inference": "older_bridge_semantics",
            "recommended_strategy": "semantic_reconstruction_candidate",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "rotation_entry",
            "token": "rotation_token",
            "mode": "token_trace_mode",
            "expected_path": ["rotation_state", "globe_angle_frame", "occlusion_decision_label"],
            "lithology_sequence": ["core_lineage", "core_lineage"],
            "lithology_transition": "core_lineage_to_core_lineage",
            "semantic_age_inference": "deep_core_semantics",
            "recommended_strategy": "shadow_interface_only",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "lod_policy_entry",
            "token": "lod_token",
            "mode": "token_trace_mode",
            "expected_path": ["lod_policy", "sampling_label", "presentation_label"],
            "lithology_sequence": ["andesite_bridge", "presentation_policy"],
            "lithology_transition": "andesite_to_presentation_policy",
            "semantic_age_inference": "presentation_surface_semantics",
            "recommended_strategy": "presentation_contract_candidate",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "globe_angle_frame_entry",
            "token": "globe_angle_token",
            "mode": "token_trace_mode",
            "expected_path": ["globe_angle_frame", "occlusion_label"],
            "lithology_sequence": ["core_lineage", "andesite_bridge"],
            "lithology_transition": "core_lineage_to_andesite_bridge",
            "semantic_age_inference": "older_bridge_semantics",
            "recommended_strategy": "runtime_characterization_candidate",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "projection_shadow_entry",
            "token": "projection_policy_ref_token",
            "mode": "token_trace_mode",
            "expected_path": ["projection_shadow", "policy_ref_label", "stop_condition_ledger"],
            "lithology_sequence": ["core_lineage", "core_interface_only"],
            "lithology_transition": "core_lineage_to_core_interface",
            "semantic_age_inference": "core_interface_semantics",
            "recommended_strategy": "shadow_interface_only",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "point_payload_entry",
            "token": "point_id_token",
            "mode": "token_trace_mode",
            "expected_path": ["point_identity", "source_lineage_identity", "hidden_visibility_allowed"],
            "lithology_sequence": ["source_lineage_guard", "source_lineage_guard"],
            "lithology_transition": "source_lineage_preserved",
            "semantic_age_inference": "source_lineage_identity_preserved",
            "recommended_strategy": "source_lineage_guard_only",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "point_payload_entry",
            "token": "coordinate_payload_token",
            "mode": "token_trace_mode",
            "expected_path": ["coordinate_payload", "computed_hidden_uncertainty_label"],
            "lithology_sequence": ["computed_but_hidden", "presentation_policy"],
            "lithology_transition": "computed_to_hidden_visibility",
            "semantic_age_inference": "visibility_not_existence_semantics",
            "recommended_strategy": "runtime_characterization_candidate",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "occlusion_policy_entry",
            "token": "occlusion_visibility_token",
            "mode": "token_trace_mode",
            "expected_path": ["occlusion_policy", "visibility_label"],
            "lithology_sequence": ["andesite_bridge", "presentation_policy"],
            "lithology_transition": "andesite_to_presentation_policy",
            "semantic_age_inference": "presentation_surface_semantics",
            "recommended_strategy": "presentation_contract_candidate",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "presentation_policy_entry",
            "token": "presentation_visibility_token",
            "mode": "token_trace_mode",
            "expected_path": ["presentation_policy", "rendered_visibility_label"],
            "lithology_sequence": ["presentation_policy", "source_lineage_guard", "forbidden_pollution"],
            "lithology_transition": "presentation_to_source_lineage_forbidden",
            "semantic_age_inference": "forbidden_reverse_pollution",
            "recommended_strategy": "forbidden_path_stop",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "source_lineage_entry",
            "token": "source_lineage_token",
            "mode": "token_trace_mode",
            "expected_path": ["source_lineage_identity", "provider_lineage_guard"],
            "lithology_sequence": ["source_lineage_guard", "source_lineage_guard"],
            "lithology_transition": "source_lineage_preserved",
            "semantic_age_inference": "source_lineage_identity_preserved",
            "recommended_strategy": "source_lineage_guard_only",
            "runtime_probe_needed": True,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "projection_shadow_entry",
            "token": "coordinate_payload_token",
            "mode": "tripwire_mode",
            "expected_path": ["coordinate_payload", "projection_formula_stop_line"],
            "lithology_sequence": ["computed_but_hidden", "core_interface_only", "forbidden_pollution"],
            "lithology_transition": "payload_to_core_formula_forbidden",
            "semantic_age_inference": "forbidden_reverse_pollution",
            "recommended_strategy": "forbidden_path_stop",
            "runtime_probe_needed": False,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "occlusion_policy_entry",
            "token": "presentation_visibility_token",
            "mode": "tripwire_mode",
            "expected_path": ["transparent_globe_leak_fault", "known_fault_ledger"],
            "lithology_sequence": ["unresolved_static_fault"],
            "lithology_transition": "fault_remains_unresolved",
            "semantic_age_inference": "unresolved_fault_semantics",
            "recommended_strategy": "evidence_gap_review",
            "runtime_probe_needed": False,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
        {
            "entrypoint": "zoom_entry",
            "token": "source_lineage_token",
            "mode": "null_mode",
            "expected_path": ["no_activation", "baseline_static_packet"],
            "lithology_sequence": ["not_enough_evidence"],
            "lithology_transition": "not_enough_evidence",
            "semantic_age_inference": "not_enough_evidence",
            "recommended_strategy": "evidence_gap_review",
            "runtime_probe_needed": False,
            "source_lineage_pollution_allowed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
        },
    ]


def build_dynamic_point_view_frame_occlusion_token_trace_lithology_transition_packet():
    return {
        "schema": "rrkal.displaytools.dynamic_point_view_frame_occlusion_token_trace_lithology_transition.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "dynamic_point_lithology_l2_local_pattern_source": "60cded8",
        "projection_shadow_source": "6289c60",
        "view_frame_occlusion_monkey_matrix": "8b5cac7",
        "core_lineage_validation_source": "bbd978d",
        "token_trace_matrix_source": "373da1e",
        "prior_gate_inputs": {
            "token_trace_mode_local_pilot": True,
            "token_trace_mode_global_methodology_authorized": False,
            "runtime_probe_candidate": True,
            "runtime_probe_authorized": False,
            "instrumentation_authorized": False,
            "source_lineage_pollution_allowed": False,
        },
        "lithology_labels": sorted(REQUIRED_LITHOLOGY_LABELS),
        "lithology_transitions": sorted(REQUIRED_TRANSITIONS),
        "semantic_age_inference_labels": sorted(REQUIRED_SEMANTIC_AGE_LABELS),
        "transition_rules": {
            "core_lineage_to_core_lineage": {
                "meaning": "signal_likely_moves_inside_core_law",
                "ordinary_helper_extraction_authorized": False,
                "preferred_strategy": "shadow_interface_only",
            },
            "core_lineage_to_core_interface": {
                "meaning": "signal_reaches_formula_or_frame_interface",
                "formula_movement_authorized": False,
                "preferred_strategy": "shadow_interface_only",
            },
            "core_lineage_to_andesite_bridge": {
                "meaning": "core_semantics_flow_to_older_bridge_layer",
                "implementation_transplant_authorized": False,
                "preferred_strategy": "semantic_reconstruction_candidate",
            },
            "andesite_to_presentation_policy": {
                "meaning": "bridge_converts_view_frame_semantics_to_display_strategy",
                "preferred_strategy": "presentation_contract_candidate",
            },
            "presentation_to_source_lineage_forbidden": {
                "meaning": "reverse_pollution_into_source_lineage",
                "pollution_allowed": False,
                "preferred_strategy": "forbidden_path_stop",
            },
            "source_lineage_preserved": {
                "meaning": "source_identity_preserved_and_hidden_is_not_missing",
                "pollution_allowed": False,
                "preferred_strategy": "source_lineage_guard_only",
            },
            "computed_to_hidden_visibility": {
                "meaning": "point_exists_but_current_visibility_is_hidden",
                "hidden_becomes_missing_source": False,
                "preferred_strategy": "runtime_characterization_candidate",
            },
            "fault_remains_unresolved": {
                "meaning": "transparent_globe_leak_or_static_fault_is_not_fixed",
                "fix_claimed": False,
                "preferred_strategy": "evidence_gap_review",
            },
        },
        "transition_matrix": _transition_rows(),
        "decision_output": {
            "lithology_transition_gate_passed": True,
            "token_trace_mode_local_pilot": True,
            "token_trace_mode_global_methodology_authorized": False,
            "semantic_seismic_tomography_local_pattern_candidate": True,
            "semantic_seismic_tomography_global_methodology_authorized": False,
            "runtime_probe_candidate": True,
            "runtime_probe_authorized": False,
            "instrumentation_authorized": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "renderer_runtime_authorized": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "performance_claimed": False,
            "transparent_globe_leak_fix_claimed": False,
            "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point view-frame occlusion token-trace lithology transition gate. "
            "No helper module creation, no source movement, no production source change, "
            "no existing token trace matrix change, no checker script change, "
            "no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, "
            "no monolith import, no runtime execution, no instrumentation, no sys.settrace, no debugger/IDE automation, "
            "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, "
            "no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, "
            "no transparent-globe leak fix claim, no runtime probe authorization, "
            "no token-trace global methodology authorization, no semantic-seismic-tomography global methodology authorization, "
            "no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointViewFrameOcclusionTokenTraceLithologyTransitionTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_view_frame_occlusion_token_trace_lithology_transition_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_view_frame_occlusion_token_trace_lithology_transition.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["dynamic_point_lithology_l2_local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["projection_shadow_source"], "6289c60")
        self.assertEqual(self.packet["view_frame_occlusion_monkey_matrix"], "8b5cac7")
        self.assertEqual(self.packet["core_lineage_validation_source"], "bbd978d")
        self.assertEqual(self.packet["token_trace_matrix_source"], "373da1e")

    def test_prior_gate_inputs_are_preserved(self):
        prior = self.packet["prior_gate_inputs"]
        self.assertTrue(prior["token_trace_mode_local_pilot"])
        self.assertFalse(prior["token_trace_mode_global_methodology_authorized"])
        self.assertTrue(prior["runtime_probe_candidate"])
        self.assertFalse(prior["runtime_probe_authorized"])
        self.assertFalse(prior["instrumentation_authorized"])
        self.assertFalse(prior["source_lineage_pollution_allowed"])

    def test_required_lithology_labels_transitions_and_age_labels(self):
        self.assertEqual(set(self.packet["lithology_labels"]), REQUIRED_LITHOLOGY_LABELS)
        self.assertEqual(set(self.packet["lithology_transitions"]), REQUIRED_TRANSITIONS)
        self.assertEqual(set(self.packet["semantic_age_inference_labels"]), REQUIRED_SEMANTIC_AGE_LABELS)

    def test_required_transition_rules_present(self):
        rules = self.packet["transition_rules"]
        for key in [
            "core_lineage_to_core_lineage",
            "core_lineage_to_core_interface",
            "core_lineage_to_andesite_bridge",
            "andesite_to_presentation_policy",
            "presentation_to_source_lineage_forbidden",
            "source_lineage_preserved",
            "computed_to_hidden_visibility",
            "fault_remains_unresolved",
        ]:
            self.assertIn(key, rules)
            self.assertIn("preferred_strategy", rules[key])
        self.assertFalse(rules["core_lineage_to_core_interface"]["formula_movement_authorized"])
        self.assertFalse(rules["core_lineage_to_andesite_bridge"]["implementation_transplant_authorized"])
        self.assertFalse(rules["presentation_to_source_lineage_forbidden"]["pollution_allowed"])
        self.assertFalse(rules["computed_to_hidden_visibility"]["hidden_becomes_missing_source"])
        self.assertFalse(rules["fault_remains_unresolved"]["fix_claimed"])

    def test_required_matrix_combinations_are_covered(self):
        combos = {(row["entrypoint"], row["token"]) for row in self.packet["transition_matrix"]}
        self.assertTrue(REQUIRED_COMBOS.issubset(combos))

    def test_matrix_rows_have_required_shape_and_allowed_values(self):
        for row in self.packet["transition_matrix"]:
            self.assertEqual(set(row), ROW_KEYS)
            self.assertTrue(row["expected_path"])
            self.assertTrue(row["lithology_sequence"])
            self.assertTrue(set(row["lithology_sequence"]).issubset(REQUIRED_LITHOLOGY_LABELS))
            self.assertIn(row["lithology_transition"], REQUIRED_TRANSITIONS)
            self.assertIn(row["semantic_age_inference"], REQUIRED_SEMANTIC_AGE_LABELS)
            self.assertIn(row["recommended_strategy"], RECOMMENDED_STRATEGIES)
            self.assertFalse(row["source_lineage_pollution_allowed"])
            self.assertFalse(row["coordinate_correctness_claimed"])
            self.assertFalse(row["visual_correctness_claimed"])

    def test_core_interface_and_formula_stop_rows(self):
        rows = {(row["entrypoint"], row["token"], row["mode"]): row for row in self.packet["transition_matrix"]}
        projection = rows[("projection_shadow_entry", "projection_policy_ref_token", "token_trace_mode")]
        self.assertEqual(projection["lithology_transition"], "core_lineage_to_core_interface")
        self.assertEqual(projection["recommended_strategy"], "shadow_interface_only")
        payload_stop = rows[("projection_shadow_entry", "coordinate_payload_token", "tripwire_mode")]
        self.assertEqual(payload_stop["lithology_transition"], "payload_to_core_formula_forbidden")
        self.assertEqual(payload_stop["recommended_strategy"], "forbidden_path_stop")

    def test_source_lineage_and_hidden_semantics(self):
        rows = {(row["entrypoint"], row["token"], row["mode"]): row for row in self.packet["transition_matrix"]}
        point_id = rows[("point_payload_entry", "point_id_token", "token_trace_mode")]
        self.assertEqual(point_id["lithology_transition"], "source_lineage_preserved")
        self.assertEqual(point_id["semantic_age_inference"], "source_lineage_identity_preserved")
        coordinate = rows[("point_payload_entry", "coordinate_payload_token", "token_trace_mode")]
        self.assertEqual(coordinate["lithology_transition"], "computed_to_hidden_visibility")
        self.assertEqual(coordinate["semantic_age_inference"], "visibility_not_existence_semantics")

    def test_fault_remains_unresolved(self):
        fault_rows = [
            row for row in self.packet["transition_matrix"]
            if row["lithology_transition"] == "fault_remains_unresolved"
        ]
        self.assertTrue(fault_rows)
        self.assertEqual(fault_rows[0]["semantic_age_inference"], "unresolved_fault_semantics")
        self.assertEqual(fault_rows[0]["recommended_strategy"], "evidence_gap_review")

    def test_decision_output_blocks_runtime_and_global_methods(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["lithology_transition_gate_passed"])
        self.assertTrue(decision["token_trace_mode_local_pilot"])
        self.assertFalse(decision["token_trace_mode_global_methodology_authorized"])
        self.assertTrue(decision["semantic_seismic_tomography_local_pattern_candidate"])
        self.assertFalse(decision["semantic_seismic_tomography_global_methodology_authorized"])
        self.assertTrue(decision["runtime_probe_candidate"])
        self.assertFalse(decision["runtime_probe_authorized"])
        self.assertFalse(decision["instrumentation_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
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

    def test_boundary_statement_contains_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no existing token trace matrix change", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no instrumentation", boundary)
        self.assertIn("no sys.settrace", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no semantic-seismic-tomography global methodology authorization", boundary)


if __name__ == "__main__":
    unittest.main()
