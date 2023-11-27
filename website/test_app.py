import unittest
from flask import Flask
import os

# Assuming your Flask app is named 'app.py' and your main Flask application is named 'app'
from app import fridge, get_db

class FlaskFridgeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(fridge)
        self.client = self.app.test_client()
    
    # Test for Login Page
    def test_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Test for Main Page
    def test_index_page(self):
        response = self.client.get('/fridge')
        self.assertEqual(response.status_code, 200)

    # Test for Recipes Page
    def test_recipes_page(self):
        response = self.client.get('/recipes')
        self.assertEqual(response.status_code, 200)
    

    # More tests for other routes and database interactions can be added here

if __name__ == '__main__':
    unittest.main()
