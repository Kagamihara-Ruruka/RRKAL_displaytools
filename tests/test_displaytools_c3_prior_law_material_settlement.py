"""Docs/test-only settlement for c_3 prior-law materials.

This test classifies existing lab and product evidence into prior candidates,
authority references, legacy fossils, ideal-form embryos, and stop-lines before
any YAML prior dictionary, prior card schema, prototype, or runtime work.
"""

from pathlib import Path
import unittest

from tests import test_displaytools_c3_prior_dictionary_international_law_registry as international_law
from tests import test_displaytools_dynamic_point_andesite_registry_milestone_settlement as andesite_registry
from tests import test_displaytools_dynamic_point_mask_occlusion_legacy_anatomy_classification as mask_anatomy


LAB_EVIDENCE_PATHS = {
    "uiux_authority_scout": Path(r"L:\RRKAL_lab\external_research\analysis\a1_c3_photoshop_like_uiux_authority_scouting_note.zh-TW.md"),
    "uiux_phenomenon_translation_matrix": Path(r"L:\RRKAL_lab\external_research\analysis\a1_c3_uiux_phenomenon_translation_matrix.zh-TW.md"),
    "graphics_geospatial_prior_authority_scout": Path(r"L:\RRKAL_lab\external_research\analysis\a1_c3_graphics_geospatial_prior_authority_scout.zh-TW.md"),
    "legacy_fossil_translation_readonly_map": Path(r"L:\RRKAL_lab\evidence\c3_legacy_fossil_translation_readonly_map.md"),
    "c4_odoriba_c3_prior_handoff_position_scout": Path(r"L:\RRKAL_lab\external_research\analysis\c4_odoriba_c3_prior_handoff_position_scout.zh-TW.md"),
    "calcutta_shipyard_methodology_note": Path(r"L:\RRKAL_lab\external_research\analysis\o1_c3_calcutta_shipyard_methodology_note.zh-TW.md"),
}

PRODUCT_EVIDENCE_PATHS = {
    "prior_dictionary_international_law_registry_first_pass": Path("docs/DISPLAYTOOLS_C3_PRIOR_DICTIONARY_INTERNATIONAL_LAW_REGISTRY_GATE.zh-TW.md"),
    "andesite_registry_milestone_settlement": Path("docs/DISPLAYTOOLS_DYNAMIC_POINT_ANDESITE_REGISTRY_MILESTONE_SETTLEMENT_GATE.zh-TW.md"),
    "mask_occlusion_legacy_anatomy_classification": Path("docs/DISPLAYTOOLS_DYNAMIC_POINT_MASK_OCCLUSION_LEGACY_ANATOMY_CLASSIFICATION_GATE.zh-TW.md"),
}

SETTLEMENT_CATEGORIES = [
    "prior_dictionary_candidate",
    "authority_reference_only",
    "legacy_fossil_evidence",
    "ideal_form_embryo",
    "prototype_behavior_candidate",
    "schema_field_candidate",
    "validator_rule_candidate",
    "granite_stop_line",
    "unknown_stop_line",
    "not_yet_allowed",
]

MATERIAL_INVENTORY = [
    "uiux_phenomenon_translation_matrix",
    "graphics_geospatial_prior_authority_scout",
    "legacy_fossil_translation_readonly_map",
    "c4_odoriba_c3_prior_handoff_position_scout",
    "calcutta_shipyard_methodology_note",
    "prior_dictionary_international_law_registry_first_pass",
    "andesite_registry_milestone_settlement",
    "mask_occlusion_legacy_anatomy_classification",
]

P0_PHENOMENA = [
    "composition_stack_prior",
    "host_shell_docking_layout_prior",
    "viewport_camera_transformation_prior",
    "interaction_state_dispatcher_prior",
    "attributes_inspector_prior",
    "state_command_history_prior",
    "unified_command_dispatcher_prior",
    "temporal_playback_controller_prior",
    "tabular_data_inspector_prior",
    "plugin_extension_registry_prior",
    "host_shell_rendered_viewport_relation_stop_line",
    "legacy_mask_translation_prior",
    "crs_coordinate_projection_prior",
    "multiresolution_data_lod_prior",
    "declarative_alpha_compositing_policy",
    "view_family_prior",
    "c4_mediates_both_ingress_and_egress",
    "recipe_owns_truth_prior",
]

