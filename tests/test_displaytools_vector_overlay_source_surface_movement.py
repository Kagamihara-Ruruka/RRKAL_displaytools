import unittest


SURFACE_CATEGORIES = {
    "category_a_descriptor_policy_ledger",
    "category_b_provider_cache_contract",
    "category_c_projection_mask_consumer",
    "category_d_controller_registry_mutation",
    "category_e_runtime_overlay_class",
    "category_f_hot_path_blocked",
}


SURFACE_ENTRY_KEYS = {
    "symbol_or_surface",
    "observed_owner",
    "movement_category",
    "candidate_for_first_cut",
    "reason",
    "required_guard",
    "forbidden_next_action",
}


REQUIRED_SURFACES = {
    "GeoVectorLineOverlay",
    "borders provider descriptor",
    "hydrology provider descriptor",
    "vector overlay descriptor builder",
    "vector dirty/reload ledger",
    "vector controller registry descriptor",
    "vector projection policy label",
    "vector mask policy label",
    "provider cache status label",
    "actual provider/cache loader",
    "projection formula",
    "mask clipping formula",
    "controller dirty flag mutation",
    "controller reload request mutation",
    "alpha/apply/composition hot path",
    "metadata/artifact writer",
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "source_movement_authorized_true",
    "GeoVectorLineOverlay_first_cut",
}


def surface_entry(
    symbol_or_surface,
    observed_owner,
    movement_category,
    candidate_for_first_cut,
    reason,
    required_guard,
    forbidden_next_action,
):
    return {
        "symbol_or_surface": symbol_or_surface,
        "observed_owner": observed_owner,
        "movement_category": movement_category,
        "candidate_for_first_cut": candidate_for_first_cut,
        "reason": reason,
        "required_guard": required_guard,
        "forbidden_next_action": forbidden_next_action,
    }


