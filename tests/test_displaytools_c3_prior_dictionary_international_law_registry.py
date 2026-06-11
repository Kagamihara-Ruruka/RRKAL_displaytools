"""External authority-source registry for future c_3 prior dictionaries.

This docs/test-only gate records candidate external and RRKAL-native sources for
future semantic dictionary work. It does not create YAML dictionaries, prior
cards, helpers, runtime code, or prototype interfaces.
"""

import unittest

from render_core import dynamic_point_computed_but_hidden_boundary as computed_hidden
from render_core import dynamic_point_presentation_count_boundary as presentation_count
from render_core import dynamic_point_presentation_reduction_boundary as presentation_reduction
from render_core import dynamic_point_sampling_visibility_boundary as sampling_visibility
from render_core import dynamic_point_source_lineage_guard_boundary as source_lineage
from tests import test_displaytools_dynamic_point_andesite_registry_milestone_settlement as andesite_registry
from tests import test_displaytools_dynamic_point_mask_occlusion_legacy_anatomy_classification as mask_anatomy


PRIOR_LAYERS = [
    "data_spacetime_prior",
    "graphics_prior",
    "geospatial_prior",
    "uiux_prior",
    "runtime_budget_prior",
    "rrkal_governance_prior",
    "legacy_fossil_translation",
]

AUTHORITY_KINDS = [
    "external_standard",
    "external_reference_implementation",
    "external_mature_tool_model",
    "rrkal_native_governance",
    "legacy_fossil_evidence",
    "candidate_pending_review",
]

REQUIRED_MATRIX_FIELDS = [
    "source_id",
    "prior_layer",
    "authority_kind",
    "source_name",
    "source_url_or_local_ref",
    "why_relevant_to_c3",
    "terms_expected_to_govern",
    "adoption_status",
    "rrkal_translation_needed",
    "forbidden_overread",
    "future_dictionary_candidate",
    "stop_condition",
]

STATIC_SCAN_TERMS = [
    "mask",
    "occlusion",
    "projection",
    "LOD",
    "bake",
    "layer",
    "frame",
    "alpha",
    "tile",
    "grid",
    "trajectory",
    "time",
    "schema",
    "source_lineage",
]

