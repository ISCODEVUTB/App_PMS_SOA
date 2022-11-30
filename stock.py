# we invoke the necessary libraries
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import stock_controller
from os import getenv
from flask_wtf.csrf import CSRFProtect

# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)

# The connection point to the base is created.
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('BD')
server.config['WTF_CSRF_ENABLED'] = getenv('PROTECT')
mysql = MySQL(server)


# The route to enter the service is created.
@server.get('/vehicles')
def index():
    try:
        return stock_controller.stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The path displaying unit information is created.
@server.get('/vehicle/<string:id>')
def get_vehicle(id):
    try:
       return stock_controller.vehicle(mysql, id)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new vehicle is created.
@server.post('/vehicle')
def create_vehicle():
    try:
        return stock_controller.create_vehicle(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new stock is created.
@server.post('/stock')
def create_stock():
    try:
        return stock_controller.create_stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# The route is created to remove the stock
@server.delete("/stock/<string:id>")
def delete_stock(id):
    try:
        return stock_controller.delete_stock(mysql, id)
    except Exception as ex:
        return jsonify({'message': ex})


# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True)
