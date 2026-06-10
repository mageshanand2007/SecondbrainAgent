from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/api/tasks")
def get_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    return jsonify(tasks)

@app.route("/api/analysis")
def get_analysis():
    with open("analysis.txt", "r", encoding="utf-8") as f:
        analysis = f.read()

    return jsonify({"analysis": analysis})

if __name__ == "__main__":
    app.run(debug=True)