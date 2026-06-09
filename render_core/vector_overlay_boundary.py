"""Pure descriptor/policy/ledger helpers for vector overlay boundaries.

This module is intentionally scalar-only. It does not import or execute
renderer, controller, provider/cache, projection, mask, or artifact code.
"""

from __future__ import annotations


BOUNDARY_SPECS = {
    "borders": {
        "name": "\u570b\u754c",
        "color": (220, 225, 235),
        "prefix": "border",
        "natural_earth_layer": "admin_0_boundary_lines_land",
        "source_note": (
            "Natural Earth admin_0_boundary_lines_land. "
            "For strict work, pin the dataset version and dispute policy."
        ),
    },
    "territorial_sea": {
        "name": "\u9818\u6d77",
        "color": (64, 224, 255),
        "prefix": "territorial_sea",
        "marine_regions_layer": "eez_12nm",
        "source_note": (
            "Strict mode should use Marine Regions World 12 Nautical Miles Zone "
            "or equivalent official maritime boundary data."
        ),
    },
    "eez": {
        "name": "\u7d93\u6fdf\u6d77\u57df EEZ",
        "color": (255, 213, 74),
        "prefix": "eez",
        "marine_regions_layer": "eez_boundaries",
        "source_note": (
            "Strict mode should use Marine Regions World EEZ or equivalent "
            "official maritime boundary data."
        ),
    },
    "high_seas": {
        "name": "\u516c\u6d77",
        "color": (177, 130, 255),
        "prefix": "high_seas",
        "marine_regions_layer": "high_seas",
        "source_note": (
            "High-seas visualization should come from a maritime boundary dataset, "
            "not from guessed country buffers."
        ),
    },
}


HYDROLOGY_SPECS = {
    "lakes": {
        "name": "\u6e56\u6cca / \u6c34\u5eab",
        "color": (74, 194, 235),
        "natural_earth_layer": "lakes",
        "source_note": (
            "Natural Earth lakes are the basic layer; strict/local work should "
            "switch to HydroLAKES or OSM water polygons."
        ),
        "prefix": "lake",
    },
    "rivers": {
        "name": "\u4e3b\u8981\u6cb3\u5ddd",
        "color": (92, 210, 255),
        "natural_earth_layer": "rivers_lake_centerlines",
        "source_note": (
            "Natural Earth rivers_lake_centerlines are the basic layer; strict/local "
            "work should switch to HydroRIVERS, MERIT Hydro, or OSM waterways."
        ),
        "prefix": "river",
    },
}


def _copy_mapping(mapping: dict) -> dict:
    return {
        key: dict(value) if isinstance(value, dict) else value
        for key, value in mapping.items()
    }


def build_vector_overlay_descriptor(
    overlay_kind: str,
    provider_ref: dict | None = None,
    projection_policy: dict | None = None,
    mask_policy: dict | None = None,
    cache_status: dict | None = None,
) -> dict:
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.descriptor.v1",
        "overlay_kind": str(overlay_kind or "unknown"),
        "provider_ref": dict(provider_ref or build_vector_provider_ref_descriptor(overlay_kind)),
        "projection_policy": dict(projection_policy or build_vector_projection_policy_label_descriptor()),
        "mask_policy": dict(mask_policy or build_vector_mask_policy_label_descriptor()),
        "cache_status": dict(cache_status or build_vector_cache_status_label_descriptor()),
        "runtime_dependency_allowed": False,
        "runtime_render_invoked": False,
        "source_movement_authorized": False,
        "forbidden_next_action": "do_not_instantiate_runtime_overlay_or_execute_provider_cache",
    }


