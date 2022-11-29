# we invoke the necessary libraries
from flask import Flask, render_template,jsonify, request

from dotenv import load_dotenv
from os import getenv
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
import contraller


# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)

# The connection point to the base is created
# The connection point to the base is created
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('BD')
server.config['WTF_CSRF_ENABLED'] = getenv('PROTECT')
mysql = MySQL(server)


@server.get('/')
def index():
    try:
        return contraller.clear()
    except Exception as error:
        return page_not_found(error)


@server.route('/show')
def show():
    try:
        return contraller.show_car()
    except Exception as ex:
        return page_not_found(ex)


@server.route('/shotcar')
def car():
    try:
        return contraller.show_list()
    except Exception as ex:
        return page_not_found(ex)


@server.get('/shotcar/<id>')
def car_product(id):
    try:
        return contraller.into_shopcar(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.register_error_handler(404, page_not_found)
    server.run(debug=True)