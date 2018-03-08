from flask import Flask, url_for, render_template, jsonify, request, redirect, session
from flask_pymongo import PyMongo
import tweepy


app = Flask(__name__)
app.secret_key = 'LA Hackathon!'
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
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return render_template('index.html')

@app.route('/applicantdataentry')
def applicant():
    return render_template('applicant_Data_Entry.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    user = request.form
    session['username'] = user
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)