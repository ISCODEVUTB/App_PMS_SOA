from unittest import TestCase
import users
from os import getenv


class TestUsers(TestCase):
    update = {
        "name": "Esneider",
        "last_name": "Guzman",
        "user": "esneider23",
        "email": "esneydergp69@gmail.com",
        "password": getenv("PASSWORD", "1234567"),
        "rool": "2",
        "address": "Calle 12 # 12 - 12",
        "id": "1"
    }
    def test_all_users(self):
        r = users.all_users_1()
        self.assertEqual(len(r.json()), 2)

    def test_get_user(self):
        r = users.user()
        self.assertEqual(len(r.json()), 2)

    def test_update_user(self):
        r = users.update_user(json=self.update)
        self.assertEqual(len(r.json()), 2)
