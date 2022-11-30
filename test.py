from unittest import TestCase
from Backend.users.app import all_users_1
from app import suma

class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)

    def test_all_users(self):
        self.assertEqual(all_users_1(), 200)