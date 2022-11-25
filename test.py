import unittest
from app import app


class BasicTest(unittest.TestCase):
    def text_index(self):
        tester = app.test_client(self)
        resp = tester.get('https://servicio-stock.onrender.com/vehiculos')
        code = resp.status_code
        self.assertEqual(code, 200)


if __name__ == 'main':
    unittest.main()
