from unittest import TestCase
from app import *

class TestApiUsers(TestCase):
    def test_get_users(self):
        r = all_users_1()
        self.assertEqual(r, 200)