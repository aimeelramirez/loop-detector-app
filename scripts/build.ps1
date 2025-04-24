# PowerShell-native setup script (scripts/build.ps1)

# Navigate to project root
Set-Location "$PSScriptRoot\.."

# Create virtual environment
python -m venv venv

# Ensure pip is installed and up to date
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Install required packages
python -m pip install flask flask-cors flask-jwt-extended numpy opencv-python mediapipe

# Activate virtual environment (Windows only)
if ($env:OS -eq "Windows_NT") {
    Write-Host "Running on Windows"
    $activateScript = ".\venv\Scripts\Activate.ps1"
    Write-Host "Running: $activateScript"
    & $activateScript
} else {
    Write-Host "Non-Windows OS detected. Please use a Unix-compatible shell."
    exit 1
}

# Install Python dependencies
pip install -r backend\requirements.txt
