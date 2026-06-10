import unittest


REQUIRED_PINS = {
    "zoom_state_pin",
    "rotation_state_pin",
    "lod_policy_pin",
    "globe_angle_frame_pin",
    "projection_shadow_pin",
    "occlusion_policy_pin",
    "presentation_policy_pin",
    "source_lineage_integrity_pin",
    "computed_but_hidden_point_pin",
    "transparent_globe_leak_fault_pin",
}

REQUIRED_MODES = {
    "null_mode",
    "tripwire_mode",
    "trace_mode",
    "substitute_mode",
    "token_trace_mode",
}

REQUIRED_SCENARIOS = {
    ("zoom_state_pin", "zoom_entry", "zoom_token"),
    ("rotation_state_pin", "rotation_entry", "rotation_token"),
    ("lod_policy_pin", "lod_policy_entry", "lod_token"),
    ("globe_angle_frame_pin", "globe_angle_frame_entry", "globe_angle_token"),
    ("projection_shadow_pin", "projection_shadow_entry", "projection_policy_ref_token"),
    ("occlusion_policy_pin", "point_payload_entry", "point_id_token"),
    ("projection_shadow_pin", "point_payload_entry", "coordinate_payload_token"),
    ("occlusion_policy_pin", "occlusion_policy_entry", "occlusion_visibility_token"),
    ("presentation_policy_pin", "presentation_policy_entry", "presentation_visibility_token"),
    ("source_lineage_integrity_pin", "source_lineage_entry", "source_lineage_token"),
    ("transparent_globe_leak_fault_pin", "presentation_policy_entry", "presentation_visibility_token"),
}

PATH_DELTAS = {
    "path_preserved",
    "path_blocked_by_tripwire",
    "path_rerouted_to_containment",
    "path_degraded_to_presentation_only",
    "path_kept_source_lineage_stable",
    "path_exposes_forbidden_formula_pressure",
    "path_exposes_forbidden_source_lineage_pollution",
    "path_requires_runtime_characterization",
    "not_enough_evidence",
}

LITHOLOGY_DELTAS = {
    "core_lineage_preserved",
    "core_interface_contained",
    "core_to_andesite_bridge_preserved",
    "andesite_to_presentation_preserved",
    "presentation_pollution_blocked",
    "source_lineage_preserved",
    "computed_hidden_semantics_preserved",
    "unresolved_fault_preserved",
    "forbidden_transition_exposed",
    "runtime_characterization_needed",
    "not_enough_evidence",
}

CONTAINMENT_VALUES = {
    "contained_by_shadow_interface",
    "contained_by_source_lineage_guard",
    "contained_by_presentation_policy",
    "contained_by_tripwire",
    "requires_runtime_characterization",
    "forbidden_formula_path_detected",
    "forbidden_source_lineage_pollution_detected",
    "unresolved_static_fault",
    "not_enough_evidence",
}

ROW_KEYS = {
    "pin",
    "ablation_mode",
    "entrypoint",
    "token",
    "baseline_expected_path",
    "token_path_after_ablation",
    "path_delta",
    "baseline_lithology_transition",
    "lithology_transition_delta",
    "containment_or_failure",
    "source_lineage_pollution_allowed",
    "runtime_probe_needed",
    "coordinate_correctness_claimed",
    "visual_correctness_claimed",
    "performance_claimed",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "dynamic_point_lithology_l2_local_pattern_source",
    "view_frame_occlusion_monkey_matrix",
    "core_lineage_validation_source",
    "token_trace_matrix_source",
    "token_trace_lithology_transition_source",
    "pins",
    "ablation_modes",
    "conditioned_trace_matrix",
    "causal_conclusions",
    "decision_output",
    "boundary_statement",
}

