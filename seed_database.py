""" Script to seed database"""

import os
import json
from random import choice, randint

from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db
import crud
import server

os.system('dropdb parks')
os.system('createdb parks')

connect_to_db(server.app)
db.create_all()
    
# Make 5 Users to populate tables
user1 = User(fname = 'Mel', lname = 'Rice', 
            email = 'ricemel1@msu.edu', password = 'test1')
db.session.add(user1)
db.session.commit()

user2 = User(fname = 'Jess', lname = 'Rice', 
            email = 'ricejes1@msu.edu', password = 'test2')
db.session.add(user2)
db.session.commit()

user3 = User(fname = 'Bailey', lname = 'Rice', 
            email = 'ricebail1@msu.edu', password = 'test3')
db.session.add(user3)
db.session.commit()

user4 = User(fname = 'Glenda', lname = 'Rice', 
            email = 'gfrice@icloud.com', password = 'test4')
db.session.add(user4)
db.session.commit()

user5 = User(fname = 'Walter', lname = 'Rice', 
            email = 'wjrice@um.edu', password = 'test5')
db.session.add(user5)
db.session.commit()