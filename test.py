import unittest
import users
import supplier
import stock
from app import *
from os import getenv

class TestApp(unittest.TestCase):
    def test(self):
        self.assertEqual(suma(1,2), 3)
