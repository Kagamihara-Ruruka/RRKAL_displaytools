from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "real_clock_execution_allowed": False,
    "solar_formula_allowed": False,
    "lighting_shader_formula_allowed": False,
    "projection_flip_formula_allowed": False,
    "visual_behavior_change_allowed": False,
}


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def build_solar_time_source_descriptor(source_label: str = "time_source") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.time_source_descriptor.v1",
            "descriptor_kind": "solar_time_source_descriptor",
            "source_label": source_label,
            "source_evidence": [
                "solar lighting boundary time source descriptor",
                "UTC/local ambiguity label",
                "static frozen-light fallback label",
            ],
            "time_policy": "label_only",
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_real_clock_or_change_time_source",
        }
    )


def build_solar_direction_label_descriptor(direction_label: str = "sun_direction") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.direction_label_descriptor.v1",
            "descriptor_kind": "solar_direction_label_descriptor",
            "direction_label": direction_label,
            "policy_labels": [
                "sun_direction",
                "sun_vector_label",
                "frozen_light_label",
            ],
            "consumer_layers": [
                "lighting_consumer",
                "terrain_lighting_label",
                "ocean_lighting_label",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_move_or_execute_compute_sun_direction",
        }
    )


def build_solar_twilight_terminator_label_descriptor(
    terminator_label: str = "twilight_terminator",
) -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.twilight_terminator_descriptor.v1",
            "descriptor_kind": "solar_twilight_terminator_label_descriptor",
            "terminator_label": terminator_label,
            "policy_labels": [
                "twilight",
                "terminator",
                "label_only",
            ],
            "known_limits": [
                "twilight formula not moved",
                "terminator behavior not changed",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_change_twilight_or_terminator_formula",
        }
    )


def build_solar_local_noon_fault_ledger_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.local_noon_fault_ledger_descriptor.v1",
            "descriptor_kind": "solar_local_noon_fault_ledger_descriptor",
            "fixture_status": "unresolved_static_only",
            "known_faults": [
                "local_noon_fault",
                "Taipei local-noon dark-side candidate",
                "UTC/local-time source ambiguity",
            ],
            "local_noon_fault_resolved": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_claim_taipei_local_noon_fix",
        }
    )


def build_solar_coordinate_dependency_label_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.coordinate_dependency_descriptor.v1",
            "descriptor_kind": "solar_coordinate_dependency_label_descriptor",
            "dependency_labels": [
                "coordinate_dependency",
                "projection",
                "flip",
                "grid_starfield_frame",
            ],
            "input_frame": "coordinate_dependency_labels_only",
            "known_limits": [
                "projection formula not moved",
                "flip formula not moved",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_change_projection_or_flip_formula",
        }
    )


def build_solar_lighting_consumer_layers_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.consumer_layers_descriptor.v1",
            "descriptor_kind": "solar_lighting_consumer_layers_descriptor",
            "consumer_layers": [
                "lighting_consumer",
                "terrain_lighting_label",
                "bathymetry_lighting_label",
                "ocean_lighting_label",
                "grid_dependency_label",
            ],
            "normal_labels": [
                "world_normal",
                "bump_normal",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_change_lighting_consumer_behavior",
        }
    )


def build_solar_forbidden_formula_surface_ledger_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.solar_lighting.forbidden_formula_surface_ledger_descriptor.v1",
            "descriptor_kind": "solar_forbidden_formula_surface_ledger_descriptor",
            "fixture_status": "blocked_hot_path",
            "blocked_surfaces": [
                "compute_sun_direction",
                "sun_vector_formula",
                "light_dir_formula",
                "dot_l_formula",
                "twilight_formula",
                "normal_formula",
                "projection_formula",
                "flip_formula",
            ],
            "formula_movement_authorized": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_move_or_modify_solar_lighting_formula",
        }
    )


def solar_lighting_frame_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.solar_lighting.boundary_descriptor.v1",
        "descriptor_kind": "solar_lighting_frame_boundary_descriptor",
        "time_source_descriptor": build_solar_time_source_descriptor(),
        "direction_label_descriptor": build_solar_direction_label_descriptor(),
        "twilight_terminator_descriptor": build_solar_twilight_terminator_label_descriptor(),
        "local_noon_fault_ledger_descriptor": build_solar_local_noon_fault_ledger_descriptor(),
        "coordinate_dependency_descriptor": build_solar_coordinate_dependency_label_descriptor(),
        "lighting_consumer_layers_descriptor": build_solar_lighting_consumer_layers_descriptor(),
        "forbidden_formula_surface_ledger_descriptor": build_solar_forbidden_formula_surface_ledger_descriptor(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "local_noon_fault_resolved": False,
        "forbidden_next_action": "do_not_include_time_runtime_formula_or_renderer_host",
    }


def solar_lighting_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.solar_lighting.planning_bundle.v1",
        "descriptor_kind": "solar_lighting_planning_bundle",
        "target_candidate": "render_core/solar_lighting_frame_boundary.py",
        "boundary_descriptor": solar_lighting_frame_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "blocked_surfaces": [
            "real_clock_execution",
            "solar_formula",
            "lighting_shader_formula",
            "projection_flip_formula",
            "runtime_renderer_controller",
            "terrain_shader_sampling_bump_formula",
            "metadata_artifact_writer",
            "alpha_apply_composition_hot_path",
        ],
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "local_noon_fault_resolved": False,
        "forbidden_next_action": "do_not_authorize_source_movement_inside_bundle",
    }
