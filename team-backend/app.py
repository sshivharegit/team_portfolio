from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Supabase config
SUPABASE_URL = "https://fsuvfsijghtaeymuaexa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZzdXZmc2lqZ2h0YWV5bXVhZXhhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMyODU5NzQsImV4cCI6MjA2ODg2MTk3NH0.8FlpnTTn1AWkq6fiQ4i-M2g8bS3ntXueD9xMM6gczoU"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

# GET all team members
@app.route("/api/team", methods=["GET"])
def get_team():
    res = requests.get(f"{SUPABASE_URL}/rest/v1/team_members?select=*", headers=HEADERS)
    return jsonify(res.json())

# POST new team member
@app.route("/api/team", methods=["POST"])
def add_team_member():
    data = request.get_json()
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/team_members",
        headers={**HEADERS, "Content-Type": "application/json"},
        json=data
    )
    return jsonify(res.json())

# DELETE a team member
@app.route("/api/team/<id>", methods=["DELETE"])
def delete_member(id):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/team_members?id=eq.{id}",
        headers=HEADERS
    )
    return jsonify({"status": "deleted" if res.status_code == 204 else "error"})

# ✅ Flask entry point for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT env variable
    app.run(host="0.0.0.0", port=port)
