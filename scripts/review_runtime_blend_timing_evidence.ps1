param(
    [string]$DefaultSummaryPath,
    [string]$DefaultAnalysisPath,
    [string]$HighDensitySummaryPath,
    [string]$HighDensityAnalysisPath,
    [string]$OutputPath,
    [string]$MarkdownPath,
    [switch]$ContractOnly,
    [switch]$Json
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($DefaultSummaryPath)) {
    $DefaultSummaryPath = Join-Path $repoRoot "state\showcase\warm_frame_smoke_runtime_blend_timing\summary.json"
}
if ([string]::IsNullOrWhiteSpace($DefaultAnalysisPath)) {
    $DefaultAnalysisPath = Join-Path $repoRoot "state\showcase\warm_frame_smoke_runtime_blend_timing\analysis.json"
}
if ([string]::IsNullOrWhiteSpace($HighDensitySummaryPath)) {
    $HighDensitySummaryPath = Join-Path $repoRoot "state\showcase\warm_frame_smoke_runtime_blend_timing_high_density\summary.json"
}
if ([string]::IsNullOrWhiteSpace($HighDensityAnalysisPath)) {
    $HighDensityAnalysisPath = Join-Path $repoRoot "state\showcase\warm_frame_smoke_runtime_blend_timing_high_density\analysis.json"
}

if ($ContractOnly) {
    [pscustomobject]@{
        schema = "rrkal_displaytools.runtime_blend_timing_evidence_review_contract.v1"
        mode = "contract_only"
        reads_generated_artifacts = $true
        writes_generated_artifacts = $false
        default_summary_path = $DefaultSummaryPath
        default_analysis_path = $DefaultAnalysisPath
        high_density_summary_path = $HighDensitySummaryPath
        high_density_analysis_path = $HighDensityAnalysisPath
        optional_output_path_parameter = "OutputPath"
        optional_markdown_path_parameter = "MarkdownPath"
        required_summary_schema = "rrkal_displaytools.warm_frame_benchmark.v1"
        output_schema = "rrkal_displaytools.runtime_blend_timing_evidence_review.v1"
        next_instrumentation_gate = "data_ready_boundary_timing_gate"
        optimization_authorized = $false
        metadata_schema_changed = $false
        runtime_merge_enabled = $false
        output_behavior_changed = $false
    } | ConvertTo-Json -Depth 4
    exit 0
}

function Read-JsonFile {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Missing runtime_blend timing evidence artifact: $Path"
    }
    Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
}

function Get-Average {
    param(
        [object[]]$Rows,
        [string]$Property
    )
    if ($Rows.Count -eq 0) {
        return $null
    }
    [math]::Round([double](($Rows | Measure-Object -Property $Property -Average).Average), 3)
}

function Get-RuntimeBlendRows {
    param([object]$Summary)
    $rows = @()
    foreach ($frame in @($Summary.results)) {
        $packet = $frame.runtime_blend_timing
        if (-not $packet -or $packet.runtime_blend_timing_enabled -ne $true) {
            continue
        }
        foreach ($step in @($packet.runtime_blend_step_timings)) {
            $rows += [pscustomobject]@{
                frame = [int]$frame.frame
                step_id = [string]$step.step_id
                layer_kind = [string]$step.layer_kind
                runtime_blend_step_ms = [double]$step.runtime_blend_step_ms
                first_step = [bool]$step.first_runtime_blend_step_may_include_data_ready_wait
            }
        }
    }
    $rows
}

function Summarize-Mode {
    param(
        [string]$Mode,
        [object]$Summary,
        [object]$Analysis
    )
    if ($Summary.runtime_blend_timing_enabled -ne $true) {
        throw "Summary for $Mode is not runtime_blend timing evidence"
    }
    $rows = @(Get-RuntimeBlendRows -Summary $Summary)
    if ($rows.Count -eq 0) {
        throw "Summary for $Mode contains no runtime_blend timing rows"
    }
    $firstRows = @($rows | Where-Object { $_.first_step })
    $nonFirstRows = @($rows | Where-Object { -not $_.first_step })
    $frameTotals = @(
        @($Summary.results) | ForEach-Object {
            $packet = $_.runtime_blend_timing
            [pscustomobject]@{
                frame = [int]$_.frame
                runtime_blend_total_ms = [math]::Round([double]$packet.runtime_blend_total_ms, 3)
                render_ms = [math]::Round([double]$_.render_ms, 3)
                slowest_phase_id = [string]$_.slowest_phase_id
            }
        }
    )
    [pscustomobject]@{
        mode = $Mode
        runtime_blend_run_count = [int]$Analysis.compose_overlay_assessment.runtime_blend_run_count
        runtime_blend_total_ms_avg = [math]::Round([double]$Analysis.compose_overlay_assessment.runtime_blend_total_ms_avg, 3)
        first_runtime_blend_step_ms = Get-Average -Rows $firstRows -Property "runtime_blend_step_ms"
        non_first_runtime_blend_steps_avg_ms = Get-Average -Rows $nonFirstRows -Property "runtime_blend_step_ms"
        timing_interpretation = [string]$Analysis.compose_overlay_assessment.runtime_blend_timing_interpretation
        timing_confidence = [string]$Analysis.compose_overlay_assessment.runtime_blend_timing_confidence
        sync_risk = [string]$Analysis.compose_overlay_assessment.gpu_cpu_sync_misattribution_risk
        next_safe_target = [string]$Analysis.compose_overlay_assessment.runtime_blend_next_safe_target
        optimization_authorized = [bool]$Analysis.compose_overlay_assessment.optimization_authorized
        frame_totals = $frameTotals
    }
}

