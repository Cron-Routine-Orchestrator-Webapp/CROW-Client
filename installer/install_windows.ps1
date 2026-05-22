# =========================
# CONFIG
# =========================
$Repo = "Cron-Routine-Orchestrator-Webapp/CROW-Client"

$ZipName = "crow-client-Windows.zip"
$BinaryName = "crow-client.exe"

$InstallDir = "$env:APPDATA\crow-client"
$StartupDir = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
$ShortcutPath = "$StartupDir\crow-client.lnk"
# =========================

Write-Output "Fetching latest release..."

$release = Invoke-RestMethod -Uri "https://api.github.com/repos/$Repo/releases/latest"

$asset = $release.assets | Where-Object { $_.name -eq $ZipName } | Select-Object -First 1

if (-not $asset) {
    Write-Error "No matching Windows release found."
    exit 1
}

$zipPath = "$env:TEMP\crow-client.zip"

Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $zipPath

if (Test-Path $InstallDir) {
    Remove-Item $InstallDir -Recurse -Force
}

New-Item -ItemType Directory -Path $InstallDir | Out-Null

Expand-Archive -Path $zipPath -DestinationPath $InstallDir -Force

$exe = Get-ChildItem -Path $InstallDir -Recurse -Filter $BinaryName | Select-Object -First 1

if (-not $exe) {
    Write-Error "Binary not found."
    exit 1
}

# Create shortcut for autostart
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $exe.FullName
$Shortcut.WorkingDirectory = $exe.Directory.FullName
$Shortcut.Save()

Write-Output "Installed on Windows."
