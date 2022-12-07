# we invoke the necessary libraries
from flask import Flask, render_template,jsonify, request
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
from os import getenv
import shopcar_controller

server = Flask(__name__)

CORS(server)

server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('DB')

# The connection point to the base is created
mysql = MySQL(server)


@cross_origin
@server.get('/')
def index():
    try:
        return contraller.clear()
    except Exception as error:
        return page_not_found(error)


@cross_origin
@server.route('/show')
def show():
    try:
        return contraller.show_car()
    except Exception as ex:
        return page_not_found(ex)


@cross_origin
@server.route('/shopcar')
def car():
    try:
        return contraller.show_list()
    except Exception as ex:
        return page_not_found(ex)


@cross_origin
@server.get('/shopcar/<id>')
def car_product(id):
    try:
        return contraller.into_shopcar(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


# This function remove the cart by the ID
@cross_origin
@server.get('/del/<id>')
def del_cart(id):
    return contraller.delate_cart(id)
    


# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.register_error_handler(404, page_not_found)
    server.run(debug=True)