$defaultSummary = Read-JsonFile -Path $DefaultSummaryPath
$defaultAnalysis = Read-JsonFile -Path $DefaultAnalysisPath
$highSummary = Read-JsonFile -Path $HighDensitySummaryPath
$highAnalysis = Read-JsonFile -Path $HighDensityAnalysisPath

$defaultReview = Summarize-Mode -Mode "default" -Summary $defaultSummary -Analysis $defaultAnalysis
$highDensityReview = Summarize-Mode -Mode "high_density" -Summary $highSummary -Analysis $highAnalysis

$stepCountRatio = [math]::Round(
    [double]$highDensityReview.runtime_blend_run_count / [double]$defaultReview.runtime_blend_run_count,
    3
)
$totalTimingRatio = [math]::Round(
    [double]$highDensityReview.runtime_blend_total_ms_avg / [double]$defaultReview.runtime_blend_total_ms_avg,
    3
)
$roughlyLinearScaling = [math]::Abs($stepCountRatio - $totalTimingRatio) -le 0.5

$review = [pscustomobject]@{
    schema = "rrkal_displaytools.runtime_blend_timing_evidence_review.v1"
    default = $defaultReview
    high_density = $highDensityReview
    step_count_ratio_high_density_over_default = $stepCountRatio
    total_timing_ratio_high_density_over_default = $totalTimingRatio
    roughly_linear_with_step_count = $roughlyLinearScaling
    sync_wait_attribution = "possible_but_not_dominant_in_current_evidence"
    next_instrumentation_gate = "data_ready_boundary_timing_gate"
    optimization_authorized = $false
    output_behavior_changed = $false
    metadata_schema_changed = $false
    runtime_merge_enabled = $false
}

if (-not [string]::IsNullOrWhiteSpace($OutputPath)) {
    $outputDirectory = Split-Path -Parent $OutputPath
    if (-not [string]::IsNullOrWhiteSpace($outputDirectory)) {
        New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null
    }
    $review | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $OutputPath -Encoding UTF8
}

if (-not [string]::IsNullOrWhiteSpace($MarkdownPath)) {
    $markdownDirectory = Split-Path -Parent $MarkdownPath
    if (-not [string]::IsNullOrWhiteSpace($markdownDirectory)) {
        New-Item -ItemType Directory -Force -Path $markdownDirectory | Out-Null
    }
    $markdown = @"
# Runtime Blend Timing Evidence Review

Schema: `$($review.schema)`

## Summary

- Step count ratio high-density/default: `$($review.step_count_ratio_high_density_over_default)`
- Total timing ratio high-density/default: `$($review.total_timing_ratio_high_density_over_default)`
- Roughly linear with step count: `$($review.roughly_linear_with_step_count)`
- Sync-wait attribution: `$($review.sync_wait_attribution)`
- Next instrumentation gate: `$($review.next_instrumentation_gate)`
- Optimization authorized: `$($review.optimization_authorized)`
- Metadata schema changed: `$($review.metadata_schema_changed)`
- Runtime merge enabled: `$($review.runtime_merge_enabled)`
- Output behavior changed: `$($review.output_behavior_changed)`

## Modes

| mode | runtime_blend_run_count | runtime_blend_total_ms_avg | first_runtime_blend_step_ms | non_first_runtime_blend_steps_avg_ms | timing_interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| default | $($defaultReview.runtime_blend_run_count) | $($defaultReview.runtime_blend_total_ms_avg) | $($defaultReview.first_runtime_blend_step_ms) | $($defaultReview.non_first_runtime_blend_steps_avg_ms) | $($defaultReview.timing_interpretation) |
| high_density | $($highDensityReview.runtime_blend_run_count) | $($highDensityReview.runtime_blend_total_ms_avg) | $($highDensityReview.first_runtime_blend_step_ms) | $($highDensityReview.non_first_runtime_blend_steps_avg_ms) | $($highDensityReview.timing_interpretation) |

## Boundary

This report is evidence-only. It does not authorize runtime_blend optimization, alpha blending changes, layer ordering changes, output path changes, metadata sidecar schema changes, runtime merge, or interactive FPS readiness claims.
"@
    Set-Content -LiteralPath $MarkdownPath -Value $markdown -Encoding UTF8
}

if ($Json) {
    $review | ConvertTo-Json -Depth 8
    exit 0
}

Write-Host "Runtime blend timing evidence review"
$review |
    Select-Object schema, step_count_ratio_high_density_over_default, total_timing_ratio_high_density_over_default, roughly_linear_with_step_count, sync_wait_attribution, next_instrumentation_gate, optimization_authorized |
    Format-List
@($defaultReview, $highDensityReview) |
    Select-Object mode, runtime_blend_run_count, runtime_blend_total_ms_avg, first_runtime_blend_step_ms, non_first_runtime_blend_steps_avg_ms, timing_interpretation, timing_confidence, next_safe_target |
    Format-Table -AutoSize
