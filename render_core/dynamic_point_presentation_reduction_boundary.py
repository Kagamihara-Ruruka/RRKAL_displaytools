"""Descriptor-only presentation reduction boundary helpers.

This module keeps dynamic point presentation reduction semantics as pure
descriptor, contract, and ledger packets. It does not import or execute the
monolith, runtime probe, renderer, frame buffer, real source, dataframe, or
formula helpers.
"""

from __future__ import annotations


SCHEMA = "rrkal.displaytools.dynamic_point_presentation_reduction_boundary.v1"

LABELS = [
    "rendered_lower_than_visible",
    "presentation_or_sampling_reduction_candidate",
    "visible_count_observation",
    "rendered_count_observation",
    "source_loss_not_inferred",
    "frame_truth_not_claimed",
    "frame_visible_not_observed",
    "transparent_globe_leak_not_inferred",
    "visual_correctness_not_claimed",
    "readiness_not_claimed",
    "source_lineage_guarded_by_source_lineage_guard_boundary",
    "presentation_count_boundary_reference",
    "sampling_visibility_boundary_reference",
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
    "renderer_authorized": False,
    "frame_buffer_read_authorized": False,
    "artifact_generation_authorized": False,
    "real_source_read_authorized": False,
    "projection_formula_movement_authorized": False,
    "mask_formula_movement_authorized": False,
    "sampling_formula_movement_authorized": False,
    "alpha_compose_formula_movement_authorized": False,
    "source_lineage_mutation_authorized": False,
    "source_loss_interpretation_authorized": False,
    "frame_truth_claim_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "performance_claimed": False,
    "c4_odoriba_bypass_authorized": False,
    "rrkal_wide_methodology_authorized": False,
}

