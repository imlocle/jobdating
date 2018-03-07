import tweepy
import json
import pandas as pd
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import matplotlib.pyplot as plt


app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/login", methods=["POST"])
def register():
   return render_template("/")



if __name__ == "__main__":
    app.run(debug=True)