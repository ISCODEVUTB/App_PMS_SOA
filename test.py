from unittest import TestCase
import users
import stock
from os import getenv


class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(app.suma(2, 2), 4)


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
    create = {
        "name": "Diego Andres",
        "last_name": "Quintana",
        "user": "Qdiego25",
        "email": "dquintana@utb.edu.co",
        "password": getenv("PASSWORD", "1234567"),
        "rool": "1",
        "address": "Calle 12 # 12 - 12",
        "id": "4"
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

    def test_create_user(self):
        r = users.create_user(json=self.create)
        self.assertEqual(len(r.json()), 2)


class TestStock(TestCase):

    create = {
        'name': 154,
        'supplier': 1,
        'sell_price': 50000000,
        'quantity': 2,
    }


    def test_all_stock(self):
        r = stock.all_stock()
        self.assertEqual(len(r.json()), 2)
    
    def test_get_vehicle(self):
        r = stock.vehicle(44)
        self.assertEqual(len(r.json()), 2)

    def test_create_vehicle(self):
        r = stock.create_vehicle(json=self.create)
        self.assertEqual(len(r.json()), 2)
