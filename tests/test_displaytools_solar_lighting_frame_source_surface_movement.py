import unittest


SURFACE_CATEGORIES = {
    "category_a_descriptor_policy_ledger",
    "category_b_time_source_runtime",
    "category_c_solar_formula",
    "category_d_lighting_shader_formula",
    "category_e_projection_flip_dependency",
    "category_f_runtime_renderer_host",
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
    "time source descriptor",
    "sun direction label descriptor",
    "twilight/terminator label descriptor",
    "local-noon fault ledger",
    "coordinate dependency label",
    "lighting consumer layer descriptor",
    "forbidden formula surface ledger",
}


BLOCKED_SURFACES = {
    "current time acquisition",
    "UTC/local-time conversion",
    "real clock dependency",
    "compute_sun_direction",
    "solar vector formula",
    "sun altitude/azimuth date-time math",
    "light_dir",
    "dot_l",
    "Lambertian lighting",
    "twilight formula",
    "world normal lighting",
    "bumped normal lighting",
    "longitude/latitude flip coupling",
    "projection frame coupling",
    "grid/starfield frame coupling",
    "Taichi renderer class",
    "Qt/VisPy host",
    "runtime GUI/controller behavior",
}


FORBIDDEN_CLAIM_MARKERS = {
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_ready",
    "runtime_merge_enabled",
    "safe_to_extract",
    "local_noon_fault_resolved_true",
    "source_movement_authorized_true",
    "solar_lighting_extraction_candidate_true",
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


def build_solar_lighting_frame_source_surface_movement_packet():
    matrix = [
        surface_entry(
            "time source descriptor",
            "solar/lighting boundary fixture gate time_source_descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "time-source labels can be represented as data without reading a real clock",
            "fixture parity for descriptor key sets before planning",
            "do_not_execute_real_clock_or_change_time_source",
        ),
        surface_entry(
            "sun direction label descriptor",
            "solar/lighting boundary fixture gate sun_direction_descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "sun-direction labels can describe the surface without carrying compute_sun_direction",
            "label-only fixture and formula exclusion guard",
            "do_not_move_or_execute_compute_sun_direction",
        ),
        surface_entry(
            "twilight/terminator label descriptor",
            "solar/lighting boundary fixture gate twilight_terminator_label_descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "twilight and terminator names are policy labels when formula behavior is blocked",
            "label-only fixture with no behavior claim",
            "do_not_change_twilight_or_terminator_formula",
        ),
        surface_entry(
            "local-noon fault ledger",
            "coordinate ownership diagnostic gate and solar boundary fault ledger",
            "category_a_descriptor_policy_ledger",
            True,
            "the Taipei local-noon fault can be recorded as unresolved diagnostic data",
            "ledger fixture must keep local_noon_fault_resolved false",
            "do_not_claim_taipei_local_noon_fix",
        ),
        surface_entry(
            "coordinate dependency label",
            "coordinate ownership diagnostic gate and solar boundary coordinate dependency descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "longitude/latitude, projection, and grid dependencies can be labels only",
            "string-label fixture and formula blocker",
            "do_not_change_projection_flip_or_grid_formula",
        ),
        surface_entry(
            "lighting consumer layer descriptor",
            "terrain/bathymetry boundary gates and solar lighting consumer layer descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "consumer layer names are descriptor data when runtime lighting behavior is excluded",
            "consumer descriptor fixture and no-runtime guard",
            "do_not_change_lighting_consumer_behavior",
        ),
        surface_entry(
            "forbidden formula surface ledger",
            "solar/lighting boundary fixture gate forbidden formula surface descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "blocked formula names can be held as a prohibition ledger",
            "negative wording guard and blocked-hot-path classification",
            "do_not_move_or_modify_solar_lighting_formula",
        ),
        surface_entry(
            "current time acquisition",
            "current compute_sun_direction time source path",
            "category_b_time_source_runtime",
            False,
            "current-time acquisition depends on runtime clock state",
            "time source diagnostic gate before implementation",
            "do_not_read_real_clock_in_first_cut",
        ),
        surface_entry(
            "UTC/local-time conversion",
            "Taipei local-noon diagnostic and UTC/local ambiguity label",
            "category_b_time_source_runtime",
            False,
            "conversion behavior can change the solar frame result",
            "time conversion diagnostic gate",
            "do_not_change_utc_or_local_time_conversion",
        ),
        surface_entry(
            "real clock dependency",
            "runtime solar direction update source",
            "category_b_time_source_runtime",
            False,
            "real clock dependency is runtime behavior, not descriptor data",
            "clock injection design gate if needed",
            "do_not_execute_or_patch_runtime_clock",
        ),
        surface_entry(
            "compute_sun_direction",
            "current monolith solar direction function",
            "category_c_solar_formula",
            False,
            "compute_sun_direction is formula-bearing behavior",
            "solar formula diagnostic gate before movement",
            "do_not_move_or_modify_compute_sun_direction",
        ),
        surface_entry(
            "solar vector formula",
            "current solar direction vector calculation",
            "category_c_solar_formula",
            False,
            "solar vector math can change rendered lighting orientation",
            "formula parity gate before any implementation",
            "do_not_change_solar_vector_formula",
        ),
        surface_entry(
            "sun altitude/azimuth date-time math",
            "current solar date/time responsibility family",
            "category_c_solar_formula",
            False,
            "date/time math affects sun position and must stay out of descriptor first cut",
            "time/solar diagnostic gate",
            "do_not_change_altitude_azimuth_or_date_time_math",
        ),
        surface_entry(
            "light_dir",
            "current shader lighting vector consumer",
            "category_d_lighting_shader_formula",
            False,
            "light_dir is a shader-side consumer input and can affect pixels",
            "lighting shader formula gate",
            "do_not_move_or_modify_light_dir",
        ),
        surface_entry(
            "dot_l",
            "current Lambertian lighting branch",
            "category_d_lighting_shader_formula",
            False,
            "dot_l is formula-bearing lighting behavior",
            "lighting shader formula gate",
            "do_not_move_or_modify_dot_l",
        ),
        surface_entry(
            "Lambertian lighting",
            "current dot_l lighting surface",
            "category_d_lighting_shader_formula",
            False,
            "Lambertian behavior changes visual output and must remain blocked",
            "pixel/lighting diagnostic gate",
            "do_not_change_lambertian_lighting_behavior",
        ),
        surface_entry(
            "twilight formula",
            "current twilight/terminator lighting branch",
            "category_d_lighting_shader_formula",
            False,
            "twilight formula affects terminator appearance",
            "twilight formula diagnostic gate",
            "do_not_change_twilight_formula",
        ),
        surface_entry(
            "world normal lighting",
            "current n_world lighting consumer",
            "category_d_lighting_shader_formula",
            False,
            "world normal lighting is formula-bearing shader behavior",
            "normal consumer diagnostic gate",
            "do_not_change_world_normal_lighting",
        ),
        surface_entry(
            "bumped normal lighting",
            "current n_world_bump lighting consumer",
            "category_d_lighting_shader_formula",
            False,
            "bumped normal lighting is coupled to terrain bump behavior",
            "bump/normal diagnostic gate",
            "do_not_change_bumped_normal_lighting",
        ),
        surface_entry(
            "longitude/latitude flip coupling",
            "coordinate ownership diagnostic gate flip dependency labels",
            "category_e_projection_flip_dependency",
            False,
            "flip coupling owns coordinate behavior and active orientation faults",
            "coordinate formula gate before implementation",
            "do_not_change_flip_formula",
        ),
        surface_entry(
            "projection frame coupling",
            "coordinate ownership and globe coordinate fixture gates",
            "category_e_projection_flip_dependency",
            False,
            "projection coupling can change layer alignment and screen mapping",
            "projection diagnostic gate",
            "do_not_change_projection_formula",
        ),
        surface_entry(
            "grid/starfield frame coupling",
            "coordinate ownership diagnostic gate grid/starfield frame",
            "category_e_projection_flip_dependency",
            False,
            "grid/starfield coupling is frame ownership, not solar descriptor data",
            "coordinate frame follow-up if needed",
            "do_not_merge_grid_starfield_frame_into_solar_first_cut",
        ),
        surface_entry(
            "Taichi renderer class",
            "current TaichiGlobeRenderer runtime host",
            "category_f_runtime_renderer_host",
            False,
            "renderer class movement would import GPU/runtime behavior",
            "renderer-host map before any runtime work",
            "do_not_move_or_instantiate_renderer_class",
        ),
        surface_entry(
            "Qt/VisPy host",
            "current UI/runtime host surfaces",
            "category_f_runtime_renderer_host",
            False,
            "host behavior needs runtime execution and is outside descriptor ownership",
            "UI/host seam gate if needed",
            "do_not_import_or_execute_qt_vispy_host",
        ),
        surface_entry(
            "runtime GUI/controller behavior",
            "current controller/runtime methods that configure renderer state",
            "category_f_runtime_renderer_host",
            False,
            "controller mutation is runtime behavior rather than descriptor data",
            "controller seam map before any runtime work",
            "do_not_move_controller_or_runtime_behavior",
        ),
    ]
    decision_output = {
        "first_cut_surface": "category_a_descriptor_policy_ledger",
        "category_b_to_f_blocked_from_first_cut": True,
        "source_movement_authorized": False,
        "solar_lighting_extraction_candidate": False,
        "solar_lighting_planning_candidate": True,
        "local_noon_fault_resolved": False,
        "compute_sun_direction_formula_allowed": False,
        "lighting_shader_formula_allowed": False,
        "projection_flip_formula_allowed": False,
        "import_boundary_checker_required_now": False,
        "import_boundary_checker_reason": "not_required_until_a_descriptor_only_helper_target_is_identified",
        "recommended_next_gate": "solar_lighting_frame_boundary_minimal_extraction_planning_gate",
    }
    return {
        "test_shape": "pure_descriptor_mapping_matrix_no_monolith_import_no_runtime_dependency",
        "surface_categories": sorted(SURFACE_CATEGORIES),
        "surface_matrix": matrix,
        "decision_output": decision_output,
        "runtime_render_invoked": False,
        "real_clock_executed": False,
        "production_source_changed": False,
    }


class SolarLightingFrameSourceSurfaceMovementPreimplementationGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_solar_lighting_frame_source_surface_movement_packet()

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

    def test_time_source_runtime_surfaces_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in ["current time acquisition", "UTC/local-time conversion", "real clock dependency"]:
            self.assertEqual(matrix[surface]["movement_category"], "category_b_time_source_runtime")
            self.assertFalse(matrix[surface]["candidate_for_first_cut"])

    def test_solar_and_lighting_formula_surfaces_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in [
            "compute_sun_direction",
            "solar vector formula",
            "sun altitude/azimuth date-time math",
            "light_dir",
            "dot_l",
            "Lambertian lighting",
            "twilight formula",
            "world normal lighting",
            "bumped normal lighting",
        ]:
            self.assertFalse(matrix[surface]["candidate_for_first_cut"], surface)

    def test_projection_flip_and_runtime_host_surfaces_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in [
            "longitude/latitude flip coupling",
            "projection frame coupling",
            "grid/starfield frame coupling",
            "Taichi renderer class",
            "Qt/VisPy host",
            "runtime GUI/controller behavior",
        ]:
            self.assertFalse(matrix[surface]["candidate_for_first_cut"], surface)

    def test_required_decision_output_is_pinned(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["first_cut_surface"], "category_a_descriptor_policy_ledger")
        self.assertTrue(decision["category_b_to_f_blocked_from_first_cut"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["solar_lighting_extraction_candidate"])
        self.assertTrue(decision["solar_lighting_planning_candidate"])
        self.assertFalse(decision["local_noon_fault_resolved"])
        self.assertFalse(decision["compute_sun_direction_formula_allowed"])
        self.assertFalse(decision["lighting_shader_formula_allowed"])
        self.assertFalse(decision["projection_flip_formula_allowed"])
        self.assertFalse(decision["import_boundary_checker_required_now"])
        self.assertEqual(
            decision["import_boundary_checker_reason"],
            "not_required_until_a_descriptor_only_helper_target_is_identified",
        )
        self.assertEqual(
            decision["recommended_next_gate"],
            "solar_lighting_frame_boundary_minimal_extraction_planning_gate",
        )

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_descriptor_mapping_matrix_no_monolith_import_no_runtime_dependency",
        )
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["real_clock_executed"])
        self.assertFalse(self.packet["production_source_changed"])
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)
        for forbidden in ["import taichi", "from PyQt6", "import vispy", "import taichi_global_bathymetry"]:
            self.assertNotIn(forbidden, packet_text)


if __name__ == "__main__":
    unittest.main()
