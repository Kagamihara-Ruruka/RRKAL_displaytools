import unittest

from render_core import terrain_bathymetry_boundary as boundary


DESCRIPTOR_BUILDERS = [
    boundary.build_terrain_bathymetry_source_descriptor,
    boundary.build_terrain_height_field_descriptor,
    boundary.build_terrain_fallback_no_data_descriptor,
    boundary.build_terrain_lod_resolution_label_descriptor,
    boundary.build_terrain_cache_status_label_descriptor,
    boundary.build_terrain_palette_style_label_descriptor,
    boundary.build_terrain_known_fault_ledger_descriptor,
]


COMMON_GUARD_KEYS = {
    "runtime_dependency_allowed",
    "provider_cache_execution_allowed",
    "shader_formula_allowed",
    "projection_lighting_formula_allowed",
    "visual_behavior_change_allowed",
}


EXPECTED_KEY_SETS = {
    "source": {
        "schema",
        "descriptor_kind",
        "source_label",
        "source_evidence",
        "input_frame",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "height": {
        "schema",
        "descriptor_kind",
        "height_field_kind",
        "coordinate_payload_kind",
        "consumer_layers",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "fallback": {
        "schema",
        "descriptor_kind",
        "fallback_reason",
        "fallback_policy",
        "source_state",
        "known_limits",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "lod": {
        "schema",
        "descriptor_kind",
        "lod_label",
        "resolution_policy",
        "sampling_quality_claimed",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "cache": {
        "schema",
        "descriptor_kind",
        "cache_status",
        "cache_policy",
        "cache_lifecycle_executed",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "palette": {
        "schema",
        "descriptor_kind",
        "style_label",
        "palette_policy",
        "visual_behavior_changed",
        "allowed_content_kind",
        "forbidden_next_action",
        *COMMON_GUARD_KEYS,
    },
    "fault": {
        "schema",
        "descriptor_kind",
        "fixture_status",
        "known_faults",
        "fault_fixed",
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
}


def is_dict_list_scalar(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return True
    if isinstance(value, list):
        return all(is_dict_list_scalar(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_dict_list_scalar(item) for key, item in value.items())
    return False


class TerrainBathymetryBoundaryHelperTests(unittest.TestCase):
    def test_helper_module_import_is_safe(self):
        self.assertFalse(hasattr(boundary, "load_topography"))
        self.assertFalse(hasattr(boundary, "TaichiGlobeRenderer"))
        self.assertFalse(hasattr(boundary, "compute_sun_direction"))
        self.assertTrue(hasattr(boundary, "terrain_bathymetry_boundary_descriptor"))

    def test_exact_key_sets_for_descriptor_builders(self):
        self.assertEqual(set(boundary.build_terrain_bathymetry_source_descriptor()), EXPECTED_KEY_SETS["source"])
        self.assertEqual(set(boundary.build_terrain_height_field_descriptor()), EXPECTED_KEY_SETS["height"])
        self.assertEqual(set(boundary.build_terrain_fallback_no_data_descriptor()), EXPECTED_KEY_SETS["fallback"])
        self.assertEqual(set(boundary.build_terrain_lod_resolution_label_descriptor()), EXPECTED_KEY_SETS["lod"])
        self.assertEqual(set(boundary.build_terrain_cache_status_label_descriptor()), EXPECTED_KEY_SETS["cache"])
        self.assertEqual(set(boundary.build_terrain_palette_style_label_descriptor()), EXPECTED_KEY_SETS["palette"])
        self.assertEqual(set(boundary.build_terrain_known_fault_ledger_descriptor()), EXPECTED_KEY_SETS["fault"])

    def test_deterministic_repeat_call_parity(self):
        for builder in DESCRIPTOR_BUILDERS:
            with self.subTest(builder=builder.__name__):
                self.assertEqual(builder(), builder())
        self.assertEqual(boundary.terrain_bathymetry_boundary_descriptor(), boundary.terrain_bathymetry_boundary_descriptor())
        self.assertEqual(boundary.terrain_bathymetry_planning_bundle(), boundary.terrain_bathymetry_planning_bundle())

    def test_outputs_are_dict_list_scalar_only(self):
        for builder in DESCRIPTOR_BUILDERS:
            with self.subTest(builder=builder.__name__):
                self.assertTrue(is_dict_list_scalar(builder()))
        self.assertTrue(is_dict_list_scalar(boundary.terrain_bathymetry_boundary_descriptor()))
        self.assertTrue(is_dict_list_scalar(boundary.terrain_bathymetry_planning_bundle()))

    def test_cache_hit_and_cache_miss_label_descriptor_branches(self):
        hit = boundary.build_terrain_cache_status_label_descriptor("cache_hit")
        miss = boundary.build_terrain_cache_status_label_descriptor("cache_miss")
        malformed = boundary.build_terrain_cache_status_label_descriptor("bad")
        self.assertEqual(hit["cache_status"], "cache_hit")
        self.assertEqual(miss["cache_status"], "cache_miss")
        self.assertEqual(malformed["cache_status"], "unknown")
        self.assertFalse(hit["provider_cache_execution_allowed"])
        self.assertFalse(miss["cache_lifecycle_executed"])

    def test_fallback_lod_palette_and_known_fault_branches(self):
        fallback = boundary.build_terrain_fallback_no_data_descriptor("missing_height_field")
        lod = boundary.build_terrain_lod_resolution_label_descriptor("coarse")
        palette = boundary.build_terrain_palette_style_label_descriptor("terrain_default")
        faults = boundary.build_terrain_known_fault_ledger_descriptor()
        self.assertEqual(fallback["fallback_reason"], "missing_height_field")
        self.assertEqual(lod["lod_label"], "coarse")
        self.assertFalse(lod["sampling_quality_claimed"])
        self.assertEqual(palette["palette_policy"], "label_only")
        self.assertFalse(palette["visual_behavior_changed"])
        self.assertEqual(faults["fixture_status"], "unresolved_static_only")
        self.assertFalse(faults["fault_fixed"])

    def test_planning_bundle_guard_flags(self):
        descriptor = boundary.terrain_bathymetry_boundary_descriptor()
        bundle = boundary.terrain_bathymetry_planning_bundle()
        for packet in [descriptor, bundle]:
            self.assertFalse(packet["source_movement_authorized"])
            self.assertFalse(packet["runtime_render_invoked"])
            self.assertFalse(packet["runtime_merge_enabled"])
            self.assertFalse(packet["visual_parity_ready"])
            self.assertFalse(packet["performance_ready"])
            self.assertFalse(packet["readiness_claimed"])
        self.assertEqual(bundle["candidate_scope"], "descriptor_policy_ledger_only")

    def test_no_runtime_or_readiness_claims(self):
        packet_text = repr(boundary.terrain_bathymetry_planning_bundle())
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
