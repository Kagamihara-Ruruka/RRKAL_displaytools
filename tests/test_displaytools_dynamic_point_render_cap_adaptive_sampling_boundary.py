import unittest


DESCRIPTOR_KEYS = {
    "surface_name",
    "source_evidence",
    "classification",
    "input_labels",
    "policy_labels",
    "consumer_layers",
    "known_faults",
    "runtime_dependency_allowed",
    "readiness_claimed",
    "forbidden_next_action",
}

DECISION_KEYS = {
    "render_cap_adaptive_sampling_boundary_fixture_gate_passed",
    "render_cap_adaptive_sampling_planning_candidate",
    "render_cap_adaptive_sampling_extraction_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "runtime_render_invoked",
    "runtime_merge_enabled",
    "readiness_claimed",
    "recommended_next_gate",
}

ALLOWED_CLASSIFICATIONS = {
    "descriptor_only",
    "blocked_runtime_only",
    "unresolved_static_only",
    "adjacent_descriptor_dependency",
}


def build_descriptor(surface_name, classification, labels, known_faults=None, forbidden_next_action="do_not_execute_runtime"):
    return {
        "surface_name": surface_name,
        "source_evidence": "dynamic point render cap/adaptive sampling boundary fixture; static descriptor only",
        "classification": classification,
        "input_labels": list(labels),
        "policy_labels": list(labels),
        "consumer_layers": ["dynamic_point_descriptor_bundle", "selection_render_policy_peer", "payload_quality_peer"],
        "known_faults": list(known_faults or []),
        "runtime_dependency_allowed": False,
        "readiness_claimed": False,
        "forbidden_next_action": forbidden_next_action,
    }


