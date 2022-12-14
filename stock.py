# we invoke the necessary libraries
from flask import Flask, jsonify
from app import connection
from flask_wtf.csrf import CSRFProtect
import stock_controller


# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


# The route to enter the service is created.
@server.get('/vehicles')
def index_stock():
    return stock_controller.stock(connection())


# The path displaying unit information is created.
@server.get('/vehicle/<string:id>')
def get_vehicle(id):
    return stock_controller.vehicle(connection(), id)


# The route to create a new vehicle is created.
@server.post('/vehicle')
def create_vehicle_stock(info: dict):
    return stock_controller.create_vehicle(connection(), info)


# The route to create a new stock is created.
@server.post('/stock')
def create_stock_(info: dict):
    return stock_controller.create_stock(connection(), info)


# The route is created to remove the stock
@server.delete("/stock/<string:id>")
def stock_delete(id):
    return stock_controller.delete_stock(connection(), id)


# the application is executed
if __name__ == '__main__':
    server.run(debug=True)
