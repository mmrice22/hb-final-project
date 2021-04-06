to create the db: in terminal run -> createdb parks

now can run python3 -i model.py to connect to the db

once connected to interacive python to create tables run -> db.create_all()

to get out of python -i database run -> quit()

to get into newly created tables/db, in terminal run -> psql parks

\dt shows the schema

\d parks shows the table

to drop the db: in terminal run -> dropdb parks

create seed file like one from Movie ratings app

                NPS API:

to see info from the API in the terminal run these commands:

> > > import requests
> > > url = 'https://developer.nps.gov/api/v1/parks'
> > > payload = {'api_key': 'YOUR_API_KEY'}
> > > payload['stateCode'] = 'MI'
> > > payload

    response -> {'api_key': 'YOUR_API_KEY', 'stateCode': 'MI'}

> > > res = requests.get(url, params=payload)
> > > data = res.json()
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
