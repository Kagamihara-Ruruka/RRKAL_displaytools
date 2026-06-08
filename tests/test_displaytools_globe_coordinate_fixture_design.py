import unittest


OWNERSHIP_KEYS = {
    "frame_name",
    "source_evidence",
    "consumer_layers",
    "known_faults",
    "fixture_status",
    "forbidden_next_action",
}


FORBIDDEN_AUTHORIZATION_MARKERS = {
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "pixel_equivalence_proven",
}


def build_coordinate_fixture_design_packet():
    """Test-local descriptor only; do not import renderer/runtime modules."""
    frames = [
        {
            "frame_name": "raw_spherical_lon_lat",
            "source_evidence": [
                "taichi_global_bathymetry.py:1659 n_world = rotate_view_to_world(...)",
                "taichi_global_bathymetry.py:1660 lon = atan2(n_world.x, n_world.z)",
                "taichi_global_bathymetry.py:1661 lat = asin(n_world.y)",
                "d90b645:taichi_global_bathymetry.py:1724-1726 same raw frame family",
            ],
            "consumer_layers": ["globe_geometry", "lat_lon_grid", "lighting_base"],
            "known_faults": ["east_west_longitude_orientation_split"],
            "fixture_status": "pinned",
            "forbidden_next_action": "do_not_change_rotate_view_to_world_or_raw_lon_lat_formula",
        },
        {
            "frame_name": "terrain_sample_frame",
            "source_evidence": [
                "taichi_global_bathymetry.py:1662-1670 sample_lon/sample_lat with flip flags before topography lookup",
                "taichi_global_bathymetry.py:1737 canopy variation uses sample_lon/sample_lat",
                "taichi_global_bathymetry.py:1782-1784 ocean waves use sample_lon/sample_lat",
                "d90b645:taichi_global_bathymetry.py:1727-1735 same sample frame family",
            ],
            "consumer_layers": ["terrain_sampling", "forest_mask_sampling", "ocean_wave_sampling"],
            "known_faults": ["east_west_longitude_orientation_split", "blocky_terrain_sampling_bump_debt"],
            "fixture_status": "pinned",
            "forbidden_next_action": "do_not_change_flip_longitude_or_flip_latitude_behavior",
        },
        {
            "frame_name": "lighting_frame",
            "source_evidence": [
                "taichi_global_bathymetry.py:1644 light_dir = [sun_x, sun_y, sun_z]",
                "taichi_global_bathymetry.py:1741-1760 n_world_bump dot light_dir",
                "d90b645:taichi_global_bathymetry.py:1709 and 1806-1825 same light/bump family",
            ],
            "consumer_layers": ["solar_lighting", "ocean_specular", "cloud_day_side"],
            "known_faults": ["taipei_local_noon_dark_side_candidate"],
            "fixture_status": "unresolved_static_only",
            "forbidden_next_action": "do_not_change_light_dir_or_dot_l_formula",
        },
        {
            "frame_name": "grid_starfield_frame",
            "source_evidence": [
                "taichi_global_bathymetry.py:1812-1819 grid uses raw lon_deg/lat_deg",
                "taichi_global_bathymetry.py:1826 render_stars(yaw, pitch, zoom)",
                "d90b645:taichi_global_bathymetry.py:1877-1891 same grid/starfield family",
            ],
            "consumer_layers": ["lat_lon_grid", "starfield"],
            "known_faults": ["grid_flip_authority_unresolved"],
            "fixture_status": "unresolved_static_only",
            "forbidden_next_action": "do_not_change_grid_or_starfield_formula",
        },
        {
            "frame_name": "ais_aircraft_screen_projection_frame",
            "source_evidence": [
                "taichi_global_bathymetry.py:1948-2028 project_ais_to_screen/project_aircraft_to_screen apply flip flags before screen x/y",
                "d90b645:taichi_global_bathymetry.py:2013-2092 same dynamic projection family",
            ],
            "consumer_layers": ["ais_points", "aircraft_points", "screen_overlay_rgba"],
            "known_faults": ["dynamic_points_vector_sync_unproven"],
            "fixture_status": "pinned",
            "forbidden_next_action": "do_not_connect_live_ais_or_change_projection_formula",
        },
        {
            "frame_name": "vector_overlay_frame",
            "source_evidence": [
                "taichi_global_bathymetry.py:3888 GeoVectorLineOverlay",
                "taichi_global_bathymetry.py:3914-4041 vector render consumes flip flags and globe_mask",
                "d90b645:taichi_global_bathymetry.py:2625-2734 same vector overlay family",
            ],
            "consumer_layers": ["borders", "hydrology", "screen_overlay_rgba"],
            "known_faults": ["borders_hydrology_vector_bake_sync_issue"],
            "fixture_status": "unresolved_static_only",
            "forbidden_next_action": "do_not_change_GeoVectorLineOverlay_or_provider_loading",
        },
        {
            "frame_name": "mask_screen_rgba_frame",
            "source_evidence": [
                "taichi_global_bathymetry.py:1582 globe_mask field",
                "taichi_global_bathymetry.py:1653-1656 globe_mask writes",
                "taichi_global_bathymetry.py:2068-2072 mask_overlay_to_globe clips RGBA alpha",
                "d90b645:taichi_global_bathymetry.py:1647,1718-1721,2133-2137 same mask family",
            ],
            "consumer_layers": ["screen_rgba_overlays", "pins", "vehicle_overlay", "post_mask_layers"],
            "known_faults": ["mask_does_not_prove_internal_coordinate_sync"],
            "fixture_status": "pinned",
            "forbidden_next_action": "do_not_change_mask_overlay_to_globe_or_generate_png",
        },
        {
            "frame_name": "postprocess_composition_frame",
            "source_evidence": [
                "render_core/render_plan.py owns packet helpers after recent extractions",
                "taichi_global_bathymetry.py retains apply_layer_render_plan_composition hot path",
            ],
            "consumer_layers": ["postprocess", "composition", "final_rgba"],
            "known_faults": ["alpha_apply_path_hot_path_excluded"],
            "fixture_status": "blocked_hot_path",
            "forbidden_next_action": "do_not_touch_alpha_apply_or_metadata_output_schema",
        },
    ]
    cases = [
        {
            "case_id": "taipei_east_asia",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "flip_longitude": False,
            "flip_latitude": False,
            "expected_axis": "east_positive_raw_lon",
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "pacific_negative_longitude",
            "raw_lon": -122.4194,
            "raw_lat": 37.7749,
            "flip_longitude": False,
            "flip_latitude": False,
            "expected_axis": "west_negative_raw_lon",
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "longitude_flip_on",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "flip_longitude": True,
            "flip_latitude": False,
            "expected_sample_lon": -121.5654,
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "longitude_flip_off",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "flip_longitude": False,
            "flip_latitude": False,
            "expected_sample_lon": 121.5654,
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "latitude_flip_on",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "flip_longitude": False,
            "flip_latitude": True,
            "expected_sample_lat": -25.033,
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "latitude_flip_off",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "flip_longitude": False,
            "flip_latitude": False,
            "expected_sample_lat": 25.033,
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "equator_prime_meridian",
            "raw_lon": 0.0,
            "raw_lat": 0.0,
            "flip_longitude": True,
            "flip_latitude": True,
            "expected_sample_lon": -0.0,
            "expected_sample_lat": -0.0,
            "diagnostic_status": "pinned",
        },
        {
            "case_id": "local_noon_lighting_expectation",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "expectation": "diagnose_light_frame_against_raw_and_sample_frames",
            "diagnostic_status": "unresolved_static_only",
        },
        {
            "case_id": "vector_border_hydrology_sync_expectation",
            "raw_lon": 121.5654,
            "raw_lat": 25.033,
            "expectation": "diagnose_vector_overlay_frame_against_dynamic_projection_frame",
            "diagnostic_status": "unresolved_static_only",
        },
    ]
    return {
        "test_shape": "fixture_design_only_no_safe_import_target",
        "frames": frames,
        "synthetic_fixture_cases": cases,
        "recommended_next_gate": "vector_overlay_coordinate_sync_fixture_gate",
        "deferred_gate": "globe_coordinate_import_boundary_checker",
        "forbidden_authorization_markers": sorted(FORBIDDEN_AUTHORIZATION_MARKERS),
    }


