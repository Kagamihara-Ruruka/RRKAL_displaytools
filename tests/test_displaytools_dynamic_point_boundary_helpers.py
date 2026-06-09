import unittest

from render_core import dynamic_point_boundary as boundary


DESCRIPTOR_BUILDERS = [
    boundary.build_dynamic_point_source_descriptor,
    boundary.build_dynamic_point_payload_shape_descriptor,
    boundary.build_dynamic_point_replay_live_lineage_descriptor,
    boundary.build_dynamic_point_selection_label_descriptor,
    boundary.build_dynamic_point_render_policy_label_descriptor,
    boundary.build_dynamic_point_safety_ledger_descriptor,
    boundary.build_dynamic_point_known_fault_ledger_descriptor,
]


COMMON_GUARD_KEYS = {
    "runtime_dependency_allowed",
    "sql_live_source_execution_allowed",
    "dataframe_runtime_allowed",
    "projection_formula_allowed",
    "controller_selection_runtime_allowed",
    "renderer_runtime_allowed",
}


EXPECTED_KEY_SETS = {
    "source": {
        "schema",
        "descriptor_kind",
        "source_kind",
        "source_evidence",
        "lineage_policy",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "payload": {
        "schema",
        "descriptor_kind",
        "payload_fields",
        "coordinate_payload_kind",
        "payload_runtime_parsed",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "lineage": {
        "schema",
        "descriptor_kind",
        "lineage_label",
        "lineage_status",
        "real_clock_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "selection": {
        "schema",
        "descriptor_kind",
        "selection_label",
        "selection_policy",
        "selection_runtime_mutated",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "render": {
        "schema",
        "descriptor_kind",
        "policy_label",
        "render_policy_labels",
        "render_runtime_invoked",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "safety": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "blocked_surfaces",
        "runtime_dependency_allowed",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "fault": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "known_faults",
        "live_data_restored",
        "bug_fixed",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "runtime_ready",
    "source_movement_authorized_true",
    "dynamic_point_extraction_candidate_true",
}


def is_dict_list_scalar(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return True
    if isinstance(value, list):
        return all(is_dict_list_scalar(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_dict_list_scalar(item) for key, item in value.items())
    return False


class DynamicPointBoundaryHelperTests(unittest.TestCase):
    def test_helper_module_import_is_safe(self):
        self.assertFalse(hasattr(boundary, "pymysql"))
        self.assertFalse(hasattr(boundary, "websocket"))
        self.assertFalse(hasattr(boundary, "datashader"))
        self.assertFalse(hasattr(boundary, "TaichiGlobeRenderer"))
        self.assertTrue(hasattr(boundary, "dynamic_point_boundary_descriptor"))

    def test_exact_key_sets_for_descriptor_builders(self):
        self.assertEqual(set(boundary.build_dynamic_point_source_descriptor()), EXPECTED_KEY_SETS["source"])
        self.assertEqual(set(boundary.build_dynamic_point_payload_shape_descriptor()), EXPECTED_KEY_SETS["payload"])
        self.assertEqual(set(boundary.build_dynamic_point_replay_live_lineage_descriptor()), EXPECTED_KEY_SETS["lineage"])
        self.assertEqual(set(boundary.build_dynamic_point_selection_label_descriptor()), EXPECTED_KEY_SETS["selection"])
        self.assertEqual(set(boundary.build_dynamic_point_render_policy_label_descriptor()), EXPECTED_KEY_SETS["render"])
        self.assertEqual(set(boundary.build_dynamic_point_safety_ledger_descriptor()), EXPECTED_KEY_SETS["safety"])
        self.assertEqual(set(boundary.build_dynamic_point_known_fault_ledger_descriptor()), EXPECTED_KEY_SETS["fault"])

    def test_deterministic_repeat_call_parity(self):
        for builder in DESCRIPTOR_BUILDERS:
            with self.subTest(builder=builder.__name__):
                self.assertEqual(builder(), builder())
        self.assertEqual(boundary.dynamic_point_boundary_descriptor(), boundary.dynamic_point_boundary_descriptor())
        self.assertEqual(boundary.dynamic_point_planning_bundle(), boundary.dynamic_point_planning_bundle())

    def test_outputs_are_dict_list_scalar_only(self):
        for builder in DESCRIPTOR_BUILDERS:
            with self.subTest(builder=builder.__name__):
                self.assertTrue(is_dict_list_scalar(builder()))
        self.assertTrue(is_dict_list_scalar(boundary.dynamic_point_boundary_descriptor()))
        self.assertTrue(is_dict_list_scalar(boundary.dynamic_point_planning_bundle()))

    def test_source_and_lineage_descriptor_branches(self):
        self.assertEqual(boundary.build_dynamic_point_source_descriptor("AIS")["source_kind"], "AIS")
        self.assertEqual(boundary.build_dynamic_point_source_descriptor("ADS-B")["source_kind"], "ADS-B")
        self.assertEqual(boundary.build_dynamic_point_source_descriptor("bad")["source_kind"], "unavailable")
        self.assertEqual(
            boundary.build_dynamic_point_replay_live_lineage_descriptor("live_lineage_unresolved")["lineage_label"],
            "live_lineage_unresolved",
        )
        self.assertEqual(boundary.build_dynamic_point_replay_live_lineage_descriptor("bad")["lineage_label"], "unavailable")
        self.assertFalse(boundary.build_dynamic_point_replay_live_lineage_descriptor()["real_clock_execution_used"])

    def test_payload_selection_render_safety_and_fault_branches(self):
        payload = boundary.build_dynamic_point_payload_shape_descriptor()
        selection = boundary.build_dynamic_point_selection_label_descriptor("selected_vehicle")
        render = boundary.build_dynamic_point_render_policy_label_descriptor("adaptive_sampling_label")
        safety = boundary.build_dynamic_point_safety_ledger_descriptor()
        fault = boundary.build_dynamic_point_known_fault_ledger_descriptor()
        self.assertEqual(payload["coordinate_payload_kind"], "raw_lon_lat_label_only")
        self.assertFalse(payload["payload_runtime_parsed"])
        self.assertEqual(selection["selection_policy"], "label_only")
        self.assertFalse(selection["selection_runtime_mutated"])
        self.assertEqual(render["policy_label"], "adaptive_sampling_label")
        self.assertFalse(render["render_runtime_invoked"])
        self.assertEqual(safety["fixture_status"], "blocked_runtime_only")
        self.assertIn("SQL replay database", safety["blocked_surfaces"])
        self.assertEqual(fault["fixture_status"], "unresolved_static_only")
        self.assertFalse(fault["live_data_restored"])
        self.assertFalse(fault["bug_fixed"])

    def test_planning_bundle_guard_flags(self):
        descriptor = boundary.dynamic_point_boundary_descriptor()
        bundle = boundary.dynamic_point_planning_bundle()
        for packet in [descriptor, bundle]:
            self.assertFalse(packet["source_movement_authorized"])
            self.assertFalse(packet["runtime_render_invoked"])
            self.assertFalse(packet["runtime_merge_enabled"])
            self.assertFalse(packet["visual_parity_ready"])
            self.assertFalse(packet["performance_ready"])
            self.assertFalse(packet["readiness_claimed"])
            self.assertFalse(packet["live_data_restored"])
        self.assertEqual(bundle["candidate_scope"], "descriptor_policy_ledger_only")

    def test_no_runtime_or_readiness_claims(self):
        packet_text = repr(boundary.dynamic_point_planning_bundle())
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
