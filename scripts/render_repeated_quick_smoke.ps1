param(
    [ValidateRange(1, 99)]
    [int]$Frames = 3,
    [string]$OutputDir = "state\showcase\repeated_quick_smoke",
    [string]$StyleProfile = "scientific",
    [int]$Width = 640,
    [int]$Height = 360,
    [int]$TopoStep = 96
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

$quickSmokeScript = Join-Path $RepoRoot "scripts\render_quick_smoke.ps1"
if (-not (Test-Path -LiteralPath $quickSmokeScript)) {
    throw "Missing quick render smoke script: $quickSmokeScript"
}

$artifactDir = Join-Path $RepoRoot $OutputDir
New-Item -ItemType Directory -Force -Path $artifactDir | Out-Null

function Get-JsonProperty {
    param(
        [object]$Object,
        [string]$Name
    )
    if ($null -eq $Object) {
        return $null
    }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property) {
        return $null
    }
    return $property.Value
}

$results = @()
for ($index = 1; $index -le $Frames; $index += 1) {
    $frameId = "{0:D2}" -f $index
    $framePath = Join-Path $artifactDir "frame_$frameId.png"
    $previewPath = Join-Path $artifactDir "preview_$frameId.png"
    $relativeFramePath = Resolve-Path -LiteralPath (Split-Path -Parent $framePath) -Relative
    $relativePreviewPath = Resolve-Path -LiteralPath (Split-Path -Parent $previewPath) -Relative
    $relativeFrame = Join-Path $relativeFramePath (Split-Path -Leaf $framePath)
    $relativePreview = Join-Path $relativePreviewPath (Split-Path -Leaf $previewPath)

    powershell -NoProfile -ExecutionPolicy Bypass -File $quickSmokeScript `
        -Output $relativeFrame `
        -PreviewFrame $relativePreview `
        -StyleProfile $StyleProfile `
        -Width $Width `
        -Height $Height `
        -TopoStep $TopoStep

    if (-not (Test-Path -LiteralPath $framePath)) {
        throw "Repeated quick smoke frame missing: $framePath"
    }
    if (-not (Test-Path -LiteralPath $previewPath)) {
        throw "Repeated quick smoke preview missing: $previewPath"
    }
    if ((Get-Item -LiteralPath $previewPath).Length -le 0) {
        throw "Repeated quick smoke preview is empty: $previewPath"
    }

    $metadataPath = "$framePath.metadata.json"
    if (-not (Test-Path -LiteralPath $metadataPath)) {
        throw "Repeated quick smoke metadata missing: $metadataPath"
    }
    $metadata = Get-Content -LiteralPath $metadataPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($metadata.schema -ne "rrkal_displaytools.renderer_output_metadata.v1") {
        throw "Unexpected repeated quick smoke metadata schema: $($metadata.schema)"
    }

    $plan = Get-JsonProperty $metadata "layer_render_plan"
    $phaseRuntime = Get-JsonProperty $plan "phase_timing_runtime"
    $phaseTiming = Get-JsonProperty $phaseRuntime "phase_timing_ms"
    $recommendation = Get-JsonProperty $phaseRuntime "bottleneck_recommendation"

    $results += [ordered]@{
        frame = $index
        frame_path = $framePath
        preview_path = $previewPath
        metadata_path = $metadataPath
        metadata_schema = $metadata.schema
        render_ms = [double]$metadata.render_ms
        prepare_batches_ms = [double](Get-JsonProperty $phaseTiming "prepare_batches")
        compose_overlays_ms = [double](Get-JsonProperty $phaseTiming "compose_overlays")
        postprocess_ms = [double](Get-JsonProperty $phaseTiming "postprocess")
        slowest_phase_id = [string](Get-JsonProperty $phaseRuntime "slowest_phase_id")
        slowest_phase_ms = [double](Get-JsonProperty $phaseRuntime "slowest_phase_ms")
        slow_frame = [bool](Get-JsonProperty $phaseRuntime "slow_frame")
        bottleneck_recommendation = Get-JsonProperty $recommendation "recommended_next_action"
        runtime_optimization_applied = [bool](Get-JsonProperty $recommendation "runtime_optimization_applied")
        preview_bytes = [int64](Get-Item -LiteralPath $previewPath).Length
        output_bytes = [int64](Get-Item -LiteralPath $framePath).Length
    }
}

$renderMsValues = @($results | ForEach-Object { [double]$_["render_ms"] })
$prepareValues = @($results | ForEach-Object { [double]$_["prepare_batches_ms"] })
$composeValues = @($results | ForEach-Object { [double]$_["compose_overlays_ms"] })
$summary = [ordered]@{
    schema = "rrkal_displaytools.repeated_quick_smoke.v1"
    generated_at_utc = [DateTimeOffset]::UtcNow.ToString("o")
    source = "scripts/render_repeated_quick_smoke.ps1"
    quick_smoke_script = "scripts/render_quick_smoke.ps1"
    frame_count = $Frames
    output_dir = $artifactDir
    metadata_schema = "rrkal_displaytools.renderer_output_metadata.v1"
    render_ms_avg = ($renderMsValues | Measure-Object -Average).Average
    render_ms_min = ($renderMsValues | Measure-Object -Minimum).Minimum
    render_ms_max = ($renderMsValues | Measure-Object -Maximum).Maximum
    prepare_batches_ms_avg = ($prepareValues | Measure-Object -Average).Average
    prepare_batches_ms_min = ($prepareValues | Measure-Object -Minimum).Minimum
    prepare_batches_ms_max = ($prepareValues | Measure-Object -Maximum).Maximum
    compose_overlays_ms_avg = ($composeValues | Measure-Object -Average).Average
    compose_overlays_ms_min = ($composeValues | Measure-Object -Minimum).Minimum
    compose_overlays_ms_max = ($composeValues | Measure-Object -Maximum).Maximum
    slowest_phase_ids = @($results | ForEach-Object { $_["slowest_phase_id"] } | Sort-Object -Unique)
    bottleneck_recommendations = @($results | ForEach-Object { $_["bottleneck_recommendation"] } | Sort-Object -Unique)
    preview_artifacts_emitted = -not @($results | Where-Object { [int64]$_["preview_bytes"] -le 0 })
    runtime_merge_enabled = $false
    metadata_schema_changed = $false
    results = $results
    boundary = "Evidence-only wrapper around render_quick_smoke.ps1; does not change renderer runtime, metadata schema, runtime merge, or cross-repo integration."
}

$summaryPath = Join-Path $artifactDir "summary.json"
$summary | ConvertTo-Json -Depth 16 | Set-Content -LiteralPath $summaryPath -Encoding UTF8

Write-Host "Repeated quick smoke summary: $summaryPath"
$results |
    ForEach-Object { [PSCustomObject]$_ } |
    Select-Object frame, render_ms, prepare_batches_ms, compose_overlays_ms, slowest_phase_id, bottleneck_recommendation |
    Format-Table -AutoSize
