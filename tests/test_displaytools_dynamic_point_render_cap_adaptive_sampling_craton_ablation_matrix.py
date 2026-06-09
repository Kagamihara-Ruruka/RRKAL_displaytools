import unittest


PIN_KEYS = {
    "pin_name",
    "ablation_modes",
    "consumer_expectation",
    "rollback_method",
    "dependency_classification",
    "fixture_status",
    "forbidden_next_action",
}

DETERMINISTIC_FILL_KEYS = {
    "future_helper_target",
    "new_checker_required",
    "existing_checker_reusable",
    "render_cap_adaptive_sampling_planning_candidate",
    "render_cap_adaptive_sampling_extraction_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "candidate_helper_families",
    "blocked_runtime_surfaces",
    "recommended_next_gate",
}

REQUIRED_MODES = ["null_mode", "tripwire_mode", "trace_mode", "substitute_mode"]

REQUIRED_PINS = [
    "visible_count_pin",
    "rendered_count_pin",
    "render_cap_pin",
    "adaptive_sampling_pin",
    "cap_exceeded_fault_pin",
    "sampling_degraded_fault_pin",
    "datashader_runtime_dependency_stop_pin",
    "pandas_numpy_runtime_dependency_stop_pin",
    "renderer_runtime_dependency_stop_pin",
    "selection_policy_dependency_pin",
    "payload_quality_dependency_pin",
]

CANDIDATE_FAMILIES = [
    "build_dynamic_point_visible_count_descriptor",
    "build_dynamic_point_rendered_count_descriptor",
    "build_dynamic_point_render_cap_policy_descriptor",
    "build_dynamic_point_adaptive_sampling_policy_descriptor",
    "build_dynamic_point_sampling_dependency_descriptor",
    "build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger",
    "dynamic_point_render_cap_adaptive_sampling_boundary_descriptor",
    "dynamic_point_render_cap_adaptive_sampling_planning_bundle",
]

BLOCKED_RUNTIME_SURFACES = [
    "datashader_runtime_dependency",
    "pandas_numpy_runtime_dependency",
    "renderer_runtime_dependency",
    "projection_flip_mask_formula",
    "controller_selection_picker_hit_test_mutation",
    "sql_websocket_live_source",
    "metadata_artifact_writer",
    "alpha_apply_composition_hot_path",
]


