import unittest


VECTOR_DESCRIPTOR_KEYS = {
    "overlay_kind",
    "source_shape",
    "input_frame",
    "projection_frame",
    "flip_policy",
    "mask_policy",
    "sync_expectation",
    "fixture_status",
    "forbidden_next_action",
}


SYNC_MATRIX_FRAMES = {
    "raw_spherical_lon_lat",
    "terrain_sample_frame",
    "ais_aircraft_screen_projection_frame",
    "grid_starfield_frame",
    "mask_screen_rgba_frame",
    "postprocess_composition_frame",
}


FORBIDDEN_CLAIM_MARKERS = {
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "borders_fixed",
    "hydrology_fixed",
}


def build_vector_overlay_coordinate_sync_fixture_packet():
    """Test-local descriptor only; do not import vector providers or renderer code."""
    descriptors = [
        {
            "overlay_kind": "borders",
            "source_shape": "synthetic line",
            "input_frame": "declared lon/lat",
            "projection_frame": "vector-specific projection",
            "flip_policy": "both",
            "mask_policy": "clipped by globe mask",
            "sync_expectation": "should align with dynamic points",
            "fixture_status": "pinned",
            "forbidden_next_action": "do_not_modify_GeoVectorLineOverlay_or_projection_formula",
        },
        {
            "overlay_kind": "borders",
            "source_shape": "polyline",
            "input_frame": "declared lon/lat",
            "projection_frame": "vector-specific projection",
            "flip_policy": "both",
            "mask_policy": "clipped by globe mask",
            "sync_expectation": "should align with raw grid",
            "fixture_status": "unresolved_static_only",
            "forbidden_next_action": "do_not_claim_grid_vector_sync_without_runtime_parity",
        },
        {
            "overlay_kind": "hydrology",
            "source_shape": "synthetic line",
            "input_frame": "declared lon/lat",
            "projection_frame": "vector-specific projection",
            "flip_policy": "both",
            "mask_policy": "clipped by globe mask",
            "sync_expectation": "should align with dynamic points",
            "fixture_status": "pinned",
            "forbidden_next_action": "do_not_read_real_hydrology_cache_or_provider",
        },
        {
            "overlay_kind": "hydrology",
            "source_shape": "empty",
            "input_frame": "declared lon/lat",
            "projection_frame": "unresolved",
            "flip_policy": "unresolved",
            "mask_policy": "unresolved",
            "sync_expectation": "unresolved",
            "fixture_status": "unresolved_static_only",
            "forbidden_next_action": "do_not_treat_empty_input_as_renderer_success",
        },
        {
            "overlay_kind": "borders",
            "source_shape": "malformed",
            "input_frame": "declared lon/lat",
            "projection_frame": "unresolved",
            "flip_policy": "unresolved",
            "mask_policy": "unresolved",
            "sync_expectation": "unresolved",
            "fixture_status": "unresolved_static_only",
            "forbidden_next_action": "do_not_patch_parser_or_provider_behavior",
        },
    ]
    cases = [
        {
            "case_id": "taiwan_short_border_segment",
            "overlay_kind": "borders",
            "source_shape": "synthetic line",
            "points": [(121.0, 24.8), (121.7, 25.3)],
            "expected_descriptor_sync": "should align with dynamic points",
            "fixture_status": "pinned",
        },
        {
            "case_id": "east_asia_polyline",
            "overlay_kind": "borders",
            "source_shape": "polyline",
            "points": [(120.0, 23.5), (121.5, 25.0), (123.0, 26.5)],
            "expected_descriptor_sync": "should align with raw grid",
            "fixture_status": "unresolved_static_only",
        },
        {
            "case_id": "hydrology_river_segment",
            "overlay_kind": "hydrology",
            "source_shape": "synthetic line",
            "points": [(120.6, 23.8), (120.8, 24.1)],
            "expected_descriptor_sync": "should align with dynamic points",
            "fixture_status": "pinned",
        },
        {
            "case_id": "cross_equator_line",
            "overlay_kind": "hydrology",
            "source_shape": "polyline",
            "points": [(30.0, -1.0), (30.2, 0.0), (30.4, 1.0)],
            "expected_descriptor_sync": "should align with dynamic points",
            "fixture_status": "pinned",
        },
        {
            "case_id": "anti_meridian_crossing_candidate",
            "overlay_kind": "borders",
            "source_shape": "polyline",
            "points": [(179.5, 10.0), (-179.5, 10.2)],
            "expected_descriptor_sync": "unresolved",
            "fixture_status": "unresolved_static_only",
        },
        {
            "case_id": "empty_line_collection",
            "overlay_kind": "borders",
            "source_shape": "empty",
            "points": [],
            "expected_descriptor_sync": "unresolved",
            "fixture_status": "unresolved_static_only",
        },
        {
            "case_id": "malformed_coordinate_payload",
            "overlay_kind": "hydrology",
            "source_shape": "malformed",
            "points": ["not-a-lon-lat-pair"],
            "expected_descriptor_sync": "unresolved",
            "fixture_status": "unresolved_static_only",
        },
        {
            "case_id": "same_lonlat_against_dynamic_projection_descriptor",
            "overlay_kind": "borders",
            "source_shape": "synthetic line",
            "points": [(121.5654, 25.033), (121.5654, 25.033)],
            "comparison_frame": "ais_aircraft_screen_projection_frame",
            "expected_descriptor_sync": "should align with dynamic points",
            "fixture_status": "pinned",
        },
    ]
    sync_matrix = {
        "raw_spherical_lon_lat": {
            "relationship": "input_reference",
            "status": "pinned",
            "note": "synthetic vector points are declared lon/lat before projection",
        },
        "terrain_sample_frame": {
            "relationship": "not_direct_owner",
            "status": "unresolved_static_only",
            "note": "terrain sample flips are adjacent but not vector renderer ownership",
        },
        "ais_aircraft_screen_projection_frame": {
            "relationship": "expected_screen_sync_peer",
            "status": "pinned",
            "note": "dynamic points and vector overlay both consume flip flags before screen placement",
        },
        "grid_starfield_frame": {
            "relationship": "grid_alignment_unresolved",
            "status": "unresolved_static_only",
            "note": "grid uses raw lon/lat in shader path; vector path is screen overlay",
        },
        "mask_screen_rgba_frame": {
            "relationship": "clipping_owner",
            "status": "pinned",
            "note": "vector overlay is clipped by globe mask after screen RGBA draw",
        },
        "postprocess_composition_frame": {
            "relationship": "not_covered",
            "status": "blocked_hot_path",
            "note": "composition and alpha/apply behavior are excluded",
        },
    }
    return {
        "test_shape": "pure_dict_list_scalar_no_runtime_imports_no_real_geojson",
        "source_evidence": [
            "taichi_global_bathymetry.py:3888 GeoVectorLineOverlay",
            "taichi_global_bathymetry.py:3914-4041 vector render receives flip flags and globe_mask",
            "taichi_global_bathymetry.py:1948-2028 dynamic point projection receives flip flags",
            "d90b645:taichi_global_bathymetry.py:2625-2734 same vector overlay family",
        ],
        "descriptors": descriptors,
        "synthetic_vector_cases": cases,
        "sync_matrix": sync_matrix,
        "recommended_next_gate": "vector_overlay_monkey_patch_craton_ablation_gate",
    }


