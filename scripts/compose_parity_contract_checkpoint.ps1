param(
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

function Invoke-JsonScript {
    param(
        [string]$ScriptPath,
        [string[]]$Arguments
    )

    $output = powershell -NoProfile -ExecutionPolicy Bypass -File $ScriptPath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$ScriptPath failed with exit code $LASTEXITCODE"
    }

    return ($output -join "`n") | ConvertFrom-Json
}

function Test-Equal {
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

function Test-Null {
    param(
        [System.Collections.Generic.List[string]]$Errors,
        [string]$Field,
        [object]$Actual
    )
    if ($null -ne $Actual) {
        $Errors.Add("$Field expected null but got '$Actual'")
    }
}

$compareScript = Join-Path $RepoRoot "scripts\compare_compose_pairwise_packet.ps1"
$validatorScript = Join-Path $RepoRoot "scripts\validate_compose_pairwise_gap_packet.ps1"

$packet = Invoke-JsonScript -ScriptPath $compareScript -Arguments @("-ContractOnly")
$validation = Invoke-JsonScript -ScriptPath $validatorScript -Arguments @("-ContractOnly")
$negativeValidation = Invoke-JsonScript -ScriptPath $validatorScript -Arguments @("-ContractOnly", "-SelfTestNegative")

$errors = New-Object System.Collections.Generic.List[string]

Test-Equal $errors "packet.contract_only" $packet.contract_only $true
Test-Equal $errors "packet.runtime_merge_enabled" $packet.runtime_merge_enabled $false
Test-Null $errors "packet.visual_parity_passed" $packet.visual_parity_passed
Test-Null $errors "packet.precommit_gate_passed" $packet.precommit_gate_passed
Test-Equal $errors "packet.precommit_gate_evaluated" $packet.precommit_gate_evaluated $false
Test-Equal $errors "packet.precommit_gate_status" $packet.precommit_gate_status "not_evaluated_contract_only"
Test-Equal $errors "validation.status" $validation.status "pass"
Test-Equal $errors "negative_validation.status" $negativeValidation.status "pass"

$negativeResults = @($negativeValidation.negative_self_test_results)
$requiredNegativeIds = @(
    "visual_parity_true",
    "precommit_gate_passed_true",
    "precommit_gate_evaluated_true",
    "runtime_merge_enabled_true"
)

foreach ($id in $requiredNegativeIds) {
    $result = $negativeResults | Where-Object { $_.id -eq $id } | Select-Object -First 1
    if ($null -eq $result) {
        $errors.Add("negative self-test result missing '$id'")
        continue
    }
    Test-Equal $errors "negative_self_test.$id.detected" $result.detected $true
    Test-Equal $errors "negative_self_test.$id.status" $result.status "pass"
}

$passed = $errors.Count -eq 0

$checkpoint = [ordered]@{
    schema = "rrkal_displaytools.compose_parity_contract_checkpoint.v1"
    source = "scripts/compose_parity_contract_checkpoint.ps1"
    status = if ($passed) { "pass" } else { "fail" }
    contract_only = $true
    runtime_merge_enabled = $packet.runtime_merge_enabled
    visual_parity_passed = $packet.visual_parity_passed
    precommit_gate_passed = $packet.precommit_gate_passed
    precommit_gate_evaluated = $packet.precommit_gate_evaluated
    precommit_gate_status = $packet.precommit_gate_status
    gap_packet_status = $packet.status
    validator_status = $validation.status
    negative_self_test_status = $negativeValidation.status
    negative_self_test_detected_all_false_readiness_mutations = ($requiredNegativeIds | ForEach-Object {
        $id = $_
        $result = $negativeResults | Where-Object { $_.id -eq $id } | Select-Object -First 1
        ($null -ne $result) -and ($result.detected -eq $true) -and ($result.status -eq "pass")
    }) -notcontains $false
    negative_self_test_cases = $negativeResults
    errors = @($errors)
    boundary = "Contract-only checkpoint bundle only. It runs gap packet and validator semantics checks without renderer execution, Qt launch, baseline/candidate artifact reads, state writes, PNG/JSON artifact generation, metadata schema changes, output behavior changes, runtime merge, visual parity claims, precommit readiness claims, or interactive FPS readiness claims."
}

$checkpoint | ConvertTo-Json -Depth 10

if (-not $passed) {
    exit 1
}
