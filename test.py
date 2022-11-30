import unittest
import app

class TestApp(unittest.TestCase):
    def test_app(self):
        self.assertEqual(app.suma(2,2), 4)