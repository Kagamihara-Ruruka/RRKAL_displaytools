import importlib
import unittest

from render_core import dynamic_point_selection_render_policy_boundary as helper


BUILDER_EXPECTED_KEYS = {
    "build_dynamic_point_selection_label_descriptor": {
        "schema",
        "descriptor_kind",
        "selection_label",
        "available_selection_labels",
        "selected_runtime_object_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_hit_state_label_descriptor": {
        "schema",
        "descriptor_kind",
        "hit_state_label",
        "available_hit_state_labels",
        "hit_test_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_picker_status_descriptor": {
        "schema",
        "descriptor_kind",
        "picker_status_label",
        "available_picker_status_labels",
        "picker_runtime_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_render_count_policy_descriptor": {
        "schema",
        "descriptor_kind",
        "count_label",
        "available_count_labels",
        "runtime_count_query_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_render_cap_policy_descriptor": {
        "schema",
        "descriptor_kind",
        "render_cap_label",
        "cap_policy",
        "runtime_cap_execution_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_adaptive_sampling_policy_descriptor": {
        "schema",
        "descriptor_kind",
        "sampling_label",
        "sampling_policy",
        "runtime_sampling_used",
        "allowed_content_kind",
        "forbidden_next_action",
        "runtime_dependency_allowed",
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
    "build_dynamic_point_selection_render_known_fault_ledger": {
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
        "controller_selection_runtime_allowed",
        "picker_hit_test_runtime_allowed",
        "dataframe_sampling_runtime_allowed",
        "projection_formula_allowed",
        "renderer_runtime_allowed",
        "sql_live_source_execution_allowed",
        "cache_database_io_allowed",
        "metadata_artifact_writer_allowed",
    },
}

BUNDLE_KEYS = {
    "schema",
    "descriptor_kind",
    "selection_label_descriptor",
    "hit_state_label_descriptor",
    "picker_status_descriptor",
    "render_count_policy_descriptor",
    "render_cap_policy_descriptor",
    "adaptive_sampling_policy_descriptor",
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


class DynamicPointSelectionRenderPolicyBoundaryHelperTests(unittest.TestCase):
    def test_helper_import_is_safe(self):
        imported = importlib.import_module("render_core.dynamic_point_selection_render_policy_boundary")
        self.assertIs(imported, helper)

    def test_exact_key_sets_for_descriptor_builders(self):
        for name, expected_keys in BUILDER_EXPECTED_KEYS.items():
            packet = getattr(helper, name)()
            self.assertEqual(set(packet), expected_keys, name)

    def test_deterministic_repeat_call_parity(self):
        for name in BUILDER_EXPECTED_KEYS:
            builder = getattr(helper, name)
            self.assertEqual(builder(), builder(), name)
        self.assertEqual(helper.dynamic_point_selection_render_policy_boundary_descriptor(), helper.dynamic_point_selection_render_policy_boundary_descriptor())
        self.assertEqual(helper.dynamic_point_selection_render_policy_planning_bundle(), helper.dynamic_point_selection_render_policy_planning_bundle())

    def test_dict_list_scalar_only_output(self):
        for name in BUILDER_EXPECTED_KEYS:
            self.assertTrue(is_packet_data(getattr(helper, name)()), name)
        self.assertTrue(is_packet_data(helper.dynamic_point_selection_render_policy_boundary_descriptor()))
        self.assertTrue(is_packet_data(helper.dynamic_point_selection_render_policy_planning_bundle()))

    def test_selection_label_branches(self):
        self.assertEqual(helper.build_dynamic_point_selection_label_descriptor("selected_vehicle")["selection_label"], "selected_vehicle")
        self.assertEqual(helper.build_dynamic_point_selection_label_descriptor("selected_layer")["selection_label"], "selected_layer")
        self.assertEqual(helper.build_dynamic_point_selection_label_descriptor("unexpected")["selection_label"], "selected_vehicle")
        self.assertFalse(helper.build_dynamic_point_selection_label_descriptor()["selected_runtime_object_used"])

    def test_hit_state_and_picker_status_branches(self):
        self.assertEqual(helper.build_dynamic_point_hit_state_label_descriptor("hit_state")["hit_state_label"], "hit_state")
        self.assertEqual(helper.build_dynamic_point_hit_state_label_descriptor("hit_false")["hit_state_label"], "hit_false")
        self.assertEqual(helper.build_dynamic_point_hit_state_label_descriptor("hit_true")["hit_state_label"], "hit_true")
        self.assertEqual(helper.build_dynamic_point_hit_state_label_descriptor("bad")["hit_state_label"], "hit_state")
        self.assertEqual(helper.build_dynamic_point_picker_status_descriptor("picker_status")["picker_status_label"], "picker_status")
        self.assertEqual(helper.build_dynamic_point_picker_status_descriptor("picker_blocked")["picker_status_label"], "picker_blocked")
        self.assertEqual(helper.build_dynamic_point_picker_status_descriptor("bad")["picker_status_label"], "picker_status")
        self.assertFalse(helper.build_dynamic_point_hit_state_label_descriptor()["hit_test_execution_used"])
        self.assertFalse(helper.build_dynamic_point_picker_status_descriptor()["picker_runtime_used"])

    def test_render_count_cap_and_adaptive_sampling_branches(self):
        self.assertEqual(helper.build_dynamic_point_render_count_policy_descriptor("visible_count")["count_label"], "visible_count")
        self.assertEqual(helper.build_dynamic_point_render_count_policy_descriptor("rendered_count")["count_label"], "rendered_count")
        self.assertEqual(helper.build_dynamic_point_render_count_policy_descriptor("bad")["count_label"], "visible_count")
        self.assertEqual(helper.build_dynamic_point_render_cap_policy_descriptor("render_cap")["render_cap_label"], "render_cap")
        self.assertEqual(helper.build_dynamic_point_render_cap_policy_descriptor("bad")["render_cap_label"], "render_cap")
        self.assertEqual(helper.build_dynamic_point_adaptive_sampling_policy_descriptor("adaptive_sampling")["sampling_label"], "adaptive_sampling")
        self.assertEqual(helper.build_dynamic_point_adaptive_sampling_policy_descriptor("bad")["sampling_label"], "adaptive_sampling")
        self.assertFalse(helper.build_dynamic_point_render_count_policy_descriptor()["runtime_count_query_used"])
        self.assertFalse(helper.build_dynamic_point_render_cap_policy_descriptor()["runtime_cap_execution_used"])
        self.assertFalse(helper.build_dynamic_point_adaptive_sampling_policy_descriptor()["runtime_sampling_used"])

    def test_known_fault_ledger_branch(self):
        packet = helper.build_dynamic_point_selection_render_known_fault_ledger()
        self.assertEqual(packet["fixture_status"], "unresolved_static_only")
        for fault in [
            "selection_staleness_fault",
            "hit_test_dependency_fault",
            "render_policy_guard_flag",
            "controller_selection_runtime_dependency",
            "picker_hit_test_runtime_dependency",
            "datashader_sampling_runtime_dependency",
            "renderer_host_runtime_dependency",
        ]:
            self.assertIn(fault, packet["known_faults"])
        self.assertFalse(packet["live_data_restored"])
        self.assertFalse(packet["bug_fixed"])
        self.assertFalse(packet["safe_to_extract_claimed"])

    def test_boundary_descriptor_and_planning_bundle_guard_flags(self):
        descriptor = helper.dynamic_point_selection_render_policy_boundary_descriptor()
        planning = helper.dynamic_point_selection_render_policy_planning_bundle()
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
        self.assertEqual(planning["target_candidate"], "render_core/dynamic_point_selection_render_policy_boundary.py")
        self.assertEqual(planning["candidate_scope"], "descriptor_policy_ledger_only")
        self.assertEqual(planning["required_checker"], "scripts/validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py")
        self.assertFalse(planning["source_movement_authorized"])

    def test_no_runtime_readiness_live_data_bug_fix_or_safe_to_extract_claims(self):
        packet_text = repr(helper.dynamic_point_selection_render_policy_planning_bundle())
        for marker in [
            "runtime_dependency_allowed': True",
            "controller_selection_runtime_allowed': True",
            "picker_hit_test_runtime_allowed': True",
            "dataframe_sampling_runtime_allowed': True",
            "projection_formula_allowed': True",
            "renderer_runtime_allowed': True",
            "sql_live_source_execution_allowed': True",
            "cache_database_io_allowed': True",
            "metadata_artifact_writer_allowed': True",
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