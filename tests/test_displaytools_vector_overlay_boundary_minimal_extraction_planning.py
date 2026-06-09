import unittest


PLANNING_PACKET_KEYS = {
    "schema",
    "target_candidate",
    "source_movement_authorized",
    "requires_a1_macro_observer_before_source_movement",
    "candidate_symbols",
    "blocked_symbols",
    "fixture_parity_plan",
    "import_boundary_expectation",
    "a1_macro_observer_questions",
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
    "runtime_dependency_allowed",
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
}


REQUIRED_CANDIDATES = {
    "boundary specs descriptor",
    "hydrology specs descriptor",
    "vector overlay descriptor builder",
    "vector provider ref descriptor builder",
    "vector dirty reload ledger descriptor",
    "vector controller registry descriptor",
    "vector projection policy label descriptor",
    "vector mask policy label descriptor",
    "vector cache status label descriptor",
}


REQUIRED_BLOCKED = {
    "GeoVectorLineOverlay",
    "actual provider/cache loader",
    "projection formula",
    "mask clipping formula",
    "controller dirty flag mutation",
    "controller reload request mutation",
    "alpha/apply/composition hot path",
    "metadata/artifact writer",
    "SQL/WebSocket/AIS live path",
    "Qt/VisPy/Taichi runtime host",
}


REQUIRED_FIXTURE_PARITY = [
    "exact key-set parity for descriptor builders",
    "deterministic repeat-call parity",
    "empty provider descriptor branch",
    "malformed provider descriptor branch",
    "dirty/reload ledger clean branch",
    "dirty/reload ledger reload branch",
    "projection/mask label-only branch",
    "cache status label-only branch",
    "string-label allowance branch",
    "import-boundary checker candidate pass",
    "negative forbidden dependency fail",
]


def candidate_entry(
    candidate_name,
    source_evidence,
    source_owner,
    planned_target_name,
    allowed_content_kind,
    required_fixture,
    forbidden_next_action,
):
    return {
        "candidate_name": candidate_name,
        "source_evidence": source_evidence,
        "source_owner": source_owner,
        "planned_target_name": planned_target_name,
        "allowed_content_kind": allowed_content_kind,
        "runtime_dependency_allowed": False,
        "candidate_for_minimal_extraction": True,
        "required_fixture": required_fixture,
        "required_checker": "validate_displaytools_vector_overlay_import_boundary.py",
        "forbidden_next_action": forbidden_next_action,
    }


def blocked_entry(blocked_name, blocked_category, reason, required_future_gate, forbidden_next_action):
    return {
        "blocked_name": blocked_name,
        "blocked_category": blocked_category,
        "reason": reason,
        "required_future_gate": required_future_gate,
        "forbidden_next_action": forbidden_next_action,
    }


