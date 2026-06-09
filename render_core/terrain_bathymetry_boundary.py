from __future__ import annotations


_NO_RUNTIME_GUARDS = {
    "runtime_dependency_allowed": False,
    "provider_cache_execution_allowed": False,
    "shader_formula_allowed": False,
    "projection_lighting_formula_allowed": False,
    "visual_behavior_change_allowed": False,
}


def _with_guards(packet: dict[str, object]) -> dict[str, object]:
    return {**packet, **_NO_RUNTIME_GUARDS}


def build_terrain_bathymetry_source_descriptor(source_label: str = "terrain_bathymetry_source") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.source_descriptor.v1",
            "descriptor_kind": "terrain_bathymetry_source_descriptor",
            "source_label": source_label,
            "source_evidence": [
                "topography source label",
                "bathymetry source label",
                "fallback source label",
            ],
            "input_frame": "height_field_source_label",
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_execute_provider_or_cache_loader",
        }
    )


def build_terrain_height_field_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.height_field_descriptor.v1",
            "descriptor_kind": "terrain_height_field_descriptor",
            "height_field_kind": "raster_height_field_label",
            "coordinate_payload_kind": "sample_frame_label_only",
            "consumer_layers": [
                "terrain_shader_label",
                "bathymetry_layer_label",
                "land_mask_consumer_label",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_move_sampling_or_shader_height_lookup",
        }
    )


def build_terrain_fallback_no_data_descriptor(reason: str = "no_data") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.fallback_no_data_descriptor.v1",
            "descriptor_kind": "terrain_fallback_no_data_descriptor",
            "fallback_reason": reason,
            "fallback_policy": "label_only",
            "source_state": "unresolved_static_only",
            "known_limits": [
                "provider execution not covered",
                "synthetic terrain behavior not moved",
            ],
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_generate_download_or_load_real_topography",
        }
    )


def build_terrain_lod_resolution_label_descriptor(lod_label: str = "default_lod") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.lod_resolution_descriptor.v1",
            "descriptor_kind": "terrain_lod_resolution_label_descriptor",
            "lod_label": lod_label,
            "resolution_policy": "label_only",
            "sampling_quality_claimed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_change_resolution_or_sampling_behavior",
        }
    )


def build_terrain_cache_status_label_descriptor(status: str = "unknown") -> dict[str, object]:
    normalized = status if status in {"cache_hit", "cache_miss", "unknown"} else "unknown"
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.cache_status_descriptor.v1",
            "descriptor_kind": "terrain_cache_status_label_descriptor",
            "cache_status": normalized,
            "cache_policy": "label_only",
            "cache_lifecycle_executed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_read_write_load_save_or_evict_cache",
        }
    )


def build_terrain_palette_style_label_descriptor(style_label: str = "default_style") -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.palette_style_descriptor.v1",
            "descriptor_kind": "terrain_palette_style_label_descriptor",
            "style_label": style_label,
            "palette_policy": "label_only",
            "visual_behavior_changed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_change_palette_or_visual_behavior",
        }
    )


def build_terrain_known_fault_ledger_descriptor() -> dict[str, object]:
    return _with_guards(
        {
            "schema": "rrkal_displaytools.terrain_bathymetry.known_fault_ledger_descriptor.v1",
            "descriptor_kind": "terrain_known_fault_ledger_descriptor",
            "fixture_status": "unresolved_static_only",
            "known_faults": [
                "blocky_terrain_artifact_descriptor",
                "longitude_orientation_split_candidate",
                "latitude_flip_authority_unresolved",
                "local_noon_lighting_diagnostic",
            ],
            "fault_fixed": False,
            "allowed_content_kind": "dict/list/scalar descriptor only",
            "forbidden_next_action": "do_not_fix_or_mark_visual_fault_resolved",
        }
    )


def terrain_bathymetry_boundary_descriptor() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.terrain_bathymetry.boundary_descriptor.v1",
        "descriptor_kind": "terrain_bathymetry_boundary_descriptor",
        "source_descriptor": build_terrain_bathymetry_source_descriptor(),
        "height_field_descriptor": build_terrain_height_field_descriptor(),
        "fallback_no_data_descriptor": build_terrain_fallback_no_data_descriptor(),
        "lod_resolution_descriptor": build_terrain_lod_resolution_label_descriptor(),
        "cache_status_descriptor": build_terrain_cache_status_label_descriptor(),
        "palette_style_descriptor": build_terrain_palette_style_label_descriptor(),
        "known_fault_ledger_descriptor": build_terrain_known_fault_ledger_descriptor(),
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "forbidden_next_action": "do_not_include_runtime_formula_or_provider_loader",
    }


def terrain_bathymetry_planning_bundle() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.terrain_bathymetry.planning_bundle.v1",
        "descriptor_kind": "terrain_bathymetry_planning_bundle",
        "target_candidate": "render_core/terrain_bathymetry_boundary.py",
        "boundary_descriptor": terrain_bathymetry_boundary_descriptor(),
        "candidate_scope": "descriptor_policy_ledger_only",
        "blocked_surfaces": [
            "provider_cache_loader",
            "sampling_bump_shader_formula",
            "projection_flip_lighting_formula",
            "runtime_renderer_controller",
            "palette_visual_behavior",
            "metadata_artifact_writer",
            "alpha_apply_composition_hot_path",
        ],
        "source_movement_authorized": False,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "visual_parity_ready": False,
        "performance_ready": False,
        "readiness_claimed": False,
        "forbidden_next_action": "do_not_authorize_source_movement_inside_bundle",
    }
