import unittest


PLANNING_PACKET_KEYS = {
    "schema",
    "target_candidate",
    "source_movement_authorized",
    "helper_module_creation_authorized",
    "solar_lighting_extraction_candidate",
    "solar_lighting_planning_candidate",
    "local_noon_fault_resolved",
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
    "real_clock_execution_allowed",
    "solar_formula_allowed",
    "lighting_shader_formula_allowed",
    "projection_flip_formula_allowed",
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
    "build_solar_time_source_descriptor",
    "build_solar_direction_label_descriptor",
    "build_solar_twilight_terminator_label_descriptor",
    "build_solar_local_noon_fault_ledger_descriptor",
    "build_solar_coordinate_dependency_label_descriptor",
    "build_solar_lighting_consumer_layers_descriptor",
    "build_solar_forbidden_formula_surface_ledger_descriptor",
    "solar_lighting_frame_boundary_descriptor",
    "solar_lighting_planning_bundle",
}


REQUIRED_BLOCKED = {
    "current time acquisition",
    "UTC/local-time conversion",
    "real clock dependency",
    "compute_sun_direction",
    "solar vector / altitude / azimuth formula",
    "light_dir",
    "dot_l",
    "Lambertian lighting formula",
    "twilight / terminator formula",
    "world normal / bumped normal lighting formula",
    "longitude/latitude flip formula",
    "projection frame coupling",
    "grid/starfield frame coupling",
    "TaichiGlobeRenderer",
    "Qt/VisPy host surfaces",
    "runtime GUI/controller behavior",
    "terrain shader / sampling / bump formula",
    "metadata/artifact writers",
    "alpha/apply/composition hot path",
}


