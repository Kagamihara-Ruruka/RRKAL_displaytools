import unittest


PLANNING_PACKET_KEYS = {
    "schema",
    "target_candidate",
    "source_movement_authorized",
    "helper_module_creation_authorized",
    "terrain_bathymetry_extraction_candidate",
    "terrain_bathymetry_planning_candidate",
    "a1_macro_observer_required_before_source_movement",
    "candidate_symbols",
    "blocked_symbols",
    "fixture_parity_plan",
    "import_boundary_checker_need",
    "decision_output",
    "next_gate",
    "boundary_statement",
}


CANDIDATE_ENTRY_KEYS = {
    "candidate_name",
    "source_evidence",
    "source_owner",
    "planned_target_name",
    "allowed_content_kind",
    "movement_category",
    "runtime_dependency_allowed",
    "provider_cache_execution_allowed",
    "shader_formula_allowed",
    "projection_lighting_formula_allowed",
    "visual_behavior_change_allowed",
    "candidate_for_minimal_extraction",
    "required_fixture",
    "required_checker",
    "forbidden_next_action",
}


BLOCKED_ENTRY_KEYS = {
    "blocked_name",
    "blocked_category",
    "reason",
    "required_future_gate",
    "forbidden_next_action",
    "candidate_for_minimal_extraction",
}


REQUIRED_CANDIDATES = {
    "build_terrain_bathymetry_source_descriptor",
    "build_terrain_height_field_descriptor",
    "build_terrain_fallback_no_data_descriptor",
    "build_terrain_lod_resolution_label_descriptor",
    "build_terrain_cache_status_label_descriptor",
    "build_terrain_palette_style_label_descriptor",
    "build_terrain_known_fault_ledger_descriptor",
    "terrain_bathymetry_boundary_descriptor",
    "terrain_bathymetry_planning_bundle",
}


REQUIRED_BLOCKED = {
    "load_topography",
    "synthetic_topography behavior",
    "NOAA/GEBCO/ETOPO provider execution",
    "topography cache read/write/load/save",
    "terrain sampling formula",
    "bump/normal formula",
    "raymarch/sphere intersection/shader height lookup",
    "flip_longitude/flip_latitude formula",
    "compute_sun_direction",
    "light_dir/dot_l/twilight formula",
    "TaichiGlobeRenderer",
    "Qt/VisPy host surfaces",
    "runtime GUI/controller behavior",
    "water/land palette behavior",
    "metadata/artifact writers",
    "alpha/apply/composition hot path",
}


REQUIRED_FIXTURE_PARITY = [
    "exact key-set parity for descriptor builders",
    "deterministic repeat-call parity",
    "source descriptor branch",
    "height-field descriptor branch",
    "fallback/no-data descriptor branch",
    "LOD/resolution label-only branch",
    "cache hit/miss label-only branch",
    "palette/style label-only branch",
    "known fault ledger unresolved branch",
    "future import-boundary checker candidate pass",
    "future forbidden dependency fail",
]


FORBIDDEN_MARKERS = {
    "safe_to_extract",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_ready",
    "runtime_merge_enabled",
    "source_movement_authorized_true",
    "helper_module_creation_authorized_true",
    "terrain_bathymetry_extraction_candidate_true",
}


def candidate_entry(candidate_name, source_evidence, source_owner, planned_target_name, required_fixture, forbidden_next_action):
    return {
        "candidate_name": candidate_name,
        "source_evidence": source_evidence,
        "source_owner": source_owner,
        "planned_target_name": planned_target_name,
        "allowed_content_kind": "dict/list/scalar descriptor builder or policy/ledger table",
        "movement_category": "category_a_descriptor_policy_ledger",
        "runtime_dependency_allowed": False,
        "provider_cache_execution_allowed": False,
        "shader_formula_allowed": False,
        "projection_lighting_formula_allowed": False,
        "visual_behavior_change_allowed": False,
        "candidate_for_minimal_extraction": True,
        "required_fixture": required_fixture,
        "required_checker": "future_validate_displaytools_terrain_bathymetry_boundary_import_boundary.py",
        "forbidden_next_action": forbidden_next_action,
    }


