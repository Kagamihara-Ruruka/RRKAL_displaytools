param(
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$scriptName = "scripts/inspect_render_plan_review_packet.ps1"
$schema = "rrkal_displaytools.render_plan_review_packet.v1"

if ($ContractOnly) {
    [ordered]@{
        schema = $schema
        source = $scriptName
        status = "contract_only_no_runtime"
        inspectors = @(
            "scripts/inspect_render_plan_metadata_summary.ps1",
            "scripts/inspect_render_plan_single_pass_preflight.ps1"
        )
        included_summary_fields = @("runtime_gate_status_summary")
        zero_diff_parity_contract_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_smoke.ps1 -ContractOnly"
        zero_diff_parity_evidence_checklist = @(
            "state/compose_parity/baseline_sequential_frame_rgba.png",
            "state/compose_parity/merged_candidate_frame_rgba.png",
            "render_compose_parity_smoke.visual_parity_passed",
            "max_abs_diff=0",
            "changed_pixel_count=0"
        )
        zero_diff_parity_evidence_summary = "Zero-diff parity evidence: artifacts=baseline_sequential_frame_rgba.png,merged_candidate_frame_rgba.png; visual_parity_passed=required; tolerance=max_abs_diff=0,changed_pixel_count=0; runtime_path=disabled_until_pass"
        zero_diff_parity_source_script = "scripts\render_compose_parity_smoke.ps1"
        zero_diff_parity_manifest_path = "state/render_compose_parity_smoke_manifest.json"
        zero_diff_parity_artifact_producer_script = "scripts\render_compose_parity_artifacts.ps1"
        zero_diff_parity_artifact_producer_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_artifacts.ps1 -SkipDiff"
        zero_diff_parity_artifact_runner_manifest_path = "state/compose_parity/compose_parity_artifact_runner.json"
        zero_diff_parity_artifact_diff_manifest_path = "state/compose_parity/render_compose_parity_smoke_manifest.json"
        zero_diff_parity_diff_status_field = "render_compose_parity_smoke.diff_status"
        zero_diff_parity_precommit_gate_field = "render_compose_parity_smoke.precommit_gate_passed"
        boundary = "Reviewer packet only; it does not launch Qt, Taichi, render frames, write metadata, or enable runtime single-pass composition."
        portable = $true
    } | ConvertTo-Json -Depth 8
    exit 0
}

$metadataSummary = powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot "scripts\inspect_render_plan_metadata_summary.ps1") | ConvertFrom-Json
$singlePassPreflight = powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot "scripts\inspect_render_plan_single_pass_preflight.ps1") | ConvertFrom-Json
$ready = $metadataSummary.status -eq "ready" -and $singlePassPreflight.status -eq "ready"
$runtimeGateStatusSummary = "Runtime gate status: metadata_available=True; runtime_merge=False; single_pass_submission=$($singlePassPreflight.runtime_single_pass_enabled); zero_diff_parity_required=True; runtime_path=disabled_until_parity"

[ordered]@{
    schema = $schema
    source = $scriptName
    status = if ($ready) { "ready" } else { "incomplete" }
    metadata_summary_status = $metadataSummary.status
    metadata_summary_schema = $metadataSummary.verifies_schema
    metadata_summary_field = $metadataSummary.summary_field
    adapter_payload_summary_schema = $metadataSummary.verifies_adapter_payload_schema
    adapter_payload_status_field = $metadataSummary.adapter_payload_status_field
    adapter_payload_contract_schema = $metadataSummary.verifies_adapter_payload_contract_schema
    adapter_payload_contract_status_field = $metadataSummary.adapter_payload_contract_status_field
    single_pass_preflight_status = $singlePassPreflight.status
    single_pass_preflight_schema = $singlePassPreflight.verifies_schema
    runtime_single_pass_enabled = $singlePassPreflight.runtime_single_pass_enabled
    runtime_gate_status_summary = $runtimeGateStatusSummary
    runtime_gate_status_summary_field = "runtime_gate_status_summary"
    zero_diff_parity_required = $true
    zero_diff_parity_contract_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_smoke.ps1 -ContractOnly"
    zero_diff_parity_evidence_checklist = @(
        "state/compose_parity/baseline_sequential_frame_rgba.png",
        "state/compose_parity/merged_candidate_frame_rgba.png",
        "render_compose_parity_smoke.visual_parity_passed",
        "max_abs_diff=0",
        "changed_pixel_count=0"
    )
    zero_diff_parity_evidence_summary = "Zero-diff parity evidence: artifacts=baseline_sequential_frame_rgba.png,merged_candidate_frame_rgba.png; visual_parity_passed=required; tolerance=max_abs_diff=0,changed_pixel_count=0; runtime_path=disabled_until_pass"
    zero_diff_parity_source_script = "scripts\render_compose_parity_smoke.ps1"
    zero_diff_parity_manifest_path = "state/render_compose_parity_smoke_manifest.json"
    zero_diff_parity_artifact_producer_script = "scripts\render_compose_parity_artifacts.ps1"
    zero_diff_parity_artifact_producer_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_artifacts.ps1 -SkipDiff"
    zero_diff_parity_artifact_runner_manifest_path = "state/compose_parity/compose_parity_artifact_runner.json"
    zero_diff_parity_artifact_diff_manifest_path = "state/compose_parity/render_compose_parity_smoke_manifest.json"
    zero_diff_parity_diff_status_field = "render_compose_parity_smoke.diff_status"
    zero_diff_parity_precommit_gate_field = "render_compose_parity_smoke.precommit_gate_passed"
    next_runtime_gate_action = "run_zero_diff_parity_contract_before_enabling_single_pass_submission"
    clone_first_review_commands = @(
        "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_render_plan_review_packet.ps1",
        "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_render_plan_metadata_summary.ps1",
        "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_render_plan_single_pass_preflight.ps1"
    )
    next_step = "Use this packet as the quick render-plan decoupling review entrypoint after clone."
    boundary = "Reviewer packet only; it aggregates source-only inspectors and does not launch Qt, Taichi, render frames, write metadata, or enable runtime single-pass composition."
    portable = $true
} | ConvertTo-Json -Depth 8
