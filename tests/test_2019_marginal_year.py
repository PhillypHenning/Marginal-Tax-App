import unittest

#from main import app
from src.util.constants import logger
from main import app

class MarginalTax2019Tests(unittest.TestCase):
    def setUp(self):
        # executed prior to each test
        self.app = app.test_client()
    
    def tearDown(self):
        # executed after each test
        pass

    # Test each brackets min, median, max
    # Bracket 1 : 0-47630 [0, 20000, 47630]
    # Bracket 2 : 47631-95259 [47631, 60000, 95259]
    # Bracket 3 : 95260-147667 [95260, 147667]
    # Bracket 4 : 147668-210371 [147668, 210371]
    # Bracket 5 : 210372+ [1000000000]


    ## BRACKET 1 ##
    def test_bracket_1_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 0
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_1_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 47630
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_1_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 20000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)



    ## BRACKET 2 ##
    def test_bracket_2_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 47631
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_2_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 60000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_2_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 95259
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)



    ## BRACKET 3 ##
    def test_bracket_3_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 95260
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_3_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 120000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_3_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 147667
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)


    ## BRACKET 4 ##
    def test_bracket_4_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 147668
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_4_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 180000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_4_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 210371
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)


    ## BRACKET 5 ##
    def test_bracket_5_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2019,
            "annual income": 1000000000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
