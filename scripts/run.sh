#!/bin/bash
# Run both backend and frontend locally (Unix/Mac/Linux)

# Move to project root
cd "$(dirname "$0")/.."

# Activate virtual environment
source ./venv/bin/activate

# Start backend in background
cd backend
python app.py &

# Start frontend
cd ../frontend
python3 -m http.server 8000
