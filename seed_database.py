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


# Make 5 National Parks to populate the nat_parks table

natpark1 = NationalPark(name = 'Isle Royale National Park',
                            description = "Explore a rugged, isolated island, far from the sights and sounds of civilization. Surrounded by Lake Superior, Isle Royale offers unparalleled solitude and adventures for backpackers, hikers, boaters, kayakers, canoeists and scuba divers. Here, amid stunning scenic beauty, you'll find opportunities for reflection and discovery, and make memories that last a lifetime.",
                            state = 'MI')
db.session.add(natpark1)
db.session.commit()


natpark2 = NationalPark(name = 'Keweenaw National Historical Park',
                        description = "From 7,000 years ago to the 1900s people mined Keweenaw copper. Native peoples made copper into tools and trade items. Investors and immigrants arrived in the 1800s in a great mineral rush, developing thriving industries and cosmopolitan communities. Though the mines have since closed, their mark is still visible on the land and people.",
                        state = 'MI')
db.session.add(natpark2)
db.session.commit()


natpark3 = NationalPark(name = 'North Country National Scenic Trail',
                        description = "Come to the North Country. Trek the hills and valleys. Stand on the shores of lakes & streams from glaciers 10,000 years before. Clear-flowing water, red/gold of autumn, a fairyland of snow, open prairies, and distant horizons paint the land. Historic sites along the way tell how America settled and grew as a nation. From North Dakota to Vermont, adventure is never far away.",
                        state = 'MI')
db.session.add(natpark3)
db.session.commit()


natpark4 = NationalPark(name = 'Pictured Rocks National Lakeshore',
                        description = "Sandstone cliffs, beaches, sand dunes, waterfalls, inland lakes, deep forest, and wild shoreline beckon you to visit Pictured Rocks National Lakeshore. The power of Lake Superior shapes the park's coastal features and affects every ecosystem, creating a unique landscape to explore. Hiking, camping, sightseeing, and four-season outdoor opportunities abound.",
                        state = 'MI')
db.session.add(natpark4)
db.session.commit()


natpark5 = NationalPark(name = 'Sleeping Bear Dunes National Lakeshore',
                        description = "Miles of sand beach, bluffs that tower 450’ above Lake Michigan, lush forests, clear inland lakes, unique flora and fauna make up the natural world of Sleeping Bear Dunes. High dunes afford spectacular views across the lake. An island lighthouse, US Life-Saving Service stations, coastal villages, and picturesque farmsteads reflect the park’s rich maritime, agricultural, and recreational history.",
                        state = 'MI')
db.session.add(natpark5)
db.session.commit()