SETTLEMENT_MATRIX = [
    {
        "material_id": "uiux_phenomenon_translation_matrix",
        "categories": ["prior_dictionary_candidate", "schema_field_candidate", "validator_rule_candidate"],
        "accepted_prior_candidates": [
            "composition_stack_prior",
            "host_shell_docking_layout_prior",
            "rendered_viewport_ui_prior",
            "viewport_camera_transformation_prior",
            "interaction_state_dispatcher_prior",
            "attributes_inspector_prior",
            "state_command_history_prior",
            "unified_command_dispatcher_prior",
            "temporal_playback_controller_prior",
            "tabular_data_inspector_prior",
            "plugin_extension_registry_prior",
            "host_shell_rendered_viewport_relation_stop_line",
        ],
        "authority_reference_only": ["Photoshop", "QGIS", "Figma", "VS Code", "Blender", "JupyterLab"],
        "stop_lines": ["host_shell_rendered_viewport_relation_stop_line"],
        "why": "UIUX phenomena are translated into prior names; host shell UI and rendered viewport UI remain separate candidates.",
    },
    {
        "material_id": "graphics_geospatial_prior_authority_scout",
        "categories": ["prior_dictionary_candidate", "ideal_form_embryo", "granite_stop_line"],
        "accepted_prior_candidates": [
            "alpha_discard_mask_prior",
            "crs_coordinate_projection_prior",
            "multiresolution_data_lod_prior",
            "declarative_alpha_compositing_policy",
            "multispatial_coordinate_transform_prior",
            "globe_view",
            "map_projection_view",
            "time_series_view",
            "table_view",
            "multi_view_layout",
            "view_family_prior",
            "layered_occluding_body_visibility_contract",
        ],
        "authority_reference_only": ["Khronos", "OGC", "EPSG", "RFC 7946", "W3C Compositing"],
        "stop_lines": ["projection_formula_stop_line", "frame_buffer_truth_stop_line", "transparent_globe_leak_unresolved_stop_line"],
        "why": "Graphics and geospatial terms become vocabulary candidates, not correctness or runtime claims.",
    },
    {
        "material_id": "legacy_fossil_translation_readonly_map",
        "categories": ["legacy_fossil_evidence", "ideal_form_embryo", "granite_stop_line"],
        "accepted_prior_candidates": [
            "legacy_mask_translation_prior",
            "layered_occluding_body_visibility_contract",
            "hidden_is_not_missing",
            "presentation_or_sampling_reduction_candidate",
            "source_lineage_guard_boundary_reference",
        ],
        "authority_reference_only": [],
        "stop_lines": ["legacy_mask_direct_adoption_stop_line", "render_if_needed_runtime_stop_line", "alpha_compose_formula_stop_line"],
        "why": "21k terms are fossil evidence requiring translation before dictionary or prototype use.",
    },
    {
        "material_id": "c4_odoriba_c3_prior_handoff_position_scout",
        "categories": ["prior_dictionary_candidate", "validator_rule_candidate", "not_yet_allowed"],
        "accepted_prior_candidates": ["c4_mediates_both_ingress_and_egress", "interface_sovereignty_prior"],
        "authority_reference_only": ["RRKAL c_4/Odoriba governance"],
        "stop_lines": ["c4_implementation_change_stop_line", "direct_c3_to_c1_integration_stop_line"],
        "why": "c_4 mediation can be a governance prior candidate but not an implementation change.",
    },
    {
        "material_id": "calcutta_shipyard_methodology_note",
        "categories": ["prior_dictionary_candidate", "validator_rule_candidate", "authority_reference_only"],
        "accepted_prior_candidates": ["recipe_owns_truth_prior", "shipyard_recipe_validator_prior"],
        "authority_reference_only": ["Calcutta shipyard methodology"],
        "stop_lines": ["prototype_authorization_stop_line"],
        "why": "Recipe owns truth can guide dictionary validation, not prototype authorization.",
    },
    {
        "material_id": "prior_dictionary_international_law_registry_first_pass",
        "categories": ["authority_reference_only", "prior_dictionary_candidate"],
        "accepted_prior_candidates": ["external_authority_source_registry", "rrkal_native_governance_prior"],
        "authority_reference_only": ["STAC", "CF", "Khronos", "EPSG", "RFC 7946", "OGC", "W3C", "Material Design"],
        "stop_lines": ["yaml_creation_stop_line", "prior_card_schema_stop_line"],
        "why": "External authority sources are references for later dictionary planning, not adoption claims.",
    },
    {
        "material_id": "andesite_registry_milestone_settlement",
        "categories": ["prior_dictionary_candidate", "ideal_form_embryo", "granite_stop_line"],
        "accepted_prior_candidates": andesite_registry.MODERN_SEMANTIC_INTERFACES,
        "authority_reference_only": [],
        "stop_lines": andesite_registry.GRANITE_STOP_LINES,
        "why": "Five modern semantic interfaces are useful but still require translation before final prototype API.",
    },
    {
        "material_id": "mask_occlusion_legacy_anatomy_classification",
        "categories": ["legacy_fossil_evidence", "ideal_form_embryo", "granite_stop_line"],
        "accepted_prior_candidates": ["layered_occluding_body_visibility_contract"],
        "authority_reference_only": [],
        "stop_lines": ["legacy_mask_ideal_form_stop_line", "transparent_globe_leak_fault_stop_line"],
        "why": "Mask and occlusion anatomy supports ideal-form translation, not direct helper or prototype interface adoption.",
    },
]

