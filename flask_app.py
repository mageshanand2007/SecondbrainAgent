from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "SecondBrainAgent Backend is Live!"

@app.route("/api/tasks")
def tasks():
    with open("tasks.json", "r") as f:
        return jsonify(json.load(f))

@app.route("/api/analysis")
def analysis():
    with open("analysis.txt", "r", encoding="utf-8") as f:
        return jsonify({"analysis": f.read()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)