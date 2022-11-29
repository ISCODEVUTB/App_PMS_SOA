import unittest
import controller
import app


class MyTestCase(unittest.TestCase):
    def all_users(self):
        r = controller.get_all_users(app.mysql)
        self.assertEqual(len(r.json()), 2) # 2 users in the database

    def user_by_id(self):
        r = controller.user(app.mysql, 1)
        self.assertEqual(r.json()['name'], 'Esneider Enrique') # user with id 1


if __name__ == '__main__':
    unittest.main()