ACCEPTED_PRIOR_CANDIDATES = [
    {"candidate_id": "composition_stack_prior", "category_tags": ["schema_field_candidate", "validator_rule_candidate"]},
    {"candidate_id": "host_shell_docking_layout_prior", "category_tags": ["schema_field_candidate"]},
    {"candidate_id": "rendered_viewport_ui_prior", "category_tags": ["schema_field_candidate", "prototype_behavior_candidate"]},
    {"candidate_id": "host_shell_rendered_viewport_relation_stop_line", "category_tags": ["unknown_stop_line", "stop-line"]},
    {"candidate_id": "globe_view", "category_tags": ["schema_field_candidate", "prototype_behavior_candidate"]},
    {"candidate_id": "map_projection_view", "category_tags": ["schema_field_candidate", "prototype_behavior_candidate"]},
    {"candidate_id": "time_series_view", "category_tags": ["schema_field_candidate", "prototype_behavior_candidate"]},
    {"candidate_id": "table_view", "category_tags": ["schema_field_candidate", "prototype_behavior_candidate"]},
    {"candidate_id": "multi_view_layout", "category_tags": ["schema_field_candidate", "validator_rule_candidate"]},
    {"candidate_id": "view_family_prior", "category_tags": ["schema_field_candidate", "validator_rule_candidate"]},
    {"candidate_id": "layered_occluding_body_visibility_contract", "category_tags": ["schema_field_candidate", "validator_rule_candidate", "ideal_form_embryo"]},
    {"candidate_id": "recipe_owns_truth_prior", "category_tags": ["validator_rule_candidate"]},
    {"candidate_id": "c4_mediates_both_ingress_and_egress", "category_tags": ["validator_rule_candidate"]},
    {"candidate_id": "external_authority_source_registry", "category_tags": ["schema_field_candidate"]},
    {"candidate_id": "rrkal_native_governance_prior", "category_tags": ["validator_rule_candidate"]},
    {"candidate_id": "source_lineage_guard_boundary_reference", "category_tags": ["validator_rule_candidate"]},
    {"candidate_id": "presentation_or_sampling_reduction_candidate", "category_tags": ["schema_field_candidate", "validator_rule_candidate"]},
    {"candidate_id": "legacy_mask_translation_prior", "category_tags": ["validator_rule_candidate", "stop-line"]},
]

HIGH_RISK_BARE_TERMS = ["layer", "mask", "view", "projection", "frame", "render", "recipe"]
HIGH_RISK_BARE_TERM_COUNT = 0

UNKNOWN_STOP_LINES = [
    "host_shell_rendered_viewport_relation_stop_line",
    "unclassified_cross_shell_contrast_relation",
]

