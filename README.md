
# 🎥 Loop Detector App

> This project captures webcam video in the browser, detects loops (e.g., a pink or white thread) between two hands using computer vision (**MediaPipe + OpenCV**), and displays the result with a **dummy login UI**.

---

## ✨ Features

- 👁️ Real-time hand tracking using **MediaPipe**
- 🧶 Loop (pink string) detection with **OpenCV**
- 🔐 Fake login system (JWT-based)

# User: **admin**
# Password: **admin**

- 🌐 **Frontend:** GitHub Pages or local HTTP server
- 🧠 **Backend:** Python Flask API (**Render**)

---

🔧 **Project Structure**
```
loop-detector-app/
├── backend/
│   ├── app.py
│   ├── auth.py
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

## 🚀 Deployment on Render
The **Loop Detector App** backend is hosted on [Render](https://render.com/), ensuring easy deployment of the Flask API. It processes **image frames**, detects **loops**, and returns results in real-time.

### 🔧 Steps:
1. **Push code to GitHub**
2. Set up a **Render service** for the backend
3. Configure **environment variables** (API keys, authentication tokens)
4. Deploy and monitor in Render’s dashboard

## ⏳ AWS Lambda + EventBridge Integration (Keep Server Awake)
To prevent the Render service from **spinning down due to inactivity**, we use **AWS Lambda** + **Amazon EventBridge**.

### 🔹 Lambda Setup:
1. **Create a Lambda function** in AWS
2. **Write a Python script** to send periodic requests:

```python
import requests

def lambda_handler(event, context):
    url = "https://loop-detector-app-1.onrender.com/"
    try:
        response = requests.get(url)
        return {"status": response.status_code, "message": "Ping successful"}
    except Exception as e:
        return {"error": str(e)}
```

3. **Schedule execution using EventBridge** (every 15 minutes):
   - Navigate to **Amazon EventBridge**
   - Click **“Create Rule”** → Name it `keep-render-awake`
   - Set **schedule type** to **fixed rate** (e.g., `rate(15 minutes)`)
   - Choose **AWS Lambda** as the target
   - Save and enable the rule

### 💡 Benefits:
✅ Keeps the **Render app active** without manual intervention  
✅ Uses **free-tier AWS Lambda**, minimizing costs  
✅ Ensures **smooth user experience** without unexpected downtime

---

### 🖥️ Frontend (HTML + JavaScript)

#### Option 1: Open Directly
```bash
start frontend/index.html
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
- 🔒 For demonstration only — **not secure for production**

---

## 📄 License
This software is **proprietary**.

Unauthorized use, reproduction, or redistribution is **prohibited** without written permission from the author.

© 2025 **Aimee L. Ramirez**. Developer identity: [@aimeelramirez](https://github.com/aimeelramirez). All rights reserved.
