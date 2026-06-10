"""Descriptor-only source-lineage guard boundary helpers.

This module keeps dynamic point source identity and lineage guard semantics as
pure descriptor, contract, and ledger packets. It does not import or execute the
monolith, runtime probe, renderer, real source, dataframe, frame-buffer, or
formula helpers.
"""

from __future__ import annotations


SCHEMA = "rrkal.displaytools.dynamic_point_source_lineage_guard_boundary.v1"

LABELS = [
    "source_present_token",
    "source_label",
    "point_id",
    "source_lineage_integrity_token",
    "payload_identity_guard",
    "sampling_does_not_mutate_source",
    "presentation_count_does_not_mutate_source",
    "hidden_visibility_does_not_mutate_source",
    "mask_visibility_does_not_mutate_source",
    "occlusion_visibility_does_not_mutate_source",
    "reduced_count_is_not_source_loss",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "controlled_raw_row_compatibility_seam",
    "developmental_compensation_surface",
    "future_c4_odoriba_handoff_material",
    "direct_c1_integration_not_authorized",
]

OUTPUT_SHAPE = {
    "nested_dict": True,
    "list": True,
    "scalar": True,
    "callable": False,
    "runtime_object": False,
    "dataframe": False,
    "renderer_buffer": False,
    "file_handle": False,
    "network_object": False,
    "sql_cache_object": False,
    "live_source_object": False,
    "c1_object": False,
    "c4_odoriba_object": False,
}

FALSE_FLAGS = {
    "runtime_execution_authorized": False,
    "runtime_probe_change_authorized": False,
    "monolith_import_authorized": False,
    "render_if_needed_authorized": False,
    "controller_authorized": False,
    "render_host_authorized": False,
    "frame_surface_read_authorized": False,
    "artifact_generation_authorized": False,
    "real_source_read_authorized": False,
    "projection_formula_movement_authorized": False,
    "mask_formula_movement_authorized": False,
    "sampling_formula_movement_authorized": False,
    "alpha_formula_movement_authorized": False,
    "source_lineage_mutation_authorized": False,
    "hidden_as_missing_authorized": False,
    "reduced_count_as_source_loss_authorized": False,
    "occluded_as_source_loss_authorized": False,
    "raw_row_runtime_authorized": False,
    "raw_row_mature_c1_integration_authorized": False,
    "direct_c1_integration_authorized": False,
    "direct_c3_to_c1_dependency_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
}

PROTECTED_SURFACES = [
    "sampling_visibility_boundary",
    "presentation_count_boundary",
    "computed_but_hidden_boundary",
    "mask_visibility_contract",
    "occlusion_responsibility_contract",
]


def _packet(surface: str) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "surface": surface,
        "scope": "descriptor_contract_ledger_only",
        "allowed_output_shape": dict(OUTPUT_SHAPE),
        "allowed_labels": list(LABELS),
        "guard_flags": dict(FALSE_FLAGS),
    }


def build_dynamic_point_source_identity_contract_descriptor() -> dict[str, object]:
    packet = _packet("source_identity_contract")
    packet["contract"] = {
        "contract_id": "source_identity_contract",
        "source_present_token": {
            "label": "source_present_token",
            "meaning": "source presence, not frame visibility",
            "frame_visibility_interpretation_allowed": False,
        },
        "source_label": {
            "label": "source_label",
            "meaning": "lineage label, not mature c_1 asset object",
            "mature_c1_asset_object": False,
        },
        "point_id": {
            "label": "point_id",
            "meaning": "identity token, not renderer identity",
            "renderer_identity": False,
        },
        "protected_surfaces": list(PROTECTED_SURFACES),
    }
    return packet


def build_dynamic_point_source_lineage_integrity_descriptor() -> dict[str, object]:
    packet = _packet("source_lineage_integrity_token")
    packet["contract"] = {
        "contract_id": "source_lineage_integrity_token",
        "integrity_token": "source_lineage_integrity_token",
        "must_remain_stable_across": [
            "sampling_does_not_mutate_source",
            "presentation_count_does_not_mutate_source",
            "hidden_visibility_does_not_mutate_source",
            "mask_visibility_does_not_mutate_source",
            "occlusion_visibility_does_not_mutate_source",
        ],
        "source_lineage_mutation_authorized": False,
        "dependency_cycle_watch_enabled": True,
    }
    return packet


