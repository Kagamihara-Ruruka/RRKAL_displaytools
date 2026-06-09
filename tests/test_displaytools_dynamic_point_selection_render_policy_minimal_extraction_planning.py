import unittest


CANDIDATE_HELPERS = [
    "build_dynamic_point_selection_label_descriptor",
    "build_dynamic_point_hit_state_label_descriptor",
    "build_dynamic_point_picker_status_descriptor",
    "build_dynamic_point_render_count_policy_descriptor",
    "build_dynamic_point_render_cap_policy_descriptor",
    "build_dynamic_point_adaptive_sampling_policy_descriptor",
    "build_dynamic_point_selection_render_known_fault_ledger",
    "dynamic_point_selection_render_policy_boundary_descriptor",
    "dynamic_point_selection_render_policy_planning_bundle",
]

FIXTURE_PARITY_PLAN = [
    "helper import safety",
    "exact key-set parity for every descriptor builder",
    "deterministic repeat-call parity",
    "dict/list/scalar-only output",
    "selected vehicle label branch",
    "selected layer label branch",
    "hit state label branch",
    "picker status label branch",
    "visible count label branch",
    "rendered count label branch",
    "render cap label branch",
    "adaptive sampling label branch",
    "selection staleness fault branch",
    "hit-test dependency fault branch",
    "render policy guard flag branch",
    "known fault ledger branch",
    "planning bundle guard flags",
    "checker candidate PASS",
    "checker negative forbidden dependency FAIL",
]

BLOCKED_SURFACES = [
    "controller selection mutation",
    "selected vehicle runtime object",
    "selected layer runtime object",
    "selection state mutation",
    "picker / hit-test execution",
    "datashader / pandas / numpy runtime sampling",
    "renderer / Qt / VisPy / Taichi runtime",
    "projection / flip / mask formula",
    "SQL / WebSocket / live AIS / live ADS-B",
    "real AIS / ADS-B / cache / database read",
    "metadata / artifact writer",
    "alpha / apply / composition hot path",
    "readiness / performance / visual parity / bug-fix / live-data claims",
]

CANDIDATE_KEYS = {
    "helper_name",
    "candidate_for_minimal_extraction",
    "runtime_dependency_allowed",
    "expected_output_shape",
    "required_checker",
    "blocked_surface_refs",
    "fixture_parity_required",
}

PLANNING_PACKET_KEYS = {
    "minimal_extraction_planning_gate_passed",
    "future_helper_target",
    "required_checker",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "selection_render_policy_planning_candidate",
    "selection_render_policy_extraction_candidate",
    "a1_macro_observer_required_before_source_movement",
    "candidate_helpers",
    "fixture_parity_plan",
    "checker_expectation",
    "blocked_surfaces",
    "recommended_next_gate",
    "boundary_statement",
}

CHECKER_EXPECTATION_KEYS = {
    "current_missing_target_behavior",
    "expected_clean_candidate_behavior",
    "expected_runtime_dependency_behavior",
    "string_labels_allowed_as_data",
    "forbidden_executable_references_fail",
    "forbidden_declaration_names_fail",
}

REQUIRED_CHECKER = "scripts\\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py"
FUTURE_TARGET = "render_core\\dynamic_point_selection_render_policy_boundary.py"


def build_candidate_helpers():
    return [
        {
            "helper_name": helper_name,
            "candidate_for_minimal_extraction": True,
            "runtime_dependency_allowed": False,
            "expected_output_shape": "dict/list/scalar descriptor or planning packet",
            "required_checker": REQUIRED_CHECKER,
            "blocked_surface_refs": list(BLOCKED_SURFACES),
            "fixture_parity_required": True,
        }
        for helper_name in CANDIDATE_HELPERS
    ]


def build_checker_expectation():
    return {
        "current_missing_target_behavior": "PASS",
        "expected_clean_candidate_behavior": "PASS",
        "expected_runtime_dependency_behavior": "FAIL",
        "string_labels_allowed_as_data": True,
        "forbidden_executable_references_fail": True,
        "forbidden_declaration_names_fail": True,
    }


