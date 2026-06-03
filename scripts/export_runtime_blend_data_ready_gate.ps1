param(
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"

$gate = [pscustomobject]@{
    schema = "rrkal_displaytools.runtime_blend_data_ready_boundary_gate.v1"
    mode = "contract_only_no_renderer"
    purpose = "Define the next evidence-only gate before adding runtime_blend data-ready boundary timing."
    source_design_doc = "docs/RUNTIME_BLEND_SUBPHASE_TIMING_DESIGN.zh-TW.md"
    insertion_point = "HybridRenderController.apply_layer_render_plan_composition runtime_blend branch"
    future_instrumentation_touches_renderer_core = $true
    separate_review_required = $true
    optimization_authorized = $false
    runtime_merge_enabled = $false
    metadata_schema_changed = $false
    output_behavior_changed = $false
    interactive_fps_readiness_claim = $false
    candidate_boundaries = @(
        [pscustomobject]@{
            id = "dispatch_ready_ms"
            location = "after action/layer/overlay/dispatch packet resolution"
            intent = "separate queue/dispatch preparation from runtime_blend call timing"
        },
        [pscustomobject]@{
            id = "runtime_blend_call_ms"
            location = "around compose_runtime_blend(frame, layer_id, overlay)"
            intent = "measure the existing runtime_blend call boundary without changing pixels"
        },
        [pscustomobject]@{
            id = "post_blend_return_ms"
            location = "after runtime_blend returns and before aggregate phase timing update"
            intent = "preserve a post-return boundary for attribution"
        }
    )
    validation_required = @(
        "render_quick_smoke",
        "render_repeated_quick_smoke_frames_3",
        "render_warm_frame_smoke",
        "render_warm_frame_smoke_runtime_blend_timing",
        "render_warm_frame_smoke_high_density_runtime_blend_timing",
        "runtime_blend_timing_review_smoke",
        "smoke",
        "git_diff_check",
        "generated_artifact_ignore_audit"
    )
    parity_required_before = @(
        "runtime_blend_optimization",
        "alpha_blending_change",
        "layer_ordering_change",
        "array_copy_rewrite",
        "runtime_merge"
    )
    stop_conditions = @(
        "metadata_schema_change_needed",
        "output_pixel_change_possible",
        "layer_order_change_needed",
        "alpha_blending_change_needed",
        "runtime_merge_needed",
        "unclear_test_failure",
        "generated_artifact_not_ignored"
    )
    forbidden_scope = @(
        "renderer skin asset loader",
        "skin asset loader",
        "compression_integration",
        "cross_repo_code",
        "UI_implementation",
        "interactive_FPS_readiness_claim"
    )
}

if ($ContractOnly) {
    $gate | ConvertTo-Json -Depth 6
    exit 0
}

$gate | ConvertTo-Json -Depth 6