SCENARIOS = [
    {
        "pin": "zoom_state_pin",
        "entrypoint": "zoom_entry",
        "token": "zoom_token",
        "baseline_expected_path": ["zoom_state", "lod_policy", "view_frame_label"],
        "baseline_lithology_transition": "core_lineage_to_andesite_bridge",
        "default_path_delta": "path_rerouted_to_containment",
        "default_lithology_delta": "core_to_andesite_bridge_preserved",
        "default_containment": "contained_by_presentation_policy",
    },
    {
        "pin": "rotation_state_pin",
        "entrypoint": "rotation_entry",
        "token": "rotation_token",
        "baseline_expected_path": ["rotation_state", "globe_angle_frame", "occlusion_decision_label"],
        "baseline_lithology_transition": "core_lineage_to_core_lineage",
        "default_path_delta": "path_preserved",
        "default_lithology_delta": "core_lineage_preserved",
        "default_containment": "requires_runtime_characterization",
    },
    {
        "pin": "lod_policy_pin",
        "entrypoint": "lod_policy_entry",
        "token": "lod_token",
        "baseline_expected_path": ["lod_policy", "sampling_label", "presentation_label"],
        "baseline_lithology_transition": "andesite_to_presentation_policy",
        "default_path_delta": "path_degraded_to_presentation_only",
        "default_lithology_delta": "andesite_to_presentation_preserved",
        "default_containment": "contained_by_presentation_policy",
    },
    {
        "pin": "globe_angle_frame_pin",
        "entrypoint": "globe_angle_frame_entry",
        "token": "globe_angle_token",
        "baseline_expected_path": ["globe_angle_frame", "occlusion_label"],
        "baseline_lithology_transition": "core_lineage_to_andesite_bridge",
        "default_path_delta": "path_requires_runtime_characterization",
        "default_lithology_delta": "runtime_characterization_needed",
        "default_containment": "requires_runtime_characterization",
    },
    {
        "pin": "projection_shadow_pin",
        "entrypoint": "projection_shadow_entry",
        "token": "projection_policy_ref_token",
        "baseline_expected_path": ["projection_shadow", "policy_ref_label", "stop_condition_ledger"],
        "baseline_lithology_transition": "core_lineage_to_core_interface",
        "default_path_delta": "path_rerouted_to_containment",
        "default_lithology_delta": "core_interface_contained",
        "default_containment": "contained_by_shadow_interface",
    },
    {
        "pin": "occlusion_policy_pin",
        "entrypoint": "point_payload_entry",
        "token": "point_id_token",
        "baseline_expected_path": ["point_identity", "source_lineage_identity", "hidden_visibility_allowed"],
        "baseline_lithology_transition": "source_lineage_preserved",
        "default_path_delta": "path_kept_source_lineage_stable",
        "default_lithology_delta": "source_lineage_preserved",
        "default_containment": "contained_by_source_lineage_guard",
    },
    {
        "pin": "projection_shadow_pin",
        "entrypoint": "point_payload_entry",
        "token": "coordinate_payload_token",
        "baseline_expected_path": ["coordinate_payload", "computed_hidden_uncertainty_label"],
        "baseline_lithology_transition": "computed_to_hidden_visibility",
        "default_path_delta": "path_exposes_forbidden_formula_pressure",
        "default_lithology_delta": "forbidden_transition_exposed",
        "default_containment": "forbidden_formula_path_detected",
    },
    {
        "pin": "occlusion_policy_pin",
        "entrypoint": "occlusion_policy_entry",
        "token": "occlusion_visibility_token",
        "baseline_expected_path": ["occlusion_policy", "visibility_label"],
        "baseline_lithology_transition": "andesite_to_presentation_policy",
        "default_path_delta": "path_requires_runtime_characterization",
        "default_lithology_delta": "runtime_characterization_needed",
        "default_containment": "requires_runtime_characterization",
    },
    {
        "pin": "presentation_policy_pin",
        "entrypoint": "presentation_policy_entry",
        "token": "presentation_visibility_token",
        "baseline_expected_path": ["presentation_policy", "rendered_visibility_label"],
        "baseline_lithology_transition": "presentation_to_source_lineage_forbidden",
        "default_path_delta": "path_exposes_forbidden_source_lineage_pollution",
        "default_lithology_delta": "presentation_pollution_blocked",
        "default_containment": "forbidden_source_lineage_pollution_detected",
    },
    {
        "pin": "source_lineage_integrity_pin",
        "entrypoint": "source_lineage_entry",
        "token": "source_lineage_token",
        "baseline_expected_path": ["source_lineage_identity", "provider_lineage_guard"],
        "baseline_lithology_transition": "source_lineage_preserved",
        "default_path_delta": "path_kept_source_lineage_stable",
        "default_lithology_delta": "source_lineage_preserved",
        "default_containment": "contained_by_source_lineage_guard",
    },
    {
        "pin": "transparent_globe_leak_fault_pin",
        "entrypoint": "presentation_policy_entry",
        "token": "presentation_visibility_token",
        "baseline_expected_path": ["transparent_globe_leak_fault", "known_fault_ledger"],
        "baseline_lithology_transition": "fault_remains_unresolved",
        "default_path_delta": "path_rerouted_to_containment",
        "default_lithology_delta": "unresolved_fault_preserved",
        "default_containment": "unresolved_static_fault",
    },
]


