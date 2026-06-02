param(
    [ValidateRange(1, 30)]
    [int]$Frames = 3,
    [string]$OutputDir = "state\showcase\warm_frame_smoke",
    [string]$StyleProfile = "scientific",
    [int]$Width = 640,
    [int]$Height = 360,
    [int]$TopoStep = 96
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

$artifactDir = Join-Path $RepoRoot $OutputDir
New-Item -ItemType Directory -Force -Path $artifactDir | Out-Null

$outputPath = Join-Path $artifactDir "frame.png"
$previewPath = Join-Path $artifactDir "preview.png"
$summaryPath = Join-Path $artifactDir "summary.json"

py -3 taichi_global_bathymetry.py `
    --headless `
    --once `
    --demo-closed-loop `
    --style-profile $StyleProfile `
    --topo-source synthetic `
    --topo-step $TopoStep `
    --width $Width `
    --height $Height `
    --no-lake-layer `
    --no-river-layer `
    --no-border-layer `
    --no-territorial-sea-layer `
    --no-eez-layer `
    --no-high-seas-layer `
    --no-aircraft-layer `
    --no-pin-layer `
    --output $outputPath `
    --preview-frame-file $previewPath `
    --preview-frame-interval 0.05 `
    --benchmark-frames $Frames `
    --benchmark-summary $summaryPath

if (-not (Test-Path -LiteralPath $outputPath)) {
    throw "Warm frame smoke render output missing: $outputPath"
}
if (-not (Test-Path -LiteralPath $previewPath)) {
    throw "Warm frame smoke preview missing: $previewPath"
}
if ((Get-Item -LiteralPath $previewPath).Length -le 0) {
    throw "Warm frame smoke preview is empty: $previewPath"
}
if (-not (Test-Path -LiteralPath $summaryPath)) {
    throw "Warm frame smoke summary missing: $summaryPath"
}

$summary = Get-Content -LiteralPath $summaryPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($summary.schema -ne "rrkal_displaytools.warm_frame_benchmark.v1") {
    throw "Unexpected warm frame benchmark schema: $($summary.schema)"
}
if ([int]$summary.frame_count -ne $Frames) {
    throw "Unexpected warm frame benchmark frame count: $($summary.frame_count)"
}
if ($summary.runtime_merge_enabled -ne $false) {
    throw "Warm frame benchmark must keep runtime merge disabled"
}
if ($summary.metadata_schema_changed -ne $false) {
    throw "Warm frame benchmark must not change metadata schema"
}

Write-Host "Warm frame smoke summary: $summaryPath"
$summary.results |
    Select-Object frame, render_ms, frame_wall_ms, prepare_batches_ms, compose_overlays_ms, slowest_phase_id, bottleneck_recommendation |
    Format-Table -AutoSize
