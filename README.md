# 🎥 Loop Detector App

This project captures webcam video in the browser, detects loops (e.g., a pink thread) between two hands using computer vision (MediaPipe + OpenCV), and displays the result with a login-protected UI.

---

## ✨ Features

- 👁️ Real-time hand detection
- 🧶 Loop (pink string) detection between hands
- 🔐 Fake login system (JWT-based)
- 🌐 Frontend: GitHub Pages or local HTTP server
- 🧠 Backend: Python Flask API (Heroku or local)

---

🔧 Project Structure (Preview)
```
loop-detector-app/
├── backend/
│   ├── app.py
│   ├── detect.py
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── Procfile
│   └── README.md
├── frontend/
│   ├── index.html
│   └── README.md
├── deploy.sh
└── README.md
```

## 🐍 How to Check if Python Is Correctly Installed on Windows

### ✅ Step 1: Check if `python` is in PATH

```powershell
where python
```

**Expected Output:**
```
C:\Users\yourname\.pyenv\pyenv-win\shims\python.exe
```
or
```
C:\Users\yourname\AppData\Local\Programs\Python\Python3xx\python.exe
```

⚠️ **Not Installed:**
```
C:\Users\yourname\AppData\Local\Microsoft\WindowsApps\python.exe
```

This is a **stub** that just redirects to the Microsoft Store.

---

### ✅ Step 2: Check Python Version

```powershell
python --version
```

✅ Should return:
```
Python 3.11.9
```

⚠️ If you see:
```
Python was not found; run without arguments to install from the Microsoft Store...
```
Then Python isn’t installed correctly.

---

### ✅ Step 3: Confirm It Works in Scripts

```powershell
python -c "print('✅ Python is working!')"
```

Expected:
```
✅ Python is working!
```

---

## 🪶 Lightest on Disk Space (Least Bulk → Most Bulk)

### ✅ 1. Native `venv` (on Windows)
**~25–50MB per environment**

- Lightweight, no Python duplication
- Best if you only need one version

```bash
python -m venv venv
```

---

### 🟡 2. `pyenv-win` + `venv`
**~100–200MB per installed version**

- Each `pyenv install` adds ~100MB
- Each `venv` adds ~30–50MB

```powershell
pyenv install 3.11.7
```

---

### 🐧 3. WSL (Linux with Ubuntu)
**~5–15GB initial install**

- Full Linux environment
- Great for Docker, Linux tools
- ❌ Not ideal for minimal disk usage

```powershell
wsl --install
```

---

### 🔚 Recommendation (for 100GB of space)

| Goal                      | Best Option      |
|---------------------------|------------------|
| Minimal space use         | ✅ Native `venv` |
| Multiple Python versions  | 🟡 `pyenv-win`   |
| Linux-specific tooling    | 🐧 WSL           |

---

## 🧰 Local Setup

### 🐍 Backend (Python + Flask)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # PowerShell: venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
## ⚙️ PowerShell Setup Script (Windows Only)

You can use the provided `build.ps1` to automate backend setup:

```powershell
 Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\build.ps1
```

### Option 1: Run Only Backend for API Testing
```
cd backend
python app.py
```
Use tools like Postman, or open http://localhost:5000 to verify.

### Option 2: Use ngrok for Exposing Local Backend

```bash

ngrok http 5000
```
This will give you a temporary public URL like https://abc123.ngrok.io that your frontend or remote devices can use to POST webcam frames.


Backend available at:  
[http://localhost:5000](http://localhost:5000)

---

### 🖥️ Frontend (HTML + JavaScript)

#### Option 1: Open Directly

```bash
start frontend\index.html
```

#### Option 2: Serve with Python

```bash
cd frontend
python3 -m http.server 8000
```

Visit:  
[http://localhost:8000](http://localhost:8000)

---


## 🔐 Demo Login

- Any username/password accepted
- JWT used to protect backend endpoint
- 🔒 For demonstration only — not secure for production

---

## 📄 License

This software is **proprietary**.

Unauthorized use, reproduction, or redistribution is prohibited without written permission from the author.

© 2025 Aimee L. Ramirez. Developer identity: [@aimeelramirez](https://github.com/aimeelramirez). All rights reserved.
