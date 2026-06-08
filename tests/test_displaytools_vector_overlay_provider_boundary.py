import unittest


PROVIDER_DESCRIPTOR_KEYS = {
    "provider_kind",
    "source_kind",
    "cache_policy",
    "loader_owner",
    "output_shape",
    "coordinate_payload_kind",
    "geometry_payload_kind",
    "failure_mode",
    "consumer_contract",
    "fixture_status",
    "forbidden_next_action",
}


BOUNDARY_CLASSIFICATIONS = {
    "provider_boundary_pinned",
    "provider_boundary_unresolved_static_only",
    "provider_cache_dependency_detected",
    "controller_registry_dependency_detected",
    "projection_consumer_dependency_detected",
    "blocked_runtime_only",
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "provider_extracted",
    "vector_overlay_extracted",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "borders_fixed",
    "hydrology_fixed",
}


def fake_provider_descriptor(
    provider_kind,
    source_kind,
    cache_policy,
    output_shape,
    coordinate_payload_kind="declared_lon_lat",
    geometry_payload_kind="line_descriptors",
    failure_mode="none",
    consumer_contract="vector_overlay_descriptor_consumer",
    fixture_status="provider_boundary_pinned",
):
    return {
        "provider_kind": provider_kind,
        "source_kind": source_kind,
        "cache_policy": cache_policy,
        "loader_owner": "provider_boundary_fixture_descriptor",
        "output_shape": output_shape,
        "coordinate_payload_kind": coordinate_payload_kind,
        "geometry_payload_kind": geometry_payload_kind,
        "failure_mode": failure_mode,
        "consumer_contract": consumer_contract,
        "fixture_status": fixture_status,
        "forbidden_next_action": "do_not_execute_provider_loader_cache_or_renderer",
    }


def build_vector_overlay_provider_boundary_packet():
    providers = [
        fake_provider_descriptor(
            "borders_provider",
            "synthetic_provider",
            "no_cache",
            "synthetic borders line provider",
        ),
        fake_provider_descriptor(
            "hydrology_provider",
            "synthetic_provider",
            "no_cache",
            "synthetic hydrology line provider",
        ),
        fake_provider_descriptor(
            "natural_earth_cache_reference",
            "cache_descriptor_only",
            "cache_hit_descriptor_only",
            "cache-hit descriptor only",
            fixture_status="provider_cache_dependency_detected",
        ),
        fake_provider_descriptor(
            "hydrology_cache_reference",
            "cache_descriptor_only",
            "cache_miss_descriptor_only",
            "cache-miss descriptor only",
            failure_mode="cache_missing",
            fixture_status="provider_cache_dependency_detected",
        ),
        fake_provider_descriptor(
            "synthetic_provider",
            "synthetic_provider",
            "no_cache",
            "provider output compared against vector overlay sync descriptor",
        ),
        fake_provider_descriptor(
            "malformed_provider",
            "synthetic_provider",
            "no_cache",
            "malformed provider output",
            coordinate_payload_kind="malformed_coordinates",
            geometry_payload_kind="malformed_geometry",
            failure_mode="malformed_payload",
            fixture_status="provider_boundary_unresolved_static_only",
        ),
        fake_provider_descriptor(
            "empty_provider",
            "synthetic_provider",
            "no_cache",
            "empty provider output",
            geometry_payload_kind="empty_geometry",
        ),
        fake_provider_descriptor(
            "borders_provider",
            "provider_unavailable",
            "no_cache",
            "provider unavailable descriptor",
            failure_mode="provider_unavailable",
            fixture_status="provider_boundary_unresolved_static_only",
        ),
    ]
    cases = [
        {
            "case_id": "synthetic_borders_line_provider",
            "provider_kind": "borders_provider",
            "output_shape": "synthetic borders line provider",
            "classification": "provider_boundary_pinned",
        },
        {
            "case_id": "synthetic_hydrology_line_provider",
            "provider_kind": "hydrology_provider",
            "output_shape": "synthetic hydrology line provider",
            "classification": "provider_boundary_pinned",
        },
        {
            "case_id": "empty_borders_provider_output",
            "provider_kind": "empty_provider",
            "output_shape": "empty borders provider output",
            "classification": "provider_boundary_pinned",
        },
        {
            "case_id": "empty_hydrology_provider_output",
            "provider_kind": "empty_provider",
            "output_shape": "empty hydrology provider output",
            "classification": "provider_boundary_pinned",
        },
        {
            "case_id": "malformed_coordinate_payload",
            "provider_kind": "malformed_provider",
            "output_shape": "malformed coordinate payload",
            "classification": "provider_boundary_unresolved_static_only",
        },
        {
            "case_id": "malformed_geometry_payload",
            "provider_kind": "malformed_provider",
            "output_shape": "malformed geometry payload",
            "classification": "provider_boundary_unresolved_static_only",
        },
        {
            "case_id": "cache_hit_descriptor_only",
            "provider_kind": "natural_earth_cache_reference",
            "output_shape": "cache-hit descriptor only",
            "classification": "provider_cache_dependency_detected",
        },
        {
            "case_id": "cache_miss_descriptor_only",
            "provider_kind": "hydrology_cache_reference",
            "output_shape": "cache-miss descriptor only",
            "classification": "provider_cache_dependency_detected",
        },
        {
            "case_id": "provider_unavailable_descriptor",
            "provider_kind": "borders_provider",
            "output_shape": "provider unavailable descriptor",
            "classification": "provider_boundary_unresolved_static_only",
        },
        {
            "case_id": "provider_output_compared_against_vector_overlay_sync_descriptor",
            "provider_kind": "synthetic_provider",
            "output_shape": "provider output compared against vector overlay sync descriptor",
            "classification": "projection_consumer_dependency_detected",
        },
    ]
    consumer_boundaries = {
        "vector overlay descriptor consumer": "projection_consumer_dependency_detected",
        "controller overlay registry consumer": "controller_registry_dependency_detected",
        "projection/render path consumer": "projection_consumer_dependency_detected",
        "mask/screen RGBA consumer": "projection_consumer_dependency_detected",
    }
    decision_output = {
        "provider_source_cache_fixture_candidate": True,
        "provider_import_boundary_checker_candidate": False,
        "needs_controller_registry_seam": True,
        "needs_provider_specific_monkey_patch": False,
        "docs_only_mapping_only": False,
        "reason": "provider descriptors can be pinned, but controller registry remains in the static footprint",
    }
    return {
        "test_shape": "pure_dict_list_scalar_no_provider_execution_no_real_cache",
        "provider_boundary": [
            "borders_provider",
            "hydrology_provider",
            "natural_earth_cache_reference",
            "hydrology_cache_reference",
            "synthetic_provider",
            "malformed_provider",
            "empty_provider",
        ],
        "consumer_boundary": consumer_boundaries,
        "provider_descriptors": providers,
        "synthetic_provider_cases": cases,
        "boundary_classifications": sorted(BOUNDARY_CLASSIFICATIONS),
        "decision_output": decision_output,
        "recommended_next_gate": "vector_overlay_controller_registry_fixture_gate",
    }


class VectorOverlayProviderBoundaryFixtureGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_provider_boundary_packet()

    def test_provider_descriptor_schema_and_required_boundaries(self):
        for descriptor in self.packet["provider_descriptors"]:
            self.assertEqual(set(descriptor), PROVIDER_DESCRIPTOR_KEYS)
            self.assertIn(descriptor["fixture_status"], BOUNDARY_CLASSIFICATIONS)
        self.assertEqual(
            set(self.packet["provider_boundary"]),
            {
                "borders_provider",
                "hydrology_provider",
                "natural_earth_cache_reference",
                "hydrology_cache_reference",
                "synthetic_provider",
                "malformed_provider",
                "empty_provider",
            },
        )

    def test_synthetic_provider_cases_cover_required_outputs(self):
        cases = {case["case_id"]: case for case in self.packet["synthetic_provider_cases"]}
        self.assertEqual(
            set(cases),
            {
                "synthetic_borders_line_provider",
                "synthetic_hydrology_line_provider",
                "empty_borders_provider_output",
                "empty_hydrology_provider_output",
                "malformed_coordinate_payload",
                "malformed_geometry_payload",
                "cache_hit_descriptor_only",
                "cache_miss_descriptor_only",
                "provider_unavailable_descriptor",
                "provider_output_compared_against_vector_overlay_sync_descriptor",
            },
        )
        self.assertEqual(cases["cache_hit_descriptor_only"]["classification"], "provider_cache_dependency_detected")
        self.assertEqual(cases["cache_miss_descriptor_only"]["classification"], "provider_cache_dependency_detected")

    def test_boundary_classifications_and_consumer_edges(self):
        self.assertEqual(set(self.packet["boundary_classifications"]), BOUNDARY_CLASSIFICATIONS)
        self.assertEqual(
            self.packet["consumer_boundary"]["controller overlay registry consumer"],
            "controller_registry_dependency_detected",
        )
        self.assertEqual(
            self.packet["consumer_boundary"]["projection/render path consumer"],
            "projection_consumer_dependency_detected",
        )

    def test_decision_output_blocks_checker_until_controller_registry_gate(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["provider_source_cache_fixture_candidate"])
        self.assertFalse(decision["provider_import_boundary_checker_candidate"])
        self.assertTrue(decision["needs_controller_registry_seam"])
        self.assertFalse(decision["docs_only_mapping_only"])
        self.assertEqual(
            self.packet["recommended_next_gate"],
            "vector_overlay_controller_registry_fixture_gate",
        )

    def test_test_shape_has_no_provider_execution_or_runtime_import(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_dict_list_scalar_no_provider_execution_no_real_cache",
        )
        serialized = repr(self.packet)
        for forbidden in (
            "import taichi",
            "from PyQt6",
            "import vispy",
            "read Natural Earth",
            "read GeoJSON",
            "connect SQL",
            "instantiate GeoVectorLineOverlay",
        ):
            self.assertNotIn(forbidden, serialized)

    def test_no_extraction_bugfix_or_readiness_claims(self):
        serialized = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(f"{marker}=true", serialized)


if __name__ == "__main__":
    unittest.main()
