param(
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"

if (-not $ContractOnly) {
    throw "compare_compose_pairwise_packet.ps1 currently supports -ContractOnly only. It does not run renderer, read candidate artifacts, or evaluate visual parity."
}

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

function New-GapBranch {
    param(
        [string]$Id,
        [string]$Reason
    )
    return [ordered]@{
        status = "not_run"
        reason = $Reason
        baseline_available = $false
        candidate_available = $false
        evaluated = $false
        evidence_ready = $false
    }
}

$artifactPaths = [ordered]@{
    baseline_sequential_frame_rgba = "state/compose_parity/baseline_sequential_frame_rgba.png"
    merged_candidate_frame_rgba = "state/compose_parity/merged_candidate_frame_rgba.png"
    renderer_output_metadata = "state/compose_parity/renderer_output_metadata.json"
    render_compose_parity_smoke_manifest = "state/compose_parity/render_compose_parity_smoke_manifest.json"
}

$missingEvidence = @(
    "baseline_queue_packet",
    "candidate_queue_packet",
    "baseline_skip_reason_packet",
    "candidate_skip_reason_packet",
    "baseline_dispatch_packet",
    "candidate_dispatch_packet",
    "baseline_timing_packet",
    "candidate_timing_packet",
    "baseline_metadata_sidecar",
    "candidate_metadata_sidecar",
    "baseline_sequential_frame_rgba",
    "merged_candidate_frame_rgba",
    "artifact_diff_manifest"
)

$packet = [ordered]@{
    schema = "rrkal_displaytools.compose_parity_pairwise_gap_packet.v1"
    source = "scripts/compare_compose_pairwise_packet.ps1"
    status = "contract_only_no_runtime"
    contract_only = $true
    runtime_merge_enabled = $false
    queue_parity = New-GapBranch -Id "queue_parity" -Reason "missing_candidate"
    skip_parity = New-GapBranch -Id "skip_parity" -Reason "missing_candidate"
    dispatch_parity = New-GapBranch -Id "dispatch_parity" -Reason "missing_candidate"
    timing_packet_parity = New-GapBranch -Id "timing_packet_parity" -Reason "missing_candidate"
    metadata_sidecar_parity = New-GapBranch -Id "metadata_sidecar_parity" -Reason "missing_candidate"
    artifact_parity = [ordered]@{
        status = "not_run"
        reason = "missing_artifacts"
        baseline_available = $false
        candidate_available = $false
        evaluated = $false
        evidence_ready = $false
        required_artifacts = $artifactPaths
    }
    visual_parity_passed = $null
    precommit_gate_passed = $null
    precommit_gate_evaluated = $false
    precommit_gate_status = "not_evaluated_contract_only"
    missing_evidence = $missingEvidence
    metadata_schema_changed = $false
    output_behavior_changed = $false
    generated_artifacts_written = $false
    generated_artifacts_staged = $false
    interactive_fps_claimed = $false
    boundary = "Contract-only pairwise gap packet only. It does not run renderer, launch Qt, read candidate artifacts, write PNG/JSON artifacts, change metadata schema, change output behavior, enable runtime merge, claim visual parity, or claim interactive FPS readiness."
}

$packet | ConvertTo-Json -Depth 8
