"""Descriptor-only sampling visibility boundary helpers.

This module intentionally contains no runtime imports and no renderer access. It
only returns dict, list, and scalar contract packets for the observed dynamic
point sampling / visibility bridge.
"""

SCHEMA = "rrkal.displaytools.dynamic_point_sampling_visibility_boundary.v1"


OBSERVATION_LABELS = [
    "sampled_visible_token",
    "visible_count_observation",
    "rendered_count_observation",
    "mask_visible_token",
    "source_lineage_integrity_token",
    "frame_visible_not_observed",
    "transparent_globe_leak_not_inferred",
]


def build_dynamic_point_sampling_visibility_observation_descriptor():
    return {
        "schema": SCHEMA,
        "descriptor": "dynamic_point_sampling_visibility_observation",
        "observed_tokens": [
            "sampled_visible_token",
            "visible_count_observation",
            "rendered_count_observation",
            "mask_visible_token",
            "source_lineage_integrity_token",
        ],
        "not_observed_tokens": [
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
        ],
        "observed_bridge": {
            "sampled_visible_token": True,
            "visible_count_observation": 2,
            "rendered_count_observation": 1,
            "mask_visible_token": True,
            "source_lineage_integrity_token": True,
        },
        "runtime_execution_authorized": False,
        "formula_movement_authorized": False,
    }


def build_dynamic_point_visibility_count_contract_descriptor():
    return {
        "schema": SCHEMA,
        "descriptor": "dynamic_point_visibility_count_contract",
        "fields": [
            "source_present",
            "projected_visible",
            "sampled_visible",
            "visible_count",
            "rendered_count",
            "mask_visible",
            "source_lineage_integrity",
            "frame_visible",
        ],
        "count_semantics": {
            "visible_count_observation": "observed_scalar",
            "rendered_count_observation": "observed_scalar",
            "sampling_or_presentation_reduction_candidate": True,
        },
        "frame_visible": "frame_visible_not_observed",
        "source_lineage_guard": True,
    }


def build_dynamic_point_mask_visibility_contract_descriptor():
    return {
        "schema": SCHEMA,
        "descriptor": "dynamic_point_mask_visibility_contract",
        "tokens": ["mask_visible_token", "source_lineage_integrity_token"],
        "mask_true_semantics": "mask_visible_token",
        "mask_false_semantics": "globe_mask_responsibility_candidate",
        "source_deletion_interpretation_allowed": False,
        "source_lineage_guard": True,
    }


def build_dynamic_point_sampling_reduction_contract_descriptor():
    return {
        "schema": SCHEMA,
        "descriptor": "dynamic_point_sampling_reduction_contract",
        "visible_count_observation": 2,
        "rendered_count_observation": 1,
        "reduction_label": "sampling_or_presentation_reduction_candidate",
        "source_loss_interpretation_allowed": False,
        "formula_movement_authorized": False,
    }


def build_dynamic_point_frame_visibility_stop_line_descriptor():
    return {
        "schema": SCHEMA,
        "descriptor": "dynamic_point_frame_visibility_stop_line",
        "frame_visible": "frame_visible_not_observed",
        "blocked_surfaces": [
            "frame_visibility_stop_line",
            "render_if_needed_call_blocked",
            "controller_blocked",
            "renderer_blocked",
            "frame_buffer_read_blocked",
            "artifact_writer_blocked",
        ],
        "transparent_globe_leak_status": "transparent_globe_leak_not_inferred",
        "transparent_globe_leak_fix_claimed": False,
        "runtime_execution_authorized": False,
    }


def dynamic_point_sampling_visibility_boundary_descriptor():
    return {
        "schema": SCHEMA,
        "boundary": "dynamic_point_sampling_visibility_boundary",
        "helper_surface": "descriptor_contract_ledger_only",
        "allowed_outputs": ["dict", "list", "scalar"],
        "owned_semantics": [
            "sampled_visible_token",
            "visible_count_observation",
            "rendered_count_observation",
            "mask_visible_token",
            "source_lineage_integrity_token",
            "sampling_or_presentation_reduction_candidate",
            "globe_mask_responsibility_candidate",
            "frame_visibility_stop_line",
            "transparent_globe_leak_not_inferred",
        ],
        "blocked_actions": [
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "runtime_probe_call",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_write",
            "correctness_claim",
            "readiness_claim",
            "leak_fix_claim",
        ],
    }


def dynamic_point_sampling_visibility_planning_bundle():
    return {
        "schema": SCHEMA,
        "bundle": "dynamic_point_sampling_visibility_planning_bundle",
        "observation_descriptor": build_dynamic_point_sampling_visibility_observation_descriptor(),
        "visibility_count_contract": build_dynamic_point_visibility_count_contract_descriptor(),
        "mask_visibility_contract": build_dynamic_point_mask_visibility_contract_descriptor(),
        "sampling_reduction_contract": build_dynamic_point_sampling_reduction_contract_descriptor(),
        "frame_visibility_stop_line": build_dynamic_point_frame_visibility_stop_line_descriptor(),
        "boundary_descriptor": dynamic_point_sampling_visibility_boundary_descriptor(),
        "minimal_extraction_gate_passed": True,
        "runtime_execution_authorized": False,
        "runtime_probe_call_authorized": False,
        "formula_movement_authorized": False,
        "correctness_claimed": False,
        "readiness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
    }
