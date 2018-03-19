import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


import requests
from math import sin, cos, sqrt, atan2
from companylist import *
import datamining

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
GOOGLE_MAPS_API_KEY = 'AIzaSyC219f2IComlGJoXk6zjLOjnY2vXsnmqz8' # ended up not using this

# curtisy of https://gist.github.com/pnavarrc/5379521
def get_company_coordinates(city, state, sensor=False, region='us'):
    
    city_and_state = city + ', ' + state
        
    params = {
        'address': city_and_state,
        'sensor' : sensor,
        'region' : region
    }

    
    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    
    # print(res['results'])
    # print('\n')

    # Use the first result
    result = res['results'][0]
    loc = result['geometry']['location']
    return loc['lat'], loc['lng']

def get_job_seeker_coordinates(address, sensor=False, region='us'):
    
    params = {
        'address': address,
        'sensor' : sensor,
        'region' : region
    }
    
    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    
    # Use the first result
    result = res['results'][0]
    loc = result['geometry']['location']
    return loc['lat'], loc['lng']

def get_commute_distance(company_coordinates, job_seeker_coordinates):
    # curtesy of https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    lat1 = company_coordinates[0]
    lat2 = job_seeker_coordinates[0]

    lon1 = company_coordinates[1]
    lon2 = job_seeker_coordinates[1]

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6373.0 * c
    return distance
    
def get_company_data_frame(company_name):
    company_name = company_name.lower().replace(" ", "-")
    #print(company_name)
    url = 'http://techfair-data.comparably.com/culture/' + company_name + '.json'
    df = pd.read_json(url)
    return df

# convert a letter grade to a score between 0 and 1
def letter_grade_to_score(letter_grade):
    grades = ['A+', 'A', 'A-','B+', 'B', 'B-','C+', 'C', 'C-','D+', 'D', 'D-','F']
    return sorted(list(np.linspace(0,1,len(grades))), reverse=True)[grades.index(letter_grade)]

# input a company culture and output that companies overall culture score
def overall_company_culture(df):

    # b = np.array(map(lambda letter_grade: letter_grade_to_score(letter_grade), df['culture'])).mean()
    # causes Value error, idk why ... so concise :(

    scores = []
    for i in range(len(df['culture'])):
        try: score = letter_grade_to_score(str(df['culture'][i]['grade']))
        except: continue
        scores.append(score)

    return float(np.array(scores).mean())


def scaling(job_seeker_culture):

	# generate uniform list of sentiment examples to scale data
	scaling_sample = []

	for i in range(100):
	    scaling_sample.append(np.random.uniform(-1, 2))

	# scale the data to 0 - 1
	scale = (job_seeker_culture - min(scaling_sample))/(max(scaling_sample)-min(scaling_sample))
	# scale = (job_seeker_culture - (-1)) / (1 - (-1))
	return scale


# this returns 
def lukes_function(firstname, lastname, street, city, state, job_seeker_culture):

	samples = []
	company_names = []
	lat_lons = []
	distances_away = []
	for company_name in datamining.companies(companylist, 25):

		try:
			df = get_company_data_frame(company_name)
			city = str(df['company']['location']['city'])
			state = str(df['company']['location']['state'])
			cc = get_company_coordinates(city, state)
	
			job_seeker_address = str(street) + ', ' + str(city) + ', ' + str(state)
			jsc = get_job_seeker_coordinates(job_seeker_address)

			commute_distance = get_commute_distance(cc, jsc) # in kilometer

			# get company and job seeker culture ratings (float between 0 and 1)
			company_culture = overall_company_culture(df)
			job_seeker_culture = scaling(job_seeker_culture)

			samples.append([company_culture, 0, 0])
			company_names.append(company_name)
			lat_lons.append([cc[0], cc[1]])
			distances_away.append(commute_distance)

		except:
			continue

	# training
	k = 3
	search_radius = 0.4
	neigh = NearestNeighbors(k, search_radius)
	samples2 = np.array(samples)
	neigh.fit(samples2)

	# prediction
	if len(samples2) > k:
		prediction = neigh.kneighbors([[job_seeker_culture, 0, 0]], k, return_distance=True)

	else:
		prediction = [[], [[]]]
		for i in range(k):
			prediction[1][0].append(i)
		prediction = np.array(prediction)

	recommendation = []
	for i in range(k):
		try:
			#creating a json file
			pred = {}
			test = {}
			index = prediction[1][0][i]
			test["company"] = company_names[index]
			test["lat_lon"] = lat_lons[index]
			test["distance_away"] = distances_away[index]
			pred["recommend"] = test
			recommendation.append(test)
		except:
			pass

	return recommendation