def build_vector_overlay_boundary_minimal_extraction_planning_packet():
    candidate_symbols = [
        candidate_entry(
            "boundary specs descriptor",
            "BOUNDARY_SPECS static source anchor and source-surface movement gate",
            "taichi_global_bathymetry.py descriptor value",
            "BOUNDARY_PROVIDER_DESCRIPTOR_TABLE",
            "static descriptor table as data only",
            "boundary descriptor exact key-set and empty/malformed descriptor branches",
            "do_not_execute_boundary_provider_or_cache",
        ),
        candidate_entry(
            "hydrology specs descriptor",
            "HYDROLOGY_SPECS static source anchor and source-surface movement gate",
            "taichi_global_bathymetry.py descriptor value",
            "HYDROLOGY_PROVIDER_DESCRIPTOR_TABLE",
            "static descriptor table as data only",
            "hydrology descriptor exact key-set and empty/malformed descriptor branches",
            "do_not_execute_hydrology_provider_or_cache",
        ),
        candidate_entry(
            "vector overlay descriptor builder",
            "coordinate sync and source-surface movement gates",
            "future descriptor-only builder surface",
            "build_vector_overlay_descriptor",
            "dict/list/scalar descriptor builder",
            "descriptor builder exact key-set and deterministic repeat-call parity",
            "do_not_instantiate_GeoVectorLineOverlay",
        ),
        candidate_entry(
            "vector provider ref descriptor builder",
            "provider boundary fixture gate",
            "provider reference descriptor surface",
            "build_vector_provider_ref_descriptor",
            "provider reference descriptor as data only",
            "provider present/missing and cache label-only branches",
            "do_not_call_provider_loader_or_read_cache",
        ),
        candidate_entry(
            "vector dirty reload ledger descriptor",
            "dirty/reload fixture gate",
            "dirty/reload ledger descriptor surface",
            "build_vector_dirty_reload_ledger_descriptor",
            "dirty/reload ledger descriptor as data only",
            "clean branch and reload branch parity",
            "do_not_mutate_controller_dirty_or_reload_flags",
        ),
        candidate_entry(
            "vector controller registry descriptor",
            "controller registry fixture gate",
            "controller registry descriptor surface",
            "build_vector_controller_registry_descriptor",
            "controller registry descriptor as data only",
            "registry present/missing and consumer ref descriptor parity",
            "do_not_import_or_instantiate_controller",
        ),
        candidate_entry(
            "vector projection policy label descriptor",
            "coordinate fixture and vector coordinate sync gates",
            "projection label descriptor surface",
            "build_vector_projection_policy_label_descriptor",
            "projection policy label only",
            "projection label-only branch parity",
            "do_not_move_or_rewrite_projection_formula",
        ),
        candidate_entry(
            "vector mask policy label descriptor",
            "coordinate fixture and vector coordinate sync gates",
            "mask label descriptor surface",
            "build_vector_mask_policy_label_descriptor",
            "mask policy label only",
            "mask label-only branch parity",
            "do_not_move_or_rewrite_mask_formula",
        ),
        candidate_entry(
            "vector cache status label descriptor",
            "provider boundary and dirty/reload fixture gates",
            "cache status label descriptor surface",
            "build_vector_cache_status_label_descriptor",
            "cache status label only",
            "cache hit/miss string-label branch parity",
            "do_not_read_or_write_cache",
        ),
    ]
    blocked_symbols = [
        blocked_entry(
            "GeoVectorLineOverlay",
            "runtime_overlay_class",
            "runtime class consumes camera, flip flags, mask, image drawing, and screen-space rendering state",
            "runtime overlay parity and controller seam gate",
            "do_not_list_as_extraction_candidate",
        ),
        blocked_entry(
            "actual provider/cache loader",
            "provider_cache_runtime",
            "loader execution reads provider/cache state and constructs runtime overlays",
            "provider/cache loader boundary gate",
            "do_not_execute_or_move_loader",
        ),
        blocked_entry(
            "projection formula",
            "projection_mask_formula",
            "formula-bearing projection depends on camera and flip state",
            "projection/mask ablation follow-up gate",
            "do_not_change_projection_or_flip_formula",
        ),
        blocked_entry(
            "mask clipping formula",
            "projection_mask_formula",
            "mask clipping changes alpha/pixel behavior",
            "projection/mask ablation follow-up gate",
            "do_not_change_mask_clipping_or_alpha_behavior",
        ),
        blocked_entry(
            "controller dirty flag mutation",
            "controller_registry_mutation",
            "dirty flag assignment changes controller state",
            "controller mutation seam gate",
            "do_not_move_or_mutate_controller_dirty_flags",
        ),
        blocked_entry(
            "controller reload request mutation",
            "controller_registry_mutation",
            "reload mutates args, dirty flags, and provider references",
            "controller reload seam gate",
            "do_not_move_reload_methods",
        ),
        blocked_entry(
            "alpha/apply/composition hot path",
            "hot_path_blocked",
            "pixel composition and render-plan apply path are outside vector boundary descriptors",
            "separate alpha/apply hot-path parity gate",
            "do_not_touch_alpha_apply_or_composition_path",
        ),
        blocked_entry(
            "metadata/artifact writer",
            "metadata_artifact_writer",
            "writer behavior affects output schema or artifacts",
            "metadata/output boundary gate",
            "do_not_execute_or_move_writers",
        ),
        blocked_entry(
            "SQL/WebSocket/AIS live path",
            "live_io_runtime",
            "live data and SQL/WebSocket access are outside vector overlay descriptor planning",
            "live-source boundary gate",
            "do_not_connect_sql_websocket_or_ais_live",
        ),
        blocked_entry(
            "Qt/VisPy/Taichi runtime host",
            "runtime_ui_gpu",
            "UI/GPU/runtime hosts are explicitly forbidden by the checker and planning boundary",
            "runtime host boundary review",
            "do_not_import_or_execute_runtime_hosts",
        ),
    ]
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary_minimal_extraction_planning.v1",
        "target_candidate": r"render_core\vector_overlay_boundary.py",
        "source_movement_authorized": False,
        "requires_a1_macro_observer_before_source_movement": True,
        "candidate_symbols": candidate_symbols,
        "blocked_symbols": blocked_symbols,
        "fixture_parity_plan": list(REQUIRED_FIXTURE_PARITY),
        "import_boundary_expectation": {
            "target_missing_now": True,
            "expected_checker_status_now": "not_applicable_candidate_missing",
            "expected_checker_after_descriptor_only_candidate": "pass",
            "expected_checker_after_runtime_dependency": "fail",
        },
        "a1_macro_observer_questions": [
            "are_candidates_still_one_descriptor_policy_ledger_craton",
            "did_runtime_class_provider_loader_projection_or_mask_formula_leak_in",
            "would_plan_break_historical_view_cone_vector_overlay_boundary",
            "is_there_a_better_first_cut_candidate",
            "is_more_horizontal_or_historical_evidence_needed",
        ],
        "decision_output": {
            "next_can_be_actual_extraction": "not_yet_only_after_o1_a1_review_of_this_planning_gate",
            "needs_a1_before_movement": True,
            "source_movement_authorized": False,
            "first_cut_minimal_scope": "descriptor_policy_ledger_only",
            "import_boundary_checker_adequacy": "yes_for_descriptor_only_candidate_no_for_runtime_surfaces",
        },
        "next_gate": "vector_overlay_boundary_minimal_extraction_gate_after_a1_macro_review",
        "boundary_statement": (
            "Docs/test-only vector overlay boundary minimal extraction planning gate. "
            "No helper module creation, no source movement, no production source change, "
            "no controller/provider/cache runtime, no real GeoJSON/cache read, no runtime execution, "
            "no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, "
            "no artifact writer execution, no metadata/output schema change, no runtime merge enablement, "
            "and no safe-to-extract/visual/performance/readiness/bug-fix claim."
        ),
    }


