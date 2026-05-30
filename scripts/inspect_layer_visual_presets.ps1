param(
    [string]$Template = "fast_synthetic",
    [switch]$ContractOnly
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

$scriptName = "scripts/inspect_layer_visual_presets.ps1"

if ($ContractOnly) {
    [ordered]@{
        schema = "rrkal_displaytools.layer_visual_presets_inspector.v1"
        source = $scriptName
        status = "contract_only_no_launch_side_effect"
        launch_packet_fields = @(
            "layer_visual_presets",
            "layer_visual_preset_runtime_feedback",
            "layer_selection_tool",
            "layer_selection_affordance"
        )
        launch_packet_script = "scripts/export_launch_packet.py"
        required_contracts = @(
            "rrkal_displaytools.layer_visual_presets.v1",
            "rrkal_displaytools.layer_visual_preset_runtime_feedback.v1",
            "rrkal_displaytools.layer_selection_tool.v1",
            "rrkal_displaytools.layer_selection_affordance.v1"
        )
        default_template = $Template
        command = "powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_layer_visual_presets.ps1"
        boundary = "Inspector reads launch-packet layer preset and selection contracts only; it does not launch Qt, Taichi, provider IO, dataset discovery, import or cache governance."
        portable = $true
    } | ConvertTo-Json -Depth 8
    exit 0
}

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$venvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$useLocalVenv = Test-Path -LiteralPath $venvPython
$pythonCommand = if ($useLocalVenv) { $venvPython } else { "py" }

if ($useLocalVenv) {
    $launchPacketText = & $pythonCommand "scripts\export_launch_packet.py" "--template" $Template
} else {
    $launchPacketText = & $pythonCommand "-3" "scripts\export_launch_packet.py" "--template" $Template
}
if ($LASTEXITCODE -ne 0) {
    throw "Launch packet export failed while inspecting layer visual presets"
}

$launchPacket = ($launchPacketText -join "`n") | ConvertFrom-Json
$requiredFields = @(
    "layer_visual_presets",
    "layer_visual_preset_runtime_feedback",
    "layer_selection_tool",
    "layer_selection_affordance"
)
foreach ($field in $requiredFields) {
    if (-not $launchPacket.$field) {
        throw "Launch packet $field field is missing"
    }
}

$presets = $launchPacket.layer_visual_presets
$feedback = $launchPacket.layer_visual_preset_runtime_feedback
$selection = $launchPacket.layer_selection_tool
$affordance = $launchPacket.layer_selection_affordance

[ordered]@{
    schema = "rrkal_displaytools.layer_visual_presets_inspection.v1"
    source = $scriptName
    template = $Template
    presets_schema = $presets.schema
    preset_count = $presets.preset_count
    preset_ids = @($presets.preset_ids)
    selected_preset = $presets.selected_preset
    qt_surface = $presets.qt_surface
    brush_mask_scope = $presets.brush_mask_scope
    respects_layer_locks = $presets.respects_layer_locks
    runtime_feedback_schema = $feedback.schema
    runtime_feedback_status = $feedback.status
    runtime_feedback_requires_renderer_ack = $feedback.requires_renderer_ack_for_reproducibility
    selection_tool_schema = $selection.schema
    selection_tool_mode = $selection.tool_mode
    selection_brush_mask_scope = $selection.brush_mask_scope
    selectable_layer_count = $selection.selectable_layer_count
    supported_renderer_pick_scopes = @($selection.supported_renderer_pick_scopes)
    selection_affordance_schema = $affordance.schema
    selection_affordance_status = $affordance.status
    selection_affordance_quick_actions = @($affordance.active_quick_actions)
    layer_controls_scope = "selection_and_visibility_presets_without_brush_or_mask_tools"
    ready_for_clone_review = $true
    boundary = "Layer visual preset inspection is displaytools UI/contract review only; RRKAL owns data/cache governance and authoritative geospatial identity."
    portable = $true
} | ConvertTo-Json -Depth 12
