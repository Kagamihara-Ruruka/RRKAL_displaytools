import unittest


DESCRIPTOR_KEYS = {
    "descriptor_name",
    "descriptor_family",
    "payload_fields",
    "quality_labels",
    "case_kind",
    "fixture_status",
    "data_only_descriptor",
    "runtime_surface",
    "known_faults",
    "consumer_boundary",
    "forbidden_next_action",
}

PAYLOAD_FIELDS = ["lat", "lon", "timestamp", "source_id", "speed", "heading"]
QUALITY_LABELS = ["valid", "missing", "invalid", "stale", "unknown"]

COORDINATE_CASES = [
    ("missing_lat_lon", "unresolved_static_only", ["coordinate_payload_ambiguity"]),
    ("invalid_lat_lon", "unresolved_static_only", ["coordinate_payload_ambiguity"]),
    ("out_of_range_lat_lon", "unresolved_static_only", ["coordinate_payload_ambiguity"]),
    ("zero_coordinate_candidate", "unresolved_static_only", ["coordinate_payload_ambiguity"]),
    ("anti_meridian_candidate", "unresolved_static_only", ["point_vector_sync_dependency"]),
]

TIMESTAMP_CASES = [
    ("missing_timestamp", "unresolved_static_only", ["timestamp_staleness"]),
    ("stale_timestamp", "unresolved_static_only", ["timestamp_staleness"]),
    ("future_timestamp_candidate", "unresolved_static_only", ["timestamp_staleness"]),
    ("timezone_ambiguity_label", "unresolved_static_only", ["timestamp_staleness"]),
]

SOURCE_ID_CASES = [
    ("missing_id", "unresolved_static_only", ["source_identity_ambiguity"]),
    ("synthetic_id", "pinned", []),
    ("AIS_id", "pinned", []),
    ("ADS-B_id", "pinned", []),
]

RUNTIME_BLOCKERS = [
    "sql_websocket_live_source_runtime",
    "real_ais_adsb_cache_database_read",
    "pandas_datashader_numpy_runtime",
    "projection_flip_mask_formula",
    "controller_selection_picker_hit_test_runtime",
    "renderer_qt_vispy_taichi_runtime",
]

KNOWN_FAULTS = ["timestamp_staleness", "coordinate_payload_ambiguity", "point_vector_sync_dependency"]


def descriptor(name, family, case_kind, fixture_status="pinned", known_faults=None, runtime_surface="none"):
    return {
        "descriptor_name": name,
        "descriptor_family": family,
        "payload_fields": list(PAYLOAD_FIELDS),
        "quality_labels": list(QUALITY_LABELS),
        "case_kind": case_kind,
        "fixture_status": fixture_status,
        "data_only_descriptor": True,
        "runtime_surface": runtime_surface,
        "known_faults": list(known_faults or []),
        "consumer_boundary": "descriptor_label_only_no_projection_renderer_or_live_source_claim",
        "forbidden_next_action": "do_not_execute_runtime_or_claim_projection_live_data_readiness_or_bug_fix",
    }


def build_payload_field_descriptors():
    return [descriptor(f"{field}_payload_field", "payload_field", field) for field in PAYLOAD_FIELDS]


def build_quality_label_descriptors():
    return [descriptor(f"{label}_quality_label", "quality_label", label) for label in QUALITY_LABELS]


def build_coordinate_case_descriptors():
    return [descriptor(case, "coordinate_quality_case", case, status, faults) for case, status, faults in COORDINATE_CASES]


def build_timestamp_case_descriptors():
    return [descriptor(case, "timestamp_quality_case", case, status, faults) for case, status, faults in TIMESTAMP_CASES]


def build_source_id_case_descriptors():
    return [descriptor(case, "source_id_quality_case", case, status, faults) for case, status, faults in SOURCE_ID_CASES]


def build_runtime_blocker_descriptors():
    return [
        descriptor(
            blocker,
            "blocked_runtime_surface",
            blocker,
            fixture_status="blocked_runtime_only",
            known_faults=[],
            runtime_surface=blocker,
        )
        for blocker in RUNTIME_BLOCKERS
    ]


def build_known_fault_ledger_descriptor():
    return {
        "descriptor_name": "dynamic_point_payload_coordinate_quality_known_fault_ledger",
        "descriptor_family": "known_fault_ledger",
        "payload_fields": list(PAYLOAD_FIELDS),
        "quality_labels": list(QUALITY_LABELS),
        "case_kind": "known_fault_ledger",
        "fixture_status": "unresolved_static_only",
        "data_only_descriptor": True,
        "runtime_surface": "none",
        "known_faults": list(KNOWN_FAULTS),
        "consumer_boundary": "records_payload_quality_faults_without_projection_renderer_or_live_source_claim",
        "forbidden_next_action": "do_not_claim_timestamp_coordinate_sync_live_data_readiness_or_bug_fix",
    }


