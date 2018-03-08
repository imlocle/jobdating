from flask import Flask, url_for, render_template, jsonify, request, redirect, session
from flask_pymongo import PyMongo
import scrape_twitter

app = Flask(__name__)
#session secret key
app.secret_key = 'LA Hackathon!'
mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        scrape_twitter.twitter_dataframe(username['twitter'])
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