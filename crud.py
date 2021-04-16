"""CRUD operations"""

from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db
import server
from flask import request

import os
import requests

api_key = os.environ['NPS_KEY']




def create_user(fname, lname, email, password):
    """Create and return a new user"""

    user = User(fname = fname, lname = lname, email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by their email"""

    return User.query.filter(User.email == email).first()


def create_park(name, description, state):
    """Create and return a new park"""

    park = NationalPark(name = name,
                        description = description,
                        state = state)

    db.session.add(park)
    db.session.commit()

    return park


def get_parks():
    """Return all Parks"""

    url = 'https://developer.nps.gov/api/v1/parks'

    stateCode = request.args.get('state', '')
    payload = {'api_key': api_key, 'stateCode': stateCode}
    res = requests.get(url, params=payload)

    data = res.json()
    parks = data

    return parks


def create_favorite(user, park):
    """Create and return a new favorite"""

    favorite = Favorite(user= user, park = park)

    db.session.add(favorite)
    db.session.commit()

    return favorite









if __name__ == '__main__':
    from server import app
    connect_to_db(app)