import unittest


CATEGORY_ENTRY_KEYS = {
    "category",
    "surfaces",
    "candidate_for_descriptor_planning",
    "candidate_for_extraction",
    "runtime_dependency_allowed",
    "required_guard",
    "forbidden_next_action",
}

CANDIDATE_ENTRY_KEYS = {
    "candidate_family",
    "movement_category",
    "future_target",
    "allowed_content_kind",
    "runtime_dependency_allowed",
    "candidate_for_planning",
    "candidate_for_extraction",
    "required_checker",
    "forbidden_next_action",
}

BLOCKED_ENTRY_KEYS = {
    "blocked_surface",
    "blocked_category",
    "reason",
    "candidate_for_extraction",
    "forbidden_next_action",
}

DECISION_OUTPUT_KEYS = {
    "source_lineage_source_surface_gate_passed",
    "source_lineage_planning_candidate",
    "source_lineage_extraction_candidate",
    "source_movement_authorized",
    "helper_module_creation_authorized",
    "import_boundary_checker_required_before_extraction",
    "existing_checker",
    "future_helper_target",
    "target_decision_reason",
    "recommended_next_gate",
}

REQUIRED_CATEGORIES = {
    "category_a_source_lineage_descriptor_policy_ledger",
    "category_b_sql_replay_runtime",
    "category_c_live_websocket_runtime",
    "category_d_cache_database_io",
    "category_e_dataframe_projection_runtime",
    "category_f_controller_selection_runtime",
    "category_g_renderer_host_runtime",
}

REQUIRED_CANDIDATES = {
    "build_dynamic_point_source_lineage_descriptor",
    "build_dynamic_point_replay_lineage_label_descriptor",
    "build_dynamic_point_live_lineage_label_descriptor",
    "build_dynamic_point_source_availability_descriptor",
    "build_dynamic_point_timestamp_quality_descriptor",
    "build_dynamic_point_coordinate_payload_quality_descriptor",
    "build_dynamic_point_source_lineage_known_fault_ledger",
    "dynamic_point_source_lineage_boundary_descriptor",
    "dynamic_point_source_lineage_planning_bundle",
}

REQUIRED_BLOCKED = {
    "SQL / MySQL / pymysql / sqlalchemy / DB URL / replay query execution",
    "WebSocket / live AIS / live ADS-B stream execution",
    "real AIS / ADS-B / cache / database read",
    "pandas / datashader / numpy runtime",
    "projection / flip / mask formula",
    "controller selection / picker / hit-test mutation",
    "renderer / Qt / VisPy / Taichi runtime",
    "metadata / artifact writer",
    "alpha / apply / composition hot path",
    "readiness / performance / visual parity / bug-fix / live-data claims",
}


def build_source_lineage_category_matrix():
    return [
        {
            "category": "category_a_source_lineage_descriptor_policy_ledger",
            "surfaces": [
                "AIS source label",
                "ADS-B source label",
                "replay lineage label",
                "live lineage unresolved label",
                "synthetic source label",
                "unavailable source label",
                "timestamp quality label",
                "coordinate payload quality label",
                "source lineage known fault ledger",
            ],
            "candidate_for_descriptor_planning": True,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "descriptor_policy_ledger_only",
            "forbidden_next_action": "do_not_create_helper_or_move_source_in_this_gate",
        },
        {
            "category": "category_b_sql_replay_runtime",
            "surfaces": ["SQL", "MySQL", "pymysql", "sqlalchemy", "DB URL", "replay query execution"],
            "candidate_for_descriptor_planning": False,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "blocked_runtime_surface",
            "forbidden_next_action": "do_not_execute_or_move_sql_replay_runtime",
        },
        {
            "category": "category_c_live_websocket_runtime",
            "surfaces": ["WebSocket", "live AIS", "live ADS-B", "live stream socket"],
            "candidate_for_descriptor_planning": False,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "blocked_runtime_surface",
            "forbidden_next_action": "do_not_open_or_move_live_stream_runtime",
        },
        {
            "category": "category_d_cache_database_io",
            "surfaces": ["real AIS cache", "real ADS-B cache", "database read", "cache read"],
            "candidate_for_descriptor_planning": False,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "blocked_io_surface",
            "forbidden_next_action": "do_not_read_real_cache_or_database",
        },
        {
            "category": "category_e_dataframe_projection_runtime",
            "surfaces": ["pandas", "datashader", "numpy", "projection formula", "flip formula", "mask formula"],
            "candidate_for_descriptor_planning": False,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "blocked_runtime_formula_surface",
            "forbidden_next_action": "do_not_import_dataframe_runtime_or_change_projection_formula",
        },
        {
            "category": "category_f_controller_selection_runtime",
            "surfaces": ["selected vehicle runtime", "picker", "hit-test", "controller mutation"],
            "candidate_for_descriptor_planning": False,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "blocked_controller_surface",
            "forbidden_next_action": "do_not_mutate_controller_selection_runtime",
        },
        {
            "category": "category_g_renderer_host_runtime",
            "surfaces": ["renderer", "Qt", "VisPy", "Taichi", "GUI runtime"],
            "candidate_for_descriptor_planning": False,
            "candidate_for_extraction": False,
            "runtime_dependency_allowed": False,
            "required_guard": "blocked_renderer_host_surface",
            "forbidden_next_action": "do_not_execute_renderer_qt_vispy_taichi_runtime",
        },
    ]


