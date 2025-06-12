
# 🧠 Backend - Loop Detector API (Flask)

This Flask app receives JPEG frames via a **POST endpoint**, detects **hand landmarks** using **MediaPipe**, analyzes the space between hands, and returns the number of detected **"loops"** (e.g., a pink thread between hands).

---

## 🔧 Setup

```bash
# From project root:
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

pip install -r backend/requirements.txt
python backend/app.py
```

## 🧪 API Endpoints

### 🔐 POST `/login`
Authenticates the user and returns a **JWT token**.

**Request Body (JSON):**
```json
{
  "username": "admin",
  "password": "admin"
}
```

### 🖼️ POST `/detect`
Requires **Bearer token authentication**. Accepts an **image file** (`frame`) and returns detected loops.

**Form Data:**
- `frame`: JPEG image

**Response:**
```json
{
  "loops": 3
}
```

## 🚀 Deployment on Render
The **Loop Detector App** is hosted on [Render](https://render.com/), ensuring easy deployment with **Flask**. The backend receives image frames via **POST requests**, applies **computer vision techniques**, and returns loop detection results in real-time.

### 🔧 Deployment Steps:
1. **Push code to GitHub**.
2. Set up a **Render service** for the backend.
3. Configure **environment variables** (e.g., API keys, authentication tokens).
4. Deploy and monitor usage in Render’s dashboard.

## ⏳ AWS Lambda + EventBridge Integration (Keep Server Awake)
To prevent the Render service from **spinning down due to inactivity**, we use **AWS Lambda** + **Amazon EventBridge** to periodically **ping the app**.

### 🔹 Lambda Setup:
1. **Create a Lambda function** in AWS.
2. **Write a lightweight Python script** that sends a request to the Render app:

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
   - Navigate to **Amazon EventBridge**.
   - Click **“Create Rule”** → Name it `keep-render-awake`.
   - Set **schedule type** to **fixed rate** (e.g., `rate(15 minutes)`).
   - Choose **AWS Lambda** as the target.
   - Save and enable the rule.

### 💡 Benefits:
✅ Keeps the **Render app active** without manual intervention.  
✅ Uses **free-tier AWS Lambda**, minimizing costs.  
✅ Ensures **smooth user interactions** without unexpected downtime.

