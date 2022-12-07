# we invoke the necessary libraries
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from os import getenv
import users_controller

# The access point is created
server = Flask(__name__)

# The connection point to the base is created.
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('DB')
mysql = MySQL(server)


@server.get("/users")
def all_users():
    try:
        data = controller.all_user(mysql)
        return data
    except Exception as error:
        return {"Message": "Error"}


@server.get("/user")
def user():
    try:
        data = controller.user(mysql)
        return data
    except Exception as error:
        return {"Message": "Error"}


@server.post('/user')
def create_user():
    try:
        data = controller.create_user(mysql)
        return data
    except Exception as error:
        return jsonify({"Message": "User could not be created successfully"})

@server.put('/update')
def update_user():
    try:
        update = controller.update_user(mysql)
        return update
    except Exception as error:
        return jsonify({"Message": "It was not possible to update the user's data"})


# the application is executed
if __name__ == '__main__':
    server.run(debug=True, port=6000)