def build_source_lineage_candidate_families():
    return [
        {
            "candidate_family": name,
            "movement_category": "category_a_source_lineage_descriptor_policy_ledger",
            "future_target": "render_core\\dynamic_point_source_lineage_boundary.py",
            "allowed_content_kind": "dict/list/scalar descriptor builder or policy/ledger table",
            "runtime_dependency_allowed": False,
            "candidate_for_planning": True,
            "candidate_for_extraction": False,
            "required_checker": "scripts\\validate_displaytools_dynamic_point_import_boundary.py or narrower future checker",
            "forbidden_next_action": "do_not_create_helper_module_or_move_source_in_this_gate",
        }
        for name in [
            "build_dynamic_point_source_lineage_descriptor",
            "build_dynamic_point_replay_lineage_label_descriptor",
            "build_dynamic_point_live_lineage_label_descriptor",
            "build_dynamic_point_source_availability_descriptor",
            "build_dynamic_point_timestamp_quality_descriptor",
            "build_dynamic_point_coordinate_payload_quality_descriptor",
            "build_dynamic_point_source_lineage_known_fault_ledger",
            "dynamic_point_source_lineage_boundary_descriptor",
            "dynamic_point_source_lineage_planning_bundle",
        ]
    ]


def build_blocked_surfaces():
    return [
        {
            "blocked_surface": name,
            "blocked_category": category,
            "reason": reason,
            "candidate_for_extraction": False,
            "forbidden_next_action": action,
        }
        for name, category, reason, action in [
            (
                "SQL / MySQL / pymysql / sqlalchemy / DB URL / replay query execution",
                "category_b_sql_replay_runtime",
                "database replay is executable IO runtime",
                "do_not_execute_or_move_sql_replay_runtime",
            ),
            (
                "WebSocket / live AIS / live ADS-B stream execution",
                "category_c_live_websocket_runtime",
                "live stream opens network runtime",
                "do_not_open_or_move_live_stream_runtime",
            ),
            (
                "real AIS / ADS-B / cache / database read",
                "category_d_cache_database_io",
                "real source read is IO behavior",
                "do_not_read_real_cache_or_database",
            ),
            (
                "pandas / datashader / numpy runtime",
                "category_e_dataframe_projection_runtime",
                "dataframe/render-heavy runtime is not descriptor content",
                "do_not_import_dataframe_projection_runtime",
            ),
            (
                "projection / flip / mask formula",
                "category_e_dataframe_projection_runtime",
                "coordinate formulas change point placement or visibility",
                "do_not_change_projection_flip_or_mask_formula",
            ),
            (
                "controller selection / picker / hit-test mutation",
                "category_f_controller_selection_runtime",
                "controller selection mutates runtime state",
                "do_not_mutate_controller_selection_runtime",
            ),
            (
                "renderer / Qt / VisPy / Taichi runtime",
                "category_g_renderer_host_runtime",
                "renderer host runtime is outside source lineage descriptor planning",
                "do_not_execute_renderer_qt_vispy_taichi_runtime",
            ),
            (
                "metadata / artifact writer",
                "metadata_artifact_writer",
                "writers affect output artifacts",
                "do_not_execute_or_move_writers",
            ),
            (
                "alpha / apply / composition hot path",
                "hot_path_blocked",
                "composition hot path is outside source lineage planning",
                "do_not_touch_alpha_apply_composition",
            ),
            (
                "readiness / performance / visual parity / bug-fix / live-data claims",
                "claim_blocked",
                "claims would overstate this docs/test-only gate",
                "do_not_claim_readiness_performance_visual_parity_bug_fix_or_live_data",
            ),
        ]
    ]


