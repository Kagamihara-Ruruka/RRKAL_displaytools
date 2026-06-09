import unittest


PIN_FIELDS = {
    "pin_name",
    "ablation_modes",
    "consumer_expectation",
    "rollback_method",
    "dependency_classification",
    "fixture_status",
    "forbidden_next_action",
}

BOUNDARY_FILL_KEYS = {
    "future_helper_target",
    "descriptor_candidate_families",
    "blocked_runtime_surfaces",
    "import_boundary_checker_needed",
    "existing_checker_reusable",
    "new_checker_required",
    "selection_render_policy_planning_candidate",
    "selection_render_policy_extraction_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "checker_decision_reason",
}

REQUIRED_PINS = {
    "selected_vehicle_label",
    "selected_layer_label",
    "hit_state_label",
    "picker_status_label",
    "visible_count_label",
    "rendered_count_label",
    "render_cap_label",
    "adaptive_sampling_label",
    "selection_staleness_fault",
    "hit_test_dependency_fault",
    "render_policy_guard_flag",
    "controller_selection_runtime_dependency",
    "picker_hit_test_runtime_dependency",
    "datashader_sampling_runtime_dependency",
    "renderer_host_runtime_dependency",
}

REQUIRED_ABLATION_MODES = {"null_mode", "tripwire_mode", "trace_mode", "substitute_mode"}

