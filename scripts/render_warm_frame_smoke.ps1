param(
    [ValidateRange(1, 30)]
    [int]$Frames = 3,
    [string]$OutputDir = "state\showcase\warm_frame_smoke",
    [string]$StyleProfile = "scientific",
    [int]$Width = 640,
    [int]$Height = 360,
    [int]$TopoStep = 96,
    [switch]$HighDensityCompose
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

if ($HighDensityCompose -and $OutputDir -eq "state\showcase\warm_frame_smoke") {
    $OutputDir = "state\showcase\warm_frame_smoke_high_density"
}

$artifactDir = Join-Path $RepoRoot $OutputDir
New-Item -ItemType Directory -Force -Path $artifactDir | Out-Null

$outputPath = Join-Path $artifactDir "frame.png"
$previewPath = Join-Path $artifactDir "preview.png"
$summaryPath = Join-Path $artifactDir "summary.json"
$analysisPath = Join-Path $artifactDir "analysis.json"
$metadataPath = "$outputPath.metadata.json"
$densityMode = if ($HighDensityCompose) { "high_density_compose" } else { "bounded_quick_equivalent" }

$rendererArgs = @(
    "taichi_global_bathymetry.py",
    "--headless",
    "--once",
    "--demo-closed-loop",
    "--style-profile", $StyleProfile,
    "--topo-source", "synthetic",
    "--topo-step", $TopoStep,
    "--width", $Width,
    "--height", $Height
)
if ($HighDensityCompose) {
    $rendererArgs += @(
        "--lake-layer",
        "--river-layer",
        "--border-layer",
        "--territorial-sea-layer",
        "--eez-layer",
        "--high-seas-layer",
        "--aircraft-layer",
        "--pin-layer",
        "--vehicle-icons"
    )
} else {
    $rendererArgs += @(
        "--no-lake-layer",
        "--no-river-layer",
        "--no-border-layer",
        "--no-territorial-sea-layer",
        "--no-eez-layer",
        "--no-high-seas-layer",
        "--no-aircraft-layer",
        "--no-pin-layer"
    )
}
$rendererArgs += @(
    "--output", $outputPath,
    "--preview-frame-file", $previewPath,
    "--preview-frame-interval", 0.05,
    "--benchmark-frames", $Frames,
    "--benchmark-summary", $summaryPath
)

& py -3 @rendererArgs
if ($LASTEXITCODE -ne 0) {
    throw "Warm frame renderer command failed with exit code $LASTEXITCODE"
}

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
$runtimeBlendRunCount = @($composeRuns | Where-Object { [string]$_.run_kind -eq "runtime_layer_overlay" }).Count
$alphaComposeRunCount = @($composeRuns | Where-Object { [string]$_.run_kind -eq "alpha_compose_overlays" }).Count
$styleProfilePostprocessRunCount = @($composeRuns | Where-Object { [string]$_.run_kind -eq "postprocess" }).Count
if ($runtimeBlendRunCount -eq 0 -and $queueKindCounts.ContainsKey("runtime_blend")) {
    $runtimeBlendRunCount = [int]$queueKindCounts["runtime_blend"]
}
if ($alphaComposeRunCount -eq 0 -and $queueKindCounts.ContainsKey("alpha_compose")) {
    $alphaComposeRunCount = [int]$queueKindCounts["alpha_compose"]
}
if ($styleProfilePostprocessRunCount -eq 0 -and $queueKindCounts.ContainsKey("style_profile_postprocess")) {
    $styleProfilePostprocessRunCount = [int]$queueKindCounts["style_profile_postprocess"]
}
$alphaComposeCollapseCandidatePresent = $multiStepAlphaComposeRuns.Count -gt 0
$parityWorkflowRecommendedNow = $alphaComposeCollapseCandidatePresent
if ($alphaComposeCollapseCandidatePresent) {
    $composePressureClassification = "mostly_alpha_compose"
    $decisionClassification = "alpha_collapse_candidate_found_but_needs_parity"
    $classificationRecommendedNextTarget = "alpha_compose_parity_workflow"
    $targetedAlphaComposeEvidenceResult = "At least one multi-step alpha_compose run is present; collapse work still requires parity evidence before any optimization."
} elseif (
    $runtimeBlendRunCount -gt 0 -and
    $runtimeBlendRunCount -gt $alphaComposeRunCount -and
    $runtimeBlendRunCount -ge $styleProfilePostprocessRunCount
) {
    $composePressureClassification = "mostly_runtime_blend"
    $decisionClassification = "no_alpha_collapse_candidate_runtime_blend_dominant"
    $classificationRecommendedNextTarget = "runtime_blend_assessment"
    $targetedAlphaComposeEvidenceResult = "No multi-step alpha_compose run is present in this evidence mode; alpha collapse is not justified without a stronger target case."
} elseif (
    $styleProfilePostprocessRunCount -gt 0 -and
    $styleProfilePostprocessRunCount -gt $runtimeBlendRunCount -and
    $styleProfilePostprocessRunCount -gt $alphaComposeRunCount
) {
    $composePressureClassification = "mostly_postprocess"
    $decisionClassification = "need_more_targeted_evidence"
    $classificationRecommendedNextTarget = "postprocess_timing_evidence"
    $targetedAlphaComposeEvidenceResult = "No multi-step alpha_compose run is present, and postprocess dominates the visible run count; more targeted evidence is needed before optimization."
} else {
    $composePressureClassification = "mixed_unknown"
    $decisionClassification = "need_more_targeted_evidence"
    $classificationRecommendedNextTarget = "compose_overlay_evidence"
    $targetedAlphaComposeEvidenceResult = "Current evidence does not isolate alpha_compose, runtime_blend, or postprocess pressure strongly enough for an optimization target."
}
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
    density_mode = $densityMode
    source_metadata = $metadataPath
    input_step_count = $inputStepCount
    executable_step_count = $executableStepCount
    skipped_step_count = $skippedStepCount
    compose_run_count = $composeRunCount
    compose_merge_candidate_run_count = $composeMergeCandidateRunCount
    multi_step_alpha_compose_run_count = $multiStepAlphaComposeRuns.Count
    alpha_compose_collapse_candidate_present = $alphaComposeCollapseCandidatePresent
    runtime_blend_run_count = $runtimeBlendRunCount
    alpha_compose_run_count = $alphaComposeRunCount
    style_profile_postprocess_run_count = $styleProfilePostprocessRunCount
    compose_pressure_classification = $composePressureClassification
    parity_workflow_recommended_now = $parityWorkflowRecommendedNow
    decision_classification = $decisionClassification
    targeted_alpha_compose_evidence_result = $targetedAlphaComposeEvidenceResult
    queue_kind_counts = $queueKindRows
    skip_reason_counts = $skipReasonRows
    executable_step_ids = $executableStepIds
    skipped_step_ids = $skippedStepIds
    transparent_or_empty_overlays_skipped = ($skipReasonCounts.ContainsKey("transparent_overlay") -or $skipReasonCounts.ContainsKey("missing_overlay"))
    hidden_overlays_skipped = $skipReasonCounts.ContainsKey("hidden_layer")
    compose_overlays_ms = if ($null -ne $lastWarmFrame.compose_overlays_ms) { [math]::Round([double]$lastWarmFrame.compose_overlays_ms, 3) } else { $null }
    compose_queue_build_ms = $null
    compose_runtime_blend_ms = $null
    compose_alpha_compose_ms = $null
    compose_postprocess_ms = Get-AverageMs -Rows $warmFrames -PropertyName "postprocess_ms"
    compose_copy_or_allocation_ms = $null
    merge_candidate_count = $composeMergeCandidateRunCount
    timing_recommended_next_target = $recommendedNextTarget
    recommended_next_target = $classificationRecommendedNextTarget
    optimization_authorized = $false
    subphase_timing_limitation = "Renderer metadata currently exposes aggregate compose_overlays and postprocess timing only; runtime_blend, alpha_compose, queue-build and allocation timing would require renderer instrumentation and is intentionally not added in this evidence-only script."
    runtime_merge_enabled = $false
    metadata_schema_changed = $false
    output_pixels_changed = $false
    assessment = "Current queue already excludes skipped steps before composition; this script records queue/run facts only and does not change alpha blending, layer ordering, runtime merge, or output paths."
}
$analysis = [ordered]@{
    schema = "rrkal_displaytools.warm_frame_smoke_analysis.v1"
    source_summary = $summaryPath
    source_metadata = $metadataPath
    density_mode = $densityMode
    frame_count = $Frames
    first_frame_render_ms = [math]::Round([double]$firstFrame.render_ms, 3)
    warm_frame_count = $warmFrames.Count
    warm_frame_render_ms_avg = Get-AverageMs -Rows $warmFrames -PropertyName "render_ms"
    warm_frame_prepare_batches_ms_avg = Get-AverageMs -Rows $warmFrames -PropertyName "prepare_batches_ms"
    warm_frame_compose_overlays_ms_avg = Get-AverageMs -Rows $warmFrames -PropertyName "compose_overlays_ms"
    final_warm_slowest_phase_id = [string]$lastWarmFrame.slowest_phase_id
    timing_recommended_next_target = $recommendedNextTarget
    recommended_next_target = $classificationRecommendedNextTarget
    compose_pressure_classification = $composePressureClassification
    alpha_compose_collapse_candidate_present = $alphaComposeCollapseCandidatePresent
    multi_step_alpha_compose_run_count = $multiStepAlphaComposeRuns.Count
    runtime_blend_run_count = $runtimeBlendRunCount
    style_profile_postprocess_run_count = $styleProfilePostprocessRunCount
    parity_workflow_recommended_now = $parityWorkflowRecommendedNow
    optimization_authorized = $false
    decision_classification = $decisionClassification
    slowest_phase_counts = $slowestPhaseRows
    metadata_schema_changed = $false
    runtime_merge_enabled = $false
    measures_in_process_warm_frame = $true
    interactive_fps_readiness_claim = $false
    compose_overlay_assessment = $composeAssessment
}
$analysis | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $analysisPath -Encoding UTF8

