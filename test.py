import unittest
from app import app


def suma(a, b):
    return a+b


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test1(self):
        c = suma(5, 10)
        self.assertEqual(c, 15)

    def app_prueba(self):
        r = self.app.get('https://servicio-stock.onrender.com/vehiculo', follow_redirects=True)
        self.assertEqual(r.status_code, 200)


if __name__ == '_main_':
    unittest.main()
