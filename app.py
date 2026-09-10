import os
import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)
APPLICATION_VERSION = "1.1.0"
MODEL_VERSION = "1.1"
DATASET_VERSION = "transactions-v1"

try:
    GIT_COMMIT = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
except:
    GIT_COMMIT = "unknown"

@app.route("/")
def home():
    return jsonify({"service": "mlops-demo", "status": "running"})

@app.route("/health")
def health():
    return jsonify({
        "application_version": APPLICATION_VERSION,
        "model_version": MODEL_VERSION,
        "dataset_version": DATASET_VERSION,
        "git_commit": GIT_COMMIT,
        "status": "healthy"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = float(data["value"])
    return jsonify({
        "input": value,
        "prediction": value * 2,
        "model_version": MODEL_VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