Write-Host "Warm frame smoke summary: $summaryPath"
Write-Host "Warm frame density mode: $densityMode"
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
    timing_recommended_next_target = $analysis.timing_recommended_next_target
    recommended_next_target = $analysis.recommended_next_target
    decision_classification = $analysis.decision_classification
    compose_pressure_classification = $analysis.compose_pressure_classification
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
    alpha_compose_collapse_candidate_present = $composeAssessment.alpha_compose_collapse_candidate_present
    runtime_blend_run_count = $composeAssessment.runtime_blend_run_count
    alpha_compose_run_count = $composeAssessment.alpha_compose_run_count
    style_profile_postprocess_run_count = $composeAssessment.style_profile_postprocess_run_count
    compose_pressure_classification = $composeAssessment.compose_pressure_classification
    parity_workflow_recommended_now = $composeAssessment.parity_workflow_recommended_now
    decision_classification = $composeAssessment.decision_classification
    recommended_next_target = $composeAssessment.recommended_next_target
    optimization_authorized = $composeAssessment.optimization_authorized
    hidden_overlays_skipped = $composeAssessment.hidden_overlays_skipped
    transparent_or_empty_overlays_skipped = $composeAssessment.transparent_or_empty_overlays_skipped
} | Format-List
$queueKindRows | Format-Table -AutoSize
$skipReasonRows | Format-Table -AutoSize