REQUIRED_CANDIDATE_FAMILIES = [
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

REQUIRED_BLOCKED_SURFACES = [
    "controller selection mutation",
    "selected vehicle runtime object",
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


def pin(pin_name, consumer_expectation, rollback_method, dependency_classification, fixture_status, forbidden_next_action):
    return {
        "pin_name": pin_name,
        "ablation_modes": ["null_mode", "tripwire_mode", "trace_mode", "substitute_mode"],
        "consumer_expectation": consumer_expectation,
        "rollback_method": rollback_method,
        "dependency_classification": dependency_classification,
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_selection_render_policy_ablation_matrix():
    return [
        pin(
            "selected_vehicle_label",
            "descriptor consumers degrade to no selected vehicle label only",
            "restore selected vehicle label descriptor",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_resolve_selected_vehicle_runtime_object",
        ),
        pin(
            "selected_layer_label",
            "descriptor consumers degrade to no selected layer label only",
            "restore selected layer label descriptor",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_mutate_controller_selected_layer",
        ),
        pin(
            "hit_state_label",
            "trace mode records hit true false unresolved labels only",
            "reset test-local hit state descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_execute_picker_or_hit_test_runtime",
        ),
        pin(
            "picker_status_label",
            "tripwire marks picker status as runtime-adjacent label only",
            "restore picker status descriptor label",
            "descriptor_label_with_blocked_runtime_peer",
            "pinned",
            "do_not_execute_picker_runtime",
        ),
        pin(
            "visible_count_label",
            "null mode keeps visible count policy as scalar label",
            "restore visible count descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_query_renderer_or_dataframe_count",
        ),
        pin(
            "rendered_count_label",
            "null mode keeps rendered count policy as scalar label",
            "restore rendered count descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_query_render_buffer_or_runtime_count",
        ),
        pin(
            "render_cap_label",
            "substitute mode keeps render cap as policy label",
            "restore render cap descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_execute_datashader_sampling_or_renderer_cap_logic",
        ),
        pin(
            "adaptive_sampling_label",
            "substitute mode keeps adaptive sampling as label-only policy",
            "restore adaptive sampling descriptor label",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_execute_adaptive_sampling_runtime",
        ),
        pin(
            "selection_staleness_fault",
            "trace mode records stale selection as known fault ledger only",
            "reset selection fault ledger descriptor",
            "descriptor_policy_ledger",
            "unresolved_static_only",
            "do_not_claim_selection_bug_fix_or_runtime_sync",
        ),
        pin(
            "hit_test_dependency_fault",
            "tripwire marks hit-test dependency as blocked runtime peer",
            "reset hit-test dependency fault ledger",
            "descriptor_label_with_blocked_runtime_peer",
            "blocked_runtime_only",
            "do_not_execute_hit_test_or_picker_runtime",
        ),
        pin(
            "render_policy_guard_flag",
            "substitute mode preserves guard flags without runtime policy execution",
            "restore render policy guard flag descriptor",
            "descriptor_policy_ledger",
            "pinned",
            "do_not_weaken_render_policy_runtime_stop_lines",
        ),
        pin(
            "controller_selection_runtime_dependency",
            "tripwire must stop extraction if controller selection mutation is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_mutate_controller_selection_runtime",
        ),
        pin(
            "picker_hit_test_runtime_dependency",
            "tripwire must stop extraction if picker or hit-test execution is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_picker_or_hit_test_runtime",
        ),
        pin(
            "datashader_sampling_runtime_dependency",
            "tripwire must stop extraction if dataframe sampling runtime is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_import_datashader_pandas_numpy_runtime",
        ),
        pin(
            "renderer_host_runtime_dependency",
            "tripwire must stop extraction if renderer host runtime is required",
            "not applicable because no runtime patch is used",
            "blocked_runtime_dependency",
            "blocked_runtime_only",
            "do_not_execute_renderer_qt_vispy_taichi_runtime",
        ),
    ]


def build_deterministic_boundary_fill():
    return {
        "future_helper_target": "render_core\\dynamic_point_selection_render_policy_boundary.py",
        "descriptor_candidate_families": list(REQUIRED_CANDIDATE_FAMILIES),
        "blocked_runtime_surfaces": list(REQUIRED_BLOCKED_SURFACES),
        "import_boundary_checker_needed": True,
        "existing_checker_reusable": False,
        "new_checker_required": True,
        "selection_render_policy_planning_candidate": True,
        "selection_render_policy_extraction_candidate": False,
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "checker_decision_reason": "future target is selection-render-policy specific and needs dedicated checker before extraction planning",
    }


def build_next_gate_decision():
    return {
        "recommended_next_gate": "dynamic_point_selection_render_policy_import_boundary_checker_gate",
        "reason": "new helper target needs an independent checker because controller and picker runtime risks differ from source-lineage risks",
        "runtime_risk_excluded_by_matrix": True,
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "extraction_candidate_claimed": False,
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


class DynamicPointSelectionRenderPolicyCratonAblationMatrixTests(unittest.TestCase):
    def test_phase_a_matrix_has_required_pins_and_fields(self):
        matrix = build_selection_render_policy_ablation_matrix()
        self.assertEqual({entry["pin_name"] for entry in matrix}, REQUIRED_PINS)
        for entry in matrix:
            self.assertEqual(set(entry), PIN_FIELDS)
            self.assertEqual(set(entry["ablation_modes"]), REQUIRED_ABLATION_MODES)
            self.assertIn(entry["fixture_status"], {"pinned", "unresolved_static_only", "blocked_runtime_only"})
            self.assertIn("do_not", entry["forbidden_next_action"])

    def test_runtime_dependency_pins_are_blocked(self):
        blocked = [entry for entry in build_selection_render_policy_ablation_matrix() if entry["fixture_status"] == "blocked_runtime_only"]
        self.assertEqual(
            {entry["pin_name"] for entry in blocked},
            {
                "hit_test_dependency_fault",
                "controller_selection_runtime_dependency",
                "picker_hit_test_runtime_dependency",
                "datashader_sampling_runtime_dependency",
                "renderer_host_runtime_dependency",
            },
        )
        for entry in blocked:
            self.assertIn(entry["dependency_classification"], {"blocked_runtime_dependency", "descriptor_label_with_blocked_runtime_peer"})

    def test_descriptor_policy_pins_remain_planning_only(self):
        descriptor_entries = [entry for entry in build_selection_render_policy_ablation_matrix() if entry["dependency_classification"].startswith("descriptor")]
        self.assertGreaterEqual(len(descriptor_entries), 10)
        for entry in descriptor_entries:
            if entry["pin_name"] != "hit_test_dependency_fault":
                self.assertNotEqual(entry["fixture_status"], "blocked_runtime_only")

    def test_phase_b_deterministic_boundary_fill_is_pinned(self):
        fill = build_deterministic_boundary_fill()
        self.assertEqual(set(fill), BOUNDARY_FILL_KEYS)
        self.assertEqual(fill["future_helper_target"], "render_core\\dynamic_point_selection_render_policy_boundary.py")
        self.assertEqual(fill["descriptor_candidate_families"], REQUIRED_CANDIDATE_FAMILIES)
        self.assertEqual(fill["blocked_runtime_surfaces"], REQUIRED_BLOCKED_SURFACES)
        self.assertTrue(fill["import_boundary_checker_needed"])
        self.assertFalse(fill["existing_checker_reusable"])
        self.assertTrue(fill["new_checker_required"])
        self.assertTrue(fill["selection_render_policy_planning_candidate"])
        self.assertFalse(fill["selection_render_policy_extraction_candidate"])
        self.assertFalse(fill["helper_module_creation_authorized"])
        self.assertFalse(fill["source_movement_authorized"])

    def test_candidate_families_are_descriptor_only(self):
        fill = build_deterministic_boundary_fill()
        self.assertEqual(fill["descriptor_candidate_families"], REQUIRED_CANDIDATE_FAMILIES)
        for name in fill["descriptor_candidate_families"]:
            self.assertTrue(name.startswith("build_dynamic_point_") or name.startswith("dynamic_point_"))

    def test_phase_c_recommends_new_import_boundary_checker_gate(self):
        decision = build_next_gate_decision()
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_selection_render_policy_import_boundary_checker_gate")
        self.assertTrue(decision["runtime_risk_excluded_by_matrix"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["extraction_candidate_claimed"])

    def test_packets_are_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_selection_render_policy_ablation_matrix()))
        self.assertTrue(is_packet_data(build_deterministic_boundary_fill()))
        self.assertTrue(is_packet_data(build_next_gate_decision()))

    def test_no_helper_runtime_or_claim_markers(self):
        packet_text = repr(build_selection_render_policy_ablation_matrix()) + repr(build_deterministic_boundary_fill()) + repr(build_next_gate_decision())
        for marker in [
            "taichi_global_bathymetry",
            "helper_module_creation_authorized_true",
            "source_movement_authorized_true",
            "selection_render_policy_extraction_candidate_true",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "readiness_claimed",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
