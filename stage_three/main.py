"""
This module defines what will happen in stage_3.
"""
from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/api/v1/evaluate", methods=["GET", "POST"])
def evaluate():
    return make_response(jsonify({"value": 3.1415926535}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
