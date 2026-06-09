import unittest


DESCRIPTOR_KEYS = {
    "surface_name",
    "source_evidence",
    "input_frame",
    "consumer_layers",
    "policy_labels",
    "known_faults",
    "fixture_status",
    "forbidden_next_action",
}


FIXTURE_STATUSES = {"pinned", "unresolved_static_only", "blocked_hot_path"}


REQUIRED_DESCRIPTORS = {
    "time_source_descriptor",
    "sun_direction_descriptor",
    "world_normal_consumer_descriptor",
    "bump_normal_consumer_descriptor",
    "twilight_terminator_label_descriptor",
    "local_noon_fault_ledger_descriptor",
    "coordinate_frame_dependency_descriptor",
    "lighting_consumer_layers_descriptor",
    "forbidden_formula_surface_descriptor",
}


REQUIRED_CASES = {
    "taipei_local_noon_diagnostic_label",
    "utc_local_time_source_ambiguity_label",
    "compute_sun_direction_formula_surface_blocked",
    "light_dir_vector_consumer_blocked",
    "dot_l_lambertian_formula_blocked",
    "twilight_terminator_label_only_descriptor",
    "world_normal_vs_bumped_normal_consumer_split",
    "terrain_bump_lighting_consumer_label",
    "grid_starfield_coordinate_dependency_label",
    "longitude_flip_dependency_label",
    "latitude_flip_dependency_label",
    "static_frozen_light_fallback_label",
    "no_runtime_no_renderer_guard_flags",
}


FORBIDDEN_CLAIM_MARKERS = {
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_ready",
    "runtime_merge_enabled",
    "taipei_local_noon_fixed",
    "safe_to_extract",
}


