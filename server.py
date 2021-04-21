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
    if user_email:
        flash("Email is associated with an account. Please Login.")
    else:
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
        if user.password == password:
            session["user_id"] = user.user_id
            return redirect("/findparks")
        else:
            flash("Wrong password, please try again")
            return redirect('/login')
    else:
        if "user_id" in session:
            return redirect("/findparks")
        return render_template("login.html")





@app.route('/findparks', methods = ['GET','POST'])
def show_parks_form():
    """Show park search form"""


    if "user_id" in session:
        user = User.query.get(session['user_id'])
        return render_template('search-form.html', user = user)
    
    else:
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

    # first need to get a user
    if "user" in session:
        user = session["user"]
    
    #grab the specific liked park when the button in clicked
    

    favorite = crud.create_favorite(user,park)

    return render_template('favorites.html', user = user, park = park)




@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)