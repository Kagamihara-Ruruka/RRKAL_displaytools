import unittest


SURFACE_CATEGORIES = {
    "category_a_descriptor_policy_ledger",
    "category_b_provider_cache_loader",
    "category_c_sampling_shader_formula",
    "category_d_projection_flip_lighting",
    "category_e_runtime_renderer_host",
    "category_f_visual_style_palette",
}


SURFACE_ENTRY_KEYS = {
    "surface_name",
    "observed_owner",
    "movement_category",
    "candidate_for_first_cut",
    "reason",
    "required_guard",
    "forbidden_next_action",
}


CATEGORY_A_SURFACES = {
    "terrain/bathymetry source descriptor",
    "height-field descriptor",
    "fallback/no-data descriptor",
    "LOD/resolution label descriptor",
    "cache status label descriptor",
    "palette/style label descriptor",
    "known fault ledger descriptor",
}


BLOCKED_SURFACES = {
    "NOAA/GEBCO/ETOPO provider execution",
    "real cache read/write",
    "download/fetch/load lifecycle",
    "terrain sampling formula",
    "bump/normal calculation",
    "raymarch/sphere intersection/shader height lookup",
    "longitude/latitude flip formula",
    "sun direction/twilight/dot lighting",
    "grid/starfield frame coupling",
    "Taichi renderer class",
    "Qt/VisPy host",
    "runtime GUI/controller behavior",
    "water/land palette behavior",
    "style profile behavior",
}


FORBIDDEN_CLAIM_MARKERS = {
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_ready",
    "runtime_merge_enabled",
    "source_movement_authorized_true",
    "terrain_bathymetry_extraction_candidate_true",
}


def surface_entry(
    surface_name,
    observed_owner,
    movement_category,
    candidate_for_first_cut,
    reason,
    required_guard,
    forbidden_next_action,
):
    return {
        "surface_name": surface_name,
        "observed_owner": observed_owner,
        "movement_category": movement_category,
        "candidate_for_first_cut": candidate_for_first_cut,
        "reason": reason,
        "required_guard": required_guard,
        "forbidden_next_action": forbidden_next_action,
    }


