
import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame runtime characterization planning gate. "
    "No helper module creation, no source movement, no production source change, no checker script change, "
    "no monolith import, no runtime execution, no instrumentation, no monkey patch implementation, "
    "no __getattribute__ implementation, no sys.settrace, no SQL/WebSocket/live-source execution, "
    "no real AIS/ADS-B/cache/database read, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, "
    "no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, "
    "no renderer behavior change, no compose order change, no metadata/output schema change, "
    "no coordinate/visual correctness claim, no transparent-globe leak fix claim, "
    "no runtime characterization authorization, no global methodology promotion, no runtime merge enablement, "
    "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
)


REPRESENTATIVE_SLICE_STRATEGY = [
    {
        "slice_id": "5_12_core_baseline",
        "role": "early_view_frame_globe_runtime_core_reference",
        "dynamic_point_present": False,
        "use_in_plan": "core_reference",
        "status": "static_reference_only",
    },
    {
        "slice_id": "current_21k_target",
        "role": "dynamic_point_graft_lod_occlusion_presentation_target",
        "dynamic_point_present": True,
        "use_in_plan": "primary_runtime_characterization_target",
        "status": "planning_only_no_runtime_execution",
    },
    {
        "slice_id": "5_29_grafting_reference",
        "role": "dynamic_point_grafting_reference",
        "dynamic_point_present": True,
        "use_in_plan": "compare_graft_prototype_to_current_metamorphosis",
        "status": "static_reference_only",
    },
    {
        "slice_id": "5_10_geometry_lighting_seed",
        "role": "geometry_lighting_seed_without_dynamic_point_graft_path",
        "dynamic_point_present": False,
        "use_in_plan": "excluded_for_dynamic_point_runtime_characterization",
        "status": "excluded_for_dynamic_point_runtime_characterization",
    },
]


ENTRYPOINT_MATRIX = [
    {
        "entrypoint": "render_if_needed",
        "slice_owner": "current_21k_target",
        "runtime_probe_candidate": True,
        "runtime_probe_authorized": False,
        "source_lineage_mutation_allowed": False,
        "formula_mutation_allowed": False,
        "renderer_behavior_mutation_allowed": False,
    },
    {
        "entrypoint": "project_ais_to_screen",
        "slice_owner": "current_21k_target",
        "runtime_probe_candidate": True,
        "runtime_probe_authorized": False,
        "source_lineage_mutation_allowed": False,
        "formula_mutation_allowed": False,
        "renderer_behavior_mutation_allowed": False,
    },
    {
        "entrypoint": "mask_overlay_to_globe",
        "slice_owner": "current_21k_target",
        "runtime_probe_candidate": True,
        "runtime_probe_authorized": False,
        "source_lineage_mutation_allowed": False,
        "formula_mutation_allowed": False,
        "renderer_behavior_mutation_allowed": False,
    },
    {
        "entrypoint": "controller_fixed_one_shot_render_path",
        "slice_owner": "current_21k_target",
        "runtime_probe_candidate": True,
        "runtime_probe_authorized": False,
        "source_lineage_mutation_allowed": False,
        "formula_mutation_allowed": False,
        "renderer_behavior_mutation_allowed": False,
    },
    {
        "entrypoint": "early_5_12_render_globe_baseline",
        "slice_owner": "5_12_core_baseline",
        "runtime_probe_candidate": True,
        "runtime_probe_authorized": False,
        "source_lineage_mutation_allowed": False,
        "formula_mutation_allowed": False,
        "renderer_behavior_mutation_allowed": False,
    },
    {
        "entrypoint": "early_5_29_dynamic_point_grafting_reference",
        "slice_owner": "5_29_grafting_reference",
        "runtime_probe_candidate": True,
        "runtime_probe_authorized": False,
        "source_lineage_mutation_allowed": False,
        "formula_mutation_allowed": False,
        "renderer_behavior_mutation_allowed": False,
    },
]