STOP_LINE_TERMS = [
    "legacy_mask_direct_adoption_stop_line",
    "alpha_compose_formula_stop_line",
    "projection_formula_stop_line",
    "frame_buffer_truth_stop_line",
    "render_if_needed_runtime_stop_line",
    "renderer_controller_runtime_stop_line",
    "runtime_replacement_stop_line",
]

DECISION_OUTPUT = {
    "settlement_passed": True,
    "yaml_skeleton_planning_active_before_settlement": False,
    "yaml_skeleton_planning_recommended_after_pass": True,
    "graphics_geospatial_materials_incorporated": True,
    "legacy_mask_adopted_as_ideal_form": False,
    "layered_occluding_body_visibility_contract_prior_candidate": True,
    "layered_occluding_body_visibility_contract_implementation_authorized": False,
    "recipe_owns_truth_prior_candidate": True,
    "recipe_owns_truth_prototype_authorized": False,
    "c4_mediates_both_ingress_and_egress_governance_prior_candidate": True,
    "c4_implementation_change_authorized": False,
    "host_shell_ui_and_rendered_viewport_ui_separate_candidates": True,
    "contrast_relation_stop_line_or_relation_only": True,
    "view_family_candidates_not_product_readiness": True,
    "legacy_21k_status": "legacy_fossil_evidence_source_temporary_operational_renderer_not_blueprint",
    "readiness_claimed": False,
    "visual_correctness_claimed": False,
    "projection_correctness_claimed": False,
    "leak_fix_claimed": False,
    "runtime_replacement_authorized": False,
    "prototype_authorized": False,
}

RECOMMENDED_NEXT_GATE = "c3_prior_semantic_dictionary_yaml_skeleton_planning_gate"

BOUNDARY_STATEMENT = (
    "Docs/test-only c_3 prior law material settlement gate. This gate classifies existing lab and product evidence "
    "into prior candidates, references, fossils, ideal-form embryos, behavior/schema/validator candidates, and stop-lines. "
    "It does not create YAML dictionary, prior card schema, prototype code, renderer/runtime behavior, formula movement, "
    "repo topology change, readiness claim, correctness claim, leak-fix claim, or runtime replacement authorization."
)


