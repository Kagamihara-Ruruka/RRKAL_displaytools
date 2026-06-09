import unittest


SURFACE_CATEGORIES = {
    "category_a_descriptor_policy_ledger",
    "category_b_sql_replay_database",
    "category_c_live_stream",
    "category_d_runtime_dataframe_projection",
    "category_e_controller_selection_runtime",
    "category_f_renderer_host",
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
    "source labels",
    "point payload shape labels",
    "replay/live lineage labels",
    "selection labels",
    "render cap/adaptive sampling labels",
    "known fault ledger",
}


BLOCKED_SURFACES = {
    "MySQL replay database",
    "pymysql dependency",
    "sqlalchemy dependency",
    "DB URL / replay query",
    "WebSocket live source",
    "live AIS stream",
    "ADS-B stream",
    "pandas runtime dataframe",
    "datashader runtime",
    "numpy runtime arrays",
    "projection formula",
    "flip formula",
    "mask formula",
    "selected vehicle mutation",
    "picker / hit-test mutation",
    "controller selection runtime",
    "Qt host",
    "VisPy host",
    "Taichi renderer host",
    "renderer GUI runtime",
}


FORBIDDEN_CLAIM_MARKERS = {
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


def build_dynamic_point_source_surface_movement_packet():
    matrix = [
        surface_entry(
            "source labels",
            "dynamic point boundary source descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "AIS, ADS-B, replay, synthetic, and unavailable states can be represented as source labels",
            "boundary fixture exact key-set parity before planning",
            "do_not_execute_sql_websocket_live_or_cache_source",
        ),
        surface_entry(
            "point payload shape labels",
            "dynamic point boundary point payload descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "lat/lon/speed/heading/timestamp/id names can be descriptor data",
            "payload shape fixture and no parser/runtime import guard",
            "do_not_parse_real_payload_or_import_dataframe_runtime",
        ),
        surface_entry(
            "replay/live lineage labels",
            "dynamic point boundary time/replay descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "static replay and live lineage can be unresolved labels without executing sources",
            "lineage ledger fixture with unresolved status",
            "do_not_execute_replay_query_websocket_or_real_clock",
        ),
        surface_entry(
            "selection labels",
            "dynamic point boundary selection descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "selected vehicle, selected layer, and hit false can be labels while controller mutation is blocked",
            "selection label fixture and controller mutation blocker",
            "do_not_mutate_controller_selection_runtime",
        ),
        surface_entry(
            "render cap/adaptive sampling labels",
            "dynamic point boundary render policy label descriptor",
            "category_a_descriptor_policy_ledger",
            True,
            "visible/rendered count, cap, and adaptive sampling can be policy labels only",
            "render policy label fixture and datashader runtime blocker",
            "do_not_execute_datashader_or_renderer_runtime",
        ),
        surface_entry(
            "known fault ledger",
            "dynamic point boundary known fault ledger",
            "category_a_descriptor_policy_ledger",
            True,
            "live-vs-replay ambiguity, timestamp staleness, and point/vector sync dependency can be unresolved ledger data",
            "known fault fixture with no fix/readiness claim",
            "do_not_claim_live_data_bug_fix_or_visual_parity",
        ),
        surface_entry(
            "MySQL replay database",
            "monolith dynamic source database/replay lineage",
            "category_b_sql_replay_database",
            False,
            "database replay can execute IO and depends on DB connection state",
            "SQL replay boundary fixture before any movement",
            "do_not_connect_mysql_or_execute_replay_query",
        ),
        surface_entry(
            "pymysql dependency",
            "monolith database dependency family",
            "category_b_sql_replay_database",
            False,
            "pymysql import would bring executable database access",
            "SQL import-boundary checker later",
            "do_not_import_pymysql",
        ),
        surface_entry(
            "sqlalchemy dependency",
            "database dependency family",
            "category_b_sql_replay_database",
            False,
            "sqlalchemy import would bring executable database access",
            "SQL import-boundary checker later",
            "do_not_import_sqlalchemy",
        ),
        surface_entry(
            "DB URL / replay query",
            "database replay configuration and query surface",
            "category_b_sql_replay_database",
            False,
            "DB URLs and queries are connection/runtime behavior, not descriptor first cut",
            "database config boundary gate",
            "do_not_move_db_url_or_replay_query_behavior",
        ),
        surface_entry(
            "WebSocket live source",
            "live source lineage",
            "category_c_live_stream",
            False,
            "WebSocket live source can connect to network/runtime stream",
            "live-source boundary gate before implementation",
            "do_not_open_websocket_or_live_source",
        ),
        surface_entry(
            "live AIS stream",
            "AIS live lineage",
            "category_c_live_stream",
            False,
            "live AIS stream is runtime/network behavior",
            "AIS live-source diagnostic gate",
            "do_not_execute_live_ais_stream",
        ),
        surface_entry(
            "ADS-B stream",
            "aircraft live lineage",
            "category_c_live_stream",
            False,
            "ADS-B live stream is runtime/network behavior",
            "ADS-B live-source diagnostic gate",
            "do_not_execute_adsb_stream",
        ),
        surface_entry(
            "pandas runtime dataframe",
            "dynamic point dataframe processing family",
            "category_d_runtime_dataframe_projection",
            False,
            "runtime dataframe processing can parse or transform real payloads",
            "dataframe parser/normalizer gate only",
            "do_not_import_pandas_or_process_real_dataframe",
        ),
        surface_entry(
            "datashader runtime",
            "dynamic point render policy and sampling family",
            "category_d_runtime_dataframe_projection",
            False,
            "datashader execution is render-heavy runtime behavior",
            "datashader sampling policy gate before runtime work",
            "do_not_import_or_execute_datashader",
        ),
        surface_entry(
            "numpy runtime arrays",
            "dynamic point array and render payload family",
            "category_d_runtime_dataframe_projection",
            False,
            "numpy arrays are runtime data objects, not descriptor labels",
            "array/runtime boundary gate",
            "do_not_import_numpy_or_create_runtime_arrays",
        ),
        surface_entry(
            "projection formula",
            "coordinate and dynamic point projection surface",
            "category_d_runtime_dataframe_projection",
            False,
            "projection formula changes screen mapping and point/vector sync",
            "projection diagnostic gate",
            "do_not_change_projection_formula",
        ),
        surface_entry(
            "flip formula",
            "coordinate flip dependency",
            "category_d_runtime_dataframe_projection",
            False,
            "flip formula owns coordinate orientation behavior",
            "coordinate formula gate",
            "do_not_change_flip_formula",
        ),
        surface_entry(
            "mask formula",
            "mask/screen RGBA frame dependency",
            "category_d_runtime_dataframe_projection",
            False,
            "mask formula can affect visibility and pixels",
            "projection/mask diagnostic gate",
            "do_not_change_mask_formula",
        ),
        surface_entry(
            "selected vehicle mutation",
            "controller selected vehicle state",
            "category_e_controller_selection_runtime",
            False,
            "selected vehicle mutation changes controller runtime state",
            "controller selection seam gate",
            "do_not_mutate_selected_vehicle",
        ),
        surface_entry(
            "picker / hit-test mutation",
            "controller picker and hit-test runtime",
            "category_e_controller_selection_runtime",
            False,
            "picker and hit-test behavior depends on runtime screen state",
            "hit-test seam gate",
            "do_not_execute_picker_or_hit_test_runtime",
        ),
        surface_entry(
            "controller selection runtime",
            "controller selection behavior",
            "category_e_controller_selection_runtime",
            False,
            "controller selection is runtime mutation rather than descriptor data",
            "controller selection runtime boundary gate",
            "do_not_move_controller_selection_behavior",
        ),
        surface_entry(
            "Qt host",
            "UI host surface",
            "category_f_renderer_host",
            False,
            "Qt host requires UI runtime",
            "UI host seam gate",
            "do_not_import_or_execute_qt",
        ),
        surface_entry(
            "VisPy host",
            "render host surface",
            "category_f_renderer_host",
            False,
            "VisPy host requires render runtime",
            "render host seam gate",
            "do_not_import_or_execute_vispy",
        ),
        surface_entry(
            "Taichi renderer host",
            "renderer host surface",
            "category_f_renderer_host",
            False,
            "Taichi renderer host requires GPU/runtime behavior",
            "renderer host map",
            "do_not_import_or_execute_taichi_renderer",
        ),
        surface_entry(
            "renderer GUI runtime",
            "runtime GUI/render loop",
            "category_f_renderer_host",
            False,
            "renderer GUI runtime cannot be validated in a descriptor-only gate",
            "runtime host diagnostic gate",
            "do_not_execute_renderer_gui_runtime",
        ),
    ]
    decision_output = {
        "dynamic_point_planning_candidate": True,
        "dynamic_point_extraction_candidate": False,
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "import_boundary_checker_required_before_extraction": True,
        "import_boundary_checker_reason": "required_after_descriptor_only_target_is_named_and_before_source_movement",
        "recommended_next_gate": "dynamic_point_boundary_minimal_extraction_planning_gate",
    }
    return {
        "test_shape": "pure_descriptor_mapping_matrix_no_monolith_import_no_runtime_dependency",
        "surface_categories": sorted(SURFACE_CATEGORIES),
        "surface_matrix": matrix,
        "decision_output": decision_output,
        "runtime_render_invoked": False,
        "production_source_changed": False,
        "helper_module_created": False,
        "sql_websocket_live_source_executed": False,
        "real_cache_database_or_network_read": False,
        "dataframe_projection_runtime_imported": False,
        "controller_selection_runtime_changed": False,
    }


class DynamicPointSourceSurfaceMovementPreimplementationGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_source_surface_movement_packet()

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

    def test_sql_replay_and_live_stream_surfaces_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in ["MySQL replay database", "pymysql dependency", "sqlalchemy dependency", "DB URL / replay query"]:
            self.assertEqual(matrix[surface]["movement_category"], "category_b_sql_replay_database")
            self.assertFalse(matrix[surface]["candidate_for_first_cut"])
        for surface in ["WebSocket live source", "live AIS stream", "ADS-B stream"]:
            self.assertEqual(matrix[surface]["movement_category"], "category_c_live_stream")
            self.assertFalse(matrix[surface]["candidate_for_first_cut"])

    def test_dataframe_projection_controller_and_runtime_surfaces_are_blocked(self):
        matrix = {entry["surface_name"]: entry for entry in self.packet["surface_matrix"]}
        for surface in [
            "pandas runtime dataframe",
            "datashader runtime",
            "numpy runtime arrays",
            "projection formula",
            "flip formula",
            "mask formula",
            "selected vehicle mutation",
            "picker / hit-test mutation",
            "controller selection runtime",
            "Qt host",
            "VisPy host",
            "Taichi renderer host",
            "renderer GUI runtime",
        ]:
            self.assertFalse(matrix[surface]["candidate_for_first_cut"], surface)

    def test_required_decision_output_is_pinned(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["dynamic_point_planning_candidate"])
        self.assertFalse(decision["dynamic_point_extraction_candidate"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertTrue(decision["import_boundary_checker_required_before_extraction"])
        self.assertEqual(
            decision["import_boundary_checker_reason"],
            "required_after_descriptor_only_target_is_named_and_before_source_movement",
        )
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_boundary_minimal_extraction_planning_gate",
        )

    def test_no_runtime_or_readiness_claims_are_introduced(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_descriptor_mapping_matrix_no_monolith_import_no_runtime_dependency",
        )
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["production_source_changed"])
        self.assertFalse(self.packet["helper_module_created"])
        self.assertFalse(self.packet["sql_websocket_live_source_executed"])
        self.assertFalse(self.packet["real_cache_database_or_network_read"])
        self.assertFalse(self.packet["dataframe_projection_runtime_imported"])
        self.assertFalse(self.packet["controller_selection_runtime_changed"])
        packet_text = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(marker, packet_text)
        for forbidden in [
            "import taichi_global_bathymetry",
            "import pandas",
            "import datashader",
            "import numpy",
            "import pymysql",
            "import sqlalchemy",
            "import websocket",
        ]:
            self.assertNotIn(forbidden, packet_text)


if __name__ == "__main__":
    unittest.main()