class DisplaytoolsGlobeCoordinateFixtureDesignTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_coordinate_fixture_design_packet()

    def test_frame_inventory_schema_and_statuses(self):
        statuses = set()
        for frame in self.packet["frames"]:
            self.assertEqual(set(frame), OWNERSHIP_KEYS)
            self.assertIsInstance(frame["source_evidence"], list)
            self.assertIsInstance(frame["consumer_layers"], list)
            self.assertIsInstance(frame["known_faults"], list)
            statuses.add(frame["fixture_status"])
        self.assertEqual(statuses, {"pinned", "unresolved_static_only", "blocked_hot_path"})

    def test_required_coordinate_frames_present(self):
        self.assertEqual(
            {frame["frame_name"] for frame in self.packet["frames"]},
            {
                "raw_spherical_lon_lat",
                "terrain_sample_frame",
                "lighting_frame",
                "grid_starfield_frame",
                "ais_aircraft_screen_projection_frame",
                "vector_overlay_frame",
                "mask_screen_rgba_frame",
                "postprocess_composition_frame",
            },
        )

    def test_synthetic_fixture_cases_pin_expected_axes(self):
        cases = {case["case_id"]: case for case in self.packet["synthetic_fixture_cases"]}
        self.assertEqual(cases["taipei_east_asia"]["expected_axis"], "east_positive_raw_lon")
        self.assertEqual(cases["pacific_negative_longitude"]["expected_axis"], "west_negative_raw_lon")
        self.assertEqual(cases["longitude_flip_on"]["expected_sample_lon"], -121.5654)
        self.assertEqual(cases["longitude_flip_off"]["expected_sample_lon"], 121.5654)
        self.assertEqual(cases["latitude_flip_on"]["expected_sample_lat"], -25.033)
        self.assertEqual(cases["latitude_flip_off"]["expected_sample_lat"], 25.033)
        self.assertEqual(cases["equator_prime_meridian"]["expected_sample_lon"], -0.0)
        self.assertEqual(cases["equator_prime_meridian"]["expected_sample_lat"], -0.0)

    def test_unresolved_diagnostics_are_not_behavior_claims(self):
        cases = {case["case_id"]: case for case in self.packet["synthetic_fixture_cases"]}
        self.assertEqual(
            cases["local_noon_lighting_expectation"]["diagnostic_status"],
            "unresolved_static_only",
        )
        self.assertEqual(
            cases["vector_border_hydrology_sync_expectation"]["diagnostic_status"],
            "unresolved_static_only",
        )
        serialized = repr(self.packet)
        for marker in FORBIDDEN_AUTHORIZATION_MARKERS:
            self.assertNotIn(f"{marker}=true", serialized)

    def test_test_shape_avoids_runtime_import_target(self):
        self.assertEqual(self.packet["test_shape"], "fixture_design_only_no_safe_import_target")
        serialized = repr(self.packet)
        for forbidden in ("import taichi", "from PyQt6", "from PySide6", "import vispy"):
            self.assertNotIn(forbidden, serialized)

    def test_recommended_next_gate_is_diagnostic_not_implementation(self):
        self.assertEqual(
            self.packet["recommended_next_gate"],
            "vector_overlay_coordinate_sync_fixture_gate",
        )
        self.assertEqual(self.packet["deferred_gate"], "globe_coordinate_import_boundary_checker")


if __name__ == "__main__":
    unittest.main()