class DisplaytoolsVectorOverlayCoordinateSyncFixtureTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_coordinate_sync_fixture_packet()

    def test_vector_overlay_descriptor_schema(self):
        statuses = set()
        for descriptor in self.packet["descriptors"]:
            self.assertEqual(set(descriptor), VECTOR_DESCRIPTOR_KEYS)
            self.assertIn(descriptor["overlay_kind"], {"borders", "hydrology"})
            self.assertIn(descriptor["fixture_status"], {"pinned", "unresolved_static_only", "blocked_hot_path"})
            statuses.add(descriptor["fixture_status"])
        self.assertEqual(statuses, {"pinned", "unresolved_static_only"})

    def test_synthetic_vector_cases_cover_required_shapes(self):
        cases = {case["case_id"]: case for case in self.packet["synthetic_vector_cases"]}
        self.assertEqual(
            set(cases),
            {
                "taiwan_short_border_segment",
                "east_asia_polyline",
                "hydrology_river_segment",
                "cross_equator_line",
                "anti_meridian_crossing_candidate",
                "empty_line_collection",
                "malformed_coordinate_payload",
                "same_lonlat_against_dynamic_projection_descriptor",
            },
        )
        self.assertEqual(cases["empty_line_collection"]["points"], [])
        self.assertEqual(cases["malformed_coordinate_payload"]["points"], ["not-a-lon-lat-pair"])
        self.assertEqual(
            cases["same_lonlat_against_dynamic_projection_descriptor"]["comparison_frame"],
            "ais_aircraft_screen_projection_frame",
        )

    def test_sync_matrix_covers_required_coordinate_frames(self):
        self.assertEqual(set(self.packet["sync_matrix"]), SYNC_MATRIX_FRAMES)
        self.assertEqual(
            self.packet["sync_matrix"]["ais_aircraft_screen_projection_frame"]["relationship"],
            "expected_screen_sync_peer",
        )
        self.assertEqual(
            self.packet["sync_matrix"]["postprocess_composition_frame"]["status"],
            "blocked_hot_path",
        )

    def test_test_shape_has_no_runtime_or_real_vector_dependency(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_dict_list_scalar_no_runtime_imports_no_real_geojson",
        )
        serialized = repr(self.packet)
        for forbidden in (
            "import taichi",
            "from PyQt6",
            "import vispy",
            "Natural Earth cache read",
            "GeoJSON provider read",
            "SQL live",
            "WebSocket live",
        ):
            self.assertNotIn(forbidden, serialized)

    def test_unresolved_cases_do_not_claim_bug_fix_or_readiness(self):
        serialized = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(f"{marker}=true", serialized)
        unresolved_cases = [
            case for case in self.packet["synthetic_vector_cases"]
            if case["fixture_status"] == "unresolved_static_only"
        ]
        self.assertGreaterEqual(len(unresolved_cases), 3)

    def test_recommended_next_gate_is_diagnostic(self):
        self.assertEqual(
            self.packet["recommended_next_gate"],
            "vector_overlay_monkey_patch_craton_ablation_gate",
        )


if __name__ == "__main__":
    unittest.main()
