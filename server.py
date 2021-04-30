from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import db, User, NationalPark, Favorite, ParkActivity, Activity, connect_to_db
from pprint import pformat
import crud

import os
import requests 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'SECRETKEYSECRETKEYSECRETKEY'
app.jinja_env.undefined = StrictUndefined


api_key = os.environ['NPS_KEY']


@app.route('/')
def homepage():
    """Show homepage"""

    return render_template('homepage.html')


@app.route('/', methods = ['POST'])
def register_user():
    """Create a new user and add to database"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user_email = crud.get_user_by_email(email)
    
    # check to see if email submitted is already in the db
    if user_email:
        flash("Email is associated with an account. Please Login.")
    else:
        #if email is not in db, create the user with submitted info
        crud.create_user(fname,lname,email,password)
        flash('Account created! Please Login.')
    
    return redirect('/')



@app.route('/login', methods = ['GET', 'POST'])
def login():
    """Show Login Form"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if request.method == 'POST':
        # if the password in db matched submitted password
        if user.password == password:
            # then save in the session the users id
            session["user_id"] = user.user_id
            return redirect("/findparks")
        else:
            flash("Wrong password, please try again")
            return redirect('/login')
    else:
        # if there is a user already in the session, redirect to findparks route
        if "user_id" in session:
            return redirect("/findparks")
        
        # if there isn't a user in session, show login 
        return render_template("login.html")





@app.route('/findparks', methods = ['GET','POST'])
def show_parks_form():
    """Show park search form"""


    if "user_id" in session:
        # get the user object by their id and store the user object in the variable user
        user = User.query.get(session['user_id'])
        # now I can say user.fname, user.lname, user.email in the jinja template
        return render_template('search-form.html', user = user)
    
    else:
        # if user is not in session, direct them to login
        # a user can't go to parks form if they are not logged in
        return redirect('/login')

        


@app.route('/parks/search')
def find_parks():
    """Search for National Parks from NPS API"""

    parks = crud.get_parks()

    return render_template('search-results.html',
                            pformat = pformat,
                            parks = parks,)


@app.route('/makefavorite.json')
def make_favorite():

    parkCode = request.args.get('parkCode', '')

    api_park = crud.get_park_from_api(parkCode)
    api_park_name = api_park['data'][0]['fullName']
    api_park_description = api_park['data'][0]['description']
    api_park_state = api_park['data'][0]['addresses'][0]['stateCode']
    api_park_code = api_park['data'][0]['parkCode']

    add_park_db = crud.add_park(name = api_park_name, state = api_park_state, description = api_park_description, park_id = api_park_code)
    

    if "user_id" in session:
        user_id = session["user_id"]


    add_favorite_db = crud.create_favorite_by_id(user_id = user_id, park_id = api_park_code)

    
    return jsonify(api_park['data'][0]['fullName']) 



@app.route('/favorites', methods = ['GET','POST'])
def show_favorites():
    """Show favorited parks"""

    # first need to get a user by their id
    if "user_id" in session:
        user_id = session["user_id"]
    
    #this works --- trying to move all querys to crud.py
    # user_faves = Favorite.query.options(db.joinedload('park')).filter(Favorite.user_id == user_id).all()
    #print(user_faves)

    user_faves = crud.get_user_faves(user_id)

    return render_template('favorites.html', user_faves = user_faves)




@app.route('/visited.json', methods = ['POST'])
def change_visited():
    """Change has_been to true when button is clicked"""
    
    
    if "user_id" in session:
        user_id = session["user_id"]
        print(user_id)


    park_id = request.form["parkCode"]
    print(park_id)

    fav_obj = crud.get_fav_by_id(user_id, park_id)
    print(fav_obj)


    fav_obj.has_been = True
    print(fav_obj.has_been)
    db.session.commit()



    return jsonify(park_id)





@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You've successfully logged out")
    return redirect('/')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)