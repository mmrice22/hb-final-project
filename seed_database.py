""" Script to seed database"""

import os
import json
import random import choice, randint

import model

os.system('dropdb parks')
os.system('createdb parks')

model.connect_to_db(server.app)
model.db.create_all()



