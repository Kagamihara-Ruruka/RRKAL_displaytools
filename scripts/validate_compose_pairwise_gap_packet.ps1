param(
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"

if (-not $ContractOnly) {
    throw "validate_compose_pairwise_gap_packet.ps1 currently supports -ContractOnly only. It does not run renderer, read artifacts, or evaluate visual parity."
}

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

$packetText = powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot "scripts\compare_compose_pairwise_packet.ps1") -ContractOnly
$packet = ($packetText -join "`n") | ConvertFrom-Json

$errors = New-Object System.Collections.Generic.List[string]

function Assert-Equal {
    param(
        [string]$Field,
        [object]$Actual,
        [object]$Expected
    )
    if ($Actual -ne $Expected) {
        $script:errors.Add("$Field expected '$Expected' but got '$Actual'")
    }
}

function Assert-Null {
    param(
        [string]$Field,
        [object]$Actual
    )
    if ($null -ne $Actual) {
        $script:errors.Add("$Field expected null but got '$Actual'")
    }
}

function Assert-Branch {
    param(
        [string]$Name,
        [object]$Branch,
        [string]$Reason
    )
    if ($null -eq $Branch) {
        $script:errors.Add("$Name missing")
        return
    }
    Assert-Equal "$Name.status" $Branch.status "not_run"
    Assert-Equal "$Name.reason" $Branch.reason $Reason
    Assert-Equal "$Name.evaluated" $Branch.evaluated $false
    Assert-Equal "$Name.evidence_ready" $Branch.evidence_ready $false
}

Assert-Equal "schema" $packet.schema "rrkal_displaytools.compose_parity_pairwise_gap_packet.v1"
Assert-Equal "status" $packet.status "contract_only_no_runtime"
Assert-Equal "contract_only" $packet.contract_only $true
Assert-Equal "runtime_merge_enabled" $packet.runtime_merge_enabled $false
Assert-Null "visual_parity_passed" $packet.visual_parity_passed
Assert-Null "precommit_gate_passed" $packet.precommit_gate_passed
Assert-Equal "precommit_gate_evaluated" $packet.precommit_gate_evaluated $false
Assert-Equal "precommit_gate_status" $packet.precommit_gate_status "not_evaluated_contract_only"
Assert-Equal "metadata_schema_changed" $packet.metadata_schema_changed $false
Assert-Equal "output_behavior_changed" $packet.output_behavior_changed $false
Assert-Equal "generated_artifacts_written" $packet.generated_artifacts_written $false
Assert-Equal "generated_artifacts_staged" $packet.generated_artifacts_staged $false
Assert-Equal "interactive_fps_claimed" $packet.interactive_fps_claimed $false

Assert-Branch "queue_parity" $packet.queue_parity "missing_candidate"
Assert-Branch "skip_parity" $packet.skip_parity "missing_candidate"
Assert-Branch "dispatch_parity" $packet.dispatch_parity "missing_candidate"
Assert-Branch "timing_packet_parity" $packet.timing_packet_parity "missing_candidate"
Assert-Branch "metadata_sidecar_parity" $packet.metadata_sidecar_parity "missing_candidate"
Assert-Branch "artifact_parity" $packet.artifact_parity "missing_artifacts"

$requiredMissingEvidence = @(
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

$missingEvidence = @($packet.missing_evidence)
foreach ($item in $requiredMissingEvidence) {
    if ($missingEvidence -notcontains $item) {
        $errors.Add("missing_evidence does not include '$item'")
    }
}

$passed = $errors.Count -eq 0
$result = [ordered]@{
    schema = "rrkal_displaytools.compose_parity_pairwise_gap_packet_validation.v1"
    source = "scripts/validate_compose_pairwise_gap_packet.ps1"
    status = if ($passed) { "pass" } else { "fail" }
    contract_only = $true
    validated_packet_schema = $packet.schema
    false_readiness_signal_detected = -not $passed
    checked_fields = @(
        "contract_only",
        "runtime_merge_enabled",
        "visual_parity_passed",
        "precommit_gate_passed",
        "precommit_gate_evaluated",
        "precommit_gate_status",
        "queue_parity",
        "skip_parity",
        "dispatch_parity",
        "timing_packet_parity",
        "metadata_sidecar_parity",
        "artifact_parity",
        "missing_evidence"
    )
    errors = @($errors)
    boundary = "Contract-only validator only. It validates gap packet JSON semantics and does not run renderer, launch Qt, read baseline/candidate artifacts, write PNG/JSON artifacts, change metadata schema, change output behavior, enable runtime merge, claim visual parity, or claim interactive FPS readiness."
}

$result | ConvertTo-Json -Depth 8

if (-not $passed) {
    exit 1
}