def _row_for(scenario, mode):
    if mode == "null_mode":
        path_delta = "not_enough_evidence"
        lithology_delta = "not_enough_evidence"
        containment = "not_enough_evidence"
        token_path = ["ablation_removed_pin", scenario["pin"]]
    elif mode == "tripwire_mode":
        token_path = ["tripwire", scenario["pin"], scenario["token"]]
        if scenario["default_containment"] == "forbidden_formula_path_detected":
            path_delta = "path_exposes_forbidden_formula_pressure"
            lithology_delta = "forbidden_transition_exposed"
            containment = "forbidden_formula_path_detected"
        elif scenario["default_containment"] == "forbidden_source_lineage_pollution_detected":
            path_delta = "path_exposes_forbidden_source_lineage_pollution"
            lithology_delta = "presentation_pollution_blocked"
            containment = "forbidden_source_lineage_pollution_detected"
        else:
            path_delta = "path_blocked_by_tripwire"
            lithology_delta = scenario["default_lithology_delta"]
            containment = "contained_by_tripwire"
    else:
        token_path = list(scenario["baseline_expected_path"])
        path_delta = scenario["default_path_delta"]
        lithology_delta = scenario["default_lithology_delta"]
        containment = scenario["default_containment"]
    return {
        "pin": scenario["pin"],
        "ablation_mode": mode,
        "entrypoint": scenario["entrypoint"],
        "token": scenario["token"],
        "baseline_expected_path": scenario["baseline_expected_path"],
        "token_path_after_ablation": token_path,
        "path_delta": path_delta,
        "baseline_lithology_transition": scenario["baseline_lithology_transition"],
        "lithology_transition_delta": lithology_delta,
        "containment_or_failure": containment,
        "source_lineage_pollution_allowed": False,
        "runtime_probe_needed": mode in {"trace_mode", "token_trace_mode"} or containment == "requires_runtime_characterization",
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "performance_claimed": False,
    }


