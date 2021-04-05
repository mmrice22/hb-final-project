""" Models for National Park App """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User of the app"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String, unique = True)

    
    # repr is used to give me info back in a readable way
    def __repr__(self):
        return f'<User user_id = {self.user_id} fname = {self.fname} email = {self.email}>'


class NationalPark(db.Model):
    """National Park info"""

    __tablename__ = 'parks'

    park_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    state = db.Column(db.String(50))


    def __repr__(self):
        return f'<NationalPark park_id = {self.park_id} name = {self.name} state = {self.state}'






def connect_to_db(flask_app, db_uri='postgresql:///parks', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    # flask is the module Flask is the class
    from flask import Flask
    #creating an instance of Flask Class
    app = Flask(__name__)
    #TO DO consider making test databases by passing in different db uri here
    connect_to_db(app)