MONKEY_CONDITION_MATRIX = [
    {"condition": "zoom_state", "planning_label_only": True, "monkey_patch_implemented": False},
    {"condition": "rotation_state", "planning_label_only": True, "monkey_patch_implemented": False},
    {"condition": "lod_policy", "planning_label_only": True, "monkey_patch_implemented": False},
    {"condition": "horizon_eps", "planning_label_only": True, "monkey_patch_implemented": False},
    {"condition": "sampling_policy", "planning_label_only": True, "monkey_patch_implemented": False},
    {"condition": "mask_gate", "planning_label_only": True, "monkey_patch_implemented": False},
    {"condition": "compose_presentation_gate", "planning_label_only": True, "monkey_patch_implemented": False},
]


CONTRAST_TOKEN_MATRIX = [
    {"token": "source_present_token", "current_level": "L0_explicit_token"},
    {"token": "projected_visible_token", "current_level": "L0_explicit_token"},
    {"token": "sampled_visible_token", "current_level": "L0_explicit_token"},
    {"token": "overlay_rendered_token", "current_level": "L0_explicit_token"},
    {"token": "mask_visible_token", "current_level": "L0_explicit_token"},
    {"token": "frame_visible_token", "current_level": "L0_explicit_token"},
    {"token": "source_lineage_integrity_token", "current_level": "L0_explicit_token"},
]


FUTURE_TOKEN_UPGRADE_PATH = [
    {"level": "L0_explicit_token", "mainline_allowed_now": True, "implemented_now": False},
    {"level": "L1_repr_string_token", "mainline_allowed_now": False, "implemented_now": False},
    {"level": "L2_identity_guard_token", "mainline_allowed_now": False, "implemented_now": False},
    {"level": "L3_context_scope_token", "mainline_allowed_now": False, "implemented_now": False},
    {"level": "L4_getattribute_read_trace_token", "mainline_allowed_now": False, "implemented_now": False},
    {"level": "L5_numeric_pipeline_token", "mainline_allowed_now": False, "implemented_now": False},
]


KATYUSHA_PROBE_MATRIX_PLAN = [
    {
        "entrypoint": "project_ais_to_screen",
        "monkey_condition": "horizon_eps",
        "contrast_token": "projected_visible_token",
        "expected_path": "source_present_to_projected_visible_or_projection_drop",
        "forbidden_path": "source_lineage_mutation_or_formula_change",
        "oracle_rule": "projected_dropped_while_source_present -> projection_or_horizon_responsibility",
        "expected_lithology": "projection_grafting_bridge",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "project_ais_to_screen",
        "monkey_condition": "zoom_state",
        "contrast_token": "source_lineage_integrity_token",
        "expected_path": "zoom_affects_projection_visibility_not_source_identity",
        "forbidden_path": "zoom_token_to_source_lineage_pollution",
        "oracle_rule": "source token changed -> source_lineage_pollution_fail",
        "expected_lithology": "core_lineage_view_frame_semantics",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "render_if_needed",
        "monkey_condition": "sampling_policy",
        "contrast_token": "sampled_visible_token",
        "expected_path": "projected_visible_to_sampled_visible_or_sampling_drop",
        "forbidden_path": "sampling_as_source_filter",
        "oracle_rule": "sampled dropped while projected present -> sampling_responsibility",
        "expected_lithology": "presentation_policy_bridge",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "mask_overlay_to_globe",
        "monkey_condition": "mask_gate",
        "contrast_token": "mask_visible_token",
        "expected_path": "overlay_rendered_to_mask_visible_or_mask_hidden",
        "forbidden_path": "mask_gate_to_source_lineage_mutation",
        "oracle_rule": "mask hidden while overlay present -> globe_mask_responsibility",
        "expected_lithology": "globe_mask_occlusion_bridge",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "controller_fixed_one_shot_render_path",
        "monkey_condition": "compose_presentation_gate",
        "contrast_token": "frame_visible_token",
        "expected_path": "mask_visible_to_frame_visible_or_frame_hidden",
        "forbidden_path": "compose_order_mutation_or_correctness_claim",
        "oracle_rule": "frame visible while mask invisible -> transparent_globe_leak_candidate",
        "expected_lithology": "presentation_contract_candidate",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "early_5_12_render_globe_baseline",
        "monkey_condition": "rotation_state",
        "contrast_token": "mask_visible_token",
        "expected_path": "rotation_affects_core_globe_mask_reference",
        "forbidden_path": "dynamic_point_source_lineage_assumption_in_5_12",
        "oracle_rule": "source absent -> invalid_probe",
        "expected_lithology": "core_lineage_view_frame_semantics",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "early_5_29_dynamic_point_grafting_reference",
        "monkey_condition": "lod_policy",
        "contrast_token": "overlay_rendered_token",
        "expected_path": "sampled_visible_to_overlay_rendered_or_overlay_absent",
        "forbidden_path": "datashader_overlay_as_provider_lineage",
        "oracle_rule": "overlay absent while sampled present -> overlay_or_presentation_responsibility",
        "expected_lithology": "dynamic_point_grafting_reference",
        "runtime_probe_authorized": False,
    },
    {
        "entrypoint": "render_if_needed",
        "monkey_condition": "compose_presentation_gate",
        "contrast_token": "source_present_token",
        "expected_path": "source_present_to_frame_hidden_allowed",
        "forbidden_path": "hidden_to_missing_source",
        "oracle_rule": "source present while frame hidden -> computed_but_hidden_supported",
        "expected_lithology": "computed_but_hidden_semantics",
        "runtime_probe_authorized": False,
    },
]