def build_dynamic_point_payload_identity_guard_descriptor() -> dict[str, object]:
    packet = _packet("payload_identity_guard")
    packet["contract"] = {
        "contract_id": "payload_identity_guard",
        "owned_labels": [
            "source_label",
            "point_id",
            "payload_identity_guard",
            "source_lineage_integrity_token",
        ],
        "payload_identity_guard": True,
        "visibility_state_can_rewrite_payload_identity": False,
        "presentation_state_can_rewrite_payload_identity": False,
        "raw_row_state_can_rewrite_payload_identity": False,
    }
    return packet


def build_dynamic_point_sampling_source_guard_descriptor() -> dict[str, object]:
    packet = _packet("sampling_source_guard")
    packet["guard"] = {
        "guard_id": "sampling_source_guard",
        "owned_label": "sampling_does_not_mutate_source",
        "protected_helper": "sampling_visibility_boundary",
        "sampling_does_not_mutate_source": True,
        "reduced_count_is_not_source_loss": True,
        "source_loss_interpretation_allowed": False,
    }
    return packet


def build_dynamic_point_presentation_count_source_guard_descriptor() -> dict[str, object]:
    packet = _packet("presentation_count_source_guard")
    packet["guard"] = {
        "guard_id": "presentation_count_source_guard",
        "owned_label": "presentation_count_does_not_mutate_source",
        "protected_helper": "presentation_count_boundary",
        "presentation_count_does_not_mutate_source": True,
        "reduced_count_is_not_source_loss": True,
        "source_loss_interpretation_allowed": False,
    }
    return packet


def build_dynamic_point_hidden_visibility_source_guard_descriptor() -> dict[str, object]:
    packet = _packet("hidden_visibility_source_guard")
    packet["guard"] = {
        "guard_id": "hidden_visibility_source_guard",
        "owned_label": "hidden_visibility_does_not_mutate_source",
        "protected_helper": "computed_but_hidden_boundary",
        "hidden_visibility_does_not_mutate_source": True,
        "hidden_is_not_missing": True,
        "source_loss_interpretation_allowed": False,
    }
    return packet


def build_dynamic_point_mask_occlusion_source_guard_descriptor() -> dict[str, object]:
    packet = _packet("mask_occlusion_source_guard")
    packet["guard"] = {
        "guard_id": "mask_occlusion_source_guard",
        "owned_labels": [
            "mask_visibility_does_not_mutate_source",
            "occlusion_visibility_does_not_mutate_source",
            "occluded_is_not_source_lineage_loss",
        ],
        "mask_visibility_does_not_mutate_source": True,
        "occlusion_visibility_does_not_mutate_source": True,
        "occluded_is_not_source_lineage_loss": True,
        "source_loss_interpretation_allowed": False,
    }
    return packet


def build_dynamic_point_raw_row_compatibility_seam_descriptor() -> dict[str, object]:
    packet = _packet("controlled_raw_row_compatibility_seam")
    packet["contract"] = {
        "contract_id": "controlled_raw_row_compatibility_seam",
        "owned_labels": [
            "controlled_raw_row_compatibility_seam",
            "developmental_compensation_surface",
            "future_c4_odoriba_handoff_material",
            "direct_c1_integration_not_authorized",
        ],
        "label_ledger_handoff_material_only": True,
        "controlled_raw_row_compatibility_seam_label_allowed": True,
        "controlled_raw_row_compatibility_seam_runtime_authorized": False,
        "mature_c1_integration": False,
        "direct_c1_integration_authorized": False,
        "future_c4_odoriba_handoff_material": True,
        "c4_odoriba_mediation_required": True,
        "c4_odoriba_bypass_authorized": False,
    }
    return packet


