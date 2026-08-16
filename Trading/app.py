"""
Trading Journal 2026 - Local Web Server

A simple Flask server to serve the trading journal app.
You can also just open templates/index.html directly in your browser.
"""
import os
from flask import Flask, send_from_directory

app = Flask(__name__)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(DATA_DIR, "templates")


@app.route("/")
def index():
    return send_from_directory(TEMPLATES_DIR, "index.html")


if __name__ == "__main__":
    print("Trading Journal running at http://localhost:5000")
    print("Or open templates/index.html directly in your browser.")
    app.run(debug=True, port=5000)
