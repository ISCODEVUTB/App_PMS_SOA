import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = "https://servicio-stock.onrender.com/"
    URL = "{}/vehicles".format(API_URL)

    def test_1_get_all_vehicles(self):
        r = requests.get(ApiTest.URL)
        self.assertEqual(r.status_code, 200)

