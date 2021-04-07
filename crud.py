"""CRUD operations"""

from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db


def create_user(fname, lname, email):
    """Create and return a new user"""

    user = User(fname = fname, lname = lname, email = email)

    db.session.add(user)
    db.session.commit()

    return user


def create_park(name, description, state):
    """Create and return a new park"""

    park = NationalPark(name = fullName,
                        description = description,
                        state = states)

    db.session.add(park)
    db.session.commit()

    return park









if __name__ == '__main__':
    from server import app
    connect_to_db(app)