ALLOWED_PROBE_RULE = {
    "synthetic_data_only": True,
    "one_shot": True,
    "persistent_artifact": False,
    "derived_exclusions": [
        "no live source",
        "no real AIS / ADS-B",
        "no SQL / DB / cache read",
        "no WebSocket",
        "no long-running GUI",
        "no human GUI interaction",
        "no persistent runtime state",
    ],
}


FORBIDDEN_MUTATION_CLAIM_RULES = {
    "formula_mutation_forbidden": True,
    "renderer_behavior_mutation_forbidden": True,
    "compose_order_mutation_forbidden": True,
    "frame_semantics_mutation_forbidden": True,
    "correctness_claim_forbidden": True,
    "transparent_globe_leak_fix_claim_forbidden": True,
    "readiness_claim_forbidden": True,
}


ORACLE_RULES = {
    "source token changed": "source_lineage_pollution_fail",
    "source absent": "invalid_probe",
    "projected dropped while source present": "projection_or_horizon_responsibility",
    "sampled dropped while projected present": "sampling_responsibility",
    "overlay absent while sampled present": "overlay_or_presentation_responsibility",
    "mask hidden while overlay present": "globe_mask_responsibility",
    "frame visible while mask invisible": "transparent_globe_leak_candidate",
    "source present while frame hidden": "computed_but_hidden_supported",
}


