import mysql.connector

def suma(a,b):
    return a+b

def connect():
    try:
        connection = mysql.connector.connect( host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_23edc9681868d22',
                                                user='bee0e9755133d2',
                                                password='f3e9360a')
        if connection.is_connected():
            return "connected"
    except Exception as error:
        return error, 500
