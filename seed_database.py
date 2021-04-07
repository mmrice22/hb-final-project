""" Script to seed database"""

import os
import json
from random import choice, randint

import model

os.system('dropdb parks')
os.system('createdb parks')

model.connect_to_db(server.app)
model.db.create_all()

# load MI park data from miparks.json file
with open('data/miparks.json') as f:
    park_data = json.loads(f.read())


# create parks, store them in a list
parks_in_db = []
for park in park_data:
    name, description, state = (park['fullName'],
                                park['description'],
                                park['states']),

    db_park = crud.create_park(fullName,
                                description,
                                states)
    parks_in_db.append(db_park)

# create 10 users

