from unittest import TestCase
from Backend.users.controller import all_users
import mysql.connector
from os import getenv
from app import suma

conection= mysql.connector.connect( host= getenv('HOST'), user= getenv('USER'), password= getenv('PASSWORD'), database= getenv('BD'))
cursor= conection.cursor()


class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)
    
    def test_all_users(self):
        self.assertEqual(all_users(conection), 200)
