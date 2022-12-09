# we invoke the necessary libraries
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from os import getenv
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from stock_controller import *

# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


# The connection point to the base is created.
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('DB')
mysql = MySQL(server)


# The route to enter the service is created.
@server.get('/vehicles')
def index():
    try:
        return stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The path displaying unit information is created.
@server.get('/vehicle/<string:id>')
def get_vehicle(id):
    try:
       return vehicle(mysql, id)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new vehicle is created.
@server.post('/vehicle')
def create_vehicle():
    try:
        return create_vehicle(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new stock is created.
@server.post('/stock')
def create_stock():
    try:
        return create_stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The route is created to remove the stock
@server.delete("/stock/<string:id>")
def delete_stock(id):
    try:
        return delete_stock(mysql, id)
    except Exception as ex:
        return jsonify({'message': ex})


# A function is created to show when a page is not found.

# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True)