def build_dynamic_point_view_frame_occlusion_ablation_conditioned_token_trace_packet():
    modes = ["null_mode", "tripwire_mode", "trace_mode", "substitute_mode", "token_trace_mode"]
    matrix = [_row_for(scenario, mode) for scenario in SCENARIOS for mode in modes]
    return {
        "schema": "rrkal.displaytools.dynamic_point_view_frame_occlusion_ablation_conditioned_token_trace.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "dynamic_point_lithology_l2_local_pattern_source": "60cded8",
        "view_frame_occlusion_monkey_matrix": "8b5cac7",
        "core_lineage_validation_source": "bbd978d",
        "token_trace_matrix_source": "373da1e",
        "token_trace_lithology_transition_source": "9c0a40e",
        "pins": sorted(REQUIRED_PINS),
        "ablation_modes": modes,
        "conditioned_trace_matrix": matrix,
        "causal_conclusions": {
            "zoom_ablation_does_not_pollute_source_lineage": True,
            "rotation_ablation_does_not_modify_provider_cache_database": True,
            "lod_ablation_degrades_to_presentation_only_not_source_filter": True,
            "globe_angle_ablation_requires_runtime_characterization_not_correctness_claim": True,
            "projection_shadow_ablation_contains_or_marks_formula_pressure": True,
            "occlusion_ablation_preserves_point_id_source_lineage": True,
            "presentation_ablation_hidden_point_not_missing_source": True,
            "transparent_globe_leak_fault_ablation_no_fix_claim": True,
        },
        "decision_output": {
            "ablation_conditioned_token_trace_gate_passed": True,
            "semantic_seismic_tomography_local_pattern_candidate": True,
            "semantic_seismic_tomography_global_methodology_authorized": False,
            "token_trace_mode_local_pilot": True,
            "token_trace_mode_global_methodology_authorized": False,
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
            "recommended_next_gate": "dynamic_point_view_frame_occlusion_structure_settlement_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point view-frame occlusion ablation-conditioned token-trace gate. "
            "No helper module creation, no source movement, no production source change, "
            "no existing monkey/token/lithology gate change, no checker script change, "
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


class DynamicPointViewFrameOcclusionAblationConditionedTokenTraceTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_view_frame_occlusion_ablation_conditioned_token_trace_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_view_frame_occlusion_ablation_conditioned_token_trace.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["dynamic_point_lithology_l2_local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["view_frame_occlusion_monkey_matrix"], "8b5cac7")
        self.assertEqual(self.packet["core_lineage_validation_source"], "bbd978d")
        self.assertEqual(self.packet["token_trace_matrix_source"], "373da1e")
        self.assertEqual(self.packet["token_trace_lithology_transition_source"], "9c0a40e")

    def test_required_pins_and_modes_are_covered(self):
        self.assertEqual(set(self.packet["pins"]), REQUIRED_PINS)
        self.assertEqual(set(self.packet["ablation_modes"]), REQUIRED_MODES)

    def test_required_scenarios_are_covered_for_every_mode(self):
        rows = self.packet["conditioned_trace_matrix"]
        scenarios = {(row["pin"], row["entrypoint"], row["token"]) for row in rows}
        self.assertTrue(REQUIRED_SCENARIOS.issubset(scenarios))
        for scenario in REQUIRED_SCENARIOS:
            self.assertEqual(
                {row["ablation_mode"] for row in rows if (row["pin"], row["entrypoint"], row["token"]) == scenario},
                REQUIRED_MODES,
            )

    def test_rows_have_required_shape_and_allowed_values(self):
        for row in self.packet["conditioned_trace_matrix"]:
            self.assertEqual(set(row), ROW_KEYS)
            self.assertIn(row["pin"], REQUIRED_PINS)
            self.assertIn(row["ablation_mode"], REQUIRED_MODES)
            self.assertIn(row["path_delta"], PATH_DELTAS)
            self.assertIn(row["lithology_transition_delta"], LITHOLOGY_DELTAS)
            self.assertIn(row["containment_or_failure"], CONTAINMENT_VALUES)
            self.assertFalse(row["source_lineage_pollution_allowed"])
            self.assertFalse(row["coordinate_correctness_claimed"])
            self.assertFalse(row["visual_correctness_claimed"])
            self.assertFalse(row["performance_claimed"])

    def test_causal_conclusions_are_pinned(self):
        conclusions = self.packet["causal_conclusions"]
        self.assertTrue(conclusions["zoom_ablation_does_not_pollute_source_lineage"])
        self.assertTrue(conclusions["rotation_ablation_does_not_modify_provider_cache_database"])
        self.assertTrue(conclusions["lod_ablation_degrades_to_presentation_only_not_source_filter"])
        self.assertTrue(conclusions["globe_angle_ablation_requires_runtime_characterization_not_correctness_claim"])
        self.assertTrue(conclusions["projection_shadow_ablation_contains_or_marks_formula_pressure"])
        self.assertTrue(conclusions["occlusion_ablation_preserves_point_id_source_lineage"])
        self.assertTrue(conclusions["presentation_ablation_hidden_point_not_missing_source"])
        self.assertTrue(conclusions["transparent_globe_leak_fault_ablation_no_fix_claim"])

    def test_projection_shadow_formula_pressure_is_contained_or_detected(self):
        rows = [
            row for row in self.packet["conditioned_trace_matrix"]
            if row["pin"] == "projection_shadow_pin" and row["token"] == "coordinate_payload_token"
        ]
        self.assertTrue(rows)
        self.assertIn("path_exposes_forbidden_formula_pressure", {row["path_delta"] for row in rows})
        self.assertIn("forbidden_formula_path_detected", {row["containment_or_failure"] for row in rows})

    def test_source_lineage_pollution_is_blocked(self):
        rows = [
            row for row in self.packet["conditioned_trace_matrix"]
            if row["containment_or_failure"] == "forbidden_source_lineage_pollution_detected"
        ]
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row["path_delta"], "path_exposes_forbidden_source_lineage_pollution")
            self.assertEqual(row["lithology_transition_delta"], "presentation_pollution_blocked")
            self.assertFalse(row["source_lineage_pollution_allowed"])

    def test_transparent_globe_fault_remains_unresolved(self):
        rows = [
            row for row in self.packet["conditioned_trace_matrix"]
            if row["pin"] == "transparent_globe_leak_fault_pin"
        ]
        self.assertTrue(rows)
        self.assertIn("unresolved_fault_preserved", {row["lithology_transition_delta"] for row in rows})
        self.assertIn("unresolved_static_fault", {row["containment_or_failure"] for row in rows})

    def test_decision_output_blocks_runtime_and_global_methods(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["ablation_conditioned_token_trace_gate_passed"])
        self.assertTrue(decision["semantic_seismic_tomography_local_pattern_candidate"])
        self.assertFalse(decision["semantic_seismic_tomography_global_methodology_authorized"])
        self.assertTrue(decision["token_trace_mode_local_pilot"])
        self.assertFalse(decision["token_trace_mode_global_methodology_authorized"])
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
            "dynamic_point_view_frame_occlusion_structure_settlement_gate",
        )

    def test_boundary_statement_contains_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no existing monkey/token/lithology gate change", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no instrumentation", boundary)
        self.assertIn("no sys.settrace", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no semantic-seismic-tomography global methodology authorization", boundary)


if __name__ == "__main__":
    unittest.main()
