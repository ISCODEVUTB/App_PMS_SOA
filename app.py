import pymysql
from os import getenv
import mysql.connector


def conection():
    try:
        conection = mysql.connector.connect(host = getenv('HOST'), user = getenv('USER'), password = getenv('PASSWORD'), database = getenv('DB'))
        cursor = conection.cursor()
        return 200
    except:
        return 500

