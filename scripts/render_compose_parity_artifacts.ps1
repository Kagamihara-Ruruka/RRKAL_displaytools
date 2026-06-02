param(
    [string]$ArtifactDir = "state/compose_parity",
    [int]$Width = 640,
    [int]$Height = 360,
    [string]$TaichiArch = "cpu",
    [switch]$SkipDiff,
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

if ($ContractOnly) {
    $runnerManifest = Join-Path $ArtifactDir "compose_parity_artifact_runner.json"
    $smokeManifest = Join-Path $ArtifactDir "render_compose_parity_smoke_manifest.json"
    [ordered]@{
        schema = "rrkal_displaytools.compose_run_parity_artifact_runner.v1"
        source = "scripts/render_compose_parity_artifacts.ps1"
        status = "contract_only_no_render_side_effect"
        contract_only = $true
        writes_manifest = $false
        runs_renderer = $false
        runs_diff = $false
        runtime_merge_enabled = $false
        artifact_dir = $ArtifactDir
        runner_manifest = $runnerManifest
        smoke_manifest = $smokeManifest
        contract_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render_compose_parity_artifacts.ps1 -ContractOnly"
        manual_run_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render_compose_parity_artifacts.ps1 -SkipDiff"
        diff_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render_compose_parity_smoke.ps1 -BaselinePath state/compose_parity/baseline_sequential_frame_rgba.png -CandidatePath state/compose_parity/merged_candidate_frame_rgba.png -ManifestPath state/compose_parity/render_compose_parity_smoke_manifest.json -WriteManifest"
        precommit_gate = [ordered]@{
            schema = "rrkal_displaytools.compose_run_parity_precommit_gate.v1"
            required_before_runtime_merge = $true
            pass_fields = @(
                "visual_parity_passed",
                "max_abs_diff",
                "changed_pixel_count",
                "precommit_gate_passed"
            )
            pass_condition = "precommit_gate_passed true only after visual_parity_passed=true, max_abs_diff=0 and changed_pixel_count=0"
            runtime_merge_enabled = $false
        }
        boundary = "Contract-only mode does not create artifact directories, launch Taichi, render frames, diff images, write manifests, or enable runtime merge."
    } | ConvertTo-Json -Depth 8
    exit 0
}

function Resolve-RunnerPath {
    param([string]$PathValue)

    if ([System.IO.Path]::IsPathRooted($PathValue)) {
        return $PathValue
    }
    return Join-Path $RepoRoot $PathValue
}

$artifactPath = Resolve-RunnerPath $ArtifactDir
New-Item -ItemType Directory -Force -Path $artifactPath | Out-Null

$rendererOutput = Join-Path $ArtifactDir "renderer_frame.png"
$baselineArtifact = Join-Path $ArtifactDir "baseline_sequential_frame_rgba.png"
$candidateArtifact = Join-Path $ArtifactDir "merged_candidate_frame_rgba.png"
$metadataArtifact = Join-Path $ArtifactDir "renderer_output_metadata.json"
$runnerManifest = Join-Path $ArtifactDir "compose_parity_artifact_runner.json"
$smokeManifest = Join-Path $ArtifactDir "render_compose_parity_smoke_manifest.json"

$venvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$useLocalVenv = Test-Path -LiteralPath $venvPython
$pythonCommand = if ($useLocalVenv) { $venvPython } else { "py" }
$pythonArgs = if ($useLocalVenv) { @() } else { @("-3") }

$rendererCommand = @(
    $pythonCommand
) + $pythonArgs + @(
    "taichi_global_bathymetry.py",
    "--once",
    "--headless",
    "--topo-source",
    "synthetic",
    "--data-mode",
    "static",
    "--ti-arch",
    $TaichiArch,
    "--width",
    [string]$Width,
    "--height",
    [string]$Height,
    "--output",
    $rendererOutput,
    "--compose-parity-artifact-dir",
    $ArtifactDir
)

& $rendererCommand[0] $rendererCommand[1..($rendererCommand.Count - 1)]
if ($LASTEXITCODE -ne 0) {
    throw "Compose parity artifact renderer command failed with exit code $LASTEXITCODE"
}

$diffCommand = @(
    "powershell",
    "-NoProfile",
    "-ExecutionPolicy",
    "Bypass",
    "-File",
    "scripts\render_compose_parity_smoke.ps1",
    "-BaselinePath",
    $baselineArtifact,
    "-CandidatePath",
    $candidateArtifact,
    "-ManifestPath",
    $smokeManifest,
    "-WriteManifest"
)

$diffStatus = "diff_skipped"
if (-not $SkipDiff) {
    & $diffCommand[0] $diffCommand[1..($diffCommand.Count - 1)]
    if ($LASTEXITCODE -ne 0) {
        throw "Compose parity artifact diff failed with exit code $LASTEXITCODE"
    }
    $diffStatus = "diff_completed"
}

$packet = [ordered]@{
    schema = "rrkal_displaytools.compose_run_parity_artifact_runner.v1"
    source = "scripts/render_compose_parity_artifacts.ps1"
    status = if ($SkipDiff) { "completed_diff_skipped" } else { "completed_with_diff" }
    runtime_merge_enabled = $false
    renderer_command = $rendererCommand
    python_command = $pythonCommand
    python_uses_local_venv = [bool]$useLocalVenv
    python_fallback = "py -3"
    diff_command = $diffCommand
    diff_status = $diffStatus
    precommit_gate = [ordered]@{
        schema = "rrkal_displaytools.compose_run_parity_precommit_gate.v1"
        required_before_runtime_merge = $true
        contract_command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render_compose_parity_smoke.ps1 -ContractOnly"
        artifact_diff_command = $diffCommand
        manifest_path = $smokeManifest
        pass_fields = @(
            "visual_parity_passed",
            "max_abs_diff",
            "changed_pixel_count",
            "precommit_gate_passed"
        )
        pass_condition = "precommit_gate_passed true only after visual_parity_passed=true, max_abs_diff=0 and changed_pixel_count=0"
        skip_diff_status = "completed_diff_skipped"
        runtime_merge_enabled = $false
    }
    artifact_dir = $ArtifactDir
    artifacts = [ordered]@{
        renderer_output = $rendererOutput
        baseline_sequential_frame_rgba = $baselineArtifact
        merged_candidate_frame_rgba = $candidateArtifact
        renderer_output_metadata = $metadataArtifact
    }
    smoke_manifest = $smokeManifest
    runner_manifest = $runnerManifest
    width = $Width
    height = $Height
    taichi_arch = $TaichiArch
    boundary = "Manual cross-machine artifact runner only; precommit smoke keeps using contract-only mode and does not render."
}

$json = $packet | ConvertTo-Json -Depth 8
$runnerManifestPath = Resolve-RunnerPath $runnerManifest
$runnerManifestDirectory = Split-Path -Parent $runnerManifestPath
if ($runnerManifestDirectory) {
    New-Item -ItemType Directory -Force -Path $runnerManifestDirectory | Out-Null
}
[System.IO.File]::WriteAllText(
    $runnerManifestPath,
    $json,
    [System.Text.UTF8Encoding]::new($false)
)

$json
