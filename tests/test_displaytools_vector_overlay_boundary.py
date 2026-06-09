import subprocess
import sys
import unittest
from pathlib import Path

from render_core import vector_overlay_boundary as boundary


REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKER = REPO_ROOT / "scripts" / "validate_displaytools_vector_overlay_import_boundary.py"
TARGET = REPO_ROOT / "render_core" / "vector_overlay_boundary.py"


class DisplaytoolsVectorOverlayBoundaryTests(unittest.TestCase):
    def test_helper_module_import_is_safe(self):
        self.assertFalse(hasattr(boundary, "GeoVectorLineOverlay"))
        self.assertFalse(hasattr(boundary, "HybridRenderController"))
        self.assertTrue(hasattr(boundary, "BOUNDARY_SPECS"))
        self.assertTrue(hasattr(boundary, "HYDROLOGY_SPECS"))

    def test_extracted_specs_exact_key_sets_are_pinned(self):
        self.assertEqual(
            set(boundary.BOUNDARY_SPECS),
            {"borders", "territorial_sea", "eez", "high_seas"},
        )
        self.assertEqual(set(boundary.HYDROLOGY_SPECS), {"lakes", "rivers"})
        for spec in boundary.BOUNDARY_SPECS.values():
            self.assertIn("name", spec)
            self.assertIn("color", spec)
            self.assertIn("prefix", spec)
            self.assertIn("source_note", spec)
        for spec in boundary.HYDROLOGY_SPECS.values():
            self.assertEqual(set(spec), {"name", "color", "natural_earth_layer", "source_note", "prefix"})

    def test_descriptor_builder_exact_key_set_and_repeat_call(self):
        first = boundary.build_vector_overlay_descriptor("lakes")
        second = boundary.build_vector_overlay_descriptor("lakes")
        self.assertEqual(first, second)
        self.assertEqual(
            set(first),
            {
                "schema",
                "overlay_kind",
                "provider_ref",
                "projection_policy",
                "mask_policy",
                "cache_status",
                "runtime_dependency_allowed",
                "runtime_render_invoked",
                "source_movement_authorized",
                "forbidden_next_action",
            },
        )
        self.assertFalse(first["runtime_dependency_allowed"])
        self.assertFalse(first["runtime_render_invoked"])
        self.assertFalse(first["source_movement_authorized"])

    def test_empty_and_malformed_provider_descriptor_branches(self):
        empty = boundary.build_vector_provider_ref_descriptor("", provider_present=False)
        malformed = boundary.build_vector_provider_ref_descriptor("bad", malformed=True)
        self.assertEqual(empty["overlay_kind"], "unknown")
        self.assertFalse(empty["provider_present"])
        self.assertEqual(empty["descriptor_table"], "")
        self.assertTrue(malformed["malformed"])
        self.assertFalse(malformed["provider_execution_allowed"])
        self.assertFalse(malformed["cache_read_allowed"])

    def test_dirty_reload_clean_and_reload_branches(self):
        clean = boundary.build_vector_dirty_reload_ledger_descriptor("lakes")
        reload_packet = boundary.build_vector_dirty_reload_ledger_descriptor(
            "rivers",
            dirty=True,
            reload_requested=True,
            reason="reload_requested",
        )
        self.assertEqual(clean["ledger_status"], "clean_descriptor")
        self.assertEqual(reload_packet["ledger_status"], "reload_descriptor")
        self.assertFalse(clean["controller_mutation_allowed"])
        self.assertFalse(reload_packet["controller_mutation_allowed"])

    def test_projection_mask_and_cache_status_are_label_only(self):
        projection = boundary.build_vector_projection_policy_label_descriptor()
        mask = boundary.build_vector_mask_policy_label_descriptor()
        cache_status = boundary.build_vector_cache_status_label_descriptor("cache_status_label_only")
        self.assertFalse(projection["formula_movement_allowed"])
        self.assertFalse(mask["formula_movement_allowed"])
        self.assertFalse(cache_status["cache_lifecycle_allowed"])
        self.assertFalse(cache_status["cache_read_allowed"])
        self.assertFalse(cache_status["cache_write_allowed"])

    def test_no_runtime_dependency_claim_or_executable_leakage(self):
        packet_text = repr(
            [
                boundary.build_vector_overlay_descriptor("borders"),
                boundary.build_vector_provider_ref_descriptor("borders"),
                boundary.build_vector_controller_registry_descriptor("borders"),
            ]
        )
        forbidden_executable_markers = [
            "GeoVectorLineOverlay(",
            "HybridRenderController",
            "alpha_compose(",
            "apply_layer_render_plan_composition",
            "load_hydrology(",
            "load_boundary(",
        ]
        for marker in forbidden_executable_markers:
            self.assertNotIn(marker, packet_text)

    def test_import_boundary_checker_candidate_passes(self):
        result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(TARGET)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertIn('"boundary_passed": true', result.stdout)
        self.assertIn('"candidate_exists": true', result.stdout)


if __name__ == "__main__":
    unittest.main()