def build_dynamic_point_source_lineage_guard_stop_line_ledger() -> dict[str, object]:
    packet = _packet("source_lineage_guard_stop_line_ledger")
    packet["ledger"] = {
        "ledger_id": "source_lineage_guard_stop_line_ledger",
        "blocked_surfaces": [
            "runtime_probe_change",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_generation",
            "real_source_read",
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "alpha_formula_movement",
            "source_lineage_mutation",
            "hidden_as_missing_interpretation",
            "reduced_count_as_source_loss_interpretation",
            "occluded_as_source_lineage_loss_interpretation",
            "raw_row_seam_runtime_authorization",
            "raw_row_seam_promotion_to_mature_c1_integration",
            "direct_c3_to_c1_dependency_authorization",
            "c4_odoriba_bypass",
            "transparent_globe_leak_inference",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "leak_fix_claim",
            "rrkal_wide_methodology_promotion",
        ],
        "source_lineage_mutation_authorized": False,
        "transparent_globe_leak_inferred": False,
        "readiness_claimed": False,
        "dependency_cycle_watch_enabled": True,
    }
    return packet


def dynamic_point_source_lineage_guard_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "boundary_id": "dynamic_point_source_lineage_guard_boundary",
        "scope": "minimal_descriptor_contract_ledger_surface",
        "helper_families": [
            "build_dynamic_point_source_identity_contract_descriptor",
            "build_dynamic_point_source_lineage_integrity_descriptor",
            "build_dynamic_point_payload_identity_guard_descriptor",
            "build_dynamic_point_sampling_source_guard_descriptor",
            "build_dynamic_point_presentation_count_source_guard_descriptor",
            "build_dynamic_point_hidden_visibility_source_guard_descriptor",
            "build_dynamic_point_mask_occlusion_source_guard_descriptor",
            "build_dynamic_point_raw_row_compatibility_seam_descriptor",
            "build_dynamic_point_source_lineage_guard_stop_line_ledger",
            "dynamic_point_source_lineage_guard_boundary_descriptor",
            "dynamic_point_source_lineage_guard_planning_bundle",
        ],
        "allowed_output_shape": dict(OUTPUT_SHAPE),
        "allowed_labels": list(LABELS),
        "protected_surfaces": list(PROTECTED_SURFACES),
        "guard_flags": dict(FALSE_FLAGS),
        "classification": "source_lineage_guard_minimal_boundary",
        "local_dynamic_point_pattern_only": True,
    }


def dynamic_point_source_lineage_guard_planning_bundle() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "source_lineage_guard_minimal_extraction_passed": True,
        "helper_created": True,
        "checker_passed": True,
        "dict_list_scalar_only": True,
        "boundary_descriptor": dynamic_point_source_lineage_guard_boundary_descriptor(),
        "contracts": [
            build_dynamic_point_source_identity_contract_descriptor(),
            build_dynamic_point_source_lineage_integrity_descriptor(),
            build_dynamic_point_payload_identity_guard_descriptor(),
            build_dynamic_point_sampling_source_guard_descriptor(),
            build_dynamic_point_presentation_count_source_guard_descriptor(),
            build_dynamic_point_hidden_visibility_source_guard_descriptor(),
            build_dynamic_point_mask_occlusion_source_guard_descriptor(),
            build_dynamic_point_raw_row_compatibility_seam_descriptor(),
            build_dynamic_point_source_lineage_guard_stop_line_ledger(),
        ],
        "decision": {
            "source_lineage_guard_minimal_extraction_passed": True,
            "helper_created": True,
            "checker_passed": True,
            "dict_list_scalar_only": True,
            "runtime_execution_authorized": False,
            "source_lineage_mutation_authorized": False,
            "controlled_raw_row_compatibility_seam_label_allowed": True,
            "controlled_raw_row_compatibility_seam_runtime_authorized": False,
            "direct_c1_integration_authorized": False,
            "c4_odoriba_mediation_required": True,
            "c4_odoriba_bypass_authorized": False,
            "dependency_cycle_watch_enabled": True,
            "recommended_next_gate": "dynamic_point_source_lineage_guard_cartography_update_gate",
        },
    }
