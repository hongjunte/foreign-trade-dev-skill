$ws = New-Object -ComObject WScript.Shell
$lnkPath = Join-Path $PSScriptRoot "GCCS Trade Hunter.lnk"
$lnk = $ws.CreateShortcut($lnkPath)
$lnk.TargetPath = Join-Path $PSScriptRoot "start.bat"
$lnk.WorkingDirectory = $PSScriptRoot
$lnk.IconLocation = "shell32.dll,13"
$lnk.Description = "GCCS Trade Hunter"
$lnk.WindowStyle = 7
$lnk.Save()
Write-Host "OK: $lnkPath"
