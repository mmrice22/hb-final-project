RUNNING PROJECT (do this everytime open project)
activate environment -> source env/bin/activate
access API key (will raise KeyError if skipped) -> source secrets.sh

to create the db: in terminal run -> createdb parks

now can run python3 -i model.py to connect to the db

once connected to interacive python to create tables run -> db.create_all()

to get out of python -i database run -> quit()

to get into newly created tables/db, in terminal run -> psql parks

\dt shows the schema

\d parks shows the table

to drop the db: in terminal run -> dropdb parks

create seed file like one from Movie ratings app

TESTING SEED FILE in -i seed.py ---> >>> fav1 = Favorite.query.first() --> gives back first favorite
now fav1 should have access to users and parks >>> fav1.user --> gives me the user id, fname and email back >>> fav1.park --> gives me park id, name and state

TESTING CRUD FILE
test that create_user works by running python3 -i crud.py
call function and pass in a fake info

> > > create_user(fname='eli',lname='lowry',email='elinash@um.edu',password='testpw1')

    response --> <User user_id = 6 fname = eli email = elinash@um.edu>

    * query for it and check that it is actually there
    >>> all_users = User.query.all()
    >>> all_users
        response --> all users including the one just created
        are there

    >>> create_favorite(user='Mel',park='Isle Royale National Park')

    response --> ERROR 'str' object has no attribute '_sa_instance_state'

To use the CREATE_FAVORITE function, we need to grab a user object and a park object. So we need to create a variable and save the users info to that variable --->

    >>> first_user = User.query.get(1)
    *We have grabbed the first user by their id (thats what .get does)*
    >>> first_user--> <User user_id = 1 fname = Mel email = ricemel1@msu.edu>

    do the same exact thing for a park
    >>> first_park = NationalPark.query.get(1)
    >>> first_park --> <NationalPark park_id = 1 name = Isle Royale National Park state = MI>

    **Now we have a user instance/object and a park instance/object to use as an argument for our create_favorite function**

    >>> third_fave = create_favorite(first_user,first_park)
    ---> <Favorite favorite_id = 3 has_been = False>

    ** now I can use dot notation to access info about the specific user and the park that this fave references**

    >>> third_fave.user
    --> <User user_id = 1 fname = Mel email = ricemel1@msu.edu>

    >>> third_fave.user.fname
    --> 'Mel'

    >>> third_fave.user.email
    --> 'ricemel1@msu.edu'

    >>> third_fave.park.name
    --> 'Isle Royale National Park'

    >>> third_fave.park.description
    --> "Explore a rugged, isolated island,......"


                NPS API stuff

to see info from the API in the terminal run these commands interactively from model.py:

> > > import requests
> > > url = 'https://developer.nps.gov/api/v1/parks'
> > > payload = {'api_key': 'YOUR_API_KEY'}
> > > payload['stateCode'] = 'MI'
> > > payload

    response -> {'api_key': 'YOUR_API_KEY', 'stateCode': 'MI'}

> > > res = requests.get(url, params=payload)
> > > data = res.json()
> > > data

        response -> all the parks in Michigan

> > > park = data['data'][0] (data is a key whose value is a list of dictionaries)
> > > park

    response -> the first park [0] from the specific stateCode param (in this case, MI)

> > > park['description'] ('description' is a key)

    response -> description of the park

> > > park['activities'] ('activities' is a key)

    response -> a list of activity dictionaries

> > > park['fullName'] ('fullName' is a key)

    response -> name of the park

> > > park['images'][0] ('images' is a key)

    response -> a dictionary of the first image [0] info: gives back a credit, title,url among other things

    IN search-results.html file to get parks

      <p>{{parks[-1]['fullName']}}</p> --> Sleeping Bear Dunes
      <p>{{parks[-1]['description']}}</p> -> parks description
