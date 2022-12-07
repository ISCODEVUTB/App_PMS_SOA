# we invoke the necessary libraries
from flask import Flask, render_template,jsonify, request
from flask_mysqldb import MySQL
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
    except Exception as error:
        return page_not_found(error)


@cross_origin
@server.route('/show')
def show():
    try:
        return shopcar_controller.show_car()
    except Exception as ex:
        return page_not_found(ex)


@server.route('/shopcar')
def car():
    try:
        return shopcar_controller.show_list()
    except Exception as ex:
        return page_not_found(ex)


@server.get('/shopcar/<id>')
def car_product(id):
    try:
        return shopcar_controller.into_shop_car(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


# This function remove the cart by the ID
@server.get('/del/<id>')
def del_cart(id):
    return shopcar_controller.delate_cart(id)
    


# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.register_error_handler(404, page_not_found)
    server.run(debug=True)