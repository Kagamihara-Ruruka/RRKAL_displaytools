import importlib
import unittest

from render_core import dynamic_point_source_lineage_boundary as helper


BUILDER_EXPECTED_KEYS = {
    "build_dynamic_point_source_lineage_descriptor": {
        "schema",
        "descriptor_kind",
        "source_label",
        "lineage_label",
        "available_source_labels",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
    "build_dynamic_point_replay_lineage_label_descriptor": {
        "schema",
        "descriptor_kind",
        "lineage_label",
        "lineage_status",
        "provider_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
    "build_dynamic_point_live_lineage_label_descriptor": {
        "schema",
        "descriptor_kind",
        "lineage_label",
        "lineage_status",
        "provider_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
    "build_dynamic_point_source_availability_descriptor": {
        "schema",
        "descriptor_kind",
        "availability_label",
        "availability_policy",
        "source_probe_performed",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
    "build_dynamic_point_timestamp_quality_descriptor": {
        "schema",
        "descriptor_kind",
        "timestamp_quality",
        "quality_branches",
        "real_clock_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
    "build_dynamic_point_coordinate_payload_quality_descriptor": {
        "schema",
        "descriptor_kind",
        "coordinate_payload_quality",
        "quality_branches",
        "projection_runtime_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
    "build_dynamic_point_source_lineage_known_fault_ledger": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "known_faults",
        "live_data_restored",
        "bug_fixed",
        "safe_to_extract_claimed",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
    },
}

BUNDLE_KEYS = {
    "schema",
    "descriptor_kind",
    "source_lineage_descriptor",
    "replay_lineage_label_descriptor",
    "live_lineage_label_descriptor",
    "source_availability_descriptor",
    "timestamp_quality_descriptor",
    "coordinate_payload_quality_descriptor",
    "known_fault_ledger",
    "source_movement_authorized",
    "runtime_render_invoked",
    "runtime_merge_enabled",
    "visual_parity_ready",
    "performance_ready",
    "readiness_claimed",
    "live_data_restored",
    "safe_to_extract_claimed",
    "forbidden_next_action",
}

PLANNING_BUNDLE_KEYS = {
    "schema",
    "descriptor_kind",
    "target_candidate",
    "boundary_descriptor",
    "candidate_scope",
    "required_checker",
    "blocked_surfaces",
    "source_movement_authorized",
    "runtime_render_invoked",
    "runtime_merge_enabled",
    "visual_parity_ready",
    "performance_ready",
    "readiness_claimed",
    "live_data_restored",
    "safe_to_extract_claimed",
    "forbidden_next_action",
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


class DynamicPointSourceLineageBoundaryHelperTests(unittest.TestCase):
    def test_helper_import_is_safe(self):
        imported = importlib.import_module("render_core.dynamic_point_source_lineage_boundary")
        self.assertIs(imported, helper)

    def test_exact_key_sets_for_descriptor_builders(self):
        for name, expected_keys in BUILDER_EXPECTED_KEYS.items():
            packet = getattr(helper, name)()
            self.assertEqual(set(packet), expected_keys, name)

    def test_deterministic_repeat_call_parity(self):
        for name in BUILDER_EXPECTED_KEYS:
            builder = getattr(helper, name)
            self.assertEqual(builder(), builder(), name)
        self.assertEqual(helper.dynamic_point_source_lineage_boundary_descriptor(), helper.dynamic_point_source_lineage_boundary_descriptor())
        self.assertEqual(helper.dynamic_point_source_lineage_planning_bundle(), helper.dynamic_point_source_lineage_planning_bundle())

    def test_dict_list_scalar_only_output(self):
        for name in BUILDER_EXPECTED_KEYS:
            self.assertTrue(is_packet_data(getattr(helper, name)()), name)
        self.assertTrue(is_packet_data(helper.dynamic_point_source_lineage_boundary_descriptor()))
        self.assertTrue(is_packet_data(helper.dynamic_point_source_lineage_planning_bundle()))

    def test_source_label_branches(self):
        self.assertEqual(helper.build_dynamic_point_source_lineage_descriptor("ais_source")["source_label"], "ais_source")
        self.assertEqual(helper.build_dynamic_point_source_lineage_descriptor("adsb_source")["source_label"], "adsb_source")
        self.assertEqual(helper.build_dynamic_point_source_lineage_descriptor("synthetic_source")["source_label"], "synthetic_source")
        self.assertEqual(helper.build_dynamic_point_source_lineage_descriptor("unavailable_source")["source_label"], "unavailable_source")
        self.assertEqual(helper.build_dynamic_point_source_lineage_descriptor("unexpected")["source_label"], "unavailable_source")

    def test_replay_and_live_lineage_label_branches(self):
        self.assertEqual(helper.build_dynamic_point_replay_lineage_label_descriptor()["lineage_label"], "sql_replay_lineage")
        self.assertEqual(helper.build_dynamic_point_live_lineage_label_descriptor()["lineage_label"], "websocket_live_lineage")
        self.assertFalse(helper.build_dynamic_point_replay_lineage_label_descriptor()["provider_execution_used"])
        self.assertFalse(helper.build_dynamic_point_live_lineage_label_descriptor()["provider_execution_used"])

    def test_availability_timestamp_and_coordinate_quality_branches(self):
        self.assertEqual(helper.build_dynamic_point_source_availability_descriptor("ais_source")["availability_label"], "ais_source")
        self.assertEqual(helper.build_dynamic_point_source_availability_descriptor("unknown")["availability_label"], "unavailable_source")
        self.assertEqual(helper.build_dynamic_point_timestamp_quality_descriptor("stale_timestamp")["timestamp_quality"], "stale_timestamp")
        self.assertEqual(helper.build_dynamic_point_timestamp_quality_descriptor("missing_timestamp")["timestamp_quality"], "missing_timestamp")
        self.assertEqual(helper.build_dynamic_point_timestamp_quality_descriptor("bad")["timestamp_quality"], "timestamp_quality")
        self.assertEqual(helper.build_dynamic_point_coordinate_payload_quality_descriptor("missing_lat_lon")["coordinate_payload_quality"], "missing_lat_lon")
        self.assertEqual(helper.build_dynamic_point_coordinate_payload_quality_descriptor("invalid_lat_lon")["coordinate_payload_quality"], "invalid_lat_lon")
        self.assertEqual(helper.build_dynamic_point_coordinate_payload_quality_descriptor("bad")["coordinate_payload_quality"], "coordinate_payload_quality")

    def test_known_fault_ledger_branch(self):
        packet = helper.build_dynamic_point_source_lineage_known_fault_ledger()
        self.assertEqual(packet["fixture_status"], "unresolved_static_only")
        self.assertIn("live_vs_replay_ambiguity", packet["known_faults"])
        self.assertIn("timestamp_staleness", packet["known_faults"])
        self.assertFalse(packet["live_data_restored"])
        self.assertFalse(packet["bug_fixed"])
        self.assertFalse(packet["safe_to_extract_claimed"])

    def test_boundary_descriptor_and_planning_bundle_guard_flags(self):
        descriptor = helper.dynamic_point_source_lineage_boundary_descriptor()
        planning = helper.dynamic_point_source_lineage_planning_bundle()
        self.assertEqual(set(descriptor), BUNDLE_KEYS)
        self.assertEqual(set(planning), PLANNING_BUNDLE_KEYS)
        self.assertFalse(descriptor["source_movement_authorized"])
        self.assertFalse(descriptor["runtime_render_invoked"])
        self.assertFalse(descriptor["runtime_merge_enabled"])
        self.assertFalse(descriptor["visual_parity_ready"])
        self.assertFalse(descriptor["performance_ready"])
        self.assertFalse(descriptor["readiness_claimed"])
        self.assertFalse(descriptor["live_data_restored"])
        self.assertFalse(descriptor["safe_to_extract_claimed"])
        self.assertEqual(planning["target_candidate"], "render_core/dynamic_point_source_lineage_boundary.py")
        self.assertEqual(planning["candidate_scope"], "descriptor_policy_ledger_only")
        self.assertEqual(planning["required_checker"], "scripts/validate_displaytools_dynamic_point_source_lineage_import_boundary.py")
        self.assertFalse(planning["source_movement_authorized"])

    def test_no_runtime_readiness_live_data_bug_fix_or_safe_to_extract_claims(self):
        packet_text = repr(helper.dynamic_point_source_lineage_planning_bundle())
        for marker in [
            "runtime_dependency_allowed': True",
            "sql_live_source_execution_allowed': True",
            "cache_database_io_allowed': True",
            "dataframe_runtime_allowed': True",
            "projection_formula_allowed': True",
            "controller_selection_runtime_allowed': True",
            "renderer_runtime_allowed': True",
            "live_data_restored': True",
            "bug_fixed': True",
            "safe_to_extract_claimed': True",
            "visual_parity_ready': True",
            "performance_ready': True",
            "readiness_claimed': True",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
