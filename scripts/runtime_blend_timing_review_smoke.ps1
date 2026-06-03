param(
    [int]$Frames = 3,
    [switch]$ContractOnly,
    [switch]$Json
)

$ErrorActionPreference = "Stop"

if ($Frames -lt 2) {
    throw "Runtime blend timing review smoke requires Frames >= 2"
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$warmScript = Join-Path $PSScriptRoot "render_warm_frame_smoke.ps1"
$reviewScript = Join-Path $PSScriptRoot "review_runtime_blend_timing_evidence.ps1"
$reviewSummaryPath = Join-Path $repoRoot "state\showcase\runtime_blend_timing_review\summary.json"
$reviewMarkdownPath = Join-Path $repoRoot "state\showcase\runtime_blend_timing_review\summary.md"

if ($ContractOnly) {
    [pscustomobject]@{
        schema = "rrkal_displaytools.runtime_blend_timing_review_smoke_contract.v1"
        mode = "contract_only"
        frames = $Frames
        default_command = "render_warm_frame_smoke.ps1 -Frames $Frames -RuntimeBlendTiming"
        high_density_command = "render_warm_frame_smoke.ps1 -Frames $Frames -HighDensityCompose -RuntimeBlendTiming"
        review_command = "review_runtime_blend_timing_evidence.ps1 -OutputPath $reviewSummaryPath -MarkdownPath $reviewMarkdownPath"
        review_summary_path = $reviewSummaryPath
        review_markdown_path = $reviewMarkdownPath
        contract_only_reads_generated_artifacts = $false
        contract_only_writes_generated_artifacts = $false
        normal_mode_writes_ignored_artifacts = $true
        next_instrumentation_gate = "data_ready_boundary_timing_gate"
        optimization_authorized = $false
        metadata_schema_changed = $false
        runtime_merge_enabled = $false
        output_behavior_changed = $false
    } | ConvertTo-Json -Depth 4
    exit 0
}

Write-Host "Runtime blend timing review smoke"
Write-Host "Repo: $repoRoot"
Write-Host "Frames: $Frames"

& powershell -NoProfile -ExecutionPolicy Bypass -File $warmScript -Frames $Frames -RuntimeBlendTiming
if ($LASTEXITCODE -ne 0) {
    throw "Default runtime_blend timing warm-frame smoke failed"
}

& powershell -NoProfile -ExecutionPolicy Bypass -File $warmScript -Frames $Frames -HighDensityCompose -RuntimeBlendTiming
if ($LASTEXITCODE -ne 0) {
    throw "High-density runtime_blend timing warm-frame smoke failed"
}

$reviewArgs = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $reviewScript, "-OutputPath", $reviewSummaryPath, "-MarkdownPath", $reviewMarkdownPath)
if ($Json) {
    $reviewArgs += "-Json"
}

& powershell @reviewArgs
if ($LASTEXITCODE -ne 0) {
    throw "Runtime blend timing evidence review failed"
}

Write-Host "Runtime blend timing review smoke passed."
