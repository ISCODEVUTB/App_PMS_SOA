import unittest
from app import app


class BasicTest(unittest.TestCase):
    def text_index(self):
        tester = app.test_client(self)
        resp = tester.get('https://servicio-stock.onrender.com/vehiculos')
        code = resp.status_code
        self.assertEqual(code, 200)


<<<<<<< HEAD
if __name__ == '_main_':
    unittest.main()
=======
if __name__ == 'main':
    unittest.main()
>>>>>>> 996502837e8a0fe1c7475db6d436939eee51252d