def build_decision_output():
    return {
        "source_lineage_source_surface_gate_passed": True,
        "source_lineage_planning_candidate": True,
        "source_lineage_extraction_candidate": False,
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "import_boundary_checker_required_before_extraction": True,
        "existing_checker": "scripts\\validate_displaytools_dynamic_point_import_boundary.py",
        "future_helper_target": "render_core\\dynamic_point_source_lineage_boundary.py",
        "target_decision_reason": "source_lineage_has_second_layer_specific_candidates_distinct_from_existing_aggregate_dynamic_point_boundary",
        "recommended_next_gate": "dynamic_point_source_lineage_craton_ablation_matrix_gate",
    }


def is_scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def is_packet_data(value):
    if is_scalar(value):
        return True
    if isinstance(value, list):
        return all(is_packet_data(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_packet_data(item) for key, item in value.items())
    return False


class DynamicPointSourceLineageSourceSurfaceMovementTests(unittest.TestCase):
    def test_category_matrix_has_required_categories_and_fields(self):
        matrix = build_source_lineage_category_matrix()
        self.assertEqual({entry["category"] for entry in matrix}, REQUIRED_CATEGORIES)
        for entry in matrix:
            self.assertEqual(set(entry), CATEGORY_ENTRY_KEYS)
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertFalse(entry["candidate_for_extraction"])

    def test_only_category_a_is_planning_candidate(self):
        matrix = build_source_lineage_category_matrix()
        planning = [entry for entry in matrix if entry["candidate_for_descriptor_planning"]]
        self.assertEqual(len(planning), 1)
        self.assertEqual(planning[0]["category"], "category_a_source_lineage_descriptor_policy_ledger")
        self.assertEqual(planning[0]["required_guard"], "descriptor_policy_ledger_only")

    def test_candidate_families_are_descriptor_only_planning_candidates(self):
        candidates = build_source_lineage_candidate_families()
        self.assertEqual({entry["candidate_family"] for entry in candidates}, REQUIRED_CANDIDATES)
        for entry in candidates:
            self.assertEqual(set(entry), CANDIDATE_ENTRY_KEYS)
            self.assertEqual(entry["future_target"], "render_core\\dynamic_point_source_lineage_boundary.py")
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertTrue(entry["candidate_for_planning"])
            self.assertFalse(entry["candidate_for_extraction"])

    def test_blocked_surfaces_are_pinned(self):
        blocked = build_blocked_surfaces()
        self.assertEqual({entry["blocked_surface"] for entry in blocked}, REQUIRED_BLOCKED)
        for entry in blocked:
            self.assertEqual(set(entry), BLOCKED_ENTRY_KEYS)
            self.assertFalse(entry["candidate_for_extraction"])
            self.assertIn("do_not", entry["forbidden_next_action"])

    def test_decision_output_is_pinned(self):
        decision = build_decision_output()
        self.assertEqual(set(decision), DECISION_OUTPUT_KEYS)
        self.assertTrue(decision["source_lineage_source_surface_gate_passed"])
        self.assertTrue(decision["source_lineage_planning_candidate"])
        self.assertFalse(decision["source_lineage_extraction_candidate"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertTrue(decision["import_boundary_checker_required_before_extraction"])
        self.assertEqual(decision["existing_checker"], "scripts\\validate_displaytools_dynamic_point_import_boundary.py")
        self.assertEqual(decision["future_helper_target"], "render_core\\dynamic_point_source_lineage_boundary.py")
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_source_lineage_craton_ablation_matrix_gate")

    def test_packets_are_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_source_lineage_category_matrix()))
        self.assertTrue(is_packet_data(build_source_lineage_candidate_families()))
        self.assertTrue(is_packet_data(build_blocked_surfaces()))
        self.assertTrue(is_packet_data(build_decision_output()))

    def test_no_monolith_runtime_or_claim_markers(self):
        packet_text = repr(build_source_lineage_category_matrix()) + repr(build_source_lineage_candidate_families()) + repr(build_blocked_surfaces()) + repr(build_decision_output())
        for marker in [
            "taichi_global_bathymetry",
            "runtime_import_used",
            "source_movement_authorized_true",
            "helper_module_creation_authorized_true",
            "source_lineage_extraction_candidate_true",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "readiness_claimed",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
