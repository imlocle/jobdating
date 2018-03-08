from flask import Flask, url_for, render_template, jsonify, request, redirect, session
from flask_pymongo import PyMongo
import pandas as pd
import tweepy

# Twitter API Keys
consumer_key = "7uE7u3kJmZNSMk73PAUEDQOVI"
consumer_secret = "6pO6Q7RyFa8ahec7cTkyoM8j2clXAhdvX3zzOIZ6JOkY7BrQLI"
access_token = "29085215-jxXOHQEszQXY6J36EfMH47uu2So0sCLHk5N3xI9ud"
access_token_secret = "qFmWyNCGbcyhyOUPzdQ8NqB1HP6Lys9WEDOhe0nUNCQHs"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

app = Flask(__name__)
#session secret key
app.secret_key = 'LA Hackathon!'
mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        twitter_dataframe(username['twitter'])
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

tweet_data = {
    "tweet_source": [],
    "tweet_text": [],
    "tweet_date": [],
}

def twitter_dataframe(username):
    tweet_data = {
    "tweet_source": [],
    "tweet_text": [],
    "tweet_date": [],
    "tweet_vader_score": [],
    "tweet_neg_score": [],
    "tweet_pos_score": [],
    "tweet_neu_score": []}
    for x in range(5):
        tweets = api.user_timeline(username, page=x)
        for tweet in tweets:
            # All data is grabbed from the JSON returned by Twitter
            tweet_data["tweet_source"].append(tweet["user"]["name"])
            tweet_data["tweet_text"].append(tweet["text"])
            tweet_data["tweet_date"].append(tweet["created_at"])

            # Run sentiment analysis on each tweet using Vader
            tweet_data["tweet_vader_score"].append(analyzer.polarity_scores(tweet["text"])["compound"])
            tweet_data["tweet_pos_score"].append(analyzer.polarity_scores(tweet["text"])["pos"])
            tweet_data["tweet_neu_score"].append(analyzer.polarity_scores(tweet["text"])["neu"])
            tweet_data["tweet_neg_score"].append(analyzer.polarity_scores(tweet["text"])["neg"])
            emptylist.append(analyzer.polarity_scores(tweet["text"]))

    # Pandas dataframe
    tweet_df = pd.DataFrame(tweet_data, columns=["tweet_source", 
                                             "tweet_text", 
                                             "tweet_date",
                                             "tweet_vader_score",
                                             "tweet_pos_score",
                                             "tweet_neu_score",
                                             "tweet_neg_score"])





if __name__ == "__main__":
    app.run(debug=True)