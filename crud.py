"""CRUD operations"""

from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db


def create_user(fname, lname, email):
    """Create and return a new user"""

    user = User(fname = fname, lname = lname, email = email)

    db.session.add(user)
    db.session.commit()

    return user









if __name__ == '__main__':
    from server import app
    connect_to_db(app)