def build_vector_overlay_source_surface_movement_packet():
    matrix = [
        surface_entry(
            "GeoVectorLineOverlay",
            "taichi_global_bathymetry.py:3888 / d90b645:2625",
            "category_e_runtime_overlay_class",
            False,
            "runtime overlay class consumes lon/lat lines, camera, flip flags, globe mask, and screen-space render parameters",
            "runtime-specific parity and controller seam review after descriptor planning",
            "do_not_move_runtime_overlay_class_as_first_cut",
        ),
        surface_entry(
            "borders provider descriptor",
            "BOUNDARY_SPECS in taichi_global_bathymetry.py:4257 / d90b645:2843",
            "category_a_descriptor_policy_ledger",
            True,
            "static descriptor data can be represented without provider execution or cache reads",
            "vector overlay import-boundary checker plus a_1 macro observer before movement",
            "do_not_execute_boundary_provider_or_cache",
        ),
        surface_entry(
            "hydrology provider descriptor",
            "HYDROLOGY_SPECS in taichi_global_bathymetry.py:4289 / d90b645:2875",
            "category_a_descriptor_policy_ledger",
            True,
            "static descriptor data can be represented separately from hydrology loader execution",
            "vector overlay import-boundary checker plus a_1 macro observer before movement",
            "do_not_execute_hydrology_provider_or_cache",
        ),
        surface_entry(
            "vector overlay descriptor builder",
            "future descriptor-only surface derived from vector fixture gates",
            "category_a_descriptor_policy_ledger",
            True,
            "descriptor builders can assemble dict/list/scalar contracts without renderer or provider calls",
            "fixture parity for descriptor schema and import-boundary checker",
            "do_not_instantiate_GeoVectorLineOverlay",
        ),
        surface_entry(
            "vector dirty/reload ledger",
            "dirty/reload fixture gate and controller flags in taichi_global_bathymetry.py",
            "category_a_descriptor_policy_ledger",
            True,
            "ledger descriptors can record state transitions without mutating controller flags",
            "dirty/reload fixture plus import-boundary checker",
            "do_not_mutate_controller_dirty_or_reload_state",
        ),
        surface_entry(
            "vector controller registry descriptor",
            "controller registry fixture gate and controller overlay registries",
            "category_a_descriptor_policy_ledger",
            True,
            "registry can be represented as data descriptors while controller mutation remains excluded",
            "controller registry fixture and a_1 macro observer before movement",
            "do_not_import_or_instantiate_controller",
        ),
        surface_entry(
            "vector projection policy label",
            "projection labels from coordinate and sync fixture gates",
            "category_a_descriptor_policy_ledger",
            True,
            "policy labels are data only and do not contain projection formulas",
            "string-label allowance plus formula exclusion tests",
            "do_not_move_or_rewrite_projection_formula",
        ),
        surface_entry(
            "vector mask policy label",
            "mask labels from coordinate and sync fixture gates",
            "category_a_descriptor_policy_ledger",
            True,
            "mask policy labels are data only while clipping formula remains in current runtime surface",
            "string-label allowance plus formula exclusion tests",
            "do_not_move_or_rewrite_mask_clipping_formula",
        ),
        surface_entry(
            "provider cache status label",
            "provider boundary and dirty/reload fixture gates",
            "category_a_descriptor_policy_ledger",
            True,
            "cache hit/miss can remain a descriptor label when no cache lifecycle is executed",
            "checker must allow string labels but block executable cache references",
            "do_not_read_or_write_provider_cache",
        ),
        surface_entry(
            "actual provider/cache loader",
            "_load_hydrology_overlays/_load_boundary_overlays and provider specs",
            "category_b_provider_cache_contract",
            False,
            "loader execution reads provider/cache state and constructs runtime overlays",
            "provider/cache contract gate and separate loader boundary before any movement",
            "do_not_include_loader_execution_in_first_cut",
        ),
        surface_entry(
            "projection formula",
            "GeoVectorLineOverlay.render and point projection helpers",
            "category_c_projection_mask_consumer",
            False,
            "projection behavior is formula-bearing and tied to camera/flip state",
            "projection/mask ablation follow-up before movement",
            "do_not_change_projection_or_flip_formula",
        ),
        surface_entry(
            "mask clipping formula",
            "mask_overlay_to_globe in taichi_global_bathymetry.py:2068 / d90b645:2133",
            "category_c_projection_mask_consumer",
            False,
            "mask clipping changes pixel alpha behavior and must stay out of descriptor planning",
            "projection/mask ablation follow-up before movement",
            "do_not_change_mask_or_alpha_behavior",
        ),
        surface_entry(
            "controller dirty flag mutation",
            "overlay_dirty/hydrology_dirty/boundary_dirty assignments in controller methods",
            "category_d_controller_registry_mutation",
            False,
            "mutation changes controller state and cannot be moved as descriptor-only content",
            "controller mutation seam map before movement",
            "do_not_mutate_or_move_controller_flags",
        ),
        surface_entry(
            "controller reload request mutation",
            "reload_hydrology_layer/reload_boundary_layer controller methods",
            "category_d_controller_registry_mutation",
            False,
            "reload request mutates args, dirty flags, and provider references",
            "controller reload seam map before movement",
            "do_not_move_reload_methods_or_provider_refresh",
        ),
        surface_entry(
            "alpha/apply/composition hot path",
            "alpha helpers and build_layer_render_plan_apply_path/apply_layer_render_plan_composition",
            "category_f_hot_path_blocked",
            False,
            "pixel composition and apply path are outside vector descriptor ownership",
            "separate hot-path parity and o_1 review",
            "do_not_touch_alpha_apply_or_composition_path",
        ),
        surface_entry(
            "metadata/artifact writer",
            "render_core.metadata/render_core.preview imports and monolith writer calls",
            "category_f_hot_path_blocked",
            False,
            "writer behavior affects output schema/artifacts and is not a vector overlay descriptor surface",
            "metadata/output boundary review if ever needed",
            "do_not_execute_or_move_metadata_artifact_writers",
        ),
    ]
    first_cut_decision = {
        "first_cut_surface": "category_a_descriptor_policy_ledger",
        "first_cut_target_candidate": r"render_core\vector_overlay_boundary.py",
        "first_cut_allowed_content": [
            "descriptor builders",
            "policy tables",
            "dirty-reload ledger descriptors",
            "provider ref descriptors as data",
        ],
        "first_cut_forbidden_content": [
            "GeoVectorLineOverlay runtime class",
            "provider execution",
            "projection formula",
            "mask formula",
            "controller mutation",
            "cache reads",
        ],
        "requires_a1_macro_observer_before_source_movement": True,
        "source_movement_authorized": False,
    }
    decision_output = {
        "geovectorlineoverlay_first_cut": "no",
        "descriptor_policy_ledger_first_cut": "yes_preimplementation_only",
        "provider_cache_contract_same_cut": "no_data_descriptors_only",
        "projection_mask_formula_same_cut": "no",
        "import_boundary_checker_adequacy": "yes_for_descriptor_candidate_no_for_runtime_class",
        "requires_a1_macro_observer": True,
        "recommended_next_gate": "vector_overlay_boundary_minimal_extraction_planning_gate",
        "source_movement_authorized": False,
    }
    return {
        "test_shape": "pure_descriptor_mapping_matrix_string_labels_only",
        "surface_categories": sorted(SURFACE_CATEGORIES),
        "surface_matrix": matrix,
        "first_cut_decision": first_cut_decision,
        "decision_output": decision_output,
        "runtime_render_invoked": False,
        "production_source_changed": False,
    }


