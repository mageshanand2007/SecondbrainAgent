from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/tasks")
def tasks():
    with open("tasks.json", "r") as f:
        return jsonify(json.load(f))

@app.route("/api/analysis")
def analysis():
    with open("analysis.txt", "r", encoding="utf-8") as f:
        return jsonify({"analysis": f.read()})

if __name__ == "__main__":
    app.run(debug=True)