def build_pin(pin_name, dependency_classification, fixture_status, consumer_expectation, forbidden_next_action):
    return {
        "pin_name": pin_name,
        "ablation_modes": list(REQUIRED_MODES),
        "consumer_expectation": consumer_expectation,
        "rollback_method": "restore test-local descriptor matrix only",
        "dependency_classification": dependency_classification,
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_render_cap_adaptive_sampling_ablation_matrix_packet():
    phase_a_matrix = [
        build_pin("visible_count_pin", "descriptor_policy_label", "pinned", "descriptor bundle can lose visible count label without requiring runtime count query", "do_not_query_renderer_visible_count"),
        build_pin("rendered_count_pin", "descriptor_policy_label", "pinned", "descriptor bundle can trace rendered count label without requiring renderer buffer", "do_not_query_renderer_rendered_count"),
        build_pin("render_cap_pin", "descriptor_policy_label", "pinned", "cap policy label can be substituted as data-only descriptor", "do_not_execute_render_cap_runtime"),
        build_pin("adaptive_sampling_pin", "descriptor_policy_label", "pinned", "adaptive sampling label can be substituted without datashader runtime", "do_not_execute_adaptive_sampling_runtime"),
        build_pin("cap_exceeded_fault_pin", "known_fault_ledger", "unresolved_static_only", "tripwire records cap-exceeded ambiguity and stops before runtime count parity", "do_not_claim_cap_exceeded_behavior_fixed"),
        build_pin("sampling_degraded_fault_pin", "known_fault_ledger", "unresolved_static_only", "tripwire records degraded sampling ambiguity and stops before datashader execution", "do_not_claim_sampling_degraded_behavior_fixed"),
        build_pin("datashader_runtime_dependency_stop_pin", "blocked_runtime_dependency", "blocked_runtime_only", "runtime sampling dependency is blocked and becomes extraction stop condition", "do_not_import_or_execute_datashader"),
        build_pin("pandas_numpy_runtime_dependency_stop_pin", "blocked_runtime_dependency", "blocked_runtime_only", "dataframe dependency is blocked and becomes extraction stop condition", "do_not_import_or_execute_pandas_numpy"),
        build_pin("renderer_runtime_dependency_stop_pin", "blocked_runtime_dependency", "blocked_runtime_only", "renderer host dependency is blocked and becomes extraction stop condition", "do_not_execute_renderer_qt_vispy_taichi"),
        build_pin("selection_policy_dependency_pin", "adjacent_descriptor_dependency", "pinned", "selection/render policy peer remains descriptor dependency only", "do_not_modify_selection_render_policy_helper"),
        build_pin("payload_quality_dependency_pin", "adjacent_descriptor_dependency", "pinned", "payload quality peer remains descriptor dependency only", "do_not_modify_payload_coordinate_quality_helper"),
    ]
    phase_b_fill = {
        "future_helper_target": "render_core/dynamic_point_render_cap_adaptive_sampling_boundary.py",
        "new_checker_required": True,
        "existing_checker_reusable": False,
        "render_cap_adaptive_sampling_planning_candidate": True,
        "render_cap_adaptive_sampling_extraction_candidate": False,
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "candidate_helper_families": list(CANDIDATE_FAMILIES),
        "blocked_runtime_surfaces": list(BLOCKED_RUNTIME_SURFACES),
        "recommended_next_gate": "dynamic_point_render_cap_adaptive_sampling_import_boundary_checker_gate",
    }
    return {
        "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling_craton_ablation_matrix.v1",
        "phase_a_matrix": phase_a_matrix,
        "phase_b_deterministic_boundary_fill": phase_b_fill,
        "phase_c_recommended_next_gate": "dynamic_point_render_cap_adaptive_sampling_import_boundary_checker_gate",
        "production_source_change_authorized": False,
        "helper_module_creation_authorized": False,
        "checker_creation_authorized": False,
        "generic_checker_trust_level_change_authorized": False,
        "generic_checker_blocking_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "readiness_claimed": False,
        "boundary_statement": "Docs/test-only dynamic point render cap / adaptive sampling craton ablation matrix and deterministic boundary fill gate; no helper/checker creation, source movement, runtime execution, or readiness claim.",
    }


def is_scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def is_packet_data(value):
    if is_scalar(value):
        return True
    if isinstance(value, list):
        return all(is_packet_data(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_packet_data(item) for key, item in value.items())
    return False


class DynamicPointRenderCapAdaptiveSamplingCratonAblationMatrixTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_render_cap_adaptive_sampling_ablation_matrix_packet()
        self.pins = {entry["pin_name"]: entry for entry in self.packet["phase_a_matrix"]}
        self.fill = self.packet["phase_b_deterministic_boundary_fill"]

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(self.packet))

    def test_phase_a_matrix_contains_required_pins(self):
        self.assertEqual(set(self.pins), set(REQUIRED_PINS))
        for pin in self.packet["phase_a_matrix"]:
            self.assertEqual(set(pin), PIN_KEYS)
            self.assertEqual(pin["ablation_modes"], REQUIRED_MODES)
            self.assertIn("do_not", pin["forbidden_next_action"])

    def test_descriptor_and_fault_pins_are_not_runtime_dependencies(self):
        for pin_name in ["visible_count_pin", "rendered_count_pin", "render_cap_pin", "adaptive_sampling_pin"]:
            self.assertEqual(self.pins[pin_name]["dependency_classification"], "descriptor_policy_label")
            self.assertEqual(self.pins[pin_name]["fixture_status"], "pinned")
        for pin_name in ["cap_exceeded_fault_pin", "sampling_degraded_fault_pin"]:
            self.assertEqual(self.pins[pin_name]["dependency_classification"], "known_fault_ledger")
            self.assertEqual(self.pins[pin_name]["fixture_status"], "unresolved_static_only")

    def test_runtime_dependency_pins_are_blocked(self):
        for pin_name in [
            "datashader_runtime_dependency_stop_pin",
            "pandas_numpy_runtime_dependency_stop_pin",
            "renderer_runtime_dependency_stop_pin",
        ]:
            self.assertEqual(self.pins[pin_name]["dependency_classification"], "blocked_runtime_dependency")
            self.assertEqual(self.pins[pin_name]["fixture_status"], "blocked_runtime_only")

    def test_adjacent_dependency_pins_remain_descriptor_only(self):
        self.assertEqual(self.pins["selection_policy_dependency_pin"]["dependency_classification"], "adjacent_descriptor_dependency")
        self.assertEqual(self.pins["payload_quality_dependency_pin"]["dependency_classification"], "adjacent_descriptor_dependency")

    def test_phase_b_deterministic_boundary_fill_is_pinned(self):
        self.assertEqual(set(self.fill), DETERMINISTIC_FILL_KEYS)
        self.assertEqual(self.fill["future_helper_target"], "render_core/dynamic_point_render_cap_adaptive_sampling_boundary.py")
        self.assertTrue(self.fill["new_checker_required"])
        self.assertFalse(self.fill["existing_checker_reusable"])
        self.assertTrue(self.fill["render_cap_adaptive_sampling_planning_candidate"])
        self.assertFalse(self.fill["render_cap_adaptive_sampling_extraction_candidate"])
        self.assertFalse(self.fill["helper_module_creation_authorized"])
        self.assertFalse(self.fill["source_movement_authorized"])

    def test_candidate_families_are_planning_only(self):
        self.assertEqual(self.fill["candidate_helper_families"], CANDIDATE_FAMILIES)
        self.assertFalse(self.fill["helper_module_creation_authorized"])
        self.assertFalse(self.packet["helper_module_creation_authorized"])

    def test_blocked_surfaces_are_retained(self):
        self.assertEqual(self.fill["blocked_runtime_surfaces"], BLOCKED_RUNTIME_SURFACES)
        for surface in [
            "datashader_runtime_dependency",
            "pandas_numpy_runtime_dependency",
            "renderer_runtime_dependency",
            "projection_flip_mask_formula",
            "controller_selection_picker_hit_test_mutation",
            "sql_websocket_live_source",
            "metadata_artifact_writer",
            "alpha_apply_composition_hot_path",
        ]:
            self.assertIn(surface, self.fill["blocked_runtime_surfaces"])

    def test_phase_c_recommends_import_boundary_checker_gate(self):
        self.assertEqual(self.packet["phase_c_recommended_next_gate"], "dynamic_point_render_cap_adaptive_sampling_import_boundary_checker_gate")
        self.assertEqual(self.fill["recommended_next_gate"], self.packet["phase_c_recommended_next_gate"])

    def test_no_source_movement_checker_creation_or_generic_checker_upgrade(self):
        self.assertFalse(self.packet["production_source_change_authorized"])
        self.assertFalse(self.packet["helper_module_creation_authorized"])
        self.assertFalse(self.packet["checker_creation_authorized"])
        self.assertFalse(self.packet["generic_checker_trust_level_change_authorized"])
        self.assertFalse(self.packet["generic_checker_blocking_authorized"])
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["runtime_merge_enabled"])
        self.assertFalse(self.packet["readiness_claimed"])

    def test_no_runtime_readiness_or_bug_fix_claims(self):
        packet_text = repr(self.packet)
        for marker in [
            "production_source_change_authorized': True",
            "helper_module_creation_authorized': True",
            "checker_creation_authorized': True",
            "generic_checker_trust_level_change_authorized': True",
            "generic_checker_blocking_authorized': True",
            "runtime_render_invoked': True",
            "runtime_merge_enabled': True",
            "readiness_claimed': True",
            "safe_to_extract_claimed",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "live_data_restored",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
