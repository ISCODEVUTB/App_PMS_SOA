import unittest
from app import *



class TestConectionBase(unittest.TestCase):
    def test(self):
        r = conection()
        self.assertEqual(r, 200)