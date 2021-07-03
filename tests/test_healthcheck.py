import unittest

#from main import app
from src.util.constants import logger
from main import app

class HealthTests(unittest.TestCase):
    def setUp(self):
        # executed prior to each test
        self.app = app.test_client()
    
    def tearDown(self):
        # executed after each test
        pass

    def test_healthcheck(self):
        response = self.app.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
