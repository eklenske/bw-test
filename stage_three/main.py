"""
This module defines what will happen in stage_3.
"""
from flask import Flask, jsonify, make_response
import pandas as pd

app = Flask(__name__)


@app.route("/api/v1/evaluate", methods=["GET", "POST"])
def evaluate():
    getLogs()
    return make_response(jsonify({"value": 3.1415926535}))

def getLogs():
    df = pd.load_csv('data/logs.csv')
    print(df)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
