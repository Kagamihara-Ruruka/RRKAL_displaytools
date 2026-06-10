"""Presentation count boundary descriptors for dynamic point LOD view-frame work.

This module is intentionally data-only. It records cooled descriptor,
contract, and ledger semantics for presentation counts without importing or
executing renderer, runtime, frame-buffer, projection, mask, or sampling logic.
"""


def build_dynamic_point_visible_count_contract_descriptor():
    return {
        "helper": "build_dynamic_point_visible_count_contract_descriptor",
        "surface": "presentation_count_contract",
        "contract_field": "visible_count",
        "observation_label": "visible_count_observation",
        "semantic_meaning": "count contract field observed before frame truth",
        "not_source_completeness": True,
        "source_lineage_guard": "source_lineage_integrity_token",
        "source_loss_status": "source_loss_not_inferred",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "output_shape": "dict_list_scalar_only",
    }


def build_dynamic_point_rendered_count_contract_descriptor():
    return {
        "helper": "build_dynamic_point_rendered_count_contract_descriptor",
        "surface": "presentation_count_contract",
        "contract_field": "rendered_count",
        "observation_label": "rendered_count_observation",
        "semantic_meaning": "count contract field, not renderer frame truth",
        "not_frame_truth": True,
        "source_lineage_guard": "source_lineage_integrity_token",
        "source_loss_status": "source_loss_not_inferred",
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "output_shape": "dict_list_scalar_only",
    }


def build_dynamic_point_presentation_reduction_candidate_descriptor():
    return {
        "helper": "build_dynamic_point_presentation_reduction_candidate_descriptor",
        "surface": "presentation_count_contract",
        "comparison_label": "rendered_lower_than_visible",
        "classification": "sampling_or_presentation_reduction_candidate",
        "allowed_interpretation": "rendered_count lower than visible_count is a reduction candidate",
        "forbidden_interpretation": "source loss is not inferred from rendered_count lower than visible_count",
        "source_loss_status": "source_loss_not_inferred",
        "source_loss_interpretation_allowed": False,
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "output_shape": "dict_list_scalar_only",
    }


def build_dynamic_point_presentation_count_source_lineage_guard_descriptor():
    return {
        "helper": "build_dynamic_point_presentation_count_source_lineage_guard_descriptor",
        "surface": "presentation_count_contract",
        "guard_token": "source_lineage_integrity_token",
        "source_lineage_impact": "guard_only_no_mutation",
        "source_loss_status": "source_loss_not_inferred",
        "count_fields_do_not_delete_source": True,
        "sampling_or_mask_do_not_mutate_source": True,
        "renderer_frame_dependency": "none",
        "formula_dependency": "none",
        "output_shape": "dict_list_scalar_only",
    }


def build_dynamic_point_presentation_count_stop_line_ledger():
    return {
        "helper": "build_dynamic_point_presentation_count_stop_line_ledger",
        "surface": "frame_and_leak_stop_line",
        "frame_visibility": "frame_visible_not_observed",
        "transparent_globe_leak": "transparent_globe_leak_not_inferred",
        "transparent_globe_leak_fix_claimed": False,
        "visual_correctness": "visual_correctness_not_claimed",
        "coordinate_correctness_claimed": False,
        "readiness": "readiness_not_claimed",
        "frame_buffer_read": False,
        "renderer_executed": False,
        "renderer_frame_dependency": "blocked_stop_line_only",
        "formula_dependency": "none",
        "output_shape": "dict_list_scalar_only",
    }


def dynamic_point_presentation_count_boundary_descriptor():
    return {
        "boundary": "dynamic_point_presentation_count_boundary",
        "scope": "descriptor_contract_ledger_only",
        "owned_semantics": [
            "visible_count",
            "rendered_count",
            "visible_count_observation",
            "rendered_count_observation",
            "rendered_lower_than_visible",
            "sampling_or_presentation_reduction_candidate",
            "presentation_count_contract",
            "source_lineage_integrity_token",
            "source_loss_not_inferred",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
        ],
        "allowed_outputs": ["dict", "list", "scalar"],
        "blocked_actions": [
            "runtime_probe_change",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_write",
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "source_loss_interpretation",
            "transparent_globe_leak_inference",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "leak_fix_claim",
        ],
        "local_dynamic_point_pattern_only": True,
    }


def dynamic_point_presentation_count_planning_bundle():
    return {
        "minimal_extraction_gate_passed": True,
        "helper_created": True,
        "checker_protected": True,
        "output_shape": "dict_list_scalar_only",
        "descriptors": [
            build_dynamic_point_visible_count_contract_descriptor(),
            build_dynamic_point_rendered_count_contract_descriptor(),
            build_dynamic_point_presentation_reduction_candidate_descriptor(),
            build_dynamic_point_presentation_count_source_lineage_guard_descriptor(),
            build_dynamic_point_presentation_count_stop_line_ledger(),
            dynamic_point_presentation_count_boundary_descriptor(),
        ],
        "runtime_execution_authorized": False,
        "runtime_probe_change_authorized": False,
        "formula_movement_authorized": False,
        "renderer_frame_buffer_authorized": False,
        "source_loss_interpretation_authorized": False,
        "transparent_globe_leak_inferred": False,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "readiness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
        "rrkal_wide_methodology_authorized": False,
    }
