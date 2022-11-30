from unittest import TestCase
import app
import users

class Test(TestCase):
    def test(self):
        r = app.suma(1, 2)
        self.assertEqual(r, 3)

class TestUsers(TestCase):
    def test(self):
        r = users.all_users_1()
        self.assertEqual(len(r.json()), 2)