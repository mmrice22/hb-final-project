"""CRUD operations"""

from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db
import server
from flask import request

import os
import requests

api_key = os.environ['NPS_KEY']



#------------------User functions----------------#


def create_user(fname, lname, email, password):
    """Create and return a new user"""

    user = User(fname = fname, lname = lname, email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by their email"""

    return User.query.filter(User.email == email).first()




#------------------National Park functions----------------#


def get_parks():
    """Return all Parks"""

    url = 'https://developer.nps.gov/api/v1/parks'

    stateCode = request.args.get('state', '')
    payload = {'api_key': api_key, 'stateCode': stateCode}
    res = requests.get(url, params=payload)

    data = res.json()
    parks = data['data']

    return parks



def add_park(name, state, description, park_id):
    """Add park to the National Park table"""

    park = NationalPark.query.filter(NationalPark.name == name).first()
    
    if park is None:
        park = NationalPark(name = name,
                        state = state,
                        description = description,
                        park_id = park_id)

        db.session.add(park)
        db.session.commit()

    return park


def get_park_by_id(park_id):
    """Get a park by their id from the National Park table"""

    return NationalPark.query.get(park_id)


def get_park_from_api(parkCode):

    url = 'https://developer.nps.gov/api/v1/parks'


    payload = {'api_key': api_key, 'parkCode': parkCode}
    res = requests.get(url, params=payload)

    return res.json()



#------------------Favorite functions----------------#


def create_favorite_by_id(user_id, park_id):
    """Create and add new favorite to Favorite table"""


    favorite = Favorite.query.filter((Favorite.park_id == park_id) & (Favorite.user_id == user_id)).first()


    if favorite is None:
        favorite = Favorite(user_id= user_id, 
                            park_id = park_id)
        db.session.add(favorite)
        db.session.commit()

    return favorite



def get_favorites_by_park_id(parkCode):
    """Get a favorite using user_id and park_id"""
    
    park = get_park_from_api(parkCode)

    get_favorites_by_id = park['data'][0]['parkCode']


    return get_favorites_by_id



def get_favorites_by_park_name(parkCode):
    """Get a favorite using user_id and park_id"""
    
    park = get_park_from_api(parkCode)

    get_favorites_by_park_name = park['data'][0]['fullName']


    return get_favorites_by_park_name



def get_favorites_by_description(parkCode):
    """Get a favorite using user_id and park_id"""
    
    park = get_park_from_api(parkCode)

    get_favorites_by_description = park['data'][0]['description']


    return get_favorites_by_description



def get_favorites_by_directions(parkCode):
    """Get a favorite using user_id and park_id"""
    
    park = get_park_from_api(parkCode)

    get_favorites_by_directions = park['data'][0]['directionsInfo']


    return get_favorites_by_directions



def get_favorites_by_state(parkCode):
    """Get a favorite using user_id and park_id"""
    
    park = get_park_from_api(parkCode)

    get_favorites_by_state = park['data'][0]['addresses'][0]['stateCode']


    return get_favorites_by_state












if __name__ == '__main__':
    from server import app
    connect_to_db(app)