def build_render_cap_adaptive_sampling_fixture_packet():
    descriptors = [
        build_descriptor("visible_count_label", "descriptor_only", ["visible_count", "below_cap", "equals_cap", "exceeds_cap"]),
        build_descriptor("rendered_count_label", "descriptor_only", ["rendered_count", "lower_than_visible", "equals_visible"]),
        build_descriptor("render_cap_label", "descriptor_only", ["render_cap", "cap_enabled", "cap_disabled", "cap_unknown"]),
        build_descriptor("adaptive_sampling_label", "descriptor_only", ["adaptive_sampling", "enabled", "disabled", "degraded"]),
        build_descriptor("cap_exceeded_label", "unresolved_static_only", ["cap_exceeded"], ["cap_exceeded_without_runtime_count_parity"]),
        build_descriptor("sampling_degraded_label", "unresolved_static_only", ["sampling_degraded"], ["adaptive_sampling_degraded_without_datashader_runtime"]),
        build_descriptor("datashader_runtime_dependency", "blocked_runtime_only", ["datashader_runtime_dependency"], ["runtime_sampling_dependency"], "do_not_import_or_execute_datashader"),
        build_descriptor("pandas_numpy_runtime_dependency", "blocked_runtime_only", ["pandas_numpy_runtime_dependency"], ["dataframe_runtime_dependency"], "do_not_import_or_execute_pandas_numpy"),
        build_descriptor("renderer_runtime_dependency", "blocked_runtime_only", ["renderer_runtime_dependency"], ["renderer_runtime_dependency"], "do_not_execute_renderer_qt_vispy_taichi"),
        build_descriptor("selection_policy_dependency", "adjacent_descriptor_dependency", ["selection_render_policy_dependency"], ["selection_policy_sync_unproven"], "do_not_modify_selection_render_policy_helper"),
        build_descriptor("payload_quality_dependency", "adjacent_descriptor_dependency", ["payload_quality_dependency"], ["payload_quality_sync_unproven"], "do_not_modify_payload_coordinate_quality_helper"),
        build_descriptor("known_fault_ledger", "unresolved_static_only", ["render_cap_fault", "adaptive_sampling_fault"], ["cap_exceeded_without_runtime_count_parity", "adaptive_sampling_degraded_without_datashader_runtime", "selection_payload_dependency_unproven"]),
    ]
    fixture_cases = [
        {"case_id": "visible_count_below_cap", "surface_name": "visible_count_label", "expected_classification": "descriptor_only"},
        {"case_id": "visible_count_equals_cap", "surface_name": "visible_count_label", "expected_classification": "descriptor_only"},
        {"case_id": "visible_count_exceeds_cap", "surface_name": "cap_exceeded_label", "expected_classification": "unresolved_static_only"},
        {"case_id": "rendered_count_lower_than_visible", "surface_name": "rendered_count_label", "expected_classification": "descriptor_only"},
        {"case_id": "render_cap_disabled_label", "surface_name": "render_cap_label", "expected_classification": "descriptor_only"},
        {"case_id": "render_cap_unknown_label", "surface_name": "render_cap_label", "expected_classification": "descriptor_only"},
        {"case_id": "adaptive_sampling_enabled_label", "surface_name": "adaptive_sampling_label", "expected_classification": "descriptor_only"},
        {"case_id": "adaptive_sampling_disabled_label", "surface_name": "adaptive_sampling_label", "expected_classification": "descriptor_only"},
        {"case_id": "adaptive_sampling_degraded_label", "surface_name": "sampling_degraded_label", "expected_classification": "unresolved_static_only"},
        {"case_id": "datashader_runtime_blocked_surface", "surface_name": "datashader_runtime_dependency", "expected_classification": "blocked_runtime_only"},
        {"case_id": "pandas_numpy_runtime_blocked_surface", "surface_name": "pandas_numpy_runtime_dependency", "expected_classification": "blocked_runtime_only"},
        {"case_id": "renderer_runtime_blocked_surface", "surface_name": "renderer_runtime_dependency", "expected_classification": "blocked_runtime_only"},
        {"case_id": "selection_render_policy_dependency_label", "surface_name": "selection_policy_dependency", "expected_classification": "adjacent_descriptor_dependency"},
        {"case_id": "payload_quality_dependency_label", "surface_name": "payload_quality_dependency", "expected_classification": "adjacent_descriptor_dependency"},
    ]
    return {
        "schema": "rrkal_displaytools.dynamic_point_render_cap_adaptive_sampling_boundary_fixture.v1",
        "descriptors": descriptors,
        "fixture_cases": fixture_cases,
        "decision_output": {
            "render_cap_adaptive_sampling_boundary_fixture_gate_passed": True,
            "render_cap_adaptive_sampling_planning_candidate": True,
            "render_cap_adaptive_sampling_extraction_candidate": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "runtime_render_invoked": False,
            "runtime_merge_enabled": False,
            "readiness_claimed": False,
            "recommended_next_gate": "dynamic_point_render_cap_adaptive_sampling_craton_ablation_matrix_gate",
        },
        "boundary_statement": "Docs/test-only dynamic point render cap / adaptive sampling boundary fixture gate; no runtime, source movement, helper creation, checker change, or readiness claim.",
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


class DynamicPointRenderCapAdaptiveSamplingBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_render_cap_adaptive_sampling_fixture_packet()
        self.descriptors = {entry["surface_name"]: entry for entry in self.packet["descriptors"]}

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(self.packet))

    def test_descriptor_key_sets_and_allowed_classifications(self):
        for descriptor in self.packet["descriptors"]:
            self.assertEqual(set(descriptor), DESCRIPTOR_KEYS)
            self.assertIn(descriptor["classification"], ALLOWED_CLASSIFICATIONS)
            self.assertFalse(descriptor["runtime_dependency_allowed"])
            self.assertFalse(descriptor["readiness_claimed"])

    def test_required_surfaces_are_present(self):
        self.assertEqual(
            set(self.descriptors),
            {
                "visible_count_label",
                "rendered_count_label",
                "render_cap_label",
                "adaptive_sampling_label",
                "cap_exceeded_label",
                "sampling_degraded_label",
                "datashader_runtime_dependency",
                "pandas_numpy_runtime_dependency",
                "renderer_runtime_dependency",
                "selection_policy_dependency",
                "payload_quality_dependency",
                "known_fault_ledger",
            },
        )

    def test_descriptor_policy_labels_are_descriptor_only(self):
        for surface in ["visible_count_label", "rendered_count_label", "render_cap_label", "adaptive_sampling_label"]:
            self.assertEqual(self.descriptors[surface]["classification"], "descriptor_only")

    def test_runtime_dependencies_are_blocked_runtime_only(self):
        for surface in ["datashader_runtime_dependency", "pandas_numpy_runtime_dependency", "renderer_runtime_dependency"]:
            descriptor = self.descriptors[surface]
            self.assertEqual(descriptor["classification"], "blocked_runtime_only")
            self.assertIn("do_not", descriptor["forbidden_next_action"])

    def test_unresolved_sampling_faults_remain_static_only(self):
        for surface in ["cap_exceeded_label", "sampling_degraded_label", "known_fault_ledger"]:
            self.assertEqual(self.descriptors[surface]["classification"], "unresolved_static_only")

    def test_adjacent_dependencies_are_descriptor_dependencies(self):
        self.assertEqual(self.descriptors["selection_policy_dependency"]["classification"], "adjacent_descriptor_dependency")
        self.assertEqual(self.descriptors["payload_quality_dependency"]["classification"], "adjacent_descriptor_dependency")

    def test_required_fixture_cases_are_covered(self):
        case_ids = {case["case_id"] for case in self.packet["fixture_cases"]}
        for case_id in [
            "visible_count_below_cap",
            "visible_count_equals_cap",
            "visible_count_exceeds_cap",
            "rendered_count_lower_than_visible",
            "render_cap_disabled_label",
            "render_cap_unknown_label",
            "adaptive_sampling_enabled_label",
            "adaptive_sampling_disabled_label",
            "adaptive_sampling_degraded_label",
            "datashader_runtime_blocked_surface",
            "pandas_numpy_runtime_blocked_surface",
            "renderer_runtime_blocked_surface",
            "selection_render_policy_dependency_label",
            "payload_quality_dependency_label",
        ]:
            self.assertIn(case_id, case_ids)

    def test_fixture_cases_match_surface_classification(self):
        for case in self.packet["fixture_cases"]:
            self.assertEqual(self.descriptors[case["surface_name"]]["classification"], case["expected_classification"])

    def test_decision_output_disables_extraction_and_runtime(self):
        decision = self.packet["decision_output"]
        self.assertEqual(set(decision), DECISION_KEYS)
        self.assertTrue(decision["render_cap_adaptive_sampling_boundary_fixture_gate_passed"])
        self.assertTrue(decision["render_cap_adaptive_sampling_planning_candidate"])
        self.assertFalse(decision["render_cap_adaptive_sampling_extraction_candidate"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["runtime_render_invoked"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_render_cap_adaptive_sampling_craton_ablation_matrix_gate")

    def test_no_runtime_readiness_or_bug_fix_claims(self):
        packet_text = repr(self.packet)
        for marker in [
            "runtime_dependency_allowed': True",
            "source_movement_authorized': True",
            "helper_module_creation_authorized': True",
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
