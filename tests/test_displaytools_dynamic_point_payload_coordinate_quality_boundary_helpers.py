import importlib
import unittest

from render_core import dynamic_point_payload_coordinate_quality_boundary as helper


BUILDER_EXPECTED_KEYS = {
    "build_dynamic_point_payload_shape_descriptor": {
        "schema",
        "descriptor_kind",
        "payload_shape",
        "payload_fields",
        "quality_labels",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_coordinate_quality_descriptor": {
        "schema",
        "descriptor_kind",
        "coordinate_quality",
        "quality_branches",
        "known_fault_refs",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_timestamp_quality_descriptor": {
        "schema",
        "descriptor_kind",
        "timestamp_quality",
        "quality_branches",
        "real_clock_execution_used",
        "known_fault_refs",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_source_id_quality_descriptor": {
        "schema",
        "descriptor_kind",
        "source_id_quality",
        "quality_branches",
        "source_lookup_performed",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_speed_heading_quality_descriptor": {
        "schema",
        "descriptor_kind",
        "speed_heading_quality",
        "quality_branches",
        "runtime_sampling_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "dataframe_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "renderer_runtime_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_payload_coordinate_quality_known_fault_ledger": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "known_faults",
        "blocked_surfaces",
        "payload_coordinate_quality_extraction_candidate",
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
        "metadata_artifact_writer_allowed",
    },
}

