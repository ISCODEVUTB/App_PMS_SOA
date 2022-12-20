# we invoke the necessary libraries
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from os import getenv
from flask_wtf.csrf import CSRFProtect
import users_controller
from dotenv import load_dotenv

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


@server.get("/users")
def all_users():
    try:
        data = users_controller.all_user(mysql)
        return data
    except ValueError:
        return {"Message": "Error"}


@server.get("/user")
def user():
    try:
        data = users_controller.get_user(mysql)
        return data
    except ValueError:
        return {"Message": "Error"}


@server.post('/user')
def create_user():
    try:
        data = users_controller.create_user(mysql)
        return data
    except ValueError:
        return jsonify({"Message": "User could not be created successfully"})


@server.put('/update')
def update_user():
    try:
        update = users_controller.update_user(mysql)
        return update
    except ValueError:
        return jsonify({"Message": "It was not possible to update the user's data"})


# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True, port=6000)