def build_minimal_extraction_planning_packet():
    return {
        "minimal_extraction_planning_gate_passed": True,
        "future_helper_target": FUTURE_TARGET,
        "required_checker": REQUIRED_CHECKER,
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "selection_render_policy_planning_candidate": True,
        "selection_render_policy_extraction_candidate": False,
        "a1_macro_observer_required_before_source_movement": False,
        "candidate_helpers": build_candidate_helpers(),
        "fixture_parity_plan": list(FIXTURE_PARITY_PLAN),
        "checker_expectation": build_checker_expectation(),
        "blocked_surfaces": list(BLOCKED_SURFACES),
        "recommended_next_gate": "dynamic_point_selection_render_policy_minimal_extraction_gate",
        "boundary_statement": "Docs/test-only dynamic point selection/render policy minimal extraction planning gate; no helper module creation or source movement authorized.",
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


class DynamicPointSelectionRenderPolicyMinimalExtractionPlanningTests(unittest.TestCase):
    def test_planning_packet_has_required_target_and_decisions(self):
        packet = build_minimal_extraction_planning_packet()

        self.assertEqual(set(packet), PLANNING_PACKET_KEYS)
        self.assertTrue(packet["minimal_extraction_planning_gate_passed"])
        self.assertEqual(packet["future_helper_target"], FUTURE_TARGET)
        self.assertEqual(packet["required_checker"], REQUIRED_CHECKER)
        self.assertTrue(packet["selection_render_policy_planning_candidate"])
        self.assertFalse(packet["selection_render_policy_extraction_candidate"])
        self.assertFalse(packet["helper_module_creation_authorized"])
        self.assertFalse(packet["source_movement_authorized"])
        self.assertFalse(packet["a1_macro_observer_required_before_source_movement"])
        self.assertEqual(packet["recommended_next_gate"], "dynamic_point_selection_render_policy_minimal_extraction_gate")

    def test_candidate_helper_list_is_exact_and_descriptor_only(self):
        candidates = build_candidate_helpers()

        self.assertEqual([entry["helper_name"] for entry in candidates], CANDIDATE_HELPERS)
        for entry in candidates:
            self.assertEqual(set(entry), CANDIDATE_KEYS)
            self.assertTrue(entry["candidate_for_minimal_extraction"])
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertEqual(entry["required_checker"], REQUIRED_CHECKER)
            self.assertTrue(entry["fixture_parity_required"])
            self.assertEqual(entry["blocked_surface_refs"], BLOCKED_SURFACES)

    def test_fixture_parity_plan_is_complete(self):
        packet = build_minimal_extraction_planning_packet()

        self.assertEqual(packet["fixture_parity_plan"], FIXTURE_PARITY_PLAN)
        for required_case in [
            "helper import safety",
            "selected vehicle label branch",
            "selected layer label branch",
            "hit state label branch",
            "picker status label branch",
            "visible count label branch",
            "rendered count label branch",
            "render cap label branch",
            "adaptive sampling label branch",
            "checker candidate PASS",
            "checker negative forbidden dependency FAIL",
        ]:
            self.assertIn(required_case, packet["fixture_parity_plan"])

    def test_checker_expectation_is_pinned(self):
        expectation = build_checker_expectation()

        self.assertEqual(set(expectation), CHECKER_EXPECTATION_KEYS)
        self.assertEqual(expectation["current_missing_target_behavior"], "PASS")
        self.assertEqual(expectation["expected_clean_candidate_behavior"], "PASS")
        self.assertEqual(expectation["expected_runtime_dependency_behavior"], "FAIL")
        self.assertTrue(expectation["string_labels_allowed_as_data"])
        self.assertTrue(expectation["forbidden_executable_references_fail"])
        self.assertTrue(expectation["forbidden_declaration_names_fail"])

    def test_blocked_surfaces_are_complete_and_not_candidates(self):
        packet = build_minimal_extraction_planning_packet()

        self.assertEqual(packet["blocked_surfaces"], BLOCKED_SURFACES)
        for blocked_surface in packet["blocked_surfaces"]:
            self.assertIn(blocked_surface, BLOCKED_SURFACES)

    def test_packets_are_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_candidate_helpers()))
        self.assertTrue(is_packet_data(build_checker_expectation()))
        self.assertTrue(is_packet_data(build_minimal_extraction_planning_packet()))

    def test_no_helper_creation_source_movement_runtime_or_claim_markers(self):
        packet_text = repr(build_minimal_extraction_planning_packet())
        for marker in [
            "taichi_global_bathymetry",
            "helper_module_creation_authorized_true",
            "source_movement_authorized_true",
            "selection_render_policy_extraction_candidate_true",
            "controller_runtime_allowed",
            "picker_runtime_allowed",
            "datashader_runtime_allowed",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "readiness_claimed",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()