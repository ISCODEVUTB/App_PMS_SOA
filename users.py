# we invoke the necessary libraries
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import user_controller
from flask_wtf.csrf import CSRFProtect
import os

# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)

# The connection point to the base is created.
server.config['MYSQL_HOST'] = os.getenv('HOST')
server.config['MYSQL_USER'] = os.getenv('USER')
server.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
server.config['MYSQL_DB'] = os.getenv('BD')
server.config['WTF_CSRF_ENABLED'] = os.getenv('PROTECT')
mysql = MySQL(server)



def all_users_1():
    try:
        data = user_controller.all_user(mysql)
        return data
    except ValueError:
        return {"Message": "Error"}


def user():
    try:
        data = user_controller.user(mysql, 1)
        return data
    except ValueError:
        return {"Message": "Error"}


def create_user(crete: dict):
    try:
        data = user_controller.create_user(mysql)
        return data
    except ValueError:
        return {"Message": "User could not be created successfully"}


def update_user(update : dict):
    try:
        update = user_controller.update_user(mysql)
        return update
    except ValueError:
        return jsonify({"Message": "It was not possible to update the user's data"})


if __name__ == '__main__':
    server.run(debug=True)
