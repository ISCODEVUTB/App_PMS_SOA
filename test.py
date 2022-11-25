import unittest
import requests


def suma(a, b):
    return a+b


class BasicTest(unittest.TestCase):

    def test1(self):
        c = suma(5, 10)
        self.assertEqual(c, 15)

    def app_prueba(self):
        URL = 'https://servicio-stock.onrender.com/vehiculo'
        r = requests.get(URL)
        self.assertEqual(r.status_code, 200)


if __name__ == '_main_':
    unittest.main()
