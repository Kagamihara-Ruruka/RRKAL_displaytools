param(
    [switch]$SelfTestNegative
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

function Invoke-Checkpoint {
    $checkpointScript = Join-Path $RepoRoot "scripts\compose_parity_contract_checkpoint.ps1"
    $output = powershell -NoProfile -ExecutionPolicy Bypass -File $checkpointScript
    if ($LASTEXITCODE -ne 0) {
        throw "$checkpointScript failed with exit code $LASTEXITCODE"
    }
    return ($output -join "`n") | ConvertFrom-Json
}

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

function Test-Checkpoint {
    param([object]$Checkpoint)

    $errors = New-Object System.Collections.Generic.List[string]

    Assert-Equal $errors "schema" $Checkpoint.schema "rrkal_displaytools.compose_parity_contract_checkpoint.v1"
    Assert-Equal $errors "status" $Checkpoint.status "pass"
    Assert-Equal $errors "contract_only" $Checkpoint.contract_only $true
    Assert-Equal $errors "runtime_merge_enabled" $Checkpoint.runtime_merge_enabled $false
    Assert-Null $errors "visual_parity_passed" $Checkpoint.visual_parity_passed
    Assert-Null $errors "precommit_gate_passed" $Checkpoint.precommit_gate_passed
    Assert-Equal $errors "precommit_gate_evaluated" $Checkpoint.precommit_gate_evaluated $false
    Assert-Equal $errors "precommit_gate_status" $Checkpoint.precommit_gate_status "not_evaluated_contract_only"
    Assert-Equal $errors "visual_parity_ready" $Checkpoint.visual_parity_ready $false
    Assert-Equal $errors "artifact_parity_ready" $Checkpoint.artifact_parity_ready $false
    Assert-Equal $errors "negative_self_test_detected_all_false_readiness_mutations" $Checkpoint.negative_self_test_detected_all_false_readiness_mutations $true

    $missingEvidence = @($Checkpoint.missing_evidence)
    if ($missingEvidence.Count -eq 0) {
        $errors.Add("missing_evidence expected non-empty but got empty")
    }

    $negativeCases = @($Checkpoint.negative_self_test_cases)
    if ($negativeCases.Count -eq 0) {
        $errors.Add("negative_self_test_cases expected non-empty but got empty")
    }

    return @($errors)
}

function Copy-Checkpoint {
    param([object]$Checkpoint)
    return ($Checkpoint | ConvertTo-Json -Depth 20 | ConvertFrom-Json)
}

$checkpoint = Invoke-Checkpoint
$errors = Test-Checkpoint $checkpoint
$passed = $errors.Count -eq 0
$negativeResults = @()

if ($SelfTestNegative) {
    $cases = @(
        @{ id = "visual_parity_ready_true"; field = "visual_parity_ready"; value = $true },
        @{ id = "artifact_parity_ready_true"; field = "artifact_parity_ready"; value = $true },
        @{ id = "runtime_merge_enabled_true"; field = "runtime_merge_enabled"; value = $true }
    )

    foreach ($case in $cases) {
        $badCheckpoint = Copy-Checkpoint $checkpoint
        $badCheckpoint.($case.field) = $case.value
        $caseErrors = Test-Checkpoint $badCheckpoint
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
    schema = "rrkal_displaytools.compose_parity_contract_checkpoint_validation.v1"
    source = "scripts/validate_compose_parity_contract_checkpoint.ps1"
    status = if ($passed) { "pass" } else { "fail" }
    contract_only = $true
    validated_checkpoint_schema = $checkpoint.schema
    checked_fields = @(
        "contract_only",
        "runtime_merge_enabled",
        "visual_parity_passed",
        "precommit_gate_passed",
        "precommit_gate_evaluated",
        "precommit_gate_status",
        "visual_parity_ready",
        "artifact_parity_ready",
        "missing_evidence",
        "negative_self_test_detected_all_false_readiness_mutations"
    )
    false_readiness_signal_detected = -not $passed
    negative_self_test_enabled = [bool]$SelfTestNegative
    negative_self_test_results = $negativeResults
    errors = @($errors)
    boundary = "Contract-only checkpoint validator only. It validates checkpoint JSON semantics without renderer execution, Qt launch, baseline/candidate artifact reads, state writes, PNG/JSON artifact generation, metadata schema changes, output behavior changes, runtime merge, visual parity claims, precommit readiness claims, or interactive FPS readiness claims."
}

$result | ConvertTo-Json -Depth 10

if (-not $passed) {
    exit 1
}
