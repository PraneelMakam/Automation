from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    logs = []
    log_dir = "../logs"
    if not os.path.exists(log_dir):
        return "No logs found. Run tests first."
    for file in sorted(os.listdir(log_dir), reverse=True):
        if file.endswith(".json"):
            with open(os.path.join(log_dir, file)) as f:
                logs.append({"filename": file, "data": json.load(f)})
    return render_template("index.html", logs=logs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
