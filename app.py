# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>My first Flask app</h1>"