def build_terrain_bathymetry_source_surface_movement_packet():
    matrix = [
        surface_entry(
            "terrain/bathymetry source descriptor",
            "current load_topography/topography args and d90b645 GEBCO/topography family",
            "category_a_descriptor_policy_ledger",
            True,
            "source labels can be represented as data without opening providers or caches",
            "fixture parity for descriptor key sets before any planning gate",
            "do_not_execute_provider_or_cache_loader",
        ),
        surface_entry(
            "height-field descriptor",
            "current topo field, synthetic_topography fallback, and renderer input shape labels",
            "category_a_descriptor_policy_ledger",
            True,
            "height-field metadata can be represented as dict/list/scalar descriptors",
            "descriptor fixture and no-runtime import boundary planning later",
            "do_not_move_sampling_or_shader_height_lookup",
        ),
        surface_entry(
            "fallback/no-data descriptor",
            "current load_topography fallback branch and synthetic_topography label",
            "category_a_descriptor_policy_ledger",
            True,
            "fallback/no-data status is a ledger label when provider execution remains excluded",
            "fallback descriptor fixture with malformed/no-data branch",
            "do_not_download_or_generate_real_topography",
        ),
        surface_entry(
            "LOD/resolution label descriptor",
            "current topo_step parser, cache path step label, and derived cache stride label",
            "category_a_descriptor_policy_ledger",
            True,
            "LOD/resolution can be pinned as label data without proving sampling quality",
            "exact label fixture and decision table before movement planning",
            "do_not_change_resolution_or_sampling_behavior",
        ),
        surface_entry(
            "cache status label descriptor",
            "current topography cache hit/miss/fallback branches",
            "category_a_descriptor_policy_ledger",
            True,
            "cache hit/miss labels can be data descriptors when lifecycle execution remains blocked",
            "string-label allowance and cache-lifecycle exclusion tests",
            "do_not_read_write_download_or_evict_cache",
        ),
        surface_entry(
            "palette/style label descriptor",
            "current terrain_color and water/land palette labels",
            "category_a_descriptor_policy_ledger",
            True,
            "style labels can be carried as data while visual behavior remains excluded",
            "palette label fixture and no visual-readiness wording guard",
            "do_not_change_palette_or_style_behavior",
        ),
        surface_entry(
            "known fault ledger descriptor",
            "current coordinate/craton gates list blocky terrain, flip, and lighting faults",
            "category_a_descriptor_policy_ledger",
            True,
            "known fault ledger records unresolved diagnostics without claiming fixes",
            "ledger fixture with unresolved/static-only status values",
            "do_not_fix_or_mark_visual_fault_resolved",
        ),
        surface_entry(
            "NOAA/GEBCO/ETOPO provider execution",
            "current load_topography provider path and historical GEBCO source family",
            "category_b_provider_cache_loader",
            False,
            "provider execution can read files, download, or transform real terrain data",
            "provider/cache boundary fixture before any separate movement route",
            "do_not_include_provider_execution_in_first_cut",
        ),
        surface_entry(
            "real cache read/write",
            "current topography_cache_path and cache save/load branches",
            "category_b_provider_cache_loader",
            False,
            "cache IO is lifecycle behavior rather than descriptor data",
            "cache lifecycle map and artifact audit guard",
            "do_not_read_or_write_real_cache",
        ),
        surface_entry(
            "download/fetch/load lifecycle",
            "current topography source loader and external data source branches",
            "category_b_provider_cache_loader",
            False,
            "download/fetch/load changes IO and provider ownership",
            "provider loader boundary before movement",
            "do_not_fetch_download_or_load_real_terrain_data",
        ),
        surface_entry(
            "terrain sampling formula",
            "current sample_lon/sample_lat to tx/ty and z_val sampling path",
            "category_c_sampling_shader_formula",
            False,
            "sampling formula is shader behavior and can affect pixels",
            "sampling diagnostic gate and parity evidence before any formula work",
            "do_not_move_or_change_sampling_formula",
        ),
        surface_entry(
            "bump/normal calculation",
            "current dz_dx/dz_dy, n_world_bump, and bump scale path",
            "category_c_sampling_shader_formula",
            False,
            "bump/normal calculation is hot shader-side behavior",
            "bump/normal diagnostic gate only",
            "do_not_move_or_change_bump_normal_formula",
        ),
        surface_entry(
            "raymarch/sphere intersection/shader height lookup",
            "current Taichi globe renderer shader-side geometry path",
            "category_c_sampling_shader_formula",
            False,
            "shader geometry and height lookup are runtime hot path surfaces",
            "separate renderer hot-path review",
            "do_not_touch_raymarch_sphere_or_height_lookup",
        ),
        surface_entry(
            "longitude/latitude flip formula",
            "current flip_longitude/flip_latitude branches and coordinate fixture gates",
            "category_d_projection_flip_lighting",
            False,
            "flip formula owns coordinate behavior and active orientation faults",
            "coordinate formula diagnostic gate before implementation",
            "do_not_change_flip_formula",
        ),
        surface_entry(
            "sun direction/twilight/dot lighting",
            "current light_dir, dot_l, n_world and n_world_bump usage",
            "category_d_projection_flip_lighting",
            False,
            "lighting changes visual output and active local-noon diagnostics",
            "solar frame diagnostic gate before implementation",
            "do_not_change_lighting_or_twilight_formula",
        ),
        surface_entry(
            "grid/starfield frame coupling",
            "current coordinate ownership gate lists grid/starfield frame separately",
            "category_d_projection_flip_lighting",
            False,
            "frame coupling is coordinate ownership, not terrain descriptor movement",
            "coordinate fixture follow-up if needed",
            "do_not_merge_grid_starfield_frame_with_terrain_first_cut",
        ),
        surface_entry(
            "Taichi renderer class",
            "current TaichiGlobeRenderer owns fields, kernels, shader and render host behavior",
            "category_e_runtime_renderer_host",
            False,
            "renderer class movement would import runtime/GPU behavior",
            "renderer-host decomposition map only",
            "do_not_move_or_instantiate_renderer_class",
        ),
        surface_entry(
            "Qt/VisPy host",
            "current UI/runtime host surfaces outside terrain descriptor layer",
            "category_e_runtime_renderer_host",
            False,
            "host behavior needs runtime execution and is unrelated to descriptor first cut",
            "UI/host seam gate if needed",
            "do_not_import_or_execute_qt_vispy_host",
        ),
        surface_entry(
            "runtime GUI/controller behavior",
            "current controller/runtime methods set renderer args and reload behavior",
            "category_e_runtime_renderer_host",
            False,
            "controller mutation is runtime behavior rather than source descriptor data",
            "controller seam map before any runtime work",
            "do_not_move_controller_or_runtime_behavior",
        ),
        surface_entry(
            "water/land palette behavior",
            "current terrain_color visual behavior and style profile consumers",
            "category_f_visual_style_palette",
            False,
            "palette behavior can affect output colors; only label descriptors are candidate",
            "style label fixture before any behavior movement",
            "do_not_move_or_change_palette_behavior",
        ),
        surface_entry(
            "style profile behavior",
            "current style/profile labels and postprocess consumers",
            "category_f_visual_style_palette",
            False,
            "style behavior is broader than terrain descriptor ownership",
            "style/profile boundary map if needed",
            "do_not_move_or_change_style_profile_behavior",
        ),
    ]
    decision_output = {
        "first_cut_surface": "category_a_descriptor_policy_ledger",
        "category_b_to_f_blocked_from_first_cut": True,
        "source_movement_authorized": False,
        "terrain_bathymetry_extraction_candidate": False,
        "terrain_bathymetry_planning_candidate": True,
        "import_boundary_checker_required_now": False,
        "import_boundary_checker_reason": "not_required_until_a_safe_descriptor_helper_target_is_identified",
        "recommended_next_gate": "terrain_bathymetry_boundary_minimal_extraction_planning_gate",
    }
    return {
        "test_shape": "pure_descriptor_mapping_matrix_no_monolith_import_no_runtime_dependency",
        "surface_categories": sorted(SURFACE_CATEGORIES),
        "surface_matrix": matrix,
        "decision_output": decision_output,
        "runtime_render_invoked": False,
        "production_source_changed": False,
    }


