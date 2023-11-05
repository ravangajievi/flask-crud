import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Ensure that the home page loads correctly
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Greeting Application', response.data)

    # Ensure that the greeting page loads correctly
    def test_greeting_page_loads(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username="John Doe"))
        self.assertIn(b'Hello, John Doe!', response.data)

    # Ensure the greeting page responds correctly given the posted data
    def test_greeting_page_data(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username="John Doe"))
        self.assertTrue(b'Hello, John Doe!' in response.data)

if __name__ == '__main__':
    unittest.main()
