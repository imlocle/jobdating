from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    