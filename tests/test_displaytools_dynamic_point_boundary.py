import unittest


DESCRIPTOR_KEYS = {
    "surface_name",
    "source_evidence",
    "input_frame",
    "consumer_layers",
    "policy_labels",
    "known_faults",
    "fixture_status",
    "forbidden_next_action",
}


FIXTURE_STATUSES = {"pinned", "unresolved_static_only", "blocked_hot_path"}


REQUIRED_DESCRIPTORS = {
    "source_descriptor",
    "point_payload_descriptor",
    "projection_label_descriptor",
    "time_replay_label_descriptor",
    "selection_descriptor",
    "render_policy_label_descriptor",
    "safety_ledger_descriptor",
    "known_fault_ledger_descriptor",
}


REQUIRED_CASES = {
    "ais_source_descriptor",
    "adsb_source_descriptor",
    "replay_source_descriptor",
    "synthetic_source_descriptor",
    "unavailable_source_descriptor",
    "point_payload_lat_lon_speed_heading_timestamp_id",
    "projection_label_no_formula",
    "static_replay_label",
    "live_lineage_unresolved_label",
    "selected_vehicle_descriptor",
    "selected_layer_descriptor",
    "hit_false_descriptor",
    "visible_count_rendered_count_cap_adaptive_sampling",
    "sql_websocket_live_source_blocked",
    "live_vs_replay_ambiguity_fault",
    "timestamp_staleness_fault",
    "point_vector_sync_dependency_fault",
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
}


def descriptor(
    surface_name,
    source_evidence,
    input_frame,
    consumer_layers,
    policy_labels,
    known_faults,
    fixture_status="pinned",
    forbidden_next_action="do_not_execute_dynamic_point_runtime",
):
    return {
        "surface_name": surface_name,
        "source_evidence": list(source_evidence),
        "input_frame": input_frame,
        "consumer_layers": list(consumer_layers),
        "policy_labels": list(policy_labels),
        "known_faults": list(known_faults),
        "fixture_status": fixture_status,
        "forbidden_next_action": forbidden_next_action,
    }


