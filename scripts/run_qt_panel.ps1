param(
    [string]$Profile
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $RepoRoot

$args = @("-3", "rrkal_displaytools_qt_panel.py")
if ($Profile) {
    $args += @("--profile", $Profile)
}
py @args
