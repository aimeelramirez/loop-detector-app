# 🧠 Backend - Loop Detector API (Flask)

This Flask app receives JPEG frames via a POST endpoint, detects hand landmarks using MediaPipe, analyzes the space between hands, and returns the number of detected "loops" (e.g., pink thread between hands).

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

## 🧪 Endpoints

### POST `/login`
Authenticate and return a JWT.

**Body (JSON):**
```json
{
  "username": "admin",
  "password": "admin"
}
```

### POST `/detect`
Requires Bearer token. Accepts an image file (`frame`) and returns detected loops.

**Form Data:**
- `frame`: JPEG image

**Response:**
```json
{
  "loops": 3
}
```

## 🚀 Deploy to Heroku
```bash
heroku login
heroku create loop-detector-api
git init
git add .
git commit -m "deploy"
heroku git:remote -a loop-detector-api
git push heroku master
```
