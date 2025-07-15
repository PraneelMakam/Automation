from flask import Flask, render_template, jsonify
import os
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    logs = []
    log_dir = "../logs"
    # If logs directory is missing or empty, run tests to generate logs
    if not os.path.exists(log_dir) or len(os.listdir(log_dir)) == 0:
        subprocess.run(["python", "run_tests.py", "--output", "logs"])
    # After running tests, proceed to load logs as usual
    if os.path.exists(log_dir):
        for file in sorted(os.listdir(log_dir), reverse=True):
            if file.endswith(".json"):
                with open(os.path.join(log_dir, file)) as f:
                    logs.append({"filename": file, "data": json.load(f)})
    return render_template("index.html", logs=logs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