BOUNDARY_DESCRIPTOR_KEYS = {
    "schema",
    "descriptor_kind",
    "payload_shape_descriptor",
    "coordinate_quality_descriptor",
    "timestamp_quality_descriptor",
    "source_id_quality_descriptor",
    "speed_heading_quality_descriptor",
    "known_fault_ledger",
    "source_movement_authorized",
    "runtime_render_invoked",
    "runtime_merge_enabled",
    "readiness_claimed",
    "visual_parity_ready",
    "performance_ready",
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
    "helper_module_creation_authorized",
    "payload_coordinate_quality_extraction_candidate",
    "required_checker",
    "blocked_surfaces",
    "source_movement_authorized",
    "runtime_render_invoked",
    "runtime_merge_enabled",
    "readiness_claimed",
    "visual_parity_ready",
    "performance_ready",
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


class DynamicPointPayloadCoordinateQualityBoundaryHelperTests(unittest.TestCase):
    def test_helper_import_is_safe(self):
        imported = importlib.import_module("render_core.dynamic_point_payload_coordinate_quality_boundary")
        self.assertIs(imported, helper)

    def test_exact_key_sets_for_descriptor_builders(self):
        for name, expected_keys in BUILDER_EXPECTED_KEYS.items():
            packet = getattr(helper, name)()
            self.assertEqual(set(packet), expected_keys, name)

    def test_deterministic_repeat_call_parity(self):
        for name in BUILDER_EXPECTED_KEYS:
            builder = getattr(helper, name)
            self.assertEqual(builder(), builder(), name)
        self.assertEqual(helper.dynamic_point_payload_coordinate_quality_boundary_descriptor(), helper.dynamic_point_payload_coordinate_quality_boundary_descriptor())
        self.assertEqual(helper.dynamic_point_payload_coordinate_quality_planning_bundle(), helper.dynamic_point_payload_coordinate_quality_planning_bundle())

    def test_dict_list_scalar_only_output(self):
        for name in BUILDER_EXPECTED_KEYS:
            self.assertTrue(is_packet_data(getattr(helper, name)()), name)
        self.assertTrue(is_packet_data(helper.dynamic_point_payload_coordinate_quality_boundary_descriptor()))
        self.assertTrue(is_packet_data(helper.dynamic_point_payload_coordinate_quality_planning_bundle()))

    def test_payload_shape_branches(self):
        packet = helper.build_dynamic_point_payload_shape_descriptor()
        self.assertEqual(packet["payload_fields"], ["lat", "lon", "timestamp", "source_id", "speed", "heading"])
        self.assertEqual(packet["quality_labels"], ["valid", "missing", "invalid", "stale", "unknown"])
        self.assertEqual(helper.build_dynamic_point_payload_shape_descriptor("unknown")["payload_shape"], "unknown")

    def test_coordinate_quality_branches(self):
        for label in ["coordinate_quality", "missing_lat_lon", "invalid_lat_lon", "out_of_range_lat_lon", "zero_coordinate_candidate", "anti_meridian_candidate"]:
            self.assertEqual(helper.build_dynamic_point_coordinate_quality_descriptor(label)["coordinate_quality"], label)
        self.assertEqual(helper.build_dynamic_point_coordinate_quality_descriptor("bad")["coordinate_quality"], "coordinate_quality")
        self.assertIn("coordinate_payload_ambiguity", helper.build_dynamic_point_coordinate_quality_descriptor()["known_fault_refs"])

    def test_timestamp_quality_branches(self):
        for label in ["timestamp_quality", "missing_timestamp", "stale_timestamp", "future_timestamp_candidate", "timezone_ambiguity"]:
            self.assertEqual(helper.build_dynamic_point_timestamp_quality_descriptor(label)["timestamp_quality"], label)
        self.assertEqual(helper.build_dynamic_point_timestamp_quality_descriptor("bad")["timestamp_quality"], "timestamp_quality")
        self.assertFalse(helper.build_dynamic_point_timestamp_quality_descriptor()["real_clock_execution_used"])

    def test_source_id_quality_branches(self):
        for label in ["source_id_quality", "missing_id", "synthetic_id", "AIS_id", "ADS-B_id"]:
            self.assertEqual(helper.build_dynamic_point_source_id_quality_descriptor(label)["source_id_quality"], label)
        self.assertEqual(helper.build_dynamic_point_source_id_quality_descriptor("bad")["source_id_quality"], "source_id_quality")
        self.assertFalse(helper.build_dynamic_point_source_id_quality_descriptor()["source_lookup_performed"])

    def test_speed_heading_quality_branches(self):
        for label in ["speed_heading_quality", "missing_speed", "missing_heading", "invalid_speed", "invalid_heading", "unknown"]:
            self.assertEqual(helper.build_dynamic_point_speed_heading_quality_descriptor(label)["speed_heading_quality"], label)
        self.assertEqual(helper.build_dynamic_point_speed_heading_quality_descriptor("bad")["speed_heading_quality"], "speed_heading_quality")
        self.assertFalse(helper.build_dynamic_point_speed_heading_quality_descriptor()["runtime_sampling_used"])

    def test_known_fault_ledger_and_bundle_guard_flags(self):
        ledger = helper.build_dynamic_point_payload_coordinate_quality_known_fault_ledger()
        descriptor = helper.dynamic_point_payload_coordinate_quality_boundary_descriptor()
        planning = helper.dynamic_point_payload_coordinate_quality_planning_bundle()
        self.assertEqual(ledger["known_faults"], ["timestamp_staleness", "coordinate_payload_ambiguity", "point_vector_sync_dependency"])
        self.assertFalse(ledger["payload_coordinate_quality_extraction_candidate"])
        self.assertEqual(set(descriptor), BOUNDARY_DESCRIPTOR_KEYS)
        self.assertEqual(set(planning), PLANNING_BUNDLE_KEYS)
        self.assertTrue(planning["helper_module_creation_authorized"])
        self.assertFalse(planning["payload_coordinate_quality_extraction_candidate"])
        self.assertFalse(planning["source_movement_authorized"])
        self.assertFalse(planning["runtime_render_invoked"])
        self.assertFalse(planning["runtime_merge_enabled"])
        self.assertFalse(planning["readiness_claimed"])
        self.assertFalse(planning["live_data_restored"])
        self.assertFalse(planning["safe_to_extract_claimed"])
        self.assertEqual(planning["target_candidate"], "render_core/dynamic_point_payload_coordinate_quality_boundary.py")

    def test_no_runtime_readiness_live_data_bug_fix_or_safe_to_extract_claims(self):
        packet_text = repr(helper.dynamic_point_payload_coordinate_quality_planning_bundle())
        for marker in [
            "runtime_dependency_allowed': True",
            "sql_live_source_execution_allowed': True",
            "cache_database_io_allowed': True",
            "dataframe_runtime_allowed': True",
            "projection_formula_allowed': True",
            "controller_selection_runtime_allowed': True",
            "renderer_runtime_allowed': True",
            "metadata_artifact_writer_allowed': True",
            "source_movement_authorized': True",
            "runtime_render_invoked': True",
            "runtime_merge_enabled': True",
            "readiness_claimed': True",
            "live_data_restored': True",
            "bug_fixed': True",
            "safe_to_extract_claimed': True",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()