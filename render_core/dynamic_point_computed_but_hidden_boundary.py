"""Descriptor-only computed-but-hidden boundary helpers.

This module keeps dynamic point computed-but-hidden semantics as data-only
descriptor, contract, and ledger packets. It does not import or execute the
monolith, renderer, frame surfaces, probe tooling, or formula helpers.
"""

from __future__ import annotations


SCHEMA = "rrkal.displaytools.dynamic_point_computed_but_hidden_boundary.v1"

LABELS = [
    "source_present_token",
    "computed_point_token",
    "hidden_visibility_token",
    "frame_visible_not_observed",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "computed_but_hidden_contract",
    "transparent_globe_leak_not_inferred",
    "source_loss_not_inferred",
    "frame_buffer_read_blocked",
    "renderer_execution_blocked",
    "readiness_not_claimed",
]

OUTPUT_SHAPE = {
    "nested_dict": True,
    "list": True,
    "scalar": True,
    "callable": False,
    "object_handle": False,
}

FALSE_FLAGS = {
    "runtime_execution_authorized": False,
    "probe_execution_authorized": False,
    "monolith_import_authorized": False,
    "render_if_needed_authorized": False,
    "controller_authorized": False,
    "render_host_authorized": False,
    "frame_surface_read_authorized": False,
    "artifact_generation_authorized": False,
    "projection_formula_movement_authorized": False,
    "mask_formula_movement_authorized": False,
    "sampling_formula_movement_authorized": False,
    "alpha_formula_movement_authorized": False,
    "hidden_as_missing_authorized": False,
    "source_lineage_loss_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
}


def _packet(surface: str) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "surface": surface,
        "scope": "descriptor_contract_ledger_only",
        "allowed_output_shape": dict(OUTPUT_SHAPE),
        "allowed_labels": list(LABELS),
        "guard_flags": dict(FALSE_FLAGS),
    }


def build_dynamic_point_computed_but_hidden_contract_descriptor() -> dict[str, object]:
    packet = _packet("computed_but_hidden_contract")
    packet["contract"] = {
        "contract_id": "computed_but_hidden_contract",
        "source_presence": {
            "label": "source_present_token",
            "can_be_true": True,
            "meaning": "source identity can exist before visibility or presentation judgement",
        },
        "computed_presence": {
            "label": "computed_point_token",
            "can_be_true": True,
            "meaning": "point can be computed without becoming frame-visible evidence",
        },
        "hidden_visibility": {
            "label": "hidden_visibility_token",
            "meaning": "visibility or presentation hidden state only",
        },
        "semantic_guards": [
            "hidden_is_not_missing",
            "occluded_is_not_source_lineage_loss",
            "source_loss_not_inferred",
            "transparent_globe_leak_not_inferred",
        ],
    }
    return packet


def build_dynamic_point_hidden_visibility_contract_descriptor() -> dict[str, object]:
    packet = _packet("hidden_visibility_token")
    packet["contract"] = {
        "contract_id": "hidden_visibility_token",
        "owned_labels": [
            "hidden_visibility_token",
            "hidden_is_not_missing",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
        ],
        "meaning": "hidden state records visibility or presentation hiding only",
        "blocked_interpretations": [
            "hidden_as_missing_interpretation",
            "frame_truth_claim",
            "transparent_globe_leak_inference",
        ],
    }
    return packet


def build_dynamic_point_computed_point_contract_descriptor() -> dict[str, object]:
    packet = _packet("computed_point_token")
    packet["contract"] = {
        "contract_id": "computed_point_token",
        "owned_labels": [
            "source_present_token",
            "computed_point_token",
            "computed_but_hidden_contract",
        ],
        "computed_state_can_be_true": True,
        "coordinate_correctness_claimed": False,
        "visual_parity_claimed": False,
        "meaning": "computed state is a contract label, not coordinate or frame truth",
    }
    return packet


def build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor() -> dict[str, object]:
    packet = _packet("source_lineage_guard")
    packet["guard"] = {
        "guard_id": "computed_but_hidden_source_lineage_guard",
        "owned_labels": [
            "source_present_token",
            "occluded_is_not_source_lineage_loss",
            "source_loss_not_inferred",
        ],
        "source_identity_preserved": True,
        "source_lineage_mutation_allowed": False,
        "hidden_can_delete_source": False,
        "occlusion_can_delete_source": False,
    }
    return packet


def build_dynamic_point_computed_but_hidden_stop_line_ledger() -> dict[str, object]:
    packet = _packet("computed_but_hidden_stop_line_ledger")
    packet["ledger"] = {
        "ledger_id": "computed_but_hidden_stop_line_ledger",
        "blocked_surfaces": [
            "frame_visible_not_observed",
            "frame_buffer_read_blocked",
            "renderer_execution_blocked",
            "transparent_globe_leak_not_inferred",
            "readiness_not_claimed",
        ],
        "frame_visible_not_observed": True,
        "frame_buffer_read_blocked": True,
        "renderer_execution_blocked": True,
        "transparent_globe_leak_not_inferred": True,
        "readiness_not_claimed": True,
        "leak_fix_claimed": False,
    }
    return packet


def dynamic_point_computed_but_hidden_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "boundary_id": "dynamic_point_computed_but_hidden_boundary",
        "scope": "minimal_descriptor_contract_ledger_surface",
        "helper_families": [
            "build_dynamic_point_computed_but_hidden_contract_descriptor",
            "build_dynamic_point_hidden_visibility_contract_descriptor",
            "build_dynamic_point_computed_point_contract_descriptor",
            "build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor",
            "build_dynamic_point_computed_but_hidden_stop_line_ledger",
            "dynamic_point_computed_but_hidden_boundary_descriptor",
            "dynamic_point_computed_but_hidden_planning_bundle",
        ],
        "allowed_output_shape": dict(OUTPUT_SHAPE),
        "allowed_labels": list(LABELS),
        "guard_flags": dict(FALSE_FLAGS),
        "classification": "computed_but_hidden_minimal_boundary",
    }


def dynamic_point_computed_but_hidden_planning_bundle() -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "minimal_extraction_gate_passed": True,
        "boundary_descriptor": dynamic_point_computed_but_hidden_boundary_descriptor(),
        "contracts": [
            build_dynamic_point_computed_but_hidden_contract_descriptor(),
            build_dynamic_point_hidden_visibility_contract_descriptor(),
            build_dynamic_point_computed_point_contract_descriptor(),
            build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor(),
            build_dynamic_point_computed_but_hidden_stop_line_ledger(),
        ],
        "decision": {
            "dict_list_scalar_output_only": True,
            "source_present_token_can_be_true": True,
            "computed_point_token_can_be_true": True,
            "hidden_visibility_token_is_visibility_or_presentation_only": True,
            "hidden_is_not_missing": True,
            "occluded_is_not_source_lineage_loss": True,
            "frame_visible_not_observed": True,
            "transparent_globe_leak_not_inferred": True,
            "source_loss_not_inferred": True,
            "visual_parity_claimed": False,
            "readiness_claimed": False,
            "transparent_globe_leak_fix_claimed": False,
        },
    }
