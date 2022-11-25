import unittest
import requests


def suma(a, b):
    return a+b


class BasicTest(unittest.TestCase):

    def test1(self):
        c = suma(5, 10)
        self.assertEqual(c, 15)

    def index(self):
        URl = 'https://servicio-stock.onrender.com/vehiculos'
        res = requests.get(self.URL)
        self.assertEqual(res.status_code, 200)


if __name__ == '_main_':
    unittest.main()
