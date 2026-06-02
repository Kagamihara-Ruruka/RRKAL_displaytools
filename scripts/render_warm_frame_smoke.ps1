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
$analysisPath = Join-Path $artifactDir "analysis.json"
$metadataPath = "$outputPath.metadata.json"

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
if (-not (Test-Path -LiteralPath $metadataPath)) {
    throw "Warm frame smoke metadata missing: $metadataPath"
}

$summary = Get-Content -LiteralPath $summaryPath -Raw -Encoding UTF8 | ConvertFrom-Json
$metadata = Get-Content -LiteralPath $metadataPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($summary.schema -ne "rrkal_displaytools.warm_frame_benchmark.v1") {
    throw "Unexpected warm frame benchmark schema: $($summary.schema)"
}
if ($metadata.schema -ne "rrkal_displaytools.renderer_output_metadata.v1") {
    throw "Unexpected warm frame renderer metadata schema: $($metadata.schema)"
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

$results = @($summary.results)
if ($results.Count -ne $Frames) {
    throw "Unexpected warm frame result count: $($results.Count)"
}

function Get-AverageMs {
    param(
        [object[]]$Rows,
        [string]$PropertyName
    )

    $values = @(
        $Rows | ForEach-Object {
            $property = $_.PSObject.Properties[$PropertyName]
            if ($null -ne $property -and $null -ne $property.Value) {
                [double]$property.Value
            }
        }
    )
    if ($values.Count -eq 0) {
        return $null
    }
    $total = 0.0
    foreach ($value in $values) {
        $total += $value
    }
    return [math]::Round($total / $values.Count, 3)
}

$firstFrame = $results[0]
$warmFrames = @($results | Select-Object -Skip 1)
if ($warmFrames.Count -eq 0) {
    $warmFrames = @($firstFrame)
}
$lastWarmFrame = $warmFrames[-1]
$slowestPhaseCounts = @{}
foreach ($result in $results) {
    $phase = [string]$result.slowest_phase_id
    if ([string]::IsNullOrWhiteSpace($phase)) {
        $phase = "unknown"
    }
    if (-not $slowestPhaseCounts.ContainsKey($phase)) {
        $slowestPhaseCounts[$phase] = 0
    }
    $slowestPhaseCounts[$phase] += 1
}
$slowestPhaseRows = @(
    $slowestPhaseCounts.GetEnumerator() |
        Sort-Object Name |
        ForEach-Object {
            [pscustomobject]@{
                slowest_phase_id = $_.Key
                count = $_.Value
            }
        }
)
$recommendedNextTarget = switch ([string]$lastWarmFrame.slowest_phase_id) {
    "compose_overlays" { "compose_overlays" }
    "prepare_batches" { "prepare_batches" }
    default { "timing_summary_review" }
}
$renderPlan = $metadata.layer_render_plan
$renderPlan = if ($renderPlan) { $renderPlan } else { [pscustomobject]@{} }
$composeQueuePacket = $renderPlan.compose_queue_packet
$composeQueuePacket = if ($composeQueuePacket) { $composeQueuePacket } else { [pscustomobject]@{} }
$composeQueue = @($composeQueuePacket.queue)
$skippedSteps = @($composeQueuePacket.skipped_steps)
$composeRuns = @($composeQueuePacket.compose_runs)
$queueKindCounts = @{}
foreach ($step in $composeQueue) {
    $kind = [string]$step.kind
    if ([string]::IsNullOrWhiteSpace($kind)) {
        $kind = "unknown"
    }
    if (-not $queueKindCounts.ContainsKey($kind)) {
        $queueKindCounts[$kind] = 0
    }
    $queueKindCounts[$kind] += 1
}
$queueKindRows = @(
    $queueKindCounts.GetEnumerator() |
        Sort-Object Name |
        ForEach-Object {
            [pscustomobject]@{
                kind = $_.Key
                count = $_.Value
            }
        }
)
$skipReasonCounts = @{}
foreach ($step in $skippedSteps) {
    $reason = [string]$step.reason
    if ([string]::IsNullOrWhiteSpace($reason)) {
        $reason = "unknown"
    }
    if (-not $skipReasonCounts.ContainsKey($reason)) {
        $skipReasonCounts[$reason] = 0
    }
    $skipReasonCounts[$reason] += 1
}
$skipReasonRows = @(
    $skipReasonCounts.GetEnumerator() |
        Sort-Object Name |
        ForEach-Object {
            [pscustomobject]@{
                reason = $_.Key
                count = $_.Value
            }
        }
)
$multiStepAlphaComposeRuns = @(
    $composeRuns | Where-Object {
        $_.run_kind -eq "alpha_compose_overlays" -and
        $_.merge_safe -eq $true -and
        [int]$_.step_count -gt 1
    }
)
$inputStepCount = if ($null -ne $composeQueuePacket.input_step_count) { [int]$composeQueuePacket.input_step_count } else { 0 }
$executableStepCount = if ($null -ne $composeQueuePacket.executable_step_count) { [int]$composeQueuePacket.executable_step_count } else { $composeQueue.Count }
$skippedStepCount = if ($null -ne $composeQueuePacket.skipped_step_count) { [int]$composeQueuePacket.skipped_step_count } else { $skippedSteps.Count }
$composeRunCount = if ($null -ne $composeQueuePacket.compose_run_count) { [int]$composeQueuePacket.compose_run_count } else { $composeRuns.Count }
$composeMergeCandidateRunCount = if ($null -ne $composeQueuePacket.compose_merge_candidate_run_count) { [int]$composeQueuePacket.compose_merge_candidate_run_count } else { 0 }
$executableStepIds = @(
    $composeQueue | ForEach-Object {
        $stepId = [string]$_.id
        if ([string]::IsNullOrWhiteSpace($stepId)) {
            $stepId = [string]$_.layer_id
        }
        if ([string]::IsNullOrWhiteSpace($stepId)) {
            $stepId = "unknown_step"
        }
        $stepId
    }
)
$skippedStepIds = @(
    $skippedSteps | ForEach-Object {
        $stepId = [string]$_.id
        if ([string]::IsNullOrWhiteSpace($stepId)) {
            $stepId = "unknown_step"
        }
        $stepId
    }
)
$composeAssessment = [ordered]@{
    schema = "rrkal_displaytools.compose_overlay_assessment.v1"
    source_metadata = $metadataPath
    input_step_count = $inputStepCount
    executable_step_count = $executableStepCount
    skipped_step_count = $skippedStepCount
    compose_run_count = $composeRunCount
    compose_merge_candidate_run_count = $composeMergeCandidateRunCount
    multi_step_alpha_compose_run_count = $multiStepAlphaComposeRuns.Count
    queue_kind_counts = $queueKindRows
    skip_reason_counts = $skipReasonRows
    executable_step_ids = $executableStepIds
    skipped_step_ids = $skippedStepIds
    transparent_or_empty_overlays_skipped = ($skipReasonCounts.ContainsKey("transparent_overlay") -or $skipReasonCounts.ContainsKey("missing_overlay"))
    hidden_overlays_skipped = $skipReasonCounts.ContainsKey("hidden_layer")
    runtime_merge_enabled = $false
    metadata_schema_changed = $false
    output_pixels_changed = $false
    assessment = "Current queue already excludes skipped steps before composition; this script records queue/run facts only and does not change alpha blending, layer ordering, runtime merge, or output paths."
}
$analysis = [ordered]@{
    schema = "rrkal_displaytools.warm_frame_smoke_analysis.v1"
    source_summary = $summaryPath
    source_metadata = $metadataPath
    frame_count = $Frames
    first_frame_render_ms = [math]::Round([double]$firstFrame.render_ms, 3)
    warm_frame_count = $warmFrames.Count
    warm_frame_render_ms_avg = Get-AverageMs -Rows $warmFrames -PropertyName "render_ms"
    warm_frame_prepare_batches_ms_avg = Get-AverageMs -Rows $warmFrames -PropertyName "prepare_batches_ms"
    warm_frame_compose_overlays_ms_avg = Get-AverageMs -Rows $warmFrames -PropertyName "compose_overlays_ms"
    final_warm_slowest_phase_id = [string]$lastWarmFrame.slowest_phase_id
    recommended_next_target = $recommendedNextTarget
    slowest_phase_counts = $slowestPhaseRows
    metadata_schema_changed = $false
    runtime_merge_enabled = $false
    measures_in_process_warm_frame = $true
    interactive_fps_readiness_claim = $false
    compose_overlay_assessment = $composeAssessment
}
$analysis | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $analysisPath -Encoding UTF8

Write-Host "Warm frame smoke summary: $summaryPath"
$summary.results |
    Select-Object frame, render_ms, frame_wall_ms, prepare_batches_ms, compose_overlays_ms, slowest_phase_id, bottleneck_recommendation |
    Format-Table -AutoSize

Write-Host "Warm frame smoke analysis: $analysisPath"
[pscustomobject]@{
    first_frame_render_ms = $analysis.first_frame_render_ms
    warm_frame_render_ms_avg = $analysis.warm_frame_render_ms_avg
    warm_frame_prepare_batches_ms_avg = $analysis.warm_frame_prepare_batches_ms_avg
    warm_frame_compose_overlays_ms_avg = $analysis.warm_frame_compose_overlays_ms_avg
    final_warm_slowest_phase_id = $analysis.final_warm_slowest_phase_id
    recommended_next_target = $analysis.recommended_next_target
} | Format-List
$slowestPhaseRows | Format-Table -AutoSize

Write-Host "Compose overlay assessment:"
[pscustomobject]@{
    input_step_count = $composeAssessment.input_step_count
    executable_step_count = $composeAssessment.executable_step_count
    skipped_step_count = $composeAssessment.skipped_step_count
    compose_run_count = $composeAssessment.compose_run_count
    compose_merge_candidate_run_count = $composeAssessment.compose_merge_candidate_run_count
    multi_step_alpha_compose_run_count = $composeAssessment.multi_step_alpha_compose_run_count
    hidden_overlays_skipped = $composeAssessment.hidden_overlays_skipped
    transparent_or_empty_overlays_skipped = $composeAssessment.transparent_or_empty_overlays_skipped
} | Format-List
$queueKindRows | Format-Table -AutoSize
$skipReasonRows | Format-Table -AutoSize
