from unittest import TestCase
from Backend.users.controller import all_users_1


class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)