REQUIRED_FIXTURE_PARITY = [
    "exact key-set parity for descriptor builders",
    "deterministic repeat-call parity",
    "time source descriptor branch",
    "sun direction label-only branch",
    "twilight/terminator label-only branch",
    "local-noon fault unresolved ledger branch",
    "coordinate dependency label-only branch",
    "lighting consumer layer descriptor branch",
    "forbidden formula surface ledger branch",
    "future import-boundary checker candidate pass",
    "future forbidden runtime/formula dependency fail",
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
    "solar_lighting_extraction_candidate_true",
    "local_noon_fault_resolved_true",
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
        "real_clock_execution_allowed": False,
        "solar_formula_allowed": False,
        "lighting_shader_formula_allowed": False,
        "projection_flip_formula_allowed": False,
        "visual_behavior_change_allowed": False,
        "candidate_for_minimal_extraction": True,
        "required_fixture": required_fixture,
        "required_checker": "future_validate_displaytools_solar_lighting_frame_import_boundary.py",
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


def build_solar_lighting_frame_boundary_minimal_extraction_planning_packet():
    candidate_symbols = [
        candidate_entry(
            "build_solar_time_source_descriptor",
            "solar/lighting boundary and source-surface gates time source descriptor",
            "future descriptor-only surface",
            "build_solar_time_source_descriptor",
            "time source descriptor exact key-set and repeat-call parity",
            "do_not_execute_real_clock_or_change_time_source",
        ),
        candidate_entry(
            "build_solar_direction_label_descriptor",
            "solar/lighting boundary sun direction label descriptor",
            "future label descriptor surface",
            "build_solar_direction_label_descriptor",
            "sun direction label-only parity",
            "do_not_move_or_execute_compute_sun_direction",
        ),
        candidate_entry(
            "build_solar_twilight_terminator_label_descriptor",
            "twilight/terminator label descriptor from boundary fixture gate",
            "future label descriptor surface",
            "build_solar_twilight_terminator_label_descriptor",
            "twilight/terminator label-only parity",
            "do_not_change_twilight_or_terminator_formula",
        ),
        candidate_entry(
            "build_solar_local_noon_fault_ledger_descriptor",
            "local-noon fault ledger from coordinate and solar boundary gates",
            "future ledger descriptor surface",
            "build_solar_local_noon_fault_ledger_descriptor",
            "local-noon unresolved ledger parity",
            "do_not_claim_taipei_local_noon_fix",
        ),
        candidate_entry(
            "build_solar_coordinate_dependency_label_descriptor",
            "coordinate dependency labels from coordinate ownership and source-surface gates",
            "future label descriptor surface",
            "build_solar_coordinate_dependency_label_descriptor",
            "coordinate dependency label-only parity",
            "do_not_change_projection_or_flip_formula",
        ),
        candidate_entry(
            "build_solar_lighting_consumer_layers_descriptor",
            "lighting consumer layer descriptor from solar and terrain boundary gates",
            "future descriptor-only surface",
            "build_solar_lighting_consumer_layers_descriptor",
            "lighting consumer descriptor parity",
            "do_not_change_lighting_consumer_behavior",
        ),
        candidate_entry(
            "build_solar_forbidden_formula_surface_ledger_descriptor",
            "forbidden formula surface ledger from solar boundary fixture gate",
            "future ledger descriptor surface",
            "build_solar_forbidden_formula_surface_ledger_descriptor",
            "forbidden formula ledger parity",
            "do_not_move_or_modify_solar_lighting_formula",
        ),
        candidate_entry(
            "solar_lighting_frame_boundary_descriptor",
            "optional aggregate descriptor from category A families only",
            "future aggregate descriptor value",
            "solar_lighting_frame_boundary_descriptor",
            "aggregate descriptor exact key-set parity",
            "do_not_include_time_runtime_formula_or_renderer_host",
        ),
        candidate_entry(
            "solar_lighting_planning_bundle",
            "optional planning bundle from category A candidate families only",
            "future planning bundle value",
            "solar_lighting_planning_bundle",
            "bundle key-set and blocked-surface declaration parity",
            "do_not_authorize_source_movement_inside_bundle",
        ),
    ]
    blocked_symbols = [
        blocked_entry("current time acquisition", "time_source_runtime", "real current-time read is runtime behavior", "time source diagnostic gate", "do_not_read_real_clock"),
        blocked_entry("UTC/local-time conversion", "time_source_runtime", "conversion behavior can change solar frame result", "time conversion diagnostic gate", "do_not_change_utc_or_local_time_conversion"),
        blocked_entry("real clock dependency", "time_source_runtime", "runtime clock dependency is not descriptor data", "clock seam design gate", "do_not_execute_or_patch_runtime_clock"),
        blocked_entry("compute_sun_direction", "solar_formula", "solar direction formula can change lighting orientation", "solar formula diagnostic gate", "do_not_move_or_change_compute_sun_direction"),
        blocked_entry("solar vector / altitude / azimuth formula", "solar_formula", "solar vector and date-time math affect rendered lighting", "solar formula parity gate", "do_not_change_solar_vector_or_date_time_math"),
        blocked_entry("light_dir", "lighting_shader_formula", "shader lighting vector affects pixels", "lighting shader formula gate", "do_not_move_or_modify_light_dir"),
        blocked_entry("dot_l", "lighting_shader_formula", "Lambertian dot term is formula-bearing behavior", "lighting shader formula gate", "do_not_move_or_modify_dot_l"),
        blocked_entry("Lambertian lighting formula", "lighting_shader_formula", "lighting model changes visual output", "lighting shader formula gate", "do_not_change_lambertian_lighting"),
        blocked_entry("twilight / terminator formula", "lighting_shader_formula", "twilight formula affects terminator appearance", "twilight formula gate", "do_not_change_twilight_or_terminator_formula"),
        blocked_entry("world normal / bumped normal lighting formula", "lighting_shader_formula", "normal lighting is coupled to shader and terrain bump behavior", "normal lighting diagnostic gate", "do_not_change_world_or_bumped_normal_lighting"),
        blocked_entry("longitude/latitude flip formula", "projection_flip_dependency", "flip formula owns coordinate orientation faults", "coordinate formula gate", "do_not_change_flip_formula"),
        blocked_entry("projection frame coupling", "projection_flip_dependency", "projection coupling can change frame alignment", "projection diagnostic gate", "do_not_change_projection_formula"),
        blocked_entry("grid/starfield frame coupling", "projection_flip_dependency", "frame coupling is coordinate ownership, not solar descriptor data", "coordinate frame gate", "do_not_merge_grid_starfield_frame_into_first_cut"),
        blocked_entry("TaichiGlobeRenderer", "runtime_renderer_host", "renderer class owns GPU/runtime state", "renderer host map", "do_not_import_or_instantiate_renderer"),
        blocked_entry("Qt/VisPy host surfaces", "runtime_renderer_host", "UI/render host requires runtime", "UI/host seam gate", "do_not_import_or_execute_qt_vispy"),
        blocked_entry("runtime GUI/controller behavior", "runtime_renderer_host", "controller behavior mutates runtime state", "controller seam gate", "do_not_move_controller_behavior"),
        blocked_entry("terrain shader / sampling / bump formula", "terrain_shader_hot_path", "terrain shader and bump formulas affect lighting inputs and pixels", "terrain shader diagnostic gate", "do_not_touch_terrain_shader_sampling_or_bump"),
        blocked_entry("metadata/artifact writers", "metadata_artifact_writer", "writer behavior changes output/artifacts", "metadata/output boundary gate", "do_not_execute_or_move_writers"),
        blocked_entry("alpha/apply/composition hot path", "hot_path_blocked", "composition hot path is outside solar descriptor planning", "alpha/apply hot-path gate", "do_not_touch_alpha_apply_composition"),
    ]
    return {
        "schema": "rrkal_displaytools.solar_lighting_frame_boundary_minimal_extraction_planning.v1",
        "target_candidate": r"render_core\solar_lighting_frame_boundary.py",
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "solar_lighting_extraction_candidate": False,
        "solar_lighting_planning_candidate": True,
        "local_noon_fault_resolved": False,
        "a1_macro_observer_required_before_source_movement": True,
        "candidate_symbols": candidate_symbols,
        "blocked_symbols": blocked_symbols,
        "fixture_parity_plan": list(REQUIRED_FIXTURE_PARITY),
        "import_boundary_checker_need": {
            "required_before_extraction": True,
            "required_now": False,
            "reason": "planning_only_no_helper_target_created_in_this_slice",
            "future_checker_target": r"render_core\solar_lighting_frame_boundary.py",
        },
        "decision_output": {
            "next_can_be_actual_extraction": "not_yet_only_after_a1_macro_observer_and_o1_review",
            "first_cut_minimal_scope": "descriptor_policy_ledger_only",
            "candidate_categories": ["category_a_descriptor_policy_ledger"],
            "blocked_categories": [
                "category_b_time_source_runtime",
                "category_c_solar_formula",
                "category_d_lighting_shader_formula",
                "category_e_projection_flip_dependency",
                "category_f_runtime_renderer_host",
            ],
        },
        "next_gate": "solar_lighting_frame_import_boundary_checker_gate",
        "boundary_statement": (
            "Docs/test-only solar/lighting frame boundary minimal extraction planning gate. "
            "No helper module creation, no source movement, no production source change, no monolith import, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no real clock/render/provider execution, "
            "no compute_sun_direction/sun-vector/light_dir/dot_l/twilight/normal/projection/flip formula change, "
            "no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim."
        ),
    }


class SolarLightingFrameBoundaryMinimalExtractionPlanningGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_solar_lighting_frame_boundary_minimal_extraction_planning_packet()

    def test_planning_packet_top_level_contract_is_pinned(self):
        self.assertEqual(set(self.packet), PLANNING_PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal_displaytools.solar_lighting_frame_boundary_minimal_extraction_planning.v1",
        )
        self.assertEqual(self.packet["target_candidate"], r"render_core\solar_lighting_frame_boundary.py")
        self.assertFalse(self.packet["source_movement_authorized"])
        self.assertFalse(self.packet["helper_module_creation_authorized"])
        self.assertFalse(self.packet["solar_lighting_extraction_candidate"])
        self.assertTrue(self.packet["solar_lighting_planning_candidate"])
        self.assertFalse(self.packet["local_noon_fault_resolved"])
        self.assertTrue(self.packet["a1_macro_observer_required_before_source_movement"])

    def test_candidate_descriptor_families_are_category_a_only(self):
        names = {entry["candidate_name"] for entry in self.packet["candidate_symbols"]}
        self.assertEqual(names, REQUIRED_CANDIDATES)
        for entry in self.packet["candidate_symbols"]:
            self.assertEqual(set(entry), CANDIDATE_ENTRY_KEYS)
            self.assertEqual(entry["movement_category"], "category_a_descriptor_policy_ledger")
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertFalse(entry["real_clock_execution_allowed"])
            self.assertFalse(entry["solar_formula_allowed"])
            self.assertFalse(entry["lighting_shader_formula_allowed"])
            self.assertFalse(entry["projection_flip_formula_allowed"])
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
        self.assertEqual(need["future_checker_target"], r"render_core\solar_lighting_frame_boundary.py")

    def test_a1_and_decision_output_block_source_movement(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["next_can_be_actual_extraction"], "not_yet_only_after_a1_macro_observer_and_o1_review")
        self.assertEqual(decision["first_cut_minimal_scope"], "descriptor_policy_ledger_only")
        self.assertEqual(decision["candidate_categories"], ["category_a_descriptor_policy_ledger"])
        self.assertEqual(
            decision["blocked_categories"],
            [
                "category_b_time_source_runtime",
                "category_c_solar_formula",
                "category_d_lighting_shader_formula",
                "category_e_projection_flip_dependency",
                "category_f_runtime_renderer_host",
            ],
        )
        self.assertEqual(self.packet["next_gate"], "solar_lighting_frame_import_boundary_checker_gate")

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_MARKERS:
            self.assertNotIn(marker, packet_text)
        boundary = self.packet["boundary_statement"].lower()
        self.assertIn("no helper module creation", boundary)
        self.assertIn("no safe-to-extract", boundary)


if __name__ == "__main__":
    unittest.main()
