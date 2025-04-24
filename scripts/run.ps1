# Run both backend and frontend locally (PowerShell version)

# Navigate to project root
$projectRoot = Join-Path $PSScriptRoot ".."
Set-Location $projectRoot

# Run backend in a new PowerShell window
Start-Process powershell -ArgumentList '-NoExit', '-Command', "Set-Location '$projectRoot\backend'; ..\venv\Scripts\Activate.ps1; python app.py"

# Run frontend in another PowerShell window
Start-Process powershell -ArgumentList '-NoExit', '-Command', "Set-Location '$projectRoot\frontend'; python -m http.server 8000"