def build_dynamic_point_boundary_packet():
    descriptors = [
        {
            "descriptor_id": "source_descriptor",
            "descriptor": descriptor(
                "AIS / aircraft source descriptor",
                ["AIS source labels", "ADS-B source labels", "replay and synthetic source labels"],
                "source lineage label",
                ["point payload descriptor", "time/replay descriptor"],
                ["AIS", "ADS-B", "replay", "synthetic", "unavailable"],
                ["live-vs-replay ambiguity"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_execute_sql_websocket_live_or_cache_source",
            ),
        },
        {
            "descriptor_id": "point_payload_descriptor",
            "descriptor": descriptor(
                "dynamic point payload descriptor",
                ["lat/lon/speed/heading/timestamp/id packet labels"],
                "raw lon/lat payload label",
                ["projection label descriptor", "selection descriptor", "render policy label descriptor"],
                ["lat", "lon", "speed", "heading", "timestamp", "id"],
                ["timestamp staleness"],
                fixture_status="pinned",
                forbidden_next_action="do_not_import_pandas_datashader_numpy_or_parse_real_payload",
            ),
        },
        {
            "descriptor_id": "projection_label_descriptor",
            "descriptor": descriptor(
                "dynamic point projection label descriptor",
                ["globe coordinate fixture design gate", "vector overlay coordinate sync fixture gate"],
                "screen projection peer label",
                ["AIS screen points", "aircraft screen points", "vector overlay sync diagnostics"],
                ["screen_projection_peer", "no_projection_formula"],
                ["point/vector sync dependency"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_change_projection_flip_or_mask_formula",
            ),
        },
        {
            "descriptor_id": "time_replay_label_descriptor",
            "descriptor": descriptor(
                "time / replay label descriptor",
                ["static replay label", "live lineage unresolved label"],
                "timestamp lineage label",
                ["source descriptor", "render policy label descriptor"],
                ["static_replay", "live_lineage_unresolved", "timestamp_label"],
                ["timestamp staleness", "live-vs-replay ambiguity"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_execute_real_clock_sql_websocket_or_live_replay",
            ),
        },
        {
            "descriptor_id": "selection_descriptor",
            "descriptor": descriptor(
                "dynamic point selection descriptor",
                ["selected vehicle label", "selected layer label", "hit false label"],
                "selection label only",
                ["controller selection UI label", "point payload descriptor"],
                ["selected_vehicle", "selected_layer", "hit_false"],
                ["controller selection runtime excluded"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_mutate_controller_selection_runtime",
            ),
        },
        {
            "descriptor_id": "render_policy_label_descriptor",
            "descriptor": descriptor(
                "dynamic point render policy label descriptor",
                ["visible/rendered count labels", "cap/adaptive sampling labels"],
                "render policy label only",
                ["point overlay budget label", "datashader sampling label"],
                ["visible_count", "rendered_count", "cap", "adaptive_sampling"],
                ["datashader runtime not covered"],
                fixture_status="pinned",
                forbidden_next_action="do_not_execute_datashader_or_renderer_runtime",
            ),
        },
        {
            "descriptor_id": "safety_ledger_descriptor",
            "descriptor": descriptor(
                "dynamic point safety ledger descriptor",
                ["SQL/WebSocket/live source blocked", "pandas/datashader/numpy runtime blocked"],
                "safety ledger label",
                ["source descriptor", "render policy label descriptor"],
                ["sql_blocked", "websocket_blocked", "live_source_blocked", "datashader_blocked"],
                ["live data not restored", "runtime source execution blocked"],
                fixture_status="blocked_hot_path",
                forbidden_next_action="do_not_execute_sql_websocket_live_datashader_or_runtime_source",
            ),
        },
        {
            "descriptor_id": "known_fault_ledger_descriptor",
            "descriptor": descriptor(
                "dynamic point known fault ledger descriptor",
                ["live-vs-replay ambiguity", "timestamp staleness", "point/vector sync dependency"],
                "known fault ledger label",
                ["source descriptor", "projection label descriptor", "time/replay label descriptor"],
                ["live_vs_replay_ambiguity", "timestamp_staleness", "point_vector_sync_dependency"],
                ["live-vs-replay ambiguity", "timestamp staleness", "point/vector sync dependency"],
                fixture_status="unresolved_static_only",
                forbidden_next_action="do_not_claim_live_data_bug_fix_or_visual_parity",
            ),
        },
    ]
    cases = [
        {"case_id": "ais_source_descriptor", "descriptor_id": "source_descriptor"},
        {"case_id": "adsb_source_descriptor", "descriptor_id": "source_descriptor"},
        {"case_id": "replay_source_descriptor", "descriptor_id": "source_descriptor"},
        {"case_id": "synthetic_source_descriptor", "descriptor_id": "source_descriptor"},
        {"case_id": "unavailable_source_descriptor", "descriptor_id": "source_descriptor"},
        {"case_id": "point_payload_lat_lon_speed_heading_timestamp_id", "descriptor_id": "point_payload_descriptor"},
        {"case_id": "projection_label_no_formula", "descriptor_id": "projection_label_descriptor"},
        {"case_id": "static_replay_label", "descriptor_id": "time_replay_label_descriptor"},
        {"case_id": "live_lineage_unresolved_label", "descriptor_id": "time_replay_label_descriptor"},
        {"case_id": "selected_vehicle_descriptor", "descriptor_id": "selection_descriptor"},
        {"case_id": "selected_layer_descriptor", "descriptor_id": "selection_descriptor"},
        {"case_id": "hit_false_descriptor", "descriptor_id": "selection_descriptor"},
        {"case_id": "visible_count_rendered_count_cap_adaptive_sampling", "descriptor_id": "render_policy_label_descriptor"},
        {"case_id": "sql_websocket_live_source_blocked", "descriptor_id": "safety_ledger_descriptor"},
        {"case_id": "live_vs_replay_ambiguity_fault", "descriptor_id": "known_fault_ledger_descriptor"},
        {"case_id": "timestamp_staleness_fault", "descriptor_id": "known_fault_ledger_descriptor"},
        {"case_id": "point_vector_sync_dependency_fault", "descriptor_id": "known_fault_ledger_descriptor"},
    ]
    return {
        "test_shape": "pure_descriptor_fixture_matrix_no_monolith_import",
        "descriptors": descriptors,
        "fixture_cases": cases,
        "runtime_render_invoked": False,
        "production_source_changed": False,
        "helper_module_created": False,
        "sql_websocket_live_source_executed": False,
        "real_cache_or_database_read": False,
        "pandas_datashader_numpy_runtime_imported": False,
        "projection_formula_change_authorized": False,
        "live_source_restoration_claimed": False,
        "recommended_next_gate": "dynamic_point_source_surface_movement_preimplementation_gate",
    }


def is_dict_list_scalar(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return True
    if isinstance(value, list):
        return all(is_dict_list_scalar(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_dict_list_scalar(item) for key, item in value.items())
    return False


class DynamicPointBoundaryFixtureGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_boundary_packet()

    def test_descriptor_exact_key_sets_and_statuses(self):
        statuses = set()
        for entry in self.packet["descriptors"]:
            descriptor_packet = entry["descriptor"]
            self.assertEqual(set(descriptor_packet), DESCRIPTOR_KEYS)
            self.assertIn(descriptor_packet["fixture_status"], FIXTURE_STATUSES)
            statuses.add(descriptor_packet["fixture_status"])
        self.assertEqual(statuses, FIXTURE_STATUSES)

    def test_required_descriptors_and_cases_are_present(self):
        self.assertEqual({entry["descriptor_id"] for entry in self.packet["descriptors"]}, REQUIRED_DESCRIPTORS)
        self.assertEqual({case["case_id"] for case in self.packet["fixture_cases"]}, REQUIRED_CASES)

    def test_deterministic_repeat_call_and_scalar_shape(self):
        self.assertEqual(build_dynamic_point_boundary_packet(), build_dynamic_point_boundary_packet())
        self.assertTrue(is_dict_list_scalar(self.packet))

    def test_source_and_point_payload_descriptors_pin_labels_only(self):
        descriptors = {entry["descriptor_id"]: entry["descriptor"] for entry in self.packet["descriptors"]}
        source = descriptors["source_descriptor"]
        payload = descriptors["point_payload_descriptor"]
        for label in ["AIS", "ADS-B", "replay", "synthetic", "unavailable"]:
            self.assertIn(label, source["policy_labels"])
        for label in ["lat", "lon", "speed", "heading", "timestamp", "id"]:
            self.assertIn(label, payload["policy_labels"])

    def test_projection_time_selection_and_render_policy_are_label_only(self):
        descriptors = {entry["descriptor_id"]: entry["descriptor"] for entry in self.packet["descriptors"]}
        self.assertIn("no_projection_formula", descriptors["projection_label_descriptor"]["policy_labels"])
        self.assertIn("static_replay", descriptors["time_replay_label_descriptor"]["policy_labels"])
        self.assertIn("live_lineage_unresolved", descriptors["time_replay_label_descriptor"]["policy_labels"])
        self.assertIn("selected_vehicle", descriptors["selection_descriptor"]["policy_labels"])
        self.assertIn("hit_false", descriptors["selection_descriptor"]["policy_labels"])
        self.assertIn("adaptive_sampling", descriptors["render_policy_label_descriptor"]["policy_labels"])

    def test_safety_and_known_fault_ledgers_block_runtime_and_claims(self):
        descriptors = {entry["descriptor_id"]: entry["descriptor"] for entry in self.packet["descriptors"]}
        safety = descriptors["safety_ledger_descriptor"]
        faults = descriptors["known_fault_ledger_descriptor"]
        self.assertEqual(safety["fixture_status"], "blocked_hot_path")
        for label in ["sql_blocked", "websocket_blocked", "live_source_blocked", "datashader_blocked"]:
            self.assertIn(label, safety["policy_labels"])
        self.assertEqual(faults["fixture_status"], "unresolved_static_only")
        self.assertIn("live-vs-replay ambiguity", faults["known_faults"])
        self.assertIn("timestamp staleness", faults["known_faults"])
        self.assertIn("point/vector sync dependency", faults["known_faults"])

    def test_no_runtime_import_execution_or_readiness_claims(self):
        self.assertEqual(self.packet["test_shape"], "pure_descriptor_fixture_matrix_no_monolith_import")
        self.assertFalse(self.packet["runtime_render_invoked"])
        self.assertFalse(self.packet["production_source_changed"])
        self.assertFalse(self.packet["helper_module_created"])
        self.assertFalse(self.packet["sql_websocket_live_source_executed"])
        self.assertFalse(self.packet["real_cache_or_database_read"])
        self.assertFalse(self.packet["pandas_datashader_numpy_runtime_imported"])
        self.assertFalse(self.packet["projection_formula_change_authorized"])
        self.assertFalse(self.packet["live_source_restoration_claimed"])
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