def blocked_entry(blocked_name, blocked_category, reason, required_future_gate, forbidden_next_action):
    return {
        "blocked_name": blocked_name,
        "blocked_category": blocked_category,
        "reason": reason,
        "required_future_gate": required_future_gate,
        "forbidden_next_action": forbidden_next_action,
        "candidate_for_minimal_extraction": False,
    }


def build_terrain_bathymetry_boundary_minimal_extraction_planning_packet():
    candidate_symbols = [
        candidate_entry(
            "build_terrain_bathymetry_source_descriptor",
            "terrain/bathymetry source descriptor from boundary and source-surface gates",
            "future descriptor-only surface",
            "build_terrain_bathymetry_source_descriptor",
            "source descriptor exact key-set and repeat-call parity",
            "do_not_execute_load_topography_or_provider_cache",
        ),
        candidate_entry(
            "build_terrain_height_field_descriptor",
            "height-field descriptor from topography field and renderer input labels",
            "future descriptor-only surface",
            "build_terrain_height_field_descriptor",
            "height-field descriptor exact key-set parity",
            "do_not_move_sampling_or_shader_height_lookup",
        ),
        candidate_entry(
            "build_terrain_fallback_no_data_descriptor",
            "fallback/no-data descriptor from load_topography fallback and synthetic label",
            "future descriptor-only surface",
            "build_terrain_fallback_no_data_descriptor",
            "fallback/no-data branch parity",
            "do_not_generate_or_download_real_topography",
        ),
        candidate_entry(
            "build_terrain_lod_resolution_label_descriptor",
            "LOD/resolution label from topo_step, cache path, and stride labels",
            "future label descriptor surface",
            "build_terrain_lod_resolution_label_descriptor",
            "LOD/resolution label-only parity",
            "do_not_change_resolution_or_sampling_behavior",
        ),
        candidate_entry(
            "build_terrain_cache_status_label_descriptor",
            "cache status label from cache hit/miss/fallback branches",
            "future label descriptor surface",
            "build_terrain_cache_status_label_descriptor",
            "cache hit/miss label-only parity",
            "do_not_read_write_load_save_or_evict_cache",
        ),
        candidate_entry(
            "build_terrain_palette_style_label_descriptor",
            "palette/style label from water/land palette descriptor boundary",
            "future label descriptor surface",
            "build_terrain_palette_style_label_descriptor",
            "palette/style label-only parity",
            "do_not_change_palette_or_visual_behavior",
        ),
        candidate_entry(
            "build_terrain_known_fault_ledger_descriptor",
            "known fault ledger from blocky terrain, flip, and lighting unresolved gates",
            "future ledger descriptor surface",
            "build_terrain_known_fault_ledger_descriptor",
            "known fault unresolved/static-only ledger parity",
            "do_not_mark_visual_fault_fixed_or_ready",
        ),
        candidate_entry(
            "terrain_bathymetry_boundary_descriptor",
            "optional aggregate descriptor from category A families only",
            "future aggregate descriptor value",
            "terrain_bathymetry_boundary_descriptor",
            "aggregate descriptor exact key-set parity",
            "do_not_include_runtime_formula_or_provider_loader",
        ),
        candidate_entry(
            "terrain_bathymetry_planning_bundle",
            "optional planning bundle from category A candidate families only",
            "future planning bundle value",
            "terrain_bathymetry_planning_bundle",
            "bundle key-set and blocked-surface declaration parity",
            "do_not_authorize_source_movement_inside_bundle",
        ),
    ]
    blocked_symbols = [
        blocked_entry("load_topography", "provider_cache_loader", "loads terrain/provider/cache data", "provider/cache boundary gate", "do_not_move_or_call_loader"),
        blocked_entry("synthetic_topography behavior", "provider_cache_loader", "generates fallback terrain behavior, not a descriptor", "fallback behavior parity gate", "do_not_move_or_change_synthetic_generation"),
        blocked_entry("NOAA/GEBCO/ETOPO provider execution", "provider_cache_loader", "external provider execution is IO/lifecycle behavior", "provider/cache loader gate", "do_not_fetch_download_or_execute_provider"),
        blocked_entry("topography cache read/write/load/save", "provider_cache_loader", "cache lifecycle reads/writes files", "cache lifecycle boundary gate", "do_not_read_write_load_save_cache"),
        blocked_entry("terrain sampling formula", "sampling_shader_formula", "formula maps sample frame to height lookup", "terrain sampling diagnostic gate", "do_not_move_or_change_sampling_formula"),
        blocked_entry("bump/normal formula", "sampling_shader_formula", "formula affects normals and lighting", "bump/normal diagnostic gate", "do_not_move_or_change_bump_formula"),
        blocked_entry("raymarch/sphere intersection/shader height lookup", "sampling_shader_formula", "shader hot path affects pixels", "renderer hot-path gate", "do_not_touch_shader_geometry_path"),
        blocked_entry("flip_longitude/flip_latitude formula", "projection_flip_lighting_formula", "flip behavior owns coordinate faults", "coordinate formula gate", "do_not_change_flip_formula"),
        blocked_entry("compute_sun_direction", "projection_flip_lighting_formula", "solar frame behavior affects lighting", "solar frame diagnostic gate", "do_not_move_or_change_sun_direction"),
        blocked_entry("light_dir/dot_l/twilight formula", "projection_flip_lighting_formula", "lighting formula affects rendered output", "lighting diagnostic gate", "do_not_move_or_change_lighting_formula"),
        blocked_entry("TaichiGlobeRenderer", "runtime_renderer_host", "renderer class owns GPU/runtime state", "renderer host map", "do_not_import_or_instantiate_renderer"),
        blocked_entry("Qt/VisPy host surfaces", "runtime_renderer_host", "UI/render host requires runtime", "UI/host seam gate", "do_not_import_or_execute_qt_vispy"),
        blocked_entry("runtime GUI/controller behavior", "runtime_renderer_host", "controller behavior mutates runtime state", "controller seam gate", "do_not_move_controller_behavior"),
        blocked_entry("water/land palette behavior", "visual_style_behavior", "visual color behavior is not label-only data", "palette behavior parity gate", "do_not_change_palette_behavior"),
        blocked_entry("metadata/artifact writers", "metadata_artifact_writer", "writer behavior changes output/artifacts", "metadata/output boundary gate", "do_not_execute_or_move_writers"),
        blocked_entry("alpha/apply/composition hot path", "hot_path_blocked", "composition hot path is outside terrain descriptor planning", "alpha/apply hot-path gate", "do_not_touch_alpha_apply_composition"),
    ]
    return {
        "schema": "rrkal_displaytools.terrain_bathymetry_boundary_minimal_extraction_planning.v1",
        "target_candidate": r"render_core\terrain_bathymetry_boundary.py",
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "terrain_bathymetry_extraction_candidate": False,
        "terrain_bathymetry_planning_candidate": True,
        "a1_macro_observer_required_before_source_movement": True,
        "candidate_symbols": candidate_symbols,
        "blocked_symbols": blocked_symbols,
        "fixture_parity_plan": list(REQUIRED_FIXTURE_PARITY),
        "import_boundary_checker_need": {
            "required_before_extraction": True,
            "required_now": False,
            "reason": "planning_only_no_helper_target_created_in_this_slice",
            "future_checker_target": r"render_core\terrain_bathymetry_boundary.py",
        },
        "decision_output": {
            "next_can_be_actual_extraction": "not_yet_only_after_a1_macro_observer_and_o1_review",
            "first_cut_minimal_scope": "descriptor_policy_ledger_only",
            "candidate_categories": ["category_a_descriptor_policy_ledger"],
            "blocked_categories": [
                "category_b_provider_cache_loader",
                "category_c_sampling_shader_formula",
                "category_d_projection_flip_lighting",
                "category_e_runtime_renderer_host",
                "category_f_visual_style_palette_behavior",
            ],
        },
        "next_gate": "terrain_bathymetry_import_boundary_checker_gate",
        "boundary_statement": (
            "Docs/test-only terrain/bathymetry boundary minimal extraction planning gate. "
            "No helper module creation, no source movement, no production source change, no monolith import, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no real terrain/cache/provider read, "
            "no shader/sampling/bump/projection/flip/lighting formula change, no metadata/output schema change, "
            "no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim."
        ),
    }


