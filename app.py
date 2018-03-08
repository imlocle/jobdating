from flask import Flask, url_for, render_template, jsonify, request, redirect, session
import pymongo
from companylist import *
import scrape_twitter
import datamining

app = Flask(__name__)
#session secret key
app.secret_key = 'LA Hackathon!'

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

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

@app.route('/companydataentry')
def company():
    return render_template('company_Data_Entry.html')

@app.route('/submit_company_form', methods=['POST'])
def submit_company_form():
    company = request.form
    twitter = request.form['twitter']
    session['company'] = company
    return render_template('show_company_data.html', company=company)

#NEED TO ADD DATA
#CONNECTS WITH D3
@app.route('/companyjson')
def companyjson():
    return jsonify()

if __name__ == "__main__":
    app.run(debug=True)