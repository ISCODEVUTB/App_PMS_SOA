# we invoke the necessary libraries
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from os import getenv
from flask_wtf.csrf import CSRFProtect
import shopcar_controller


server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('DB')

# The connection point to the base is created
mysql = MySQL(server)


@server.get('/')
def index():
    try:
        return shopcar_controller.clear()
    except ValueError:
        return {"Message": "Error"}


# The route to enter the service is created
@server.route('/show')
def show():
    try:
        return shopcar_controller.show_car()
    except ValueError:
        return {"Message": "Error"}


@server.route('/shopcar')
def car():
    try:
        return shopcar_controller.show_list()
    except ValueError:
        return {'message': 'error'}


@server.get('/shopcar/<id>')
def car_product(id):
    try:
        return shopcar_controller.into_shop_car(mysql, id)
    except ValueError:
        return {"Message": "Error"}


# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True)