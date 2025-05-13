from flask import Flask, request, jsonify
from flask_cors import CORS 
from auth import validate_credentials, validate_user, requires_auth_and_whitelist
import numpy as np
import cv2
from detect import process_frame
import os  # needed to read the PORT environment variable

app = Flask(__name__)
CORS(app)  # enable CORS for all routes and origins

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    if not validate_credentials(username, password):
        return jsonify({"msg": "Invalid credentials"}), 401

    return jsonify({"access_token": f"dev-{username}"})

@app.route("/detect", methods=["POST"])
def detect():
    if 'frame' not in request.files:
        print("❌ No frame received")
        return jsonify({"error": "No frame provided"}), 400

    file = request.files['frame']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if frame is None:
        print("❌ Could not decode frame")
        return jsonify({"error": "Failed to decode image"}), 400

    result = process_frame(frame)  # contains both hands + loops
    print(f"✅ Processed frame — hands: {len(result['hands'])}, loops: {result['loops']}")
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render uses PORT env variable
    app.run(host="0.0.0.0", port=port)