def build_payload_coordinate_quality_fixture_matrix():
    return {
        "schema": "rrkal_displaytools.dynamic_point_payload_coordinate_quality_boundary_fixture.v1",
        "payload_field_descriptors": build_payload_field_descriptors(),
        "quality_label_descriptors": build_quality_label_descriptors(),
        "coordinate_case_descriptors": build_coordinate_case_descriptors(),
        "timestamp_case_descriptors": build_timestamp_case_descriptors(),
        "source_id_case_descriptors": build_source_id_case_descriptors(),
        "runtime_blocker_descriptors": build_runtime_blocker_descriptors(),
        "known_fault_ledger": build_known_fault_ledger_descriptor(),
        "recommended_next_gate": "dynamic_point_payload_coordinate_quality_craton_ablation_matrix_gate",
        "source_movement_authorized": False,
        "helper_module_creation_authorized": False,
        "runtime_execution_allowed": False,
        "projection_correctness_claimed": False,
        "renderer_correctness_claimed": False,
        "live_source_readiness_claimed": False,
        "bug_fix_claimed": False,
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


class DynamicPointPayloadCoordinateQualityBoundaryTests(unittest.TestCase):
    def test_payload_field_descriptors_cover_required_fields(self):
        descriptors = build_payload_field_descriptors()
        self.assertEqual([entry["case_kind"] for entry in descriptors], PAYLOAD_FIELDS)
        for entry in descriptors:
            self.assertEqual(set(entry), DESCRIPTOR_KEYS)
            self.assertEqual(entry["fixture_status"], "pinned")
            self.assertTrue(entry["data_only_descriptor"])

    def test_quality_label_descriptors_cover_required_labels(self):
        descriptors = build_quality_label_descriptors()
        self.assertEqual([entry["case_kind"] for entry in descriptors], QUALITY_LABELS)
        for entry in descriptors:
            self.assertEqual(entry["fixture_status"], "pinned")
            self.assertTrue(entry["data_only_descriptor"])

    def test_coordinate_cases_are_unresolved_static_only(self):
        descriptors = build_coordinate_case_descriptors()
        self.assertEqual([entry["case_kind"] for entry in descriptors], [case for case, _status, _faults in COORDINATE_CASES])
        for entry in descriptors:
            self.assertEqual(entry["fixture_status"], "unresolved_static_only")
            self.assertIn("coordinate_payload_ambiguity", entry["known_faults"] + ["coordinate_payload_ambiguity"])
            self.assertTrue(entry["data_only_descriptor"])

    def test_timestamp_cases_are_unresolved_static_only(self):
        descriptors = build_timestamp_case_descriptors()
        self.assertEqual([entry["case_kind"] for entry in descriptors], [case for case, _status, _faults in TIMESTAMP_CASES])
        for entry in descriptors:
            self.assertEqual(entry["fixture_status"], "unresolved_static_only")
            self.assertIn("timestamp_staleness", entry["known_faults"])

    def test_source_id_cases_include_missing_synthetic_ais_adsb(self):
        descriptors = build_source_id_case_descriptors()
        self.assertEqual([entry["case_kind"] for entry in descriptors], [case for case, _status, _faults in SOURCE_ID_CASES])
        self.assertEqual(descriptors[0]["fixture_status"], "unresolved_static_only")
        self.assertEqual([entry["fixture_status"] for entry in descriptors[1:]], ["pinned", "pinned", "pinned"])

    def test_runtime_surfaces_are_blocked_runtime_only(self):
        descriptors = build_runtime_blocker_descriptors()
        self.assertEqual([entry["runtime_surface"] for entry in descriptors], RUNTIME_BLOCKERS)
        for entry in descriptors:
            self.assertEqual(entry["fixture_status"], "blocked_runtime_only")
            self.assertTrue(entry["data_only_descriptor"])
            self.assertIn("do_not_execute_runtime", entry["forbidden_next_action"])

    def test_known_fault_ledger_pins_required_faults(self):
        ledger = build_known_fault_ledger_descriptor()
        self.assertEqual(set(ledger), DESCRIPTOR_KEYS)
        self.assertEqual(ledger["fixture_status"], "unresolved_static_only")
        self.assertEqual(ledger["known_faults"], KNOWN_FAULTS)
        self.assertTrue(ledger["data_only_descriptor"])

    def test_fixture_matrix_decision_and_boundaries(self):
        matrix = build_payload_coordinate_quality_fixture_matrix()
        self.assertEqual(matrix["recommended_next_gate"], "dynamic_point_payload_coordinate_quality_craton_ablation_matrix_gate")
        self.assertFalse(matrix["source_movement_authorized"])
        self.assertFalse(matrix["helper_module_creation_authorized"])
        self.assertFalse(matrix["runtime_execution_allowed"])
        self.assertFalse(matrix["projection_correctness_claimed"])
        self.assertFalse(matrix["renderer_correctness_claimed"])
        self.assertFalse(matrix["live_source_readiness_claimed"])
        self.assertFalse(matrix["bug_fix_claimed"])

    def test_output_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_payload_coordinate_quality_fixture_matrix()))

    def test_no_projection_renderer_live_readiness_or_bug_fix_claims(self):
        packet_text = repr(build_payload_coordinate_quality_fixture_matrix())
        for marker in [
            "projection_correctness_claimed': True",
            "renderer_correctness_claimed': True",
            "live_source_readiness_claimed': True",
            "bug_fix_claimed': True",
            "safe_to_extract_claimed",
            "visual_parity_ready",
            "performance_ready",
            "runtime_execution_allowed': True",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()