class VectorOverlayBoundaryMinimalExtractionPlanningGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_boundary_minimal_extraction_planning_packet()

    def test_planning_packet_top_level_schema_is_pinned(self):
        self.assertEqual(set(self.packet), PLANNING_PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal_displaytools.vector_overlay_boundary_minimal_extraction_planning.v1",
        )
        self.assertEqual(self.packet["target_candidate"], r"render_core\vector_overlay_boundary.py")
        self.assertFalse(self.packet["source_movement_authorized"])
        self.assertTrue(self.packet["requires_a1_macro_observer_before_source_movement"])

    def test_candidate_symbols_are_descriptor_policy_ledger_only(self):
        names = {entry["candidate_name"] for entry in self.packet["candidate_symbols"]}
        self.assertEqual(names, REQUIRED_CANDIDATES)
        for entry in self.packet["candidate_symbols"]:
            self.assertEqual(set(entry), CANDIDATE_ENTRY_KEYS)
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertTrue(entry["candidate_for_minimal_extraction"])
            self.assertEqual(entry["required_checker"], "validate_displaytools_vector_overlay_import_boundary.py")

    def test_blocked_symbols_are_explicitly_not_extraction_candidates(self):
        names = {entry["blocked_name"] for entry in self.packet["blocked_symbols"]}
        self.assertEqual(names, REQUIRED_BLOCKED)
        for entry in self.packet["blocked_symbols"]:
            self.assertEqual(set(entry), BLOCKED_ENTRY_KEYS)
        blocked_text = repr(self.packet["blocked_symbols"])
        for blocked_name in REQUIRED_BLOCKED:
            self.assertIn(blocked_name, blocked_text)

    def test_fixture_parity_plan_is_complete_and_ordered(self):
        self.assertEqual(self.packet["fixture_parity_plan"], REQUIRED_FIXTURE_PARITY)

    def test_import_boundary_expectation_is_pinned(self):
        expectation = self.packet["import_boundary_expectation"]
        self.assertTrue(expectation["target_missing_now"])
        self.assertEqual(expectation["expected_checker_status_now"], "not_applicable_candidate_missing")
        self.assertEqual(expectation["expected_checker_after_descriptor_only_candidate"], "pass")
        self.assertEqual(expectation["expected_checker_after_runtime_dependency"], "fail")

    def test_a1_macro_observer_questions_are_defined(self):
        self.assertEqual(
            self.packet["a1_macro_observer_questions"],
            [
                "are_candidates_still_one_descriptor_policy_ledger_craton",
                "did_runtime_class_provider_loader_projection_or_mask_formula_leak_in",
                "would_plan_break_historical_view_cone_vector_overlay_boundary",
                "is_there_a_better_first_cut_candidate",
                "is_more_horizontal_or_historical_evidence_needed",
            ],
        )

    def test_decision_output_blocks_immediate_extraction(self):
        decision = self.packet["decision_output"]
        self.assertEqual(
            decision["next_can_be_actual_extraction"],
            "not_yet_only_after_o1_a1_review_of_this_planning_gate",
        )
        self.assertTrue(decision["needs_a1_before_movement"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertEqual(decision["first_cut_minimal_scope"], "descriptor_policy_ledger_only")
        self.assertEqual(
            decision["import_boundary_checker_adequacy"],
            "yes_for_descriptor_only_candidate_no_for_runtime_surfaces",
        )
        self.assertEqual(
            self.packet["next_gate"],
            "vector_overlay_boundary_minimal_extraction_gate_after_a1_macro_review",
        )

    def test_no_forbidden_runtime_or_readiness_claim_is_introduced(self):
        packet_text = repr(self.packet)
        self.assertNotIn("GeoVectorLineOverlay runtime class candidate", packet_text)
        self.assertNotIn("provider execution candidate", packet_text)
        self.assertNotIn("projection formula candidate", packet_text)
        self.assertNotIn("mask formula candidate", packet_text)
        self.assertNotIn("source_movement_authorized': True", packet_text)
        self.assertIn("no safe-to-extract", self.packet["boundary_statement"])


if __name__ == "__main__":
    unittest.main()
