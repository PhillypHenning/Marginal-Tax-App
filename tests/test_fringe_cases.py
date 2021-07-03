import unittest

#from main import app
from src.util.constants import logger
from main import app

class FringeTests(unittest.TestCase):
    def setUp(self):
        # executed prior to each test
        self.app = app.test_client()
    
    def tearDown(self):
        # executed after each test
        pass

    # Pass in nonesense
    def test_nonsense_in_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 'asdf'
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 409)

    def test_nonsense_in_year(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 'asd',
            "annual income": 1000000000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 409)

    # Pass in date outside accepted range
    def test_outside_range_lower(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2018,
            "annual income": 1000000000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 401)


    def test_outside_range_higher(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2050,
            "annual income": 1000000000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 401)