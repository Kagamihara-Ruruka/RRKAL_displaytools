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
}

PIN_KEYS = {
    "pin_name",
    "ablation_modes",
    "causal_upstream",
    "causal_downstream",
    "semantic_boundary",
    "source_lineage_mutation_allowed",
    "runtime_execution_allowed",
    "expected_observation",
    "forbidden_next_action",
}


def build_dynamic_point_view_frame_occlusion_monkey_ablation_packet():
    pins = [
        {
            "pin_name": "zoom_state_pin",
            "ablation_modes": {
                "null_mode": "remove zoom input label and expect lod_policy to lose zoom-derived pressure only",
                "tripwire_mode": "mark zoom mutation attempts as view-frame-only violations if they touch source lineage",
                "trace_mode": "trace zoom_state to lod_policy without executing renderer",
                "substitute_mode": "substitute static zoom bucket label",
            },
            "causal_upstream": ["viewer_zoom_label"],
            "causal_downstream": ["lod_policy"],
            "semantic_boundary": "zoom changes view-frame state and may affect LOD policy; it is not source lineage",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "zoom_state_pin can affect lod_policy",
            "forbidden_next_action": "do_not_execute_renderer_or_modify_provider_lineage",
        },
        {
            "pin_name": "rotation_state_pin",
            "ablation_modes": {
                "null_mode": "remove rotation label and expect globe_angle_frame to become unresolved",
                "tripwire_mode": "fail if rotation mutation is treated as provider mutation",
                "trace_mode": "trace rotation_state to globe_angle_frame",
                "substitute_mode": "substitute static rotation bucket label",
            },
            "causal_upstream": ["viewer_rotation_label"],
            "causal_downstream": ["globe_angle_frame"],
            "semantic_boundary": "rotation changes view-frame state, not source data",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "rotation_state_pin can affect globe_angle_frame",
            "forbidden_next_action": "do_not_execute_projection_or_renderer_runtime",
        },
        {
            "pin_name": "lod_policy_pin",
            "ablation_modes": {
                "null_mode": "remove LOD policy label and expect presentation load label to become unknown",
                "tripwire_mode": "fail if LOD is treated as provider lineage",
                "trace_mode": "trace LOD to presentation load and sampling label",
                "substitute_mode": "substitute static LOD bucket",
            },
            "causal_upstream": ["zoom_state_pin"],
            "causal_downstream": ["presentation_policy_pin"],
            "semantic_boundary": "LOD is presentation and render policy, not provider lineage",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "lod_policy_pin can affect presentation load and sampling label",
            "forbidden_next_action": "do_not_run_datashader_pandas_numpy_or_renderer",
        },
        {
            "pin_name": "globe_angle_frame_pin",
            "ablation_modes": {
                "null_mode": "remove globe angle label and expect occlusion decision to be unresolved",
                "tripwire_mode": "fail if globe angle mutates dynamic point existence",
                "trace_mode": "trace globe angle frame to occlusion policy",
                "substitute_mode": "substitute front_side back_side rim label",
            },
            "causal_upstream": ["rotation_state_pin"],
            "causal_downstream": ["occlusion_policy_pin"],
            "semantic_boundary": "globe angle is upstream of visibility and occlusion, not provider existence",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "globe_angle_frame_pin can affect occlusion decision",
            "forbidden_next_action": "do_not_copy_projection_flip_mask_formula",
        },
        {
            "pin_name": "projection_shadow_pin",
            "ablation_modes": {
                "null_mode": "remove projection shadow refs and expect occlusion evidence refs to become incomplete",
                "tripwire_mode": "fail if projection formula appears",
                "trace_mode": "trace label reference ledger only",
                "substitute_mode": "substitute static projection policy ref label",
            },
            "causal_upstream": ["globe_angle_frame_pin"],
            "causal_downstream": ["occlusion_policy_pin"],
            "semantic_boundary": "projection shadow allows label reference ledger only and forbids formula movement",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "projection_shadow_pin only allows label/reference/ledger, not formulas",
            "forbidden_next_action": "do_not_read_copy_move_or_modify_projection_flip_mask_formula",
        },
        {
            "pin_name": "occlusion_policy_pin",
            "ablation_modes": {
                "null_mode": "remove occlusion policy and expect back-side visibility to become unresolved",
                "tripwire_mode": "fail if occlusion changes source lineage",
                "trace_mode": "trace occlusion policy to visibility only",
                "substitute_mode": "substitute hidden visible uncertain label",
            },
            "causal_upstream": ["globe_angle_frame_pin", "projection_shadow_pin"],
            "causal_downstream": ["presentation_policy_pin"],
            "semantic_boundary": "occlusion affects visibility and must not change source lineage",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "occlusion_policy_pin can affect visibility but cannot alter source lineage",
            "forbidden_next_action": "do_not_treat_occlusion_as_source_filter",
        },
        {
            "pin_name": "presentation_policy_pin",
            "ablation_modes": {
                "null_mode": "remove presentation policy and expect rendered visibility label to become unknown",
                "tripwire_mode": "fail if presentation touches provider cache or database",
                "trace_mode": "trace presentation to rendered visibility label",
                "substitute_mode": "substitute rendered hidden suppressed label",
            },
            "causal_upstream": ["lod_policy_pin", "occlusion_policy_pin"],
            "causal_downstream": ["rendered_visibility_label"],
            "semantic_boundary": "presentation affects rendered visibility, not provider/cache/database",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "presentation_policy_pin can affect rendered visibility only",
            "forbidden_next_action": "do_not_modify_provider_cache_database_or_renderer_runtime",
        },
        {
            "pin_name": "source_lineage_integrity_pin",
            "ablation_modes": {
                "null_mode": "remove source lineage label and expect source evidence to be missing",
                "tripwire_mode": "fail if LOD or occlusion mutates source lineage",
                "trace_mode": "trace source lineage as independent of visibility mutation",
                "substitute_mode": "substitute static AIS ADS-B synthetic lineage label",
            },
            "causal_upstream": ["provider_lineage_label"],
            "causal_downstream": ["computed_point_identity"],
            "semantic_boundary": "source lineage integrity must not be changed by LOD or occlusion",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "source_lineage_integrity_pin is stable under LOD and occlusion labels",
            "forbidden_next_action": "do_not_execute_sql_websocket_cache_database_or_live_source",
        },
        {
            "pin_name": "computed_but_hidden_point_pin",
            "ablation_modes": {
                "null_mode": "remove hidden state and expect computed point visibility distinction to be lost",
                "tripwire_mode": "fail if hidden means not computed or source filtered",
                "trace_mode": "trace computed existence separately from presentation visibility",
                "substitute_mode": "substitute computed_hidden static state",
            },
            "causal_upstream": ["source_lineage_integrity_pin", "occlusion_policy_pin"],
            "causal_downstream": ["presentation_policy_pin"],
            "semantic_boundary": "dynamic point existence and computation are not visibility or presentation",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "point can exist and be computed while hidden by occlusion or presentation",
            "forbidden_next_action": "do_not_reclassify_hidden_point_as_missing_source",
        },
        {
            "pin_name": "transparent_globe_leak_fault_pin",
            "ablation_modes": {
                "null_mode": "remove leak fault ledger and expect backside leak risk to be untracked",
                "tripwire_mode": "fail if gate claims backside point leak is fixed",
                "trace_mode": "trace leak as unresolved static fault",
                "substitute_mode": "substitute transparent_globe_leak_fault label",
            },
            "causal_upstream": ["globe_angle_frame_pin", "occlusion_policy_pin", "presentation_policy_pin"],
            "causal_downstream": ["known_fault_ledger"],
            "semantic_boundary": "back-side points leaking through globe are recorded as fault only, not fixed",
            "source_lineage_mutation_allowed": False,
            "runtime_execution_allowed": False,
            "expected_observation": "transparent globe leak remains unresolved fault without fix claim",
            "forbidden_next_action": "do_not_claim_visual_correctness_or_leak_fix",
        },
    ]

    return {
        "schema": "rrkal.displaytools.dynamic_point_view_frame_occlusion_monkey_ablation_matrix.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "projection_shadow_source": "6289c60",
        "projection_shadow_checker": "827440c",
        "projection_shadow_planning": "a67a685",
        "dynamic_point_lithology_l2_local_pattern_source": "60cded8",
        "creation_order_counterexample_source": "53afb98",
        "semantic_chain": [
            "rotation_or_zoom",
            "lod_policy",
            "globe_angle_view_frame",
            "projection_shadow",
            "occlusion_policy",
            "presentation",
        ],
        "existence_visibility_boundary": {
            "dynamic_point_existence_or_computation_is_visibility_or_presentation": False,
            "computed_point_can_be_hidden": True,
            "occlusion_is_source_filter": False,
            "lod_is_provider_lineage": False,
            "rotation_zoom_change_source_lineage": False,
            "globe_angle_is_dynamic_point_provider": False,
        },
        "ablation_matrix": pins,
        "causal_expectations": {
            "zoom_state_pin_affects_lod_policy": True,
            "rotation_state_pin_affects_globe_angle_frame": True,
            "lod_policy_pin_affects_presentation_load_sampling_label": True,
            "globe_angle_frame_pin_affects_occlusion_decision": True,
            "projection_shadow_pin_allows_label_reference_ledger_only": True,
            "projection_shadow_formula_allowed": False,
            "occlusion_policy_pin_affects_visibility_not_source_lineage": True,
            "presentation_policy_pin_affects_rendered_visibility_not_provider_cache_database": True,
            "source_lineage_integrity_pin_stable_under_lod_occlusion": True,
            "computed_but_hidden_point_semantics_preserved": True,
            "transparent_globe_leak_recorded_as_fault_not_fix": True,
        },
        "classification_output": {
            "matrix_gate_passed": True,
            "view_frame_occlusion_planning_candidate": True,
            "runtime_probe_candidate": True,
            "runtime_probe_authorized": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "renderer_runtime_authorized": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "performance_claimed": False,
            "readiness_claimed": False,
            "recommended_next_gate": "dynamic_point_view_frame_occlusion_core_lineage_validation_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point view-frame occlusion monkey ablation matrix gate. "
            "No helper module creation, no source movement, no production source change, no checker script change, "
            "no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, "
            "no monolith import, no runtime execution, no SQL/WebSocket/live-source execution, "
            "no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, "
            "no projection/flip/mask formula read/copy/movement/change, "
            "no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, "
            "no transparent-globe leak fix claim, no runtime probe authorization, no runtime merge enablement, "
            "and no readiness/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointViewFrameOcclusionMonkeyAblationMatrixTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_view_frame_occlusion_monkey_ablation_packet()

    def test_packet_schema_and_anchor_sources(self):
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_view_frame_occlusion_monkey_ablation_matrix.v1",
        )
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["projection_shadow_source"], "6289c60")
        self.assertEqual(self.packet["projection_shadow_checker"], "827440c")
        self.assertEqual(self.packet["projection_shadow_planning"], "a67a685")
        self.assertEqual(self.packet["dynamic_point_lithology_l2_local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["creation_order_counterexample_source"], "53afb98")

    def test_required_pins_present_with_required_modes(self):
        pins = {row["pin_name"]: row for row in self.packet["ablation_matrix"]}
        self.assertEqual(set(pins), REQUIRED_PINS)
        for row in pins.values():
            self.assertEqual(set(row), PIN_KEYS)
            self.assertEqual(set(row["ablation_modes"]), REQUIRED_MODES)
            self.assertFalse(row["source_lineage_mutation_allowed"])
            self.assertFalse(row["runtime_execution_allowed"])

    def test_semantic_chain_is_pinned(self):
        self.assertEqual(
            self.packet["semantic_chain"],
            [
                "rotation_or_zoom",
                "lod_policy",
                "globe_angle_view_frame",
                "projection_shadow",
                "occlusion_policy",
                "presentation",
            ],
        )

    def test_existence_and_visibility_are_separated(self):
        boundary = self.packet["existence_visibility_boundary"]
        self.assertFalse(boundary["dynamic_point_existence_or_computation_is_visibility_or_presentation"])
        self.assertTrue(boundary["computed_point_can_be_hidden"])
        self.assertFalse(boundary["occlusion_is_source_filter"])
        self.assertFalse(boundary["lod_is_provider_lineage"])
        self.assertFalse(boundary["rotation_zoom_change_source_lineage"])
        self.assertFalse(boundary["globe_angle_is_dynamic_point_provider"])

    def test_required_causal_expectations(self):
        expectations = self.packet["causal_expectations"]
        self.assertTrue(expectations["zoom_state_pin_affects_lod_policy"])
        self.assertTrue(expectations["rotation_state_pin_affects_globe_angle_frame"])
        self.assertTrue(expectations["lod_policy_pin_affects_presentation_load_sampling_label"])
        self.assertTrue(expectations["globe_angle_frame_pin_affects_occlusion_decision"])
        self.assertTrue(expectations["projection_shadow_pin_allows_label_reference_ledger_only"])
        self.assertFalse(expectations["projection_shadow_formula_allowed"])
        self.assertTrue(expectations["occlusion_policy_pin_affects_visibility_not_source_lineage"])
        self.assertTrue(expectations["presentation_policy_pin_affects_rendered_visibility_not_provider_cache_database"])
        self.assertTrue(expectations["source_lineage_integrity_pin_stable_under_lod_occlusion"])
        self.assertTrue(expectations["computed_but_hidden_point_semantics_preserved"])
        self.assertTrue(expectations["transparent_globe_leak_recorded_as_fault_not_fix"])

    def test_computed_but_hidden_pin_preserves_point_existence(self):
        pin = {
            row["pin_name"]: row for row in self.packet["ablation_matrix"]
        }["computed_but_hidden_point_pin"]
        self.assertIn("point can exist and be computed while hidden", pin["expected_observation"])
        self.assertEqual(pin["forbidden_next_action"], "do_not_reclassify_hidden_point_as_missing_source")

    def test_transparent_globe_leak_is_fault_not_fix(self):
        pin = {
            row["pin_name"]: row for row in self.packet["ablation_matrix"]
        }["transparent_globe_leak_fault_pin"]
        self.assertIn("not fixed", pin["semantic_boundary"])
        self.assertEqual(pin["forbidden_next_action"], "do_not_claim_visual_correctness_or_leak_fix")
        self.assertTrue(self.packet["causal_expectations"]["transparent_globe_leak_recorded_as_fault_not_fix"])

    def test_classification_output_blocks_runtime_and_claims(self):
        output = self.packet["classification_output"]
        self.assertTrue(output["matrix_gate_passed"])
        self.assertTrue(output["view_frame_occlusion_planning_candidate"])
        self.assertTrue(output["runtime_probe_candidate"])
        self.assertFalse(output["runtime_probe_authorized"])
        self.assertFalse(output["helper_module_creation_authorized"])
        self.assertFalse(output["source_movement_authorized"])
        self.assertFalse(output["formula_movement_authorized"])
        self.assertFalse(output["renderer_runtime_authorized"])
        self.assertFalse(output["coordinate_correctness_claimed"])
        self.assertFalse(output["visual_correctness_claimed"])
        self.assertFalse(output["performance_claimed"])
        self.assertFalse(output["readiness_claimed"])
        self.assertEqual(
            output["recommended_next_gate"],
            "dynamic_point_view_frame_occlusion_core_lineage_validation_gate",
        )

    def test_boundary_statement_contains_required_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no performance claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no runtime probe authorization", boundary)


if __name__ == "__main__":
    unittest.main()