def lighting_descriptor(
    surface_name,
    source_evidence,
    input_frame,
    consumer_layers,
    policy_labels,
    known_faults,
    fixture_status="pinned",
    forbidden_next_action="do_not_execute_renderer_or_change_lighting_formula",
):
    return {
        "surface_name": surface_name,
        "source_evidence": list(source_evidence),
        "input_frame": input_frame,
        "consumer_layers": list(consumer_layers),
        "policy_labels": list(policy_labels),
        "known_faults": list(known_faults),
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_solar_lighting_frame_boundary_packet():
    descriptors = [
        {
            "descriptor_id": "time_source_descriptor",
            "descriptor": lighting_descriptor(
                "time source descriptor",
                ["current compute_sun_direction uses current time source", "d90b645 has same solar direction family"],
                "UTC/local time source label",
                ["sun_direction_descriptor", "static_frozen_light_fallback_label"],
                ["utc_time_label", "local_time_ambiguity_label"],
                ["UTC/local-time source ambiguity label"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_change_time_source_or_compute_sun_direction",
            ),
        },
        {
            "descriptor_id": "sun_direction_descriptor",
            "descriptor": lighting_descriptor(
                "sun direction descriptor",
                ["current compute_sun_direction", "current light_dir vector consumer"],
                "solar direction label",
                ["light_dir consumer", "dot_l lighting consumer"],
                ["sun_vector_label", "frozen_light_label"],
                ["Taipei local-noon dark-side candidate"],
                fixture_status="blocked_hot_path",
                forbidden_next_action="do_not_execute_or_move_compute_sun_direction",
            ),
        },
        {
            "descriptor_id": "world_normal_consumer_descriptor",
            "descriptor": lighting_descriptor(
                "world normal consumer descriptor",
                ["current n_world raw geometry normal", "coordinate ownership diagnostic gate"],
                "world normal frame label",
                ["grid", "base lighting", "terrain geometry"],
                ["n_world_label"],
                ["world normal versus sample frame dependency unresolved"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_change_world_normal_formula",
            ),
        },
        {
            "descriptor_id": "bump_normal_consumer_descriptor",
            "descriptor": lighting_descriptor(
                "bump normal consumer descriptor",
                ["current n_world_bump and terrain bump path", "terrain boundary fixture gate"],
                "bumped normal frame label",
                ["terrain lighting", "ocean specular", "bump normal diagnostics"],
                ["n_world_bump_label", "bump_normal_label"],
                ["blocky terrain/bump debt", "local-noon diagnostic depends on normal consumer"],
                fixture_status="blocked_hot_path",
                forbidden_next_action="do_not_change_bump_or_normal_formula",
            ),
        },
        {
            "descriptor_id": "twilight_terminator_label_descriptor",
            "descriptor": lighting_descriptor(
                "twilight / terminator label descriptor",
                ["current dot_l twilight branch", "coordinate ownership diagnostic gate"],
                "terminator label only",
                ["terrain lighting", "terminator diagnostics"],
                ["twilight_label", "terminator_label"],
                ["twilight formula unresolved"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_change_twilight_or_terminator_formula",
            ),
        },
        {
            "descriptor_id": "local_noon_fault_ledger_descriptor",
            "descriptor": lighting_descriptor(
                "local-noon fault ledger descriptor",
                ["craton closeout active fault", "coordinate ownership diagnostic gate"],
                "diagnostic ledger label",
                ["solar frame diagnostics", "terrain sample frame diagnostics"],
                ["taipei_local_noon_fault_label"],
                ["Taipei local-noon dark-side candidate remains unresolved"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_claim_taipei_local_noon_fix",
            ),
        },
        {
            "descriptor_id": "coordinate_frame_dependency_descriptor",
            "descriptor": lighting_descriptor(
                "coordinate frame dependency descriptor",
                ["raw lon/lat frame", "terrain sample frame", "grid/starfield frame"],
                "coordinate dependency labels",
                ["solar lighting", "grid/starfield", "terrain sampling"],
                ["longitude_flip_dependency_label", "latitude_flip_dependency_label", "grid_starfield_dependency_label"],
                ["lighting frame relation to flipped sample frame unresolved"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_change_projection_flip_or_grid_formula",
            ),
        },
        {
            "descriptor_id": "lighting_consumer_layers_descriptor",
            "descriptor": lighting_descriptor(
                "lighting consumer layers descriptor",
                ["terrain lighting", "ocean specular", "cloud/day-side consumers"],
                "consumer layer label",
                ["terrain", "bathymetry", "ocean", "cloud", "grid dependency"],
                ["terrain_bump_lighting_consumer_label", "world_normal_consumer_label"],
                ["consumer split requires diagnostic only"],
                fixture_status="pinned",
                forbidden_next_action="do_not_change_lighting_consumer_behavior",
            ),
        },
        {
            "descriptor_id": "forbidden_formula_surface_descriptor",
            "descriptor": lighting_descriptor(
                "forbidden formula surface descriptor",
                ["compute_sun_direction", "light_dir", "dot_l", "twilight", "n_world", "n_world_bump"],
                "formula surface labels only",
                ["solar lighting hot path", "terrain shader hot path"],
                ["blocked_formula_surface_label"],
                ["formula movement blocked"],
                fixture_status="blocked_hot_path",
                forbidden_next_action="do_not_move_or_modify_solar_lighting_normal_projection_flip_formula",
            ),
        },
    ]
    cases = [
        {"case_id": "taipei_local_noon_diagnostic_label", "descriptor_id": "local_noon_fault_ledger_descriptor"},
        {"case_id": "utc_local_time_source_ambiguity_label", "descriptor_id": "time_source_descriptor"},
        {"case_id": "compute_sun_direction_formula_surface_blocked", "descriptor_id": "sun_direction_descriptor"},
        {"case_id": "light_dir_vector_consumer_blocked", "descriptor_id": "sun_direction_descriptor"},
        {"case_id": "dot_l_lambertian_formula_blocked", "descriptor_id": "forbidden_formula_surface_descriptor"},
        {"case_id": "twilight_terminator_label_only_descriptor", "descriptor_id": "twilight_terminator_label_descriptor"},
        {"case_id": "world_normal_vs_bumped_normal_consumer_split", "descriptor_id": "world_normal_consumer_descriptor"},
        {"case_id": "terrain_bump_lighting_consumer_label", "descriptor_id": "lighting_consumer_layers_descriptor"},
        {"case_id": "grid_starfield_coordinate_dependency_label", "descriptor_id": "coordinate_frame_dependency_descriptor"},
        {"case_id": "longitude_flip_dependency_label", "descriptor_id": "coordinate_frame_dependency_descriptor"},
        {"case_id": "latitude_flip_dependency_label", "descriptor_id": "coordinate_frame_dependency_descriptor"},
        {"case_id": "static_frozen_light_fallback_label", "descriptor_id": "time_source_descriptor"},
        {"case_id": "no_runtime_no_renderer_guard_flags", "descriptor_id": "forbidden_formula_surface_descriptor"},
    ]
    return {
        "test_shape": "pure_descriptor_fixture_matrix_no_monolith_import",
        "descriptors": descriptors,
        "fixture_cases": cases,
        "runtime_render_invoked": False,
        "production_source_changed": False,
        "formula_change_authorized": False,
        "recommended_next_gate": "solar_lighting_frame_source_surface_movement_preimplementation_gate",
    }


def is_dict_list_scalar(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return True
    if isinstance(value, list):
        return all(is_dict_list_scalar(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_dict_list_scalar(item) for key, item in value.items())
    return False


class DisplaytoolsSolarLightingFrameBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_solar_lighting_frame_boundary_packet()

    def test_descriptor_exact_key_sets_and_statuses(self):
        statuses = set()
        for entry in self.packet["descriptors"]:
            descriptor = entry["descriptor"]
            self.assertEqual(set(descriptor), DESCRIPTOR_KEYS)
            self.assertIn(descriptor["fixture_status"], FIXTURE_STATUSES)
            statuses.add(descriptor["fixture_status"])
        self.assertEqual(statuses, FIXTURE_STATUSES)

    def test_required_descriptors_and_cases_are_present(self):
        self.assertEqual({entry["descriptor_id"] for entry in self.packet["descriptors"]}, REQUIRED_DESCRIPTORS)
        self.assertEqual({case["case_id"] for case in self.packet["fixture_cases"]}, REQUIRED_CASES)

    def test_deterministic_repeat_call_and_scalar_shape(self):
        self.assertEqual(build_solar_lighting_frame_boundary_packet(), build_solar_lighting_frame_boundary_packet())
        self.assertTrue(is_dict_list_scalar(self.packet))

    def test_local_noon_fault_remains_unresolved(self):
        descriptors = {entry["descriptor_id"]: entry["descriptor"] for entry in self.packet["descriptors"]}
        local_noon = descriptors["local_noon_fault_ledger_descriptor"]
        self.assertEqual(local_noon["fixture_status"], "unresolved_static_only")
        self.assertIn("Taipei local-noon dark-side candidate remains unresolved", local_noon["known_faults"])
        self.assertEqual(local_noon["forbidden_next_action"], "do_not_claim_taipei_local_noon_fix")

    def test_formula_surfaces_are_blocked_hot_path(self):
        descriptors = {entry["descriptor_id"]: entry["descriptor"] for entry in self.packet["descriptors"]}
        for descriptor_id in [
            "sun_direction_descriptor",
            "bump_normal_consumer_descriptor",
            "forbidden_formula_surface_descriptor",
        ]:
            self.assertEqual(descriptors[descriptor_id]["fixture_status"], "blocked_hot_path")

    def test_label_descriptors_do_not_imply_behavior_change(self):
        descriptors = {entry["descriptor_id"]: entry["descriptor"] for entry in self.packet["descriptors"]}
        self.assertIn("twilight_label", descriptors["twilight_terminator_label_descriptor"]["policy_labels"])
        self.assertIn("longitude_flip_dependency_label", descriptors["coordinate_frame_dependency_descriptor"]["policy_labels"])
        self.assertFalse(self.packet["formula_change_authorized"])

    def test_no_monolith_runtime_or_readiness_claims(self):
        self.assertEqual(self.packet["test_shape"], "pure_descriptor_fixture_matrix_no_monolith_import")
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["production_source_changed"])
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)
        for forbidden in ["import taichi", "from PyQt6", "import vispy", "import taichi_global_bathymetry"]:
            self.assertNotIn(forbidden, packet_text)


if __name__ == "__main__":
    unittest.main()
