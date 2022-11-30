import unittest
import app
class Test(unittest.TestCase):
    def test(self):
        r = app.suma(1, 2)
        self.assertEqual(r, 3)