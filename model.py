"""Models for National Park App"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """User of the app"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    fname = db.Column(db.String(50), nullable = False)
    lname = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String)

    # has a relationship with Favorite table

    
    # repr is used to give me info back in a readable way
    def __repr__(self):
        return f'<User user_id = {self.user_id} fname = {self.fname} email = {self.email}>'


class NationalPark(db.Model):
    """National Park info"""

    __tablename__ = 'nat_parks'

    park_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    state = db.Column(db.String(2))

    # has a relationship with Favorite table

    activities = db.relationship('Activity',
                                secondary = 'park_activities',
                                backref = 'parks')


    def __repr__(self):
        return f'<NationalPark park_id = {self.park_id} name = {self.name} state = {self.state}>'


class Favorite(db.Model):
    """Favorited Parks"""

    __tablename__ = 'favorites'

    favorite_id = db.Column(db.Integer,
                            autoincrement = True,
                            primary_key = True)
    has_been = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    park_id = db.Column(db.Integer, db.ForeignKey('nat_parks.park_id'))
    

    user = db.relationship('User', backref = 'favorites')
    park = db.relationship('NationalPark', backref = 'favorites')



    def __repr__(self):
        return f'<Favorite favorite_id = {self.favorite_id} has_been = {self.has_been}>'



class ParkActivity(db.Model):
    """Connecting the National Park table and Activity Table"""

    __tablename__ = 'park_activities'

    park_activity_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True) 
    park_id = db.Column(db.Integer,
                        db.ForeignKey('nat_parks.park_id'),
                        nullable = False)
    activity_id = db.Column(db.Integer,
                            db.ForeignKey('activities.activity_id'),
                            nullable = False)

    # has relationship with NationalPark Table

    def __repr__(self):
        return f'<ParkActivity park_activity_id = {self.park_activity_id} park_id = {self.park_id}>'




class Activity(db.Model):
    """Activity"""

    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer,
                            primary_key = True,
                            autoincrement = True)
    activity = db.Column(db.String(50), unique = True)

    def __repr__(self):
        return f'<Activity activity_id = {self.activity_id} activity = {self.activity}>'







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

