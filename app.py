from flask import Flask, render_template, jsonify, request, redirect
from flask_pymongo import PyMongo
import tweepy


app = Flask(__name__)
mongo = PyMongo(app)

tweet_data = {
    "tweet_source": [],
    "tweet_text": [],
    "tweet_date": [],
    "tweet_vader_score": [],
    "tweet_neg_score": [],
    "tweet_pos_score": [],
    "tweet_neu_score": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/applicantdataentry')
def applicant():
    return render_template('applicant_Data_Entry.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    user = request.form
    print (user)
    return render_template('index.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)