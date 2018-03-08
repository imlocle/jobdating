from flask import Flask, url_for, render_template, jsonify, request, redirect, session
from flask_pymongo import PyMongo
from companylist import *
import scrape_twitter
import datamining

app = Flask(__name__)
#session secret key
app.secret_key = 'LA Hackathon!'
mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        twitter = username['twitter']
        #scraping twitter
        scrape_twitter.twitter_dataframe(twitter)
        firstname = username['firstname']
        lastname = username['lastname']
        street = username['street']
        city = username['city']
        state = username['state']
        #User's location
        datamining.userlocation(firstname, lastname, street, city, state)
        print(datamining.companies(companylist, 50))
        print("&&&&&&&&&&&&&&&&")
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