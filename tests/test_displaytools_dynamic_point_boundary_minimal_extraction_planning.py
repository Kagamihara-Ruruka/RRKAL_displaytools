import unittest


PLANNING_PACKET_KEYS = {
    "schema",
    "target_candidate",
    "helper_module_creation_authorized",
    "source_movement_authorized",
    "dynamic_point_planning_candidate",
    "dynamic_point_extraction_candidate",
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
    "sql_live_source_execution_allowed",
    "dataframe_runtime_allowed",
    "projection_formula_allowed",
    "controller_selection_runtime_allowed",
    "renderer_runtime_allowed",
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
    "build_dynamic_point_source_descriptor",
    "build_dynamic_point_payload_shape_descriptor",
    "build_dynamic_point_replay_live_lineage_descriptor",
    "build_dynamic_point_selection_label_descriptor",
    "build_dynamic_point_render_policy_label_descriptor",
    "build_dynamic_point_safety_ledger_descriptor",
    "build_dynamic_point_known_fault_ledger_descriptor",
    "dynamic_point_boundary_descriptor",
    "dynamic_point_planning_bundle",
}


REQUIRED_BLOCKED = {
    "SQL / MySQL / pymysql / sqlalchemy / replay query",
    "WebSocket / live AIS / live ADS-B",
    "real AIS / ADS-B / cache / DB reads",
    "pandas / datashader / numpy runtime",
    "projection / flip / mask formula",
    "controller selection / picker / hit-test mutation",
    "renderer / Qt / VisPy / Taichi runtime",
    "metadata/artifact writers",
    "alpha/apply/composition hot path",
}


REQUIRED_FIXTURE_PARITY = [
    "exact key-set parity for descriptor builders",
    "deterministic repeat-call parity",
    "source descriptor branch",
    "point payload shape descriptor branch",
    "replay/live lineage descriptor branch",
    "selection label descriptor branch",
    "render policy label descriptor branch",
    "safety ledger blocked-source branch",
    "known fault unresolved ledger branch",
    "future import-boundary checker missing target pass",
    "future forbidden SQL/live/dataframe/projection/controller/runtime dependency fail",
]