SOURCE_REGISTRY = [
    {
        "source_id": "stac_spec_candidate",
        "prior_layer": "data_spacetime_prior",
        "authority_kind": "external_mature_tool_model",
        "source_name": "SpatioTemporal Asset Catalog specification",
        "source_url_or_local_ref": "https://stacspec.org/",
        "why_relevant_to_c3": "mature model for assets with spatial and temporal metadata",
        "terms_expected_to_govern": ["time slice", "event", "trajectory", "raster", "vector", "geometry"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not already adopted as RRKAL asset schema",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if source metadata is treated as c_1 implementation",
    },
    {
        "source_id": "cf_conventions_candidate",
        "prior_layer": "data_spacetime_prior",
        "authority_kind": "candidate_pending_review",
        "source_name": "CF Metadata Conventions",
        "source_url_or_local_ref": "https://cfconventions.org/",
        "why_relevant_to_c3": "candidate vocabulary for gridded raster and time-indexed scientific data",
        "terms_expected_to_govern": ["grid", "raster", "time", "feature", "point cloud"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not a renderer or UI schema",
        "future_dictionary_candidate": True,
        "stop_condition": "keep pending if c_3 data terms cannot be mapped cleanly",
    },
    {
        "source_id": "khronos_rendering_pipeline",
        "prior_layer": "graphics_prior",
        "authority_kind": "external_reference_implementation",
        "source_name": "Khronos OpenGL rendering pipeline overview",
        "source_url_or_local_ref": "https://wikis.khronos.org/opengl/Rendering_Pipeline_Overview",
        "why_relevant_to_c3": "reference vocabulary for graphics pipeline stages and framebuffer-adjacent concepts",
        "terms_expected_to_govern": ["camera", "view frame", "projection", "depth", "occlusion", "clipping", "framebuffer"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "does not authorize renderer execution or formula movement",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if graphics terms become runtime behavior changes",
    },
    {
        "source_id": "khronos_gltf_candidate",
        "prior_layer": "graphics_prior",
        "authority_kind": "external_standard",
        "source_name": "Khronos glTF specification",
        "source_url_or_local_ref": "https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html",
        "why_relevant_to_c3": "candidate vocabulary for mesh, texture, material and scene graph terms",
        "terms_expected_to_govern": ["texture", "mesh", "LOD", "alpha", "compositing"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not a claim that c_3 outputs glTF",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if asset format adoption is implied",
    },
    {
        "source_id": "epsg_registry",
        "prior_layer": "geospatial_prior",
        "authority_kind": "external_standard",
        "source_name": "EPSG Geodetic Parameter Dataset",
        "source_url_or_local_ref": "https://epsg.org/home.html",
        "why_relevant_to_c3": "authority source for CRS identifiers and coordinate reference vocabulary",
        "terms_expected_to_govern": ["CRS", "EPSG", "WGS84", "projection"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not coordinate correctness proof",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if CRS label becomes projection formula movement",
    },
    {
        "source_id": "rfc7946_geojson",
        "prior_layer": "geospatial_prior",
        "authority_kind": "external_standard",
        "source_name": "RFC 7946 GeoJSON",
        "source_url_or_local_ref": "https://www.rfc-editor.org/rfc/rfc7946",
        "why_relevant_to_c3": "standardized feature and geometry vocabulary for geospatial JSON-like terms",
        "terms_expected_to_govern": ["GeoJSON-like feature", "geometry", "bbox", "vector"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not a metadata schema adoption claim",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if JSON shape becomes product schema",
    },
    {
        "source_id": "ogc_tiles_candidate",
        "prior_layer": "geospatial_prior",
        "authority_kind": "external_standard",
        "source_name": "OGC tiles and geospatial standards family",
        "source_url_or_local_ref": "https://www.ogc.org/standards/",
        "why_relevant_to_c3": "standards family for tile, bbox, geometry and geospatial interoperability terms",
        "terms_expected_to_govern": ["tile", "bbox", "geometry", "projection"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not tile runtime implementation authorization",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if tile vocabulary implies cache or renderer behavior",
    },
    {
        "source_id": "w3c_wai_aria",
        "prior_layer": "uiux_prior",
        "authority_kind": "external_standard",
        "source_name": "W3C WAI-ARIA",
        "source_url_or_local_ref": "https://www.w3.org/TR/wai-aria-1.2/",
        "why_relevant_to_c3": "reference vocabulary for UI state and interaction roles",
        "terms_expected_to_govern": ["inspector", "selection", "visibility toggle", "tool mode"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not UI implementation authorization",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if semantic labels become UI widgets",
    },
    {
        "source_id": "material_design_layering_candidate",
        "prior_layer": "uiux_prior",
        "authority_kind": "external_mature_tool_model",
        "source_name": "Material Design interaction and layout vocabulary",
        "source_url_or_local_ref": "https://m3.material.io/",
        "why_relevant_to_c3": "mature UI vocabulary for panels, layers, navigation and interaction states",
        "terms_expected_to_govern": ["layer stack", "viewport", "timeline", "style panel"],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not a visual design system adoption claim",
        "future_dictionary_candidate": True,
        "stop_condition": "keep pending if terms collide with RRKAL renderer layers",
    },
    {
        "source_id": "web_performance_budget_candidate",
        "prior_layer": "runtime_budget_prior",
        "authority_kind": "external_mature_tool_model",
        "source_name": "Web performance budget model",
        "source_url_or_local_ref": "https://web.dev/articles/performance-budgets-101",
        "why_relevant_to_c3": "mature model for bounded frontend render and resource budget vocabulary",
        "terms_expected_to_govern": [
            "bounded query",
            "streaming",
            "batching",
            "cache",
            "tile",
            "bake",
            "memory budget",
            "frontend render budget",
        ],
        "adoption_status": "candidate_pending_review",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not performance readiness or benchmark claim",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if budget label becomes performance claim",
    },
    {
        "source_id": "rrkal_asset_card_governance",
        "prior_layer": "rrkal_governance_prior",
        "authority_kind": "rrkal_native_governance",
        "source_name": "RRKAL c_1 asset card governance",
        "source_url_or_local_ref": "local_ref: APIkeys_collection governance and RRKAL_displaytools docs index",
        "why_relevant_to_c3": "separates c_3 display semantics from mature c_1 asset ownership",
        "terms_expected_to_govern": ["c_1 asset card", "interface sovereignty", "temporary backdoor"],
        "adoption_status": "local_governance_reference_only",
        "rrkal_translation_needed": False,
        "forbidden_overread": "no direct c_3-to-c_1 maturity claim",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if c_3 directly integrates c_1 without c_4 mediation",
    },
    {
        "source_id": "rrkal_c4_render_consumption_card",
        "prior_layer": "rrkal_governance_prior",
        "authority_kind": "rrkal_native_governance",
        "source_name": "RRKAL c_4 render-consumption and Odoriba mediation governance",
        "source_url_or_local_ref": "local_ref: c_4/Odoriba governance docs and current c_3 source-lineage gates",
        "why_relevant_to_c3": "requires cross-organ language mediation before mature integration claims",
        "terms_expected_to_govern": ["c_4 render-consumption card", "source lineage", "no direct c_3-to-c_1 maturity claim"],
        "adoption_status": "local_governance_reference_only",
        "rrkal_translation_needed": False,
        "forbidden_overread": "no c_4/Odoriba implementation in this gate",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if Odoriba mediation is bypassed",
    },
    {
        "source_id": "legacy_mask_fossil_registry",
        "prior_layer": "legacy_fossil_translation",
        "authority_kind": "legacy_fossil_evidence",
        "source_name": "21k mask and occlusion legacy anatomy classification",
        "source_url_or_local_ref": "local_ref: docs/DISPLAYTOOLS_DYNAMIC_POINT_MASK_OCCLUSION_LEGACY_ANATOMY_CLASSIFICATION_GATE.zh-TW.md",
        "why_relevant_to_c3": "preserves fossil evidence while blocking direct legacy adoption",
        "terms_expected_to_govern": ["mask", "transparent-globe leak", "render_if_needed", "occlusion"],
        "adoption_status": "legacy_evidence_only",
        "rrkal_translation_needed": True,
        "forbidden_overread": "legacy fossil is not ideal form or final interface",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if legacy mask becomes prototype API",
    },
    {
        "source_id": "extracted_andesite_boundaries",
        "prior_layer": "legacy_fossil_translation",
        "authority_kind": "rrkal_native_governance",
        "source_name": "Extracted c_3 dynamic point semantic boundaries",
        "source_url_or_local_ref": "local_ref: render_core dynamic_point boundary helpers",
        "why_relevant_to_c3": "local cooled semantics for computed-hidden, presentation reduction and source-lineage guard",
        "terms_expected_to_govern": ["computed-but-hidden", "presentation reduction", "source-lineage guard"],
        "adoption_status": "local_semantic_evidence_not_final_api",
        "rrkal_translation_needed": True,
        "forbidden_overread": "not readiness or prototype final API",
        "future_dictionary_candidate": True,
        "stop_condition": "stop if extracted helpers are treated as final prototype API",
    },
]

DECISION_OUTPUT = {
    "international_law_registry_gate_passed": True,
    "external_authority_registry_created": True,
    "yaml_dictionary_authorized": False,
    "prior_card_schema_authorized": False,
    "prototype_authorized": False,
    "runtime_execution_authorized": False,
    "legacy_fossil_direct_adoption_authorized": False,
    "rrkal_native_terms_separated_from_external_authority": True,
    "readiness_claimed": False,
    "performance_claimed": False,
    "correctness_claimed": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_yaml_skeleton_planning_gate"

BOUNDARY_STATEMENT = (
    "Docs/test-only external authority-source registry gate for the future new c_3 semantic dictionary. "
    "This gate identifies the international law sources that future c_3 YAML prior dictionaries may reference. "
    "It does not create the dictionary, does not create prior cards, does not implement prototype/runtime/rendering behavior, "
    "does not adopt legacy 21k terms directly, does not claim readiness, and does not push."
)


def _registry_by_layer():
    result = {layer: [] for layer in PRIOR_LAYERS}
    for row in SOURCE_REGISTRY:
        result[row["prior_layer"]].append(row)
    return result


class C3PriorDictionaryInternationalLawRegistryTest(unittest.TestCase):
    def test_registry_rows_have_required_fields_and_authority_kinds(self) -> None:
        self.assertGreaterEqual(len(SOURCE_REGISTRY), len(PRIOR_LAYERS))
        for row in SOURCE_REGISTRY:
            self.assertEqual(set(REQUIRED_MATRIX_FIELDS), set(row))
            self.assertIn(row["prior_layer"], PRIOR_LAYERS)
            self.assertIn(row["authority_kind"], AUTHORITY_KINDS)
            self.assertIsInstance(row["terms_expected_to_govern"], list)
            self.assertTrue(row["source_id"])
            self.assertTrue(row["source_url_or_local_ref"])

    def test_required_prior_layers_are_covered(self) -> None:
        by_layer = _registry_by_layer()
        for layer in PRIOR_LAYERS:
            self.assertGreaterEqual(len(by_layer[layer]), 1, layer)

    def test_data_spacetime_prior_covers_required_terms(self) -> None:
        terms = {term for row in _registry_by_layer()["data_spacetime_prior"] for term in row["terms_expected_to_govern"]}
        for term in ["grid", "raster", "vector", "feature", "geometry", "time slice", "trajectory", "event", "point cloud"]:
            self.assertIn(term, terms)

    def test_graphics_prior_covers_required_terms_without_runtime_authorization(self) -> None:
        terms = {term for row in _registry_by_layer()["graphics_prior"] for term in row["terms_expected_to_govern"]}
        for term in ["camera", "view frame", "projection", "clipping", "alpha", "compositing", "LOD", "texture", "mesh", "framebuffer"]:
            self.assertIn(term, terms)
        for row in _registry_by_layer()["graphics_prior"]:
            self.assertIn("not", row["forbidden_overread"])

    def test_geospatial_uiux_runtime_and_governance_layers_are_separated(self) -> None:
        by_layer = _registry_by_layer()
        self.assertTrue(any(row["authority_kind"] == "external_standard" for row in by_layer["geospatial_prior"]))
        self.assertTrue(any(row["authority_kind"] in {"external_standard", "external_mature_tool_model"} for row in by_layer["uiux_prior"]))
        self.assertTrue(any("budget" in row["source_id"] for row in by_layer["runtime_budget_prior"]))
        self.assertTrue(all(row["authority_kind"] == "rrkal_native_governance" for row in by_layer["rrkal_governance_prior"]))
        self.assertFalse(DECISION_OUTPUT["runtime_execution_authorized"])

    def test_legacy_fossil_translation_does_not_authorize_direct_adoption(self) -> None:
        rows = _registry_by_layer()["legacy_fossil_translation"]
        self.assertTrue(any(row["authority_kind"] == "legacy_fossil_evidence" for row in rows))
        self.assertTrue(any("mask" in row["terms_expected_to_govern"] for row in rows))
        self.assertFalse(DECISION_OUTPUT["legacy_fossil_direct_adoption_authorized"])
        self.assertFalse(mask_anatomy.DECISION_OUTPUT["legacy_mask_implementation_is_ideal_form"])
        self.assertFalse(andesite_registry.SETTLEMENT_OUTPUT["runtime_replacement_authorized"])

    def test_static_scan_terms_are_accounted_for_without_forced_classification(self) -> None:
        governed_terms = {term for row in SOURCE_REGISTRY for term in row["terms_expected_to_govern"]}
        aliases = {
            "time": "time slice",
            "schema": "c_1 asset card",
            "source_lineage": "source lineage",
            "layer": "layer stack",
            "tile": "tile",
            "frame": "view frame",
            "mask": "mask",
            "occlusion": "occlusion",
            "projection": "projection",
            "LOD": "LOD",
            "bake": "cache",
            "alpha": "alpha",
            "grid": "grid",
            "trajectory": "trajectory",
        }
        unclassified_pending_o1_review = []
        for term in STATIC_SCAN_TERMS:
            mapped = aliases.get(term)
            if mapped not in governed_terms:
                unclassified_pending_o1_review.append(term)
        self.assertEqual(unclassified_pending_o1_review, [])

    def test_existing_extracted_boundary_evidence_remains_semantic_not_runtime(self) -> None:
        sampling_descriptor = sampling_visibility.dynamic_point_sampling_visibility_boundary_descriptor()
        count_descriptor = presentation_count.dynamic_point_presentation_count_boundary_descriptor()
        hidden_descriptor = computed_hidden.dynamic_point_computed_but_hidden_boundary_descriptor()
        lineage_descriptor = source_lineage.dynamic_point_source_lineage_guard_boundary_descriptor()
        reduction_descriptor = presentation_reduction.dynamic_point_presentation_reduction_boundary_descriptor()

        self.assertIn("frame_visibility_stop_line", sampling_descriptor["owned_semantics"])
        self.assertIn("source_loss_not_inferred", count_descriptor["owned_semantics"])
        self.assertIn("hidden_is_not_missing", hidden_descriptor["allowed_labels"])
        self.assertFalse(lineage_descriptor["guard_flags"]["source_lineage_mutation_authorized"])
        self.assertIn("presentation_or_sampling_reduction_candidate", reduction_descriptor["owned_semantics"])

    def test_decisions_block_dictionary_schema_runtime_and_claims(self) -> None:
        self.assertTrue(DECISION_OUTPUT["international_law_registry_gate_passed"])
        self.assertTrue(DECISION_OUTPUT["external_authority_registry_created"])
        self.assertTrue(DECISION_OUTPUT["rrkal_native_terms_separated_from_external_authority"])
        for key in [
            "yaml_dictionary_authorized",
            "prior_card_schema_authorized",
            "prototype_authorized",
            "runtime_execution_authorized",
            "legacy_fossil_direct_adoption_authorized",
            "readiness_claimed",
            "performance_claimed",
            "correctness_claimed",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)
        self.assertEqual(RECOMMENDED_NEXT_GATE, "c3_prior_semantic_dictionary_yaml_skeleton_planning_gate")

    def test_boundary_statement_is_docs_only(self) -> None:
        self.assertIn("Docs/test-only external authority-source registry gate", BOUNDARY_STATEMENT)
        self.assertIn("does not create the dictionary", BOUNDARY_STATEMENT)
        self.assertIn("does not implement prototype/runtime/rendering behavior", BOUNDARY_STATEMENT)
        self.assertIn("does not claim readiness", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
