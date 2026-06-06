param(
    [switch]$ContractOnly,
    [switch]$SelfTestNegative
)

$ErrorActionPreference = "Stop"

if (-not $ContractOnly) {
    throw "validate_compose_pairwise_gap_packet.ps1 currently supports -ContractOnly only. It does not run renderer, read artifacts, or evaluate visual parity."
}

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

$packetText = powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $RepoRoot "scripts\compare_compose_pairwise_packet.ps1") -ContractOnly
$packet = ($packetText -join "`n") | ConvertFrom-Json

function Assert-Equal {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [string]$Field,
        [object]$Actual,
        [object]$Expected
    )
    if ($Actual -ne $Expected) {
        $Errors.Add("$Field expected '$Expected' but got '$Actual'")
    }
}

function Assert-Null {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [string]$Field,
        [object]$Actual
    )
    if ($null -ne $Actual) {
        $Errors.Add("$Field expected null but got '$Actual'")
    }
}

function Assert-Branch {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [string]$Name,
        [object]$Branch,
        [string]$Reason
    )
    if ($null -eq $Branch) {
        $Errors.Add("$Name missing")
        return
    }
    Assert-Equal $Errors "$Name.status" $Branch.status "not_run"
    Assert-Equal $Errors "$Name.reason" $Branch.reason $Reason
    Assert-Equal $Errors "$Name.evaluated" $Branch.evaluated $false
    Assert-Equal $Errors "$Name.evidence_ready" $Branch.evidence_ready $false
}

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

function Test-GapPacket {
    param([object]$Packet)

    $errors = New-Object System.Collections.Generic.List[string]

    Assert-Equal $errors "schema" $Packet.schema "rrkal_displaytools.compose_parity_pairwise_gap_packet.v1"
    Assert-Equal $errors "status" $Packet.status "contract_only_no_runtime"
    Assert-Equal $errors "contract_only" $Packet.contract_only $true
    Assert-Equal $errors "runtime_merge_enabled" $Packet.runtime_merge_enabled $false
    Assert-Null $errors "visual_parity_passed" $Packet.visual_parity_passed
    Assert-Null $errors "precommit_gate_passed" $Packet.precommit_gate_passed
    Assert-Equal $errors "precommit_gate_evaluated" $Packet.precommit_gate_evaluated $false
    Assert-Equal $errors "precommit_gate_status" $Packet.precommit_gate_status "not_evaluated_contract_only"
    Assert-Equal $errors "metadata_schema_changed" $Packet.metadata_schema_changed $false
    Assert-Equal $errors "output_behavior_changed" $Packet.output_behavior_changed $false
    Assert-Equal $errors "generated_artifacts_written" $Packet.generated_artifacts_written $false
    Assert-Equal $errors "generated_artifacts_staged" $Packet.generated_artifacts_staged $false
    Assert-Equal $errors "interactive_fps_claimed" $Packet.interactive_fps_claimed $false

    Assert-Branch $errors "queue_parity" $Packet.queue_parity "missing_candidate"
    Assert-Branch $errors "skip_parity" $Packet.skip_parity "missing_candidate"
    Assert-Branch $errors "dispatch_parity" $Packet.dispatch_parity "missing_candidate"
    Assert-Branch $errors "timing_packet_parity" $Packet.timing_packet_parity "missing_candidate"
    Assert-Branch $errors "metadata_sidecar_parity" $Packet.metadata_sidecar_parity "missing_candidate"
    Assert-Branch $errors "artifact_parity" $Packet.artifact_parity "missing_artifacts"

    $missingEvidence = @($Packet.missing_evidence)
    foreach ($item in $requiredMissingEvidence) {
        if ($missingEvidence -notcontains $item) {
            $errors.Add("missing_evidence does not include '$item'")
        }
    }

    return @($errors)
}

function Copy-Packet {
    param([object]$Packet)
    return ($Packet | ConvertTo-Json -Depth 20 | ConvertFrom-Json)
}

$errors = Test-GapPacket $packet
$passed = $errors.Count -eq 0
$negativeResults = @()

if ($SelfTestNegative) {
    $cases = @(
        @{ id = "visual_parity_true"; field = "visual_parity_passed"; value = $true },
        @{ id = "precommit_gate_passed_true"; field = "precommit_gate_passed"; value = $true },
        @{ id = "precommit_gate_evaluated_true"; field = "precommit_gate_evaluated"; value = $true },
        @{ id = "runtime_merge_enabled_true"; field = "runtime_merge_enabled"; value = $true }
    )
    foreach ($case in $cases) {
        $badPacket = Copy-Packet $packet
        $badPacket.($case.field) = $case.value
        $caseErrors = Test-GapPacket $badPacket
        $detected = @($caseErrors).Count -gt 0
        $negativeResults += [ordered]@{
            id = $case.id
            mutated_field = $case.field
            expected_detection = $true
            detected = $detected
            status = if ($detected) { "pass" } else { "fail" }
            errors = @($caseErrors)
        }
        if (-not $detected) {
            $passed = $false
            $errors += "negative self-test failed to detect $($case.id)"
        }
    }
}

$result = [ordered]@{
    schema = "rrkal_displaytools.compose_parity_pairwise_gap_packet_validation.v1"
    source = "scripts/validate_compose_pairwise_gap_packet.ps1"
    status = if ($passed) { "pass" } else { "fail" }
    contract_only = $true
    validated_packet_schema = $packet.schema
    false_readiness_signal_detected = -not $passed
    negative_self_test_enabled = [bool]$SelfTestNegative
    negative_self_test_results = $negativeResults
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
