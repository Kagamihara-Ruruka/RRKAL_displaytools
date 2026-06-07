"""Pure composition dispatch packet helpers for layer render plans."""

from __future__ import annotations


def build_layer_render_plan_composition_apply_action(step: dict[str, object]) -> dict[str, object]:
    item = step if isinstance(step, dict) else {}
    kind = str(item.get("kind") or "")
    layer_id = str(item.get("layer_id") or item.get("id") or "")
    helper_by_kind = {
        "runtime_blend": "HybridRenderController.compose_runtime_blend",
        "alpha_blend": "alpha_blend_compose",
        "alpha_compose": "alpha_compose",
        "runtime_overlay": "HybridRenderController.compose_runtime_overlay",
        "style_profile_postprocess": "apply_style_profile",
    }
    return {
        "kind": kind,
        "layer_id": layer_id,
        "blend_mode": str(item.get("blend_mode") or "Normal"),
        "apply_helper": helper_by_kind.get(kind, "unknown_apply_helper"),
        "phase_id": "postprocess" if kind == "style_profile_postprocess" else "compose_overlays",
        "requires_overlay": kind in {"runtime_blend", "alpha_blend", "alpha_compose", "runtime_overlay"},
        "single_pass_candidate": kind in {"runtime_blend", "alpha_blend", "alpha_compose", "runtime_overlay"},
    }


def build_layer_render_plan_composition_dispatch_packet(
    action: dict[str, object],
    overlay_present: object,
) -> dict[str, object]:
    item = action if isinstance(action, dict) else {}
    kind = str(item.get("kind") or "")
    requires_overlay = bool(item.get("requires_overlay"))
    has_overlay = bool(overlay_present)
    if kind == "style_profile_postprocess":
        dispatch = "style_profile_postprocess"
        should_apply = True
        skip_reason = ""
    elif requires_overlay and not has_overlay:
        dispatch = "skip"
        should_apply = False
        skip_reason = "missing_overlay"
    elif kind in {"runtime_blend", "alpha_blend", "alpha_compose", "runtime_overlay"}:
        dispatch = kind
        should_apply = True
        skip_reason = ""
    else:
        dispatch = "skip"
        should_apply = False
        skip_reason = "unknown_apply_action"
    return {
        "schema": "rrkal_displaytools.layer_render_plan_composition_dispatch.v1",
        "source": "render_core.render_plan.build_layer_render_plan_composition_dispatch_packet",
        "kind": kind,
        "layer_id": item.get("layer_id"),
        "blend_mode": item.get("blend_mode"),
        "apply_helper": item.get("apply_helper"),
        "phase_id": item.get("phase_id") or "compose_overlays",
        "requires_overlay": requires_overlay,
        "overlay_present": has_overlay,
        "should_apply": should_apply,
        "dispatch": dispatch,
        "skip_reason": skip_reason,
        "runtime_optimization_applied": False,
    }
