import importlib
import unittest

from render_core import dynamic_point_render_cap_adaptive_sampling_boundary as helper


BUILDER_EXPECTED_KEYS = {
    "build_dynamic_point_visible_count_descriptor": {
        "schema",
        "descriptor_kind",
        "visible_count",
        "available_count_labels",
        "runtime_count_query_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "runtime_sampling_allowed",
        "dataframe_runtime_allowed",
        "renderer_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_rendered_count_descriptor": {
        "schema",
        "descriptor_kind",
        "rendered_count",
        "available_count_labels",
        "runtime_count_query_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "runtime_sampling_allowed",
        "dataframe_runtime_allowed",
        "renderer_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_render_cap_policy_descriptor": {
        "schema",
        "descriptor_kind",
        "render_cap",
        "cap_policy_labels",
        "runtime_cap_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "runtime_sampling_allowed",
        "dataframe_runtime_allowed",
        "renderer_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_adaptive_sampling_policy_descriptor": {
        "schema",
        "descriptor_kind",
        "adaptive_sampling",
        "sampling_policy_labels",
        "runtime_sampling_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "runtime_sampling_allowed",
        "dataframe_runtime_allowed",
        "renderer_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_sampling_dependency_descriptor": {
        "schema",
        "descriptor_kind",
        "sampling_dependency",
        "dependency_classification",
        "dependency_labels",
        "runtime_dependency_executed",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "runtime_sampling_allowed",
        "dataframe_runtime_allowed",
        "renderer_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "known_faults",
        "blocked_surfaces",
        "render_cap_adaptive_sampling_extraction_candidate",
        "live_data_restored",
        "bug_fixed",
        "safe_to_extract_claimed",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "runtime_sampling_allowed",
        "dataframe_runtime_allowed",
        "renderer_runtime_allowed",
        "projection_formula_allowed",
        "controller_selection_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
}

BOUNDARY_DESCRIPTOR_KEYS = {
    "schema",
    "descriptor_kind",
    "visible_count_descriptor",
    "rendered_count_descriptor",
    "render_cap_policy_descriptor",
    "adaptive_sampling_policy_descriptor",
    "sampling_dependency_descriptor",
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
    "render_cap_adaptive_sampling_extraction_candidate",
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


class DynamicPointRenderCapAdaptiveSamplingBoundaryHelperTests(unittest.TestCase):
    def test_helper_import_is_safe(self):
        imported = importlib.import_module("render_core.dynamic_point_render_cap_adaptive_sampling_boundary")
        self.assertIs(imported, helper)

    def test_exact_key_sets_for_descriptor_builders(self):
        for name, expected_keys in BUILDER_EXPECTED_KEYS.items():
            packet = getattr(helper, name)()
            self.assertEqual(set(packet), expected_keys, name)

    def test_deterministic_repeat_call_parity(self):
        for name in BUILDER_EXPECTED_KEYS:
            builder = getattr(helper, name)
            self.assertEqual(builder(), builder(), name)
        self.assertEqual(helper.dynamic_point_render_cap_adaptive_sampling_boundary_descriptor(), helper.dynamic_point_render_cap_adaptive_sampling_boundary_descriptor())
        self.assertEqual(helper.dynamic_point_render_cap_adaptive_sampling_planning_bundle(), helper.dynamic_point_render_cap_adaptive_sampling_planning_bundle())

    def test_dict_list_scalar_only_output(self):
        for name in BUILDER_EXPECTED_KEYS:
            self.assertTrue(is_packet_data(getattr(helper, name)()), name)
        self.assertTrue(is_packet_data(helper.dynamic_point_render_cap_adaptive_sampling_boundary_descriptor()))
        self.assertTrue(is_packet_data(helper.dynamic_point_render_cap_adaptive_sampling_planning_bundle()))

    def test_visible_and_rendered_count_branches(self):
        for label in ["visible_count", "below_cap", "equals_cap", "exceeds_cap", "unknown"]:
            self.assertEqual(helper.build_dynamic_point_visible_count_descriptor(label)["visible_count"], label)
        self.assertEqual(helper.build_dynamic_point_visible_count_descriptor("bad")["visible_count"], "visible_count")
        for label in ["rendered_count", "lower_than_visible", "equals_visible", "unknown"]:
            self.assertEqual(helper.build_dynamic_point_rendered_count_descriptor(label)["rendered_count"], label)
        self.assertEqual(helper.build_dynamic_point_rendered_count_descriptor("bad")["rendered_count"], "rendered_count")
        self.assertFalse(helper.build_dynamic_point_visible_count_descriptor()["runtime_count_query_used"])
        self.assertFalse(helper.build_dynamic_point_rendered_count_descriptor()["runtime_count_query_used"])

    def test_render_cap_policy_branches(self):
        for label in ["render_cap", "cap_enabled", "cap_disabled", "cap_unknown"]:
            self.assertEqual(helper.build_dynamic_point_render_cap_policy_descriptor(label)["render_cap"], label)
        self.assertEqual(helper.build_dynamic_point_render_cap_policy_descriptor("bad")["render_cap"], "render_cap")
        self.assertFalse(helper.build_dynamic_point_render_cap_policy_descriptor()["runtime_cap_execution_used"])

    def test_adaptive_sampling_policy_branches(self):
        for label in ["adaptive_sampling", "enabled", "disabled", "degraded"]:
            self.assertEqual(helper.build_dynamic_point_adaptive_sampling_policy_descriptor(label)["adaptive_sampling"], label)
        self.assertEqual(helper.build_dynamic_point_adaptive_sampling_policy_descriptor("bad")["adaptive_sampling"], "adaptive_sampling")
        self.assertFalse(helper.build_dynamic_point_adaptive_sampling_policy_descriptor()["runtime_sampling_used"])

    def test_sampling_dependency_branches(self):
        blocked = ["datashader_runtime_dependency", "pandas_numpy_runtime_dependency", "renderer_runtime_dependency"]
        adjacent = ["selection_policy_dependency", "payload_quality_dependency"]
        for label in blocked:
            packet = helper.build_dynamic_point_sampling_dependency_descriptor(label)
            self.assertEqual(packet["sampling_dependency"], label)
            self.assertEqual(packet["dependency_classification"], "blocked_runtime_only")
        for label in adjacent:
            packet = helper.build_dynamic_point_sampling_dependency_descriptor(label)
            self.assertEqual(packet["sampling_dependency"], label)
            self.assertEqual(packet["dependency_classification"], "adjacent_descriptor_dependency")
        self.assertEqual(helper.build_dynamic_point_sampling_dependency_descriptor("bad")["sampling_dependency"], "datashader_runtime_dependency")
        self.assertFalse(helper.build_dynamic_point_sampling_dependency_descriptor()["runtime_dependency_executed"])

    def test_known_fault_ledger_and_bundle_guard_flags(self):
        ledger = helper.build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger()
        descriptor = helper.dynamic_point_render_cap_adaptive_sampling_boundary_descriptor()
        planning = helper.dynamic_point_render_cap_adaptive_sampling_planning_bundle()
        self.assertEqual(ledger["fixture_status"], "unresolved_static_only")
        for fault in [
            "cap_exceeded_without_runtime_count_parity",
            "adaptive_sampling_degraded_without_datashader_runtime",
            "selection_payload_dependency_unproven",
        ]:
            self.assertIn(fault, ledger["known_faults"])
        self.assertFalse(ledger["render_cap_adaptive_sampling_extraction_candidate"])
        self.assertEqual(set(descriptor), BOUNDARY_DESCRIPTOR_KEYS)
        self.assertEqual(set(planning), PLANNING_BUNDLE_KEYS)
        self.assertTrue(planning["helper_module_creation_authorized"])
        self.assertFalse(planning["render_cap_adaptive_sampling_extraction_candidate"])
        self.assertFalse(planning["source_movement_authorized"])
        self.assertFalse(planning["runtime_render_invoked"])
        self.assertFalse(planning["runtime_merge_enabled"])
        self.assertFalse(planning["readiness_claimed"])
        self.assertFalse(planning["live_data_restored"])
        self.assertFalse(planning["safe_to_extract_claimed"])
        self.assertEqual(planning["target_candidate"], "render_core/dynamic_point_render_cap_adaptive_sampling_boundary.py")

    def test_no_runtime_readiness_live_data_bug_fix_or_safe_to_extract_claims(self):
        packet_text = repr(helper.dynamic_point_render_cap_adaptive_sampling_planning_bundle())
        for marker in [
            "runtime_dependency_allowed': True",
            "runtime_sampling_allowed': True",
            "dataframe_runtime_allowed': True",
            "renderer_runtime_allowed': True",
            "projection_formula_allowed': True",
            "controller_selection_runtime_allowed': True",
            "sql_live_source_execution_allowed': True",
            "cache_database_io_allowed': True",
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
