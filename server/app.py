from flask import Flask, request, jsonify
from blockchain_interface import add_audit_record, get_all_records
from utils import verify_token

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_action():
    token = request.headers.get("Authorization")
    if not verify_token(token):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    patient_id = data["patientId"]
    user_id = data["userId"]
    action = data["action"]
    add_audit_record(patient_id, user_id, action)
    return jsonify({"status": "logged"}), 200

@app.route("/records", methods=["GET"])
def get_records():
    return jsonify(get_all_records())

if __name__ == "__main__":
    app.run(debug=True)