FORBIDDEN_MARKERS = {
    "safe_to_extract",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_ready",
    "runtime_merge_enabled",
    "live_data_restored",
    "source_movement_authorized_true",
    "helper_module_creation_authorized_true",
    "dynamic_point_extraction_candidate_true",
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
        "sql_live_source_execution_allowed": False,
        "dataframe_runtime_allowed": False,
        "projection_formula_allowed": False,
        "controller_selection_runtime_allowed": False,
        "renderer_runtime_allowed": False,
        "candidate_for_minimal_extraction": True,
        "required_fixture": required_fixture,
        "required_checker": "future_validate_displaytools_dynamic_point_import_boundary.py",
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


def build_dynamic_point_boundary_minimal_extraction_planning_packet():
    candidate_symbols = [
        candidate_entry(
            "build_dynamic_point_source_descriptor",
            "dynamic point boundary source descriptor and source-surface source labels",
            "future descriptor-only surface",
            "build_dynamic_point_source_descriptor",
            "source descriptor exact key-set and repeat-call parity",
            "do_not_execute_sql_websocket_live_or_cache_source",
        ),
        candidate_entry(
            "build_dynamic_point_payload_shape_descriptor",
            "dynamic point boundary point payload descriptor",
            "future descriptor-only surface",
            "build_dynamic_point_payload_shape_descriptor",
            "payload shape descriptor exact key-set parity",
            "do_not_parse_real_payload_or_import_dataframe_runtime",
        ),
        candidate_entry(
            "build_dynamic_point_replay_live_lineage_descriptor",
            "dynamic point boundary time/replay label descriptor",
            "future ledger descriptor surface",
            "build_dynamic_point_replay_live_lineage_descriptor",
            "replay/live lineage unresolved branch parity",
            "do_not_execute_replay_query_websocket_or_real_clock",
        ),
        candidate_entry(
            "build_dynamic_point_selection_label_descriptor",
            "dynamic point boundary selection descriptor",
            "future label descriptor surface",
            "build_dynamic_point_selection_label_descriptor",
            "selection label-only parity",
            "do_not_mutate_controller_selection_runtime",
        ),
        candidate_entry(
            "build_dynamic_point_render_policy_label_descriptor",
            "dynamic point boundary render policy label descriptor",
            "future label descriptor surface",
            "build_dynamic_point_render_policy_label_descriptor",
            "render policy label-only parity",
            "do_not_execute_datashader_or_renderer_runtime",
        ),
        candidate_entry(
            "build_dynamic_point_safety_ledger_descriptor",
            "dynamic point boundary safety ledger descriptor",
            "future safety ledger descriptor surface",
            "build_dynamic_point_safety_ledger_descriptor",
            "blocked-source safety ledger parity",
            "do_not_execute_sql_websocket_live_datashader_or_runtime_source",
        ),
        candidate_entry(
            "build_dynamic_point_known_fault_ledger_descriptor",
            "dynamic point boundary known fault ledger descriptor",
            "future known fault ledger descriptor surface",
            "build_dynamic_point_known_fault_ledger_descriptor",
            "known fault unresolved ledger parity",
            "do_not_claim_live_data_bug_fix_or_visual_parity",
        ),
        candidate_entry(
            "dynamic_point_boundary_descriptor",
            "optional aggregate descriptor from category A families only",
            "future aggregate descriptor value",
            "dynamic_point_boundary_descriptor",
            "aggregate descriptor exact key-set parity",
            "do_not_include_sql_live_dataframe_projection_controller_or_runtime_behavior",
        ),
        candidate_entry(
            "dynamic_point_planning_bundle",
            "optional planning bundle from category A candidate families only",
            "future planning bundle value",
            "dynamic_point_planning_bundle",
            "bundle key-set and blocked-surface declaration parity",
            "do_not_authorize_source_movement_inside_bundle",
        ),
    ]
    blocked_symbols = [
        blocked_entry(
            "SQL / MySQL / pymysql / sqlalchemy / replay query",
            "sql_replay_database",
            "database replay can connect, query, or depend on DB runtime",
            "SQL replay boundary fixture gate",
            "do_not_connect_database_or_move_replay_query",
        ),
        blocked_entry(
            "WebSocket / live AIS / live ADS-B",
            "live_stream",
            "live stream can connect to network/runtime sources",
            "live-source boundary fixture gate",
            "do_not_open_websocket_or_live_stream",
        ),
        blocked_entry(
            "real AIS / ADS-B / cache / DB reads",
            "real_source_io",
            "real data/cache/DB reads are IO behavior, not descriptor data",
            "source/cache IO boundary gate",
            "do_not_read_real_dynamic_point_source",
        ),
        blocked_entry(
            "pandas / datashader / numpy runtime",
            "runtime_dataframe_projection",
            "dataframe/render-heavy runtime imports can process real payloads",
            "dataframe/datashader runtime boundary gate",
            "do_not_import_dataframe_or_datashader_runtime",
        ),
        blocked_entry(
            "projection / flip / mask formula",
            "projection_formula",
            "coordinate formulas can change point position and visibility",
            "projection/mask diagnostic gate",
            "do_not_change_projection_flip_or_mask_formula",
        ),
        blocked_entry(
            "controller selection / picker / hit-test mutation",
            "controller_selection_runtime",
            "selection, picker, and hit-test behavior mutate or read runtime state",
            "controller selection seam gate",
            "do_not_move_controller_selection_runtime",
        ),
        blocked_entry(
            "renderer / Qt / VisPy / Taichi runtime",
            "renderer_host",
            "renderer/UI/GPU runtime cannot be descriptor-only content",
            "renderer host boundary map",
            "do_not_import_or_execute_renderer_runtime",
        ),
        blocked_entry(
            "metadata/artifact writers",
            "metadata_artifact_writer",
            "writer behavior changes output/artifacts",
            "metadata/output boundary gate",
            "do_not_execute_or_move_writers",
        ),
        blocked_entry(
            "alpha/apply/composition hot path",
            "hot_path_blocked",
            "composition hot path is outside dynamic point descriptor planning",
            "alpha/apply hot-path gate",
            "do_not_touch_alpha_apply_composition",
        ),
    ]
    return {
        "schema": "rrkal_displaytools.dynamic_point_boundary_minimal_extraction_planning.v1",
        "target_candidate": r"render_core\dynamic_point_boundary.py",
        "helper_module_creation_authorized": False,
        "source_movement_authorized": False,
        "dynamic_point_planning_candidate": True,
        "dynamic_point_extraction_candidate": False,
        "a1_macro_observer_required_before_source_movement": True,
        "candidate_symbols": candidate_symbols,
        "blocked_symbols": blocked_symbols,
        "fixture_parity_plan": list(REQUIRED_FIXTURE_PARITY),
        "import_boundary_checker_need": {
            "required_before_extraction": True,
            "required_now": False,
            "reason": "planning_only_no_helper_target_created_in_this_slice",
            "future_checker_target": r"render_core\dynamic_point_boundary.py",
            "target_missing_now": True,
        },
        "decision_output": {
            "next_can_be_actual_extraction": "not_yet_only_after_a1_macro_observer_and_o1_review",
            "first_cut_minimal_scope": "descriptor_policy_ledger_only",
            "candidate_categories": ["category_a_descriptor_policy_ledger"],
            "blocked_categories": [
                "category_b_sql_replay_database",
                "category_c_live_stream",
                "category_d_runtime_dataframe_projection",
                "category_e_controller_selection_runtime",
                "category_f_renderer_host",
            ],
        },
        "next_gate": "dynamic_point_import_boundary_checker_gate",
        "boundary_statement": (
            "Docs/test-only AIS/aircraft dynamic point boundary minimal extraction planning gate. "
            "No helper module creation, no source movement, no production source change, no monolith import, "
            "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask formula change, "
            "no controller selection runtime change, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/bug-fix claim."
        ),
    }


class DynamicPointBoundaryMinimalExtractionPlanningGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_boundary_minimal_extraction_planning_packet()

    def test_planning_packet_top_level_contract_is_pinned(self):
        self.assertEqual(set(self.packet), PLANNING_PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal_displaytools.dynamic_point_boundary_minimal_extraction_planning.v1",
        )
        self.assertEqual(self.packet["target_candidate"], r"render_core\dynamic_point_boundary.py")
        self.assertFalse(self.packet["helper_module_creation_authorized"])
        self.assertFalse(self.packet["source_movement_authorized"])
        self.assertTrue(self.packet["dynamic_point_planning_candidate"])
        self.assertFalse(self.packet["dynamic_point_extraction_candidate"])
        self.assertTrue(self.packet["a1_macro_observer_required_before_source_movement"])

    def test_candidate_symbols_are_descriptor_policy_ledger_only(self):
        names = {entry["candidate_name"] for entry in self.packet["candidate_symbols"]}
        self.assertEqual(names, REQUIRED_CANDIDATES)
        for entry in self.packet["candidate_symbols"]:
            self.assertEqual(set(entry), CANDIDATE_ENTRY_KEYS)
            self.assertEqual(entry["movement_category"], "category_a_descriptor_policy_ledger")
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertFalse(entry["sql_live_source_execution_allowed"])
            self.assertFalse(entry["dataframe_runtime_allowed"])
            self.assertFalse(entry["projection_formula_allowed"])
            self.assertFalse(entry["controller_selection_runtime_allowed"])
            self.assertFalse(entry["renderer_runtime_allowed"])
            self.assertTrue(entry["candidate_for_minimal_extraction"])

    def test_blocked_surfaces_are_not_extraction_candidates(self):
        names = {entry["blocked_name"] for entry in self.packet["blocked_symbols"]}
        self.assertEqual(names, REQUIRED_BLOCKED)
        for entry in self.packet["blocked_symbols"]:
            self.assertEqual(set(entry), BLOCKED_ENTRY_KEYS)
            self.assertFalse(entry["candidate_for_minimal_extraction"])

    def test_fixture_parity_plan_is_complete_and_ordered(self):
        self.assertEqual(self.packet["fixture_parity_plan"], REQUIRED_FIXTURE_PARITY)

    def test_import_boundary_checker_need_is_pinned(self):
        need = self.packet["import_boundary_checker_need"]
        self.assertTrue(need["required_before_extraction"])
        self.assertFalse(need["required_now"])
        self.assertEqual(need["future_checker_target"], r"render_core\dynamic_point_boundary.py")
        self.assertTrue(need["target_missing_now"])

    def test_a1_and_decision_output_block_source_movement(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["next_can_be_actual_extraction"], "not_yet_only_after_a1_macro_observer_and_o1_review")
        self.assertEqual(decision["first_cut_minimal_scope"], "descriptor_policy_ledger_only")
        self.assertEqual(decision["candidate_categories"], ["category_a_descriptor_policy_ledger"])
        self.assertEqual(
            decision["blocked_categories"],
            [
                "category_b_sql_replay_database",
                "category_c_live_stream",
                "category_d_runtime_dataframe_projection",
                "category_e_controller_selection_runtime",
                "category_f_renderer_host",
            ],
        )
        self.assertEqual(self.packet["next_gate"], "dynamic_point_import_boundary_checker_gate")

    def test_no_live_data_runtime_or_readiness_claims_are_introduced(self):
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_MARKERS:
            self.assertNotIn(marker, packet_text)
        boundary = self.packet["boundary_statement"].lower()
        self.assertIn("no helper module creation", boundary)
        self.assertIn("no live-data", boundary)


if __name__ == "__main__":
    unittest.main()
