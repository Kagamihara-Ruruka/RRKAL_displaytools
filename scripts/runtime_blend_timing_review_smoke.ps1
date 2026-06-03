param(
    [int]$Frames = 3,
    [switch]$Json
)

$ErrorActionPreference = "Stop"

if ($Frames -lt 2) {
    throw "Runtime blend timing review smoke requires Frames >= 2"
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$warmScript = Join-Path $PSScriptRoot "render_warm_frame_smoke.ps1"
$reviewScript = Join-Path $PSScriptRoot "review_runtime_blend_timing_evidence.ps1"

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

$reviewArgs = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $reviewScript)
if ($Json) {
    $reviewArgs += "-Json"
}

& powershell @reviewArgs
if ($LASTEXITCODE -ne 0) {
    throw "Runtime blend timing evidence review failed"
}

Write-Host "Runtime blend timing review smoke passed."
