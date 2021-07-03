import unittest

#from main import app
from src.util.constants import logger
from main import app

class MarginalTax2020Tests(unittest.TestCase):
    def setUp(self):
        # executed prior to each test
        self.app = app.test_client()
    
    def tearDown(self):
        # executed after each test
        pass

    # Test each brackets min, median, max
    # Bracket 1 : [0, 20000, 48535]
    # Bracket 2 : [48534, 60000, 97069]
    # Bracket 3 : [97070, 120000, 150473]
    # Bracket 4 : [150474, 180000, 214368]
    # Bracket 5 : [214369+]


    ## BRACKET 1 ##
    def test_bracket_1_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 0
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_1_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 48535
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_1_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 20000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)



    ## BRACKET 2 ##
    def test_bracket_2_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 48534
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_2_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 60000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_2_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 97069
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)



    ## BRACKET 3 ##
    def test_bracket_3_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 97070
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_3_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 120000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_3_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 150473
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)


    ## BRACKET 4 ##
    def test_bracket_4_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 150474
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_4_max_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 180000
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
    
    def test_bracket_4_med_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 214368
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)


    ## BRACKET 5 ##
    def test_bracket_5_min_amount(self):
        # This actually discovered an error while processing a zero value
        request_data = {
            "year" : 2020,
            "annual income": 214400
        }

        response = self.app.get('/calculate/incometax', query_string=request_data)
        self.assertEqual(response.status_code, 200)
