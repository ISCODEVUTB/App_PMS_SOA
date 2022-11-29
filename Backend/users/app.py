# we invoke the necessary libraries
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from controller import *
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


@server.get("/users")
def all_users_1():
    try:
        data = all_user(mysql)
        return data
    except ValueError:
        return {"Message": "Error"}


@server.get("/user")
def user():
    try:
        data = user(mysql)
        return data
    except ValueError:
        return {"Message": "Error"}


@server.post('/user')
def create_user():
    try:
        data = create_user(mysql)
        return data
    except ValueError:
        return {"Message": "User could not be created successfully"}

@server.put('/update')
def update_user():
    try:
        update = update_user(mysql)
        return update
    except ValueError:
        return jsonify({"Message": "It was not possible to update the user's data"})


# the application is executed
if __name__ == '__main__':
    server.run(debug=True, port=6000)