from flask import Flask, render_template, request, flash, session, redirect
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




@app.route('/favorites')
def show_favorites():
    """Show favorited parks"""

    # first need to get a user by their id
    if "user_id" in session:
        user_id = session["user_id"]
    
    #grab the specific liked park when the button in clicked
    

    favorite = crud.create_favorite(user_id,park_id)

    return render_template('favorites.html', user_id = user_id, park_id = park_id)




@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)