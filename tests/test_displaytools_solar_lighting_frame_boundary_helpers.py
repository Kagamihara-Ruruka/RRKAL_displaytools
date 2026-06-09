import unittest

from render_core import solar_lighting_frame_boundary as boundary


DESCRIPTOR_BUILDERS = [
    boundary.build_solar_time_source_descriptor,
    boundary.build_solar_direction_label_descriptor,
    boundary.build_solar_twilight_terminator_label_descriptor,
    boundary.build_solar_local_noon_fault_ledger_descriptor,
    boundary.build_solar_coordinate_dependency_label_descriptor,
    boundary.build_solar_lighting_consumer_layers_descriptor,
    boundary.build_solar_forbidden_formula_surface_ledger_descriptor,
]


COMMON_GUARD_KEYS = {
    "runtime_dependency_allowed",
    "real_clock_execution_allowed",
    "solar_formula_allowed",
    "lighting_shader_formula_allowed",
    "projection_flip_formula_allowed",
    "visual_behavior_change_allowed",
}


EXPECTED_KEY_SETS = {
    "time": {
        "schema",
        "descriptor_kind",
        "source_label",
        "source_evidence",
        "time_policy",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "direction": {
        "schema",
        "descriptor_kind",
        "direction_label",
        "policy_labels",
        "consumer_layers",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "twilight": {
        "schema",
        "descriptor_kind",
        "terminator_label",
        "policy_labels",
        "known_limits",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "local_noon": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "known_faults",
        "local_noon_fault_resolved",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "coordinate": {
        "schema",
        "descriptor_kind",
        "dependency_labels",
        "input_frame",
        "known_limits",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "consumers": {
        "schema",
        "descriptor_kind",
        "consumer_layers",
        "normal_labels",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "forbidden": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "blocked_surfaces",
        "formula_movement_authorized",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "bug_fixed",
    "runtime_readiness",
    "source_movement_authorized_true",
    "local_noon_fault_resolved_true",
}


def is_dict_list_scalar(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return True
    if isinstance(value, list):
        return all(is_dict_list_scalar(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_dict_list_scalar(item) for key, item in value.items())
    return False


class SolarLightingFrameBoundaryHelperTests(unittest.TestCase):
    def test_helper_module_import_is_safe(self):
        self.assertFalse(hasattr(boundary, "compute_sun_direction"))
        self.assertFalse(hasattr(boundary, "TaichiGlobeRenderer"))
        self.assertFalse(hasattr(boundary, "light_dir"))
        self.assertTrue(hasattr(boundary, "solar_lighting_frame_boundary_descriptor"))

    def test_exact_key_sets_for_descriptor_builders(self):
        self.assertEqual(set(boundary.build_solar_time_source_descriptor()), EXPECTED_KEY_SETS["time"])
        self.assertEqual(set(boundary.build_solar_direction_label_descriptor()), EXPECTED_KEY_SETS["direction"])
        self.assertEqual(set(boundary.build_solar_twilight_terminator_label_descriptor()), EXPECTED_KEY_SETS["twilight"])
        self.assertEqual(set(boundary.build_solar_local_noon_fault_ledger_descriptor()), EXPECTED_KEY_SETS["local_noon"])
        self.assertEqual(set(boundary.build_solar_coordinate_dependency_label_descriptor()), EXPECTED_KEY_SETS["coordinate"])
        self.assertEqual(set(boundary.build_solar_lighting_consumer_layers_descriptor()), EXPECTED_KEY_SETS["consumers"])
        self.assertEqual(set(boundary.build_solar_forbidden_formula_surface_ledger_descriptor()), EXPECTED_KEY_SETS["forbidden"])

    def test_deterministic_repeat_call_parity(self):
        for builder in DESCRIPTOR_BUILDERS:
            with self.subTest(builder=builder.__name__):
                self.assertEqual(builder(), builder())
        self.assertEqual(boundary.solar_lighting_frame_boundary_descriptor(), boundary.solar_lighting_frame_boundary_descriptor())
        self.assertEqual(boundary.solar_lighting_planning_bundle(), boundary.solar_lighting_planning_bundle())

    def test_outputs_are_dict_list_scalar_only(self):
        for builder in DESCRIPTOR_BUILDERS:
            with self.subTest(builder=builder.__name__):
                self.assertTrue(is_dict_list_scalar(builder()))
        self.assertTrue(is_dict_list_scalar(boundary.solar_lighting_frame_boundary_descriptor()))
        self.assertTrue(is_dict_list_scalar(boundary.solar_lighting_planning_bundle()))

    def test_label_descriptor_branches(self):
        time_source = boundary.build_solar_time_source_descriptor("static_time_label")
        direction = boundary.build_solar_direction_label_descriptor("frozen_light_label")
        twilight = boundary.build_solar_twilight_terminator_label_descriptor("terminator_label")
        coordinate = boundary.build_solar_coordinate_dependency_label_descriptor()
        consumers = boundary.build_solar_lighting_consumer_layers_descriptor()
        self.assertEqual(time_source["source_label"], "static_time_label")
        self.assertEqual(direction["direction_label"], "frozen_light_label")
        self.assertEqual(twilight["terminator_label"], "terminator_label")
        self.assertIn("projection", coordinate["dependency_labels"])
        self.assertIn("world_normal", consumers["normal_labels"])

    def test_local_noon_and_forbidden_formula_ledgers(self):
        local_noon = boundary.build_solar_local_noon_fault_ledger_descriptor()
        forbidden = boundary.build_solar_forbidden_formula_surface_ledger_descriptor()
        self.assertEqual(local_noon["fixture_status"], "unresolved_static_only")
        self.assertFalse(local_noon["local_noon_fault_resolved"])
        self.assertIn("local_noon_fault", local_noon["known_faults"])
        self.assertEqual(forbidden["fixture_status"], "blocked_hot_path")
        self.assertFalse(forbidden["formula_movement_authorized"])
        self.assertIn("compute_sun_direction", forbidden["blocked_surfaces"])

    def test_planning_bundle_guard_flags(self):
        descriptor = boundary.solar_lighting_frame_boundary_descriptor()
        bundle = boundary.solar_lighting_planning_bundle()
        for packet in [descriptor, bundle]:
            self.assertFalse(packet["source_movement_authorized"])
            self.assertFalse(packet["runtime_render_invoked"])
            self.assertFalse(packet["runtime_merge_enabled"])
            self.assertFalse(packet["visual_parity_ready"])
            self.assertFalse(packet["performance_ready"])
            self.assertFalse(packet["readiness_claimed"])
            self.assertFalse(packet["local_noon_fault_resolved"])
        self.assertEqual(bundle["candidate_scope"], "descriptor_policy_ledger_only")

    def test_no_runtime_or_readiness_claims(self):
        packet_text = repr(boundary.solar_lighting_planning_bundle())
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
