import os
from functools import wraps
from flask import request, jsonify

USERS = {
    "admin": "admin",
    "test": "test123"
}

def validate_credentials(username, password):
    return USERS.get(username) == password

def validate_user(username):
    return username in USERS

IS_DEV = os.getenv("FLASK_ENV") != "production"

def requires_auth_and_whitelist(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if IS_DEV:
            data = request.get_json(silent=True) or {}
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return jsonify({"msg": "Missing dev credentials"}), 400

            if not validate_credentials(username, password):
                return jsonify({"msg": "Dev credentials invalid"}), 403

            return f(*args, **kwargs)

        auth = request.headers.get("Authorization", None)
        if not auth:
            return jsonify({"msg": "Missing Authorization Header"}), 401

        return jsonify({"msg": "Token validation not implemented. Use dev mode or add real auth."}), 501

    return decorated