class C3PriorLawMaterialSettlementTest(unittest.TestCase):
    def test_required_evidence_files_are_readable(self) -> None:
        for path in [*LAB_EVIDENCE_PATHS.values(), *PRODUCT_EVIDENCE_PATHS.values()]:
            self.assertTrue(path.exists(), str(path))
            text = path.read_text(encoding="utf-8")
            self.assertGreater(len(text), 100, str(path))

    def test_settlement_categories_and_material_inventory_are_complete(self) -> None:
        self.assertEqual(
            set(SETTLEMENT_CATEGORIES),
            {
                "prior_dictionary_candidate",
                "authority_reference_only",
                "legacy_fossil_evidence",
                "ideal_form_embryo",
                "prototype_behavior_candidate",
                "schema_field_candidate",
                "validator_rule_candidate",
                "granite_stop_line",
                "unknown_stop_line",
                "not_yet_allowed",
            },
        )
        self.assertEqual({row["material_id"] for row in SETTLEMENT_MATRIX}, set(MATERIAL_INVENTORY))

    def test_p0_phenomenon_coverage_is_complete_across_materials(self) -> None:
        all_candidates = {candidate for row in SETTLEMENT_MATRIX for candidate in row["accepted_prior_candidates"]}
        for phenomenon in P0_PHENOMENA:
            self.assertIn(phenomenon, all_candidates)

    def test_high_risk_bare_terms_are_not_accepted_as_prior_ids(self) -> None:
        candidate_ids = {candidate["candidate_id"] for candidate in ACCEPTED_PRIOR_CANDIDATES}
        self.assertEqual(HIGH_RISK_BARE_TERM_COUNT, 0)
        for bare_term in HIGH_RISK_BARE_TERMS:
            self.assertNotIn(bare_term, candidate_ids)

    def test_every_accepted_candidate_has_schema_validator_behavior_or_stop_line(self) -> None:
        accepted_tags = {
            "schema_field_candidate",
            "validator_rule_candidate",
            "prototype_behavior_candidate",
            "stop-line",
            "unknown_stop_line",
        }
        for candidate in ACCEPTED_PRIOR_CANDIDATES:
            self.assertTrue(set(candidate["category_tags"]) & accepted_tags, candidate["candidate_id"])

    def test_unknown_terms_are_assigned_to_unknown_stop_line(self) -> None:
        self.assertIn("host_shell_rendered_viewport_relation_stop_line", UNKNOWN_STOP_LINES)
        self.assertIn("unclassified_cross_shell_contrast_relation", UNKNOWN_STOP_LINES)
        relation_candidate = next(c for c in ACCEPTED_PRIOR_CANDIDATES if c["candidate_id"] == "host_shell_rendered_viewport_relation_stop_line")
        self.assertIn("unknown_stop_line", relation_candidate["category_tags"])

    def test_required_decisions_are_settled_without_authorizing_implementation(self) -> None:
        self.assertFalse(DECISION_OUTPUT["yaml_skeleton_planning_active_before_settlement"])
        self.assertFalse(DECISION_OUTPUT["legacy_mask_adopted_as_ideal_form"])
        self.assertTrue(DECISION_OUTPUT["layered_occluding_body_visibility_contract_prior_candidate"])
        self.assertFalse(DECISION_OUTPUT["layered_occluding_body_visibility_contract_implementation_authorized"])
        self.assertTrue(DECISION_OUTPUT["recipe_owns_truth_prior_candidate"])
        self.assertFalse(DECISION_OUTPUT["recipe_owns_truth_prototype_authorized"])
        self.assertTrue(DECISION_OUTPUT["c4_mediates_both_ingress_and_egress_governance_prior_candidate"])
        self.assertFalse(DECISION_OUTPUT["c4_implementation_change_authorized"])
        self.assertTrue(DECISION_OUTPUT["host_shell_ui_and_rendered_viewport_ui_separate_candidates"])
        self.assertTrue(DECISION_OUTPUT["contrast_relation_stop_line_or_relation_only"])
        self.assertTrue(DECISION_OUTPUT["view_family_candidates_not_product_readiness"])

    def test_stop_line_terms_remain_closed(self) -> None:
        for stop_line in [
            "legacy_mask_direct_adoption_stop_line",
            "alpha_compose_formula_stop_line",
            "projection_formula_stop_line",
            "frame_buffer_truth_stop_line",
            "render_if_needed_runtime_stop_line",
        ]:
            self.assertIn(stop_line, STOP_LINE_TERMS)
        self.assertFalse(mask_anatomy.DECISION_OUTPUT["legacy_mask_implementation_is_ideal_form"])
        self.assertFalse(mask_anatomy.DECISION_OUTPUT["transparent_globe_leak_fix_claimed"])
        self.assertFalse(andesite_registry.SETTLEMENT_OUTPUT["runtime_replacement_authorized"])

    def test_no_material_claims_readiness_correctness_leak_fix_runtime_replacement_or_prototype_authorization(self) -> None:
        for key in [
            "readiness_claimed",
            "visual_correctness_claimed",
            "projection_correctness_claimed",
            "leak_fix_claimed",
            "runtime_replacement_authorized",
            "prototype_authorized",
        ]:
            self.assertFalse(DECISION_OUTPUT[key], key)
        self.assertFalse(international_law.DECISION_OUTPUT["prototype_authorized"])
        self.assertFalse(international_law.DECISION_OUTPUT["runtime_execution_authorized"])

    def test_yaml_skeleton_next_gate_requires_graphics_geospatial_incorporation(self) -> None:
        self.assertTrue(DECISION_OUTPUT["settlement_passed"])
        self.assertTrue(DECISION_OUTPUT["graphics_geospatial_materials_incorporated"])
        self.assertTrue(DECISION_OUTPUT["yaml_skeleton_planning_recommended_after_pass"])
        self.assertEqual(RECOMMENDED_NEXT_GATE, "c3_prior_semantic_dictionary_yaml_skeleton_planning_gate")

    def test_boundary_statement_blocks_scope_expansion(self) -> None:
        self.assertIn("Docs/test-only c_3 prior law material settlement gate", BOUNDARY_STATEMENT)
        self.assertIn("does not create YAML dictionary", BOUNDARY_STATEMENT)
        self.assertIn("does not create", BOUNDARY_STATEMENT)
        self.assertIn("runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