class VectorOverlaySourceSurfaceMovementPreimplementationGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_source_surface_movement_packet()

    def test_surface_matrix_schema_and_categories_are_pinned(self):
        self.assertEqual(set(self.packet["surface_categories"]), SURFACE_CATEGORIES)
        for entry in self.packet["surface_matrix"]:
            self.assertEqual(set(entry), SURFACE_ENTRY_KEYS)
            self.assertIn(entry["movement_category"], SURFACE_CATEGORIES)
            self.assertIsInstance(entry["candidate_for_first_cut"], bool)

    def test_required_surfaces_are_all_classified(self):
        surfaces = {entry["symbol_or_surface"] for entry in self.packet["surface_matrix"]}
        self.assertEqual(surfaces, REQUIRED_SURFACES)

    def test_first_cut_decision_is_descriptor_policy_ledger_only(self):
        decision = self.packet["first_cut_decision"]
        self.assertEqual(decision["first_cut_surface"], "category_a_descriptor_policy_ledger")
        self.assertEqual(decision["first_cut_target_candidate"], r"render_core\vector_overlay_boundary.py")
        self.assertEqual(
            decision["first_cut_allowed_content"],
            [
                "descriptor builders",
                "policy tables",
                "dirty-reload ledger descriptors",
                "provider ref descriptors as data",
            ],
        )
        self.assertEqual(
            decision["first_cut_forbidden_content"],
            [
                "GeoVectorLineOverlay runtime class",
                "provider execution",
                "projection formula",
                "mask formula",
                "controller mutation",
                "cache reads",
            ],
        )
        self.assertTrue(decision["requires_a1_macro_observer_before_source_movement"])
        self.assertFalse(decision["source_movement_authorized"])

    def test_runtime_class_and_hot_paths_are_not_first_cut_candidates(self):
        matrix = {entry["symbol_or_surface"]: entry for entry in self.packet["surface_matrix"]}
        self.assertFalse(matrix["GeoVectorLineOverlay"]["candidate_for_first_cut"])
        self.assertEqual(matrix["GeoVectorLineOverlay"]["movement_category"], "category_e_runtime_overlay_class")
        for surface in [
            "actual provider/cache loader",
            "projection formula",
            "mask clipping formula",
            "controller dirty flag mutation",
            "controller reload request mutation",
            "alpha/apply/composition hot path",
            "metadata/artifact writer",
        ]:
            self.assertFalse(matrix[surface]["candidate_for_first_cut"], surface)

    def test_descriptor_policy_ledger_surfaces_are_preimplementation_candidates(self):
        matrix = {entry["symbol_or_surface"]: entry for entry in self.packet["surface_matrix"]}
        for surface in [
            "borders provider descriptor",
            "hydrology provider descriptor",
            "vector overlay descriptor builder",
            "vector dirty/reload ledger",
            "vector controller registry descriptor",
            "vector projection policy label",
            "vector mask policy label",
            "provider cache status label",
        ]:
            self.assertTrue(matrix[surface]["candidate_for_first_cut"], surface)
            self.assertEqual(matrix[surface]["movement_category"], "category_a_descriptor_policy_ledger")

    def test_required_decision_answers_are_pinned(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["geovectorlineoverlay_first_cut"], "no")
        self.assertEqual(decision["descriptor_policy_ledger_first_cut"], "yes_preimplementation_only")
        self.assertEqual(decision["provider_cache_contract_same_cut"], "no_data_descriptors_only")
        self.assertEqual(decision["projection_mask_formula_same_cut"], "no")
        self.assertEqual(
            decision["import_boundary_checker_adequacy"],
            "yes_for_descriptor_candidate_no_for_runtime_class",
        )
        self.assertTrue(decision["requires_a1_macro_observer"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "vector_overlay_boundary_minimal_extraction_planning_gate",
        )
        self.assertFalse(decision["source_movement_authorized"])

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        self.assertEqual(self.packet["test_shape"], "pure_descriptor_mapping_matrix_string_labels_only")
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["production_source_changed"])
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
