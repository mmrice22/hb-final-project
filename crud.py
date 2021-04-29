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



# def get_favorites_by_park_id(parkCode):
#     """Get a favorite using user_id and park_id"""
    
#     park = get_park_from_api(parkCode)

#     get_favorites_by_id = park['data'][0]['parkCode']


#     return get_favorites_by_id


def get_favorite_by_park_id(park_id):
    """Get a favorite by park_id"""

    return Favorite.query.get(park_id)
    


def get_favorite_by_id(favorite_id):
    """Get a favorite by its id"""

    return Favorite.query.get(favorite_id)


def get_user_id(user_id):
    """Get a user in the Favorites table by their user_id"""

    return Favorite.query.get(user_id)



def change_has_been_to_true(user_id, favorite_id):
    """Change visited park to true when button is clicked"""


    favorited = Favorite.query.filter((Favorite.favorite_id == favorite_id) & (Favorite.favorite.user_id == user_id)).first()
    favorited.has_been = True
    #db.session.commit()

    # favorite_id = Favorite.query.get()


    # if favorite_id:
    #     has_been = Favorite(has_been = True)
    #     db.session.add(has_been)
    #     db.session.commit()

    return has_been

        



    




if __name__ == '__main__':
    from server import app
    connect_to_db(app)