DECISION_OUTPUT = {
    "planning_gate_passed": True,
    "representative_slice_strategy_defined": True,
    "entrypoint_matrix_defined": True,
    "monkey_condition_matrix_defined": True,
    "contrast_token_matrix_defined": True,
    "katyusha_matrix_plan_defined": True,
    "oracle_rules_defined": True,
    "runtime_characterization_candidate": True,
    "runtime_characterization_authorized": False,
    "runtime_execution_authorized": False,
    "formula_mutation_authorized": False,
    "renderer_behavior_mutation_authorized": False,
    "source_lineage_mutation_authorized": False,
    "persistent_artifact_authorized": False,
    "visual_correctness_claimed": False,
    "coordinate_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_probe_authorization_review_gate",
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_runtime_characterization_planning.v1",
    "good_hope_source": "44356e9",
    "representative_slice_strategy": REPRESENTATIVE_SLICE_STRATEGY,
    "entrypoint_matrix": ENTRYPOINT_MATRIX,
    "monkey_condition_matrix": MONKEY_CONDITION_MATRIX,
    "contrast_token_matrix": CONTRAST_TOKEN_MATRIX,
    "future_token_upgrade_path": FUTURE_TOKEN_UPGRADE_PATH,
    "katyusha_probe_matrix_plan": KATYUSHA_PROBE_MATRIX_PLAN,
    "allowed_probe_rule": ALLOWED_PROBE_RULE,
    "forbidden_mutation_claim_rules": FORBIDDEN_MUTATION_CLAIM_RULES,
    "oracle_rules": ORACLE_RULES,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointLodViewFrameRuntimeCharacterizationPlanningTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "good_hope_source",
                "representative_slice_strategy",
                "entrypoint_matrix",
                "monkey_condition_matrix",
                "contrast_token_matrix",
                "future_token_upgrade_path",
                "katyusha_probe_matrix_plan",
                "allowed_probe_rule",
                "forbidden_mutation_claim_rules",
                "oracle_rules",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(PACKET["schema"], "rrkal.displaytools.dynamic_point_lod_view_frame_runtime_characterization_planning.v1")
        self.assertEqual(PACKET["good_hope_source"], "44356e9")

    def test_representative_slice_strategy(self):
        rows = {row["slice_id"]: row for row in PACKET["representative_slice_strategy"]}
        self.assertEqual(set(rows), {"5_12_core_baseline", "current_21k_target", "5_29_grafting_reference", "5_10_geometry_lighting_seed"})
        self.assertFalse(rows["5_12_core_baseline"]["dynamic_point_present"])
        self.assertTrue(rows["current_21k_target"]["dynamic_point_present"])
        self.assertTrue(rows["5_29_grafting_reference"]["dynamic_point_present"])
        self.assertEqual(rows["5_10_geometry_lighting_seed"]["status"], "excluded_for_dynamic_point_runtime_characterization")

    def test_entrypoint_matrix_is_planning_only(self):
        self.assertEqual(
            {row["entrypoint"] for row in PACKET["entrypoint_matrix"]},
            {
                "render_if_needed",
                "project_ais_to_screen",
                "mask_overlay_to_globe",
                "controller_fixed_one_shot_render_path",
                "early_5_12_render_globe_baseline",
                "early_5_29_dynamic_point_grafting_reference",
            },
        )
        for row in PACKET["entrypoint_matrix"]:
            self.assertTrue(row["runtime_probe_candidate"])
            self.assertFalse(row["runtime_probe_authorized"])
            self.assertFalse(row["source_lineage_mutation_allowed"])
            self.assertFalse(row["formula_mutation_allowed"])
            self.assertFalse(row["renderer_behavior_mutation_allowed"])

    def test_monkey_conditions_are_labels_only(self):
        self.assertEqual(
            {row["condition"] for row in PACKET["monkey_condition_matrix"]},
            {"zoom_state", "rotation_state", "lod_policy", "horizon_eps", "sampling_policy", "mask_gate", "compose_presentation_gate"},
        )
        for row in PACKET["monkey_condition_matrix"]:
            self.assertTrue(row["planning_label_only"])
            self.assertFalse(row["monkey_patch_implemented"])

    def test_contrast_tokens_and_future_upgrade_path(self):
        self.assertEqual(
            {row["token"] for row in PACKET["contrast_token_matrix"]},
            {
                "source_present_token",
                "projected_visible_token",
                "sampled_visible_token",
                "overlay_rendered_token",
                "mask_visible_token",
                "frame_visible_token",
                "source_lineage_integrity_token",
            },
        )
        for row in PACKET["contrast_token_matrix"]:
            self.assertEqual(row["current_level"], "L0_explicit_token")
        upgrades = {row["level"]: row for row in PACKET["future_token_upgrade_path"]}
        self.assertEqual(set(upgrades), {"L0_explicit_token", "L1_repr_string_token", "L2_identity_guard_token", "L3_context_scope_token", "L4_getattribute_read_trace_token", "L5_numeric_pipeline_token"})
        self.assertTrue(upgrades["L0_explicit_token"]["mainline_allowed_now"])
        self.assertFalse(upgrades["L4_getattribute_read_trace_token"]["mainline_allowed_now"])
        self.assertFalse(upgrades["L4_getattribute_read_trace_token"]["implemented_now"])

    def test_katyusha_matrix_plan_selected_rows(self):
        rows = PACKET["katyusha_probe_matrix_plan"]
        self.assertGreaterEqual(len(rows), 6)
        required_keys = {"entrypoint", "monkey_condition", "contrast_token", "expected_path", "forbidden_path", "oracle_rule", "expected_lithology", "runtime_probe_authorized"}
        for row in rows:
            self.assertEqual(set(row), required_keys)
            self.assertFalse(row["runtime_probe_authorized"])
        self.assertIn("source present while frame hidden -> computed_but_hidden_supported", {row["oracle_rule"] for row in rows})

    def test_allowed_probe_rule_and_exclusions(self):
        rule = PACKET["allowed_probe_rule"]
        self.assertTrue(rule["synthetic_data_only"])
        self.assertTrue(rule["one_shot"])
        self.assertFalse(rule["persistent_artifact"])
        self.assertIn("no real AIS / ADS-B", rule["derived_exclusions"])
        self.assertIn("no persistent runtime state", rule["derived_exclusions"])

    def test_forbidden_mutation_claim_rules(self):
        rules = PACKET["forbidden_mutation_claim_rules"]
        for value in rules.values():
            self.assertTrue(value)
        self.assertTrue(rules["formula_mutation_forbidden"])
        self.assertTrue(rules["renderer_behavior_mutation_forbidden"])
        self.assertTrue(rules["transparent_globe_leak_fix_claim_forbidden"])

    def test_oracle_rules_are_defined(self):
        self.assertEqual(
            PACKET["oracle_rules"],
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

    def test_decision_output_is_planning_only(self):
        decision = PACKET["decision_output"]
        self.assertTrue(decision["planning_gate_passed"])
        self.assertTrue(decision["representative_slice_strategy_defined"])
        self.assertTrue(decision["entrypoint_matrix_defined"])
        self.assertTrue(decision["monkey_condition_matrix_defined"])
        self.assertTrue(decision["contrast_token_matrix_defined"])
        self.assertTrue(decision["katyusha_matrix_plan_defined"])
        self.assertTrue(decision["oracle_rules_defined"])
        self.assertTrue(decision["runtime_characterization_candidate"])
        self.assertFalse(decision["runtime_characterization_authorized"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["formula_mutation_authorized"])
        self.assertFalse(decision["renderer_behavior_mutation_authorized"])
        self.assertFalse(decision["source_lineage_mutation_authorized"])
        self.assertFalse(decision["persistent_artifact_authorized"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_lod_view_frame_runtime_probe_authorization_review_gate")

    def test_boundary_statement_blocks_forbidden_actions(self):
        statement = PACKET["boundary_statement"]
        self.assertIn("No helper module creation", statement)
        self.assertIn("no runtime execution", statement)
        self.assertIn("no instrumentation", statement)
        self.assertIn("no monkey patch implementation", statement)
        self.assertIn("no __getattribute__ implementation", statement)
        self.assertIn("no sys.settrace", statement)
        self.assertIn("no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change", statement)
        self.assertIn("no coordinate/visual correctness claim", statement)
        self.assertIn("no transparent-globe leak fix claim", statement)
        self.assertIn("no runtime characterization authorization", statement)
        self.assertIn("no global methodology promotion", statement)


if __name__ == "__main__":
    unittest.main()