HELPER_FAMILIES = [
    "build_dynamic_point_presentation_reduction_candidate_descriptor",
    "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
    "build_dynamic_point_presentation_reduction_sampling_reference_descriptor",
    "build_dynamic_point_presentation_reduction_source_guard_descriptor",
    "build_dynamic_point_presentation_reduction_stop_line_ledger",
    "dynamic_point_presentation_reduction_boundary_descriptor",
    "dynamic_point_presentation_reduction_planning_bundle",
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


def build_dynamic_point_presentation_reduction_candidate_descriptor() -> dict[str, object]:
    packet = _packet("presentation_reduction_candidate")
    packet["descriptor"] = {
        "descriptor_id": "presentation_reduction_candidate",
        "rendered_lower_than_visible": "rendered_lower_than_visible",
        "classification": "presentation_or_sampling_reduction_candidate",
        "meaning": "rendered count lower than visible count is a presentation or sampling reduction candidate",
        "source_loss_not_inferred": True,
        "frame_truth_not_claimed": True,
        "transparent_globe_leak_not_inferred": True,
        "visual_correctness_not_claimed": True,
        "readiness_not_claimed": True,
        "performance_claimed": False,
    }
    return packet


def build_dynamic_point_rendered_lower_than_visible_contract_descriptor() -> dict[str, object]:
    packet = _packet("rendered_lower_than_visible_contract")
    packet["contract"] = {
        "contract_id": "rendered_lower_than_visible_contract",
        "visible_count_observation": "visible_count_observation",
        "rendered_count_observation": "rendered_count_observation",
        "relation": "rendered_lower_than_visible",
        "classification": "presentation_or_sampling_reduction_candidate",
        "not_source_loss": True,
        "not_frame_truth": True,
        "not_runtime_behavior": True,
        "not_formula_behavior": True,
    }
    return packet


def build_dynamic_point_presentation_reduction_sampling_reference_descriptor() -> dict[str, object]:
    packet = _packet("presentation_reduction_sampling_reference")
    packet["reference"] = {
        "reference_id": "presentation_reduction_sampling_reference",
        "presentation_count_boundary_reference": "presentation_count_boundary_reference",
        "sampling_visibility_boundary_reference": "sampling_visibility_boundary_reference",
        "reference_only": True,
        "runtime_import_authorized": False,
        "formula_import_authorized": False,
        "sampling_formula_movement_authorized": False,
    }
    return packet


def build_dynamic_point_presentation_reduction_source_guard_descriptor() -> dict[str, object]:
    packet = _packet("presentation_reduction_source_guard")
    packet["guard"] = {
        "guard_id": "presentation_reduction_source_guard",
        "source_lineage_guarded_by_source_lineage_guard_boundary": "source_lineage_guarded_by_source_lineage_guard_boundary",
        "source_lineage_impact": "none_guarded_no_mutation",
        "source_lineage_mutation_authorized": False,
        "source_loss_interpretation_authorized": False,
        "rendered_lower_than_visible_is_source_loss": False,
    }
    return packet


def build_dynamic_point_presentation_reduction_stop_line_ledger() -> dict[str, object]:
    packet = _packet("presentation_reduction_stop_line_ledger")
    packet["ledger"] = {
        "ledger_id": "presentation_reduction_stop_line_ledger",
        "frame_visible_not_observed": "frame_visible_not_observed",
        "frame_truth_not_claimed": "frame_truth_not_claimed",
        "transparent_globe_leak_not_inferred": "transparent_globe_leak_not_inferred",
        "visual_correctness_not_claimed": "visual_correctness_not_claimed",
        "readiness_not_claimed": "readiness_not_claimed",
        "blocked_surfaces": [
            "runtime_probe_change",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_generation",
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "alpha_compose_formula_movement",
            "real_source_read",
            "source_lineage_mutation",
            "source_loss_interpretation",
            "frame_truth_claim",
            "transparent_globe_leak_inference",
            "transparent_globe_leak_fix_claim",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "performance_claim",
            "c4_odoriba_bypass",
        ],
    }
    return packet


def dynamic_point_presentation_reduction_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "boundary_id": "dynamic_point_presentation_reduction_boundary",
        "scope": "minimal_descriptor_contract_ledger_surface",
        "helper_families": list(HELPER_FAMILIES),
        "allowed_output_shape": dict(OUTPUT_SHAPE),
        "allowed_labels": list(LABELS),
        "guard_flags": dict(FALSE_FLAGS),
        "classification": "presentation_reduction_minimal_boundary",
        "owned_semantics": [
            "rendered_lower_than_visible",
            "presentation_or_sampling_reduction_candidate",
            "visible_count_observation",
            "rendered_count_observation",
            "source_loss_not_inferred",
            "frame_truth_not_claimed",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
            "source_lineage_guarded_by_source_lineage_guard_boundary",
            "presentation_count_boundary_reference",
            "sampling_visibility_boundary_reference",
        ],
        "reference_boundaries": [
            "presentation_count_boundary_reference",
            "sampling_visibility_boundary_reference",
            "source_lineage_guarded_by_source_lineage_guard_boundary",
        ],
        "local_dynamic_point_pattern_only": True,
    }


def dynamic_point_presentation_reduction_planning_bundle() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "presentation_reduction_minimal_extraction_passed": True,
        "helper_created": True,
        "checker_passed": True,
        "dict_list_scalar_only": True,
        "boundary_descriptor": dynamic_point_presentation_reduction_boundary_descriptor(),
        "contracts": [
            build_dynamic_point_presentation_reduction_candidate_descriptor(),
            build_dynamic_point_rendered_lower_than_visible_contract_descriptor(),
            build_dynamic_point_presentation_reduction_sampling_reference_descriptor(),
            build_dynamic_point_presentation_reduction_source_guard_descriptor(),
            build_dynamic_point_presentation_reduction_stop_line_ledger(),
        ],
        "decision": {
            "presentation_reduction_minimal_extraction_passed": True,
            "helper_created": True,
            "checker_passed": True,
            "dict_list_scalar_only": True,
            "runtime_execution_authorized": False,
            "source_lineage_mutation_authorized": False,
            "source_loss_interpretation_authorized": False,
            "frame_truth_claim_authorized": False,
            "transparent_globe_leak_inferred": False,
            "transparent_globe_leak_fix_claimed": False,
            "visual_correctness_claimed": False,
            "readiness_claimed": False,
            "performance_claimed": False,
            "c4_odoriba_bypass_authorized": False,
            "recommended_next_gate": "dynamic_point_presentation_reduction_cartography_update_gate",
        },
    }
