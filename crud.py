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


def get_user_faves(user_id):
    """Show all the users favorited parks"""

    user_faves = Favorite.query.options(db.joinedload('park')).filter(Favorite.user_id == user_id).all()

    return user_faves



def get_fav_by_id(user_id,park_id):
    """Get favorite by user_id and park_id"""

    return Favorite.query.filter(Favorite.park_id == park_id).filter(Favorite.user_id == user_id).first()
        



    




if __name__ == '__main__':
    from server import app
    connect_to_db(app)