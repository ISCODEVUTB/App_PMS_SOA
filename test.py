from unittest import TestCase
import users
import supplier
import stock
from app import suma
from os import getenv


class TestApp(TestCase):
    def test(self):
        self.assertEqual(suma(1, 2), 3)
