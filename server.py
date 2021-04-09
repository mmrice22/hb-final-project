from flask import Flask, render_template, request, flash, session, redirect
from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db
from pprint import pformat
import crud

import os
import requests 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'SECRETKEYSECRETKEYSECRETKEY'
app.jinja_env.undefined = StrictUndefined


api_key = os.environ['NPS_KEY']


@app.route('/')
def homepage():
    """Show homepage"""

    return render_template('homepage.html')

@app.route('/findparks')
def show_parks_form():
    """Show park search form"""

    return render_template('search-form.html')

@app.route('/parks/search')
def find_parks():
    """Search for National Parks from NPS API"""

    stateCode = request.args.get('stateCode', '')
    fullName = request.args.get('fullName', '')
    description = request.args.get('description', '')
    states = request.args.get('states', '')

    url = 'https://developer.nps.gov/api/v1/parks'
    payload = {'api_key': api_key, 
                'stateCode': stateCode,
                'fullName': fullName,
                'description': description,
                'states': states}

    response = requests.get(url, params = payload)

    data = response.json()
    parks = data['data']

    return render_template('search-results.html',
                            pformat = pformat,
                            data = data,
                            results = parks)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)