import ast
import inspect
import unittest

from scripts import dynamic_point_lod_view_frame_one_shot_probe_dry_harness as harness


FORBIDDEN_IMPORTS = {
    "pandas",
    "numpy",
    "datashader",
    "taichi",
    "PyQt",
    "vispy",
    "matplotlib",
}


EXPECTED_PAYLOAD_FIELDS = {
    "point_id",
    "source_label",
    "timestamp",
    "lat",
    "lon",
    "speed_or_altitude_label",
    "yaw",
    "pitch",
    "zoom",
    "horizon_eps",
    "lod_label",
}


EXPECTED_TOKEN_FIELDS = {
    "source_present_token",
    "projected_visible_token",
    "sampled_visible_token",
    "overlay_rendered_token",
    "mask_visible_token",
    "frame_visible_token",
    "source_lineage_integrity_token",
    "visible_count_observation",
    "rendered_count_observation",
}


class DynamicPointLodViewFrameOneShotProbeDryHarnessTest(unittest.TestCase):
    def test_dry_harness_imports_safely_and_builds_payload(self):
        payload = harness.build_synthetic_payload()
        packet = harness.packet_to_dict(payload)
        self.assertEqual(set(packet), EXPECTED_PAYLOAD_FIELDS)
        self.assertEqual(packet["point_id"], "synthetic-point-001")
        self.assertEqual(packet["source_label"], "AIS_SYNTHETIC")
        self.assertEqual(packet["timestamp"], "2026-06-10T00:00:00Z")
        self.assertIsInstance(packet["lat"], float)
        self.assertIsInstance(packet["lon"], float)

    def test_token_packet_builder_uses_l0_explicit_tokens(self):
        token_packet = harness.build_token_packet()
        packet = harness.packet_to_dict(token_packet)
        self.assertEqual(set(packet), EXPECTED_TOKEN_FIELDS)
        for field in EXPECTED_TOKEN_FIELDS:
            if field.endswith("_token"):
                self.assertIs(packet[field], True)
        self.assertEqual(packet["visible_count_observation"], 1)
        self.assertEqual(packet["rendered_count_observation"], 1)

    def test_oracle_sample_cases(self):
        cases = {
            "invalid_probe": harness.build_token_packet(source_present_token=False),
            "source_lineage_pollution_fail": harness.build_token_packet(source_lineage_integrity_token=False),
            "projection_or_horizon_responsibility": harness.build_token_packet(projected_visible_token=False),
            "sampling_responsibility": harness.build_token_packet(sampled_visible_token=False),
            "overlay_or_presentation_responsibility": harness.build_token_packet(overlay_rendered_token=False),
            "globe_mask_responsibility": harness.build_token_packet(mask_visible_token=False, frame_visible_token=False),
            "transparent_globe_leak_candidate": harness.build_token_packet(mask_visible_token=False, frame_visible_token=True),
            "computed_but_hidden_supported": harness.build_token_packet(frame_visible_token=False),
            "path_preserved_or_not_enough_evidence": harness.build_token_packet(),
        }
        for expected, packet in cases.items():
            with self.subTest(expected=expected):
                result = harness.evaluate_oracle(packet)
                self.assertEqual(result.verdict, expected)
                self.assertFalse(result.runtime_execution_authorized)
                self.assertFalse(result.runtime_probe_execution_authorized)
                self.assertFalse(result.persistent_artifact_authorized)
                self.assertFalse(result.coordinate_correctness_claimed)
                self.assertFalse(result.visual_correctness_claimed)
                self.assertFalse(result.transparent_globe_leak_fix_claimed)
                self.assertFalse(result.readiness_claimed)

    def test_self_test_cases_pass(self):
        result = harness.run_self_test()
        self.assertTrue(result["self_test_passed"])
        self.assertEqual(len(result["cases"]), 9)
        for case in result["cases"]:
            self.assertTrue(case["passed"], case)

    def test_decision_output(self):
        decision = harness.build_decision_output()
        self.assertTrue(decision["dry_harness_gate_passed"])
        self.assertTrue(decision["dry_harness_created"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["runtime_probe_execution_authorized"])
        self.assertFalse(decision["monolith_imported"])
        self.assertFalse(decision["render_core_imported"])
        self.assertFalse(decision["forbidden_runtime_imports_present"])
        self.assertTrue(decision["synthetic_data_only"])
        self.assertTrue(decision["one_shot_contract_only"])
        self.assertFalse(decision["persistent_artifact_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertTrue(decision["a1_starlink_observation_completed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_one_shot_probe_dry_harness_o1_runtime_authorization_review_gate",
        )

    def test_ast_import_boundary(self):
        source = inspect.getsource(harness)
        tree = ast.parse(source)
        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_roots.add((node.module or "").split(".", 1)[0])
        self.assertEqual(imported_roots, {"dataclasses", "json", "sys", "typing"})
        self.assertTrue(FORBIDDEN_IMPORTS.isdisjoint(imported_roots))

    def test_source_boundary_has_no_forbidden_product_references_or_helpers(self):
        source = inspect.getsource(harness)
        self.assertNotIn("taichi_global_bathymetry", source)
        self.assertNotIn("render_core", source)
        for name in FORBIDDEN_IMPORTS:
            self.assertNotIn(f"import {name}", source)
        forbidden_runtime_helpers = {
            "open(",
            "Path(",
            "read_text",
            "write_text",
            "write_bytes",
            "socket",
            "urllib",
            "requests",
            "subprocess",
            "settrace",
            "__getattribute__",
            "__array__",
        }
        for marker in forbidden_runtime_helpers:
            self.assertNotIn(marker, source)

    def test_harness_exposes_no_file_network_runtime_execution_api(self):
        public_names = {name for name in dir(harness) if not name.startswith("_")}
        forbidden_public_names = {
            "open",
            "Path",
            "requests",
            "socket",
            "subprocess",
            "settrace",
        }
        self.assertTrue(forbidden_public_names.isdisjoint(public_names))
        self.assertIn("build_synthetic_payload", public_names)
        self.assertIn("build_token_packet", public_names)
        self.assertIn("evaluate_oracle", public_names)


if __name__ == "__main__":
    unittest.main()
