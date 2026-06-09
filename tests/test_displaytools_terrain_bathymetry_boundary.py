import unittest


DESCRIPTOR_KEYS = {
    "surface_name",
    "source_evidence",
    "input_frame",
    "sampling_frame",
    "consumer_layers",
    "policy_labels",
    "known_faults",
    "fixture_status",
    "forbidden_next_action",
}


FIXTURE_STATUSES = {
    "pinned",
    "unresolved_static_only",
    "blocked_hot_path",
}


REQUIRED_CASES = {
    "ocean_depth_sample",
    "land_elevation_sample",
    "coast_transition_sample",
    "no_data_fallback_terrain",
    "longitude_flip_label",
    "latitude_flip_label",
    "lod_resolution_label",
    "bump_normal_consumer_label",
    "lighting_consumer_label",
    "water_land_palette_label",
    "cache_hit_descriptor",
    "cache_miss_descriptor",
    "blocky_terrain_artifact_descriptor",
}


FORBIDDEN_CLAIM_MARKERS = {
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_ready",
    "runtime_merge_enabled",
    "shader_formula_changed",
    "terrain_sampling_changed",
}


def terrain_descriptor(
    surface_name,
    source_evidence,
    input_frame,
    sampling_frame,
    consumer_layers,
    policy_labels,
    known_faults,
    fixture_status="pinned",
    forbidden_next_action="do_not_execute_renderer_or_modify_shader_formula",
):
    return {
        "surface_name": surface_name,
        "source_evidence": source_evidence,
        "input_frame": input_frame,
        "sampling_frame": sampling_frame,
        "consumer_layers": list(consumer_layers),
        "policy_labels": list(policy_labels),
        "known_faults": list(known_faults),
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_terrain_bathymetry_boundary_packet():
    cases = [
        {
            "case_id": "ocean_depth_sample",
            "descriptor": terrain_descriptor(
                "bathymetry depth sample",
                "current load_topography and Taichi z_val sampling; d90b645 has same GEBCO/topography family",
                "GEBCO/synthetic height-field descriptor",
                "terrain sample frame with sample_lon/sample_lat",
                ["terrain shader", "water material label", "bathymetry layer"],
                ["bathymetry_source_label", "water_depth_label"],
                ["blocky terrain artifact unresolved"],
            ),
        },
        {
            "case_id": "land_elevation_sample",
            "descriptor": terrain_descriptor(
                "land elevation sample",
                "current topo field and terrain_color; d90b645 topo field and terrain_color anchors",
                "height-field descriptor",
                "terrain sample frame with land/elevation threshold",
                ["terrain shader", "land palette label", "land_mask consumer"],
                ["elevation_source_label", "land_palette_label"],
                ["blocky terrain artifact unresolved"],
            ),
        },
        {
            "case_id": "coast_transition_sample",
            "descriptor": terrain_descriptor(
                "coast transition sample",
                "current land_mask interpolation and fallback_land around sea_level_m",
                "height-field plus land/water mask descriptor",
                "terrain sample frame with coast mix",
                ["terrain shader", "land/water palette label", "sea-level label"],
                ["coast_transition_label", "sea_level_policy_label"],
                ["coastline classification static-only"],
                fixture_status="unresolved_static_only",
            ),
        },
        {
            "case_id": "no_data_fallback_terrain",
            "descriptor": terrain_descriptor(
                "no-data fallback terrain",
                "current load_topography fallback to synthetic_topography after GEBCO load failure",
                "fallback terrain descriptor",
                "synthetic height-field descriptor",
                ["terrain shader", "startup progress label"],
                ["fallback_terrain_label", "no_data_label"],
                ["provider/cache execution not covered"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_download_or_read_real_topography_cache",
            ),
        },
        {
            "case_id": "longitude_flip_label",
            "descriptor": terrain_descriptor(
                "longitude flip label",
                "current sample_lon assignment and flip_longitude branch; d90b645 same family",
                "raw lon/lat descriptor",
                "flipped terrain sample frame label",
                ["terrain sampling", "bump normal consumer", "water material label"],
                ["flip_longitude_label"],
                ["East/West orientation split candidate"],
            ),
        },
        {
            "case_id": "latitude_flip_label",
            "descriptor": terrain_descriptor(
                "latitude flip label",
                "current sample_lat assignment and flip_latitude branch; d90b645 same family",
                "raw lon/lat descriptor",
                "flipped terrain sample frame label",
                ["terrain sampling", "bump normal consumer", "water material label"],
                ["flip_latitude_label"],
                ["latitude flip authority unresolved"],
            ),
        },
        {
            "case_id": "lod_resolution_label",
            "descriptor": terrain_descriptor(
                "LOD/resolution label",
                "current topo_step parser, topography cache path and derived cache stride",
                "topography step descriptor",
                "height-field resolution label",
                ["terrain source selector", "cache descriptor", "renderer input shape label"],
                ["topo_step_label", "resolution_label"],
                ["LOD/resolution does not prove sampling quality"],
            ),
        },
        {
            "case_id": "bump_normal_consumer_label",
            "descriptor": terrain_descriptor(
                "bump/normal consumer label",
                "current n_world_bump and dz_dx/dz_dy branches",
                "height-field descriptor",
                "bump normal consumer label",
                ["lighting", "terrain shader", "ocean material"],
                ["bump_scale_label", "normal_consumer_label"],
                ["blocky terrain/bump debt"],
                fixture_status="blocked_hot_path",
                forbidden_next_action="do_not_change_bump_or_normal_formula",
            ),
        },
        {
            "case_id": "lighting_consumer_label",
            "descriptor": terrain_descriptor(
                "lighting consumer label",
                "current n_world_bump dot light_dir",
                "world normal descriptor",
                "lighting frame label",
                ["solar lighting", "terrain shader", "ocean specular"],
                ["light_dir_label", "n_world_bump_label"],
                ["Taipei local-noon dark-side candidate"],
                fixture_status="blocked_hot_path",
                forbidden_next_action="do_not_change_lighting_formula",
            ),
        },
        {
            "case_id": "water_land_palette_label",
            "descriptor": terrain_descriptor(
                "water/land palette label",
                "current terrain_color mixes ocean and land colormap",
                "height-field plus land/water mask descriptor",
                "palette/style label",
                ["terrain shader", "water material", "land palette"],
                ["water_palette_label", "land_palette_label", "style_profile_label"],
                ["style label does not authorize visual parity"],
            ),
        },
        {
            "case_id": "cache_hit_descriptor",
            "descriptor": terrain_descriptor(
                "cache hit descriptor",
                "current topography_cache_path and cache exists branch",
                "topography cache descriptor",
                "cache status label",
                ["provider/cache boundary", "terrain source selector"],
                ["cache_hit_label"],
                ["cache lifecycle not covered"],
                forbidden_next_action="do_not_read_or_write_cache",
            ),
        },
        {
            "case_id": "cache_miss_descriptor",
            "descriptor": terrain_descriptor(
                "cache miss descriptor",
                "current GEBCO open/fallback branches and np.save cache writes",
                "topography cache descriptor",
                "cache status label",
                ["provider/cache boundary", "terrain source selector"],
                ["cache_miss_label"],
                ["cache download/write not covered"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_download_or_write_cache",
            ),
        },
        {
            "case_id": "blocky_terrain_artifact_descriptor",
            "descriptor": terrain_descriptor(
                "blocky terrain artifact descriptor",
                "current fixture and historical gates list blocky terrain sampling/bump debt",
                "visual fault descriptor",
                "artifact label only",
                ["terrain sampling diagnostics", "bump normal diagnostics"],
                ["blocky_terrain_fault_label"],
                ["blocky terrain unresolved; no bug fix claim"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_fix_terrain_sampling_or_bump_formula",
            ),
        },
    ]
    return {
        "test_shape": "pure_descriptor_fixture_matrix_no_monolith_import",
        "cases": cases,
        "fixture_statuses": sorted(FIXTURE_STATUSES),
        "recommended_next_gate": "terrain_bathymetry_source_surface_movement_preimplementation_gate",
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
    }


class TerrainBathymetryBoundaryFixtureGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_terrain_bathymetry_boundary_packet()

    def test_descriptor_schema_and_status_values_are_pinned(self):
        for case in self.packet["cases"]:
            descriptor = case["descriptor"]
            self.assertEqual(set(descriptor), DESCRIPTOR_KEYS)
            self.assertIn(descriptor["fixture_status"], FIXTURE_STATUSES)

    def test_required_cases_are_present(self):
        self.assertEqual({case["case_id"] for case in self.packet["cases"]}, REQUIRED_CASES)

    def test_sampling_and_policy_boundaries_are_descriptor_only(self):
        cases = {case["case_id"]: case["descriptor"] for case in self.packet["cases"]}
        self.assertIn("terrain sample frame", cases["ocean_depth_sample"]["sampling_frame"])
        self.assertIn("terrain sample frame", cases["land_elevation_sample"]["sampling_frame"])
        self.assertIn("flip_longitude_label", cases["longitude_flip_label"]["policy_labels"])
        self.assertIn("flip_latitude_label", cases["latitude_flip_label"]["policy_labels"])
        self.assertEqual(cases["bump_normal_consumer_label"]["fixture_status"], "blocked_hot_path")
        self.assertEqual(cases["lighting_consumer_label"]["fixture_status"], "blocked_hot_path")

    def test_cache_and_provider_cases_do_not_execute_cache(self):
        cases = {case["case_id"]: case["descriptor"] for case in self.packet["cases"]}
        self.assertEqual(cases["cache_hit_descriptor"]["forbidden_next_action"], "do_not_read_or_write_cache")
        self.assertEqual(cases["cache_miss_descriptor"]["forbidden_next_action"], "do_not_download_or_write_cache")
        self.assertEqual(cases["no_data_fallback_terrain"]["fixture_status"], "unresolved_static_only")

    def test_blocky_terrain_fault_remains_unresolved(self):
        descriptor = {
            case["case_id"]: case["descriptor"]
            for case in self.packet["cases"]
        }["blocky_terrain_artifact_descriptor"]
        self.assertEqual(descriptor["fixture_status"], "unresolved_static_only")
        self.assertIn("blocky terrain unresolved; no bug fix claim", descriptor["known_faults"])

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        self.assertEqual(self.packet["test_shape"], "pure_descriptor_fixture_matrix_no_monolith_import")
        self.assertFalse(self.packet["source_movement_authorized"])
        self.assertFalse(self.packet["runtime_render_invoked"])
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