def build_vector_provider_ref_descriptor(
    overlay_kind: str,
    provider_ref_kind: str = "descriptor_only",
    provider_present: bool = True,
    malformed: bool = False,
) -> dict:
    normalized_kind = str(overlay_kind or "unknown")
    table_name = (
        "BOUNDARY_SPECS"
        if normalized_kind in BOUNDARY_SPECS
        else "HYDROLOGY_SPECS"
        if normalized_kind in HYDROLOGY_SPECS
        else ""
    )
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.provider_ref.v1",
        "overlay_kind": normalized_kind,
        "provider_ref_kind": str(provider_ref_kind or "descriptor_only"),
        "provider_present": bool(provider_present),
        "malformed": bool(malformed),
        "descriptor_table": table_name,
        "provider_execution_allowed": False,
        "cache_read_allowed": False,
        "forbidden_next_action": "do_not_call_provider_loader_or_read_cache",
    }


def build_vector_dirty_reload_ledger_descriptor(
    overlay_kind: str,
    dirty: bool = False,
    reload_requested: bool = False,
    reason: str = "none",
) -> dict:
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.dirty_reload_ledger.v1",
        "overlay_kind": str(overlay_kind or "unknown"),
        "dirty": bool(dirty),
        "reload_requested": bool(reload_requested),
        "reason": str(reason or "none"),
        "controller_mutation_allowed": False,
        "ledger_status": "reload_descriptor" if reload_requested else "clean_descriptor" if not dirty else "dirty_descriptor",
        "forbidden_next_action": "do_not_mutate_controller_dirty_or_reload_flags",
    }


def build_vector_controller_registry_descriptor(
    overlay_kind: str,
    registry_name: str = "overlay_registry",
    provider_ref_kind: str = "descriptor_only",
    projection_consumer: str = "projection_policy_label",
    mask_consumer: str = "mask_policy_label",
) -> dict:
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.controller_registry.v1",
        "overlay_kind": str(overlay_kind or "unknown"),
        "registry_name": str(registry_name or "overlay_registry"),
        "provider_ref_kind": str(provider_ref_kind or "descriptor_only"),
        "projection_consumer": str(projection_consumer or "projection_policy_label"),
        "mask_consumer": str(mask_consumer or "mask_policy_label"),
        "controller_import_allowed": False,
        "controller_mutation_allowed": False,
        "forbidden_next_action": "do_not_import_or_instantiate_controller",
    }


def build_vector_projection_policy_label_descriptor(
    policy_label: str = "label_only_projection_policy",
    frame_label: str = "vector_overlay_projection_frame",
) -> dict:
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.projection_policy_label.v1",
        "policy_label": str(policy_label or "label_only_projection_policy"),
        "frame_label": str(frame_label or "vector_overlay_projection_frame"),
        "formula_movement_allowed": False,
        "runtime_dependency_allowed": False,
        "forbidden_next_action": "do_not_move_or_rewrite_projection_formula",
    }


def build_vector_mask_policy_label_descriptor(
    policy_label: str = "label_only_mask_policy",
    frame_label: str = "globe_mask_descriptor_frame",
) -> dict:
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.mask_policy_label.v1",
        "policy_label": str(policy_label or "label_only_mask_policy"),
        "frame_label": str(frame_label or "globe_mask_descriptor_frame"),
        "formula_movement_allowed": False,
        "runtime_dependency_allowed": False,
        "forbidden_next_action": "do_not_move_or_rewrite_mask_formula",
    }


def build_vector_cache_status_label_descriptor(
    status_label: str = "cache_status_label_only",
    cache_present: bool = False,
) -> dict:
    return {
        "schema": "rrkal_displaytools.vector_overlay_boundary.cache_status_label.v1",
        "status_label": str(status_label or "cache_status_label_only"),
        "cache_present": bool(cache_present),
        "cache_lifecycle_allowed": False,
        "cache_read_allowed": False,
        "cache_write_allowed": False,
        "forbidden_next_action": "do_not_read_or_write_cache",
    }


def boundary_specs_descriptor() -> dict:
    return _copy_mapping(BOUNDARY_SPECS)


def hydrology_specs_descriptor() -> dict:
    return _copy_mapping(HYDROLOGY_SPECS)