class TerrainBathymetrySourceSurfaceMovementPreimplementationGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_terrain_bathymetry_source_surface_movement_packet()

    def test_surface_matrix_schema_and_categories_are_pinned(self):
        self.assertEqual(set(self.packet["surface_categories"]), SURFACE_CATEGORIES)
        for entry in self.packet["surface_matrix"]:
            self.assertEqual(set(entry), SURFACE_ENTRY_KEYS)
            self.assertIn(entry["movement_category"], SURFACE_CATEGORIES)
            self.assertIsInstance(entry["candidate_for_first_cut"], bool)

    def test_category_a_is_the_only_first_cut_candidate(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        self.assertEqual(set(matrix), CATEGORY_A_SURFACES | BLOCKED_SURFACES)
        for surface in CATEGORY_A_SURFACES:
            self.assertEqual(matrix[surface]["movement_category"], "category_a_descriptor_policy_ledger")
            self.assertTrue(matrix[surface]["candidate_for_first_cut"], surface)
        for surface in BLOCKED_SURFACES:
            self.assertNotEqual(matrix[surface]["movement_category"], "category_a_descriptor_policy_ledger")
            self.assertFalse(matrix[surface]["candidate_for_first_cut"], surface)

    def test_provider_cache_loader_surfaces_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in [
            "NOAA/GEBCO/ETOPO provider execution",
            "real cache read/write",
            "download/fetch/load lifecycle",
        ]:
            self.assertEqual(matrix[surface]["movement_category"], "category_b_provider_cache_loader")
            self.assertFalse(matrix[surface]["candidate_for_first_cut"])
            self.assertIn("do_not", matrix[surface]["forbidden_next_action"])

    def test_shader_sampling_projection_lighting_and_runtime_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in [
            "terrain sampling formula",
            "bump/normal calculation",
            "raymarch/sphere intersection/shader height lookup",
            "longitude/latitude flip formula",
            "sun direction/twilight/dot lighting",
            "grid/starfield frame coupling",
            "Taichi renderer class",
            "Qt/VisPy host",
            "runtime GUI/controller behavior",
        ]:
            self.assertFalse(matrix[surface]["candidate_for_first_cut"], surface)

    def test_visual_style_behavior_is_blocked_while_style_label_descriptor_is_candidate(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        self.assertTrue(matrix["palette/style label descriptor"]["candidate_for_first_cut"])
        self.assertEqual(
            matrix["palette/style label descriptor"]["movement_category"],
            "category_a_descriptor_policy_ledger",
        )
        for surface in ["water/land palette behavior", "style profile behavior"]:
            self.assertEqual(matrix[surface]["movement_category"], "category_f_visual_style_palette")
            self.assertFalse(matrix[surface]["candidate_for_first_cut"])

    def test_required_decision_output_is_pinned(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["first_cut_surface"], "category_a_descriptor_policy_ledger")
        self.assertTrue(decision["category_b_to_f_blocked_from_first_cut"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["terrain_bathymetry_extraction_candidate"])
        self.assertTrue(decision["terrain_bathymetry_planning_candidate"])
        self.assertFalse(decision["import_boundary_checker_required_now"])
        self.assertEqual(
            decision["import_boundary_checker_reason"],
            "not_required_until_a_safe_descriptor_helper_target_is_identified",
        )
        self.assertEqual(
            decision["recommended_next_gate"],
            "terrain_bathymetry_boundary_minimal_extraction_planning_gate",
        )

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_descriptor_mapping_matrix_no_monolith_import_no_runtime_dependency",
        )
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["production_source_changed"])
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
