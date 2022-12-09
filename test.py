import MySQLdb
from os import getenv
from dotenv import load_dotenv
import sys
import json
from stock_controller import *
from unittest import TestCase
load_dotenv()


# The connection point to the base is created.
def connection():
    try:
        db = MySQLdb.connect(host=getenv('HOST'), user=getenv('USER'), passwd=getenv('PASSWORD'), db=getenv('DB'))
        return db
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)


# verify that the stocks exists
class TestApiStock(TestCase):
    def test_all_stock(self):
        info = stock(connection())
        self.assertEquals(info.status_code, 200)
