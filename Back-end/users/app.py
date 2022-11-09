# we invoke the necessary libraries
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
import controller

# The access point is created
server = Flask(__name__)

# The connection point to the base is created.
server.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
server.config['MYSQL_USER'] = 'bee0e9755133d2'
server.config['MYSQL_PASSWORD'] = 'f3e9360a'
server.config['MYSQL_DB'] = 'heroku_23edc9681868d22'
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
        return {"Message": "User could not be created successfully"}


# the application is executed
if __name__ == '__main__':
    server.run(debug=True, port=3000)