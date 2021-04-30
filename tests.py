import unittest
from server import app
from model import connect_to_db, db
from flask import session


class FlaskTests(unittest.TestCase):
    """Integration testing flask app"""


    def setUp(self):
        """Stuff to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///parks")


    
    def test_homepage_route(self):
        """Test the homepage route of app"""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Welcome to WanderList!", result.data)




    def test_user_registration(self):
        """Test the user registration page, post method"""

        result = self.client.post("/",
                                data={"fname":"Mel", "lname":"Rice", "email":"ricemel1@msu.edu", "password":"test1"},
                                follow_redirects=True)
        self.assertIn(b"Email is associated with an account.", result.data)



class FlaskTestsSession(unittest.TestCase):
    """Test a Flask route that requires a user to be in session"""
    

    def setUp(self):
        """Do before every test"""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'SECRETKEYSECRETKEYSECRETKEY'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1



    def test_parks_form_page(self):
        """Test search form parks page"""

        result = self.client.get("/findparks")
        self.assertIn(b"Welcome back", result.data)


   






if __name__ == "__main__":
    import unittest

    unittest.main()