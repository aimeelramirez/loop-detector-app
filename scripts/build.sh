#!/bin/bash
# Cross-platform setup script

# Go to project root
cd "$(dirname "$0")/.."

# Create venv
python3 -m venv venv

# Detect platform and activate venv accordingly
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    echo "Running on Windows (use PowerShell instead)"
    echo "Running: .\\venv\\Scripts\\Activate.ps1"
    powershell.exe -ExecutionPolicy Bypass -File .\\venv\\Scripts\\Activate.ps1
else
    source ./venv/bin/activate
fi
# Install Python dependencies
pip install -r backend/requirements.txt
