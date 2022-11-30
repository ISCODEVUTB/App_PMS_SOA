from unittest import TestCase
import users


class TestUsers(TestCase):
    def test(self):
        r = users.all_users_1()
        self.assertEqual(len(r.json()), 2)

    def test_2(self):
        r = users.user()
        self.assertEqual(len(r.json()), 2)
    