class TerrainBathymetryBoundaryMinimalExtractionPlanningGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_terrain_bathymetry_boundary_minimal_extraction_planning_packet()

    def test_planning_packet_top_level_contract_is_pinned(self):
        self.assertEqual(set(self.packet), PLANNING_PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal_displaytools.terrain_bathymetry_boundary_minimal_extraction_planning.v1",
        )
        self.assertEqual(self.packet["target_candidate"], r"render_core\terrain_bathymetry_boundary.py")
        self.assertFalse(self.packet["source_movement_authorized"])
        self.assertFalse(self.packet["helper_module_creation_authorized"])
        self.assertFalse(self.packet["terrain_bathymetry_extraction_candidate"])
        self.assertTrue(self.packet["terrain_bathymetry_planning_candidate"])
        self.assertTrue(self.packet["a1_macro_observer_required_before_source_movement"])

    def test_candidate_descriptor_families_are_category_a_only(self):
        names = {entry["candidate_name"] for entry in self.packet["candidate_symbols"]}
        self.assertEqual(names, REQUIRED_CANDIDATES)
        for entry in self.packet["candidate_symbols"]:
            self.assertEqual(set(entry), CANDIDATE_ENTRY_KEYS)
            self.assertEqual(entry["movement_category"], "category_a_descriptor_policy_ledger")
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertFalse(entry["provider_cache_execution_allowed"])
            self.assertFalse(entry["shader_formula_allowed"])
            self.assertFalse(entry["projection_lighting_formula_allowed"])
            self.assertFalse(entry["visual_behavior_change_allowed"])
            self.assertTrue(entry["candidate_for_minimal_extraction"])

    def test_blocked_symbols_are_not_extraction_candidates(self):
        names = {entry["blocked_name"] for entry in self.packet["blocked_symbols"]}
        self.assertEqual(names, REQUIRED_BLOCKED)
        for entry in self.packet["blocked_symbols"]:
            self.assertEqual(set(entry), BLOCKED_ENTRY_KEYS)
            self.assertFalse(entry["candidate_for_minimal_extraction"])

    def test_fixture_parity_plan_is_complete_and_ordered(self):
        self.assertEqual(self.packet["fixture_parity_plan"], REQUIRED_FIXTURE_PARITY)

    def test_import_boundary_checker_is_required_before_extraction_not_now(self):
        need = self.packet["import_boundary_checker_need"]
        self.assertTrue(need["required_before_extraction"])
        self.assertFalse(need["required_now"])
        self.assertEqual(need["reason"], "planning_only_no_helper_target_created_in_this_slice")
        self.assertEqual(need["future_checker_target"], r"render_core\terrain_bathymetry_boundary.py")

    def test_a1_and_decision_output_block_source_movement(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["next_can_be_actual_extraction"], "not_yet_only_after_a1_macro_observer_and_o1_review")
        self.assertEqual(decision["first_cut_minimal_scope"], "descriptor_policy_ledger_only")
        self.assertEqual(decision["candidate_categories"], ["category_a_descriptor_policy_ledger"])
        self.assertEqual(
            decision["blocked_categories"],
            [
                "category_b_provider_cache_loader",
                "category_c_sampling_shader_formula",
                "category_d_projection_flip_lighting",
                "category_e_runtime_renderer_host",
                "category_f_visual_style_palette_behavior",
            ],
        )
        self.assertEqual(self.packet["next_gate"], "terrain_bathymetry_import_boundary_checker_gate")

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_MARKERS:
            self.assertNotIn(marker, packet_text)
        boundary = self.packet["boundary_statement"].lower()
        self.assertIn("no helper module creation", boundary)
        self.assertIn("no safe-to-extract", boundary)


if __name__ == "__main__":
    unittest.main()
