# we invoke the necessary libraries
from flask import Flask
import json
from flask_wtf.csrf import CSRFProtect
import users_controller
from app import connection

# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


@server.get("/users")
def all_users_():
    return users_controller.all_user(connection())


@server.get("/user")
def user(info: dict):
    return users_controller.get_user(connection(), info)


@server.post('/user')
def user_create(info: dict):
    return users_controller.create_user(connection(), info)


@server.put('/update')
def user_update(info: dict):
    return users_controller.update_user(connection(), info)


# the application is executed
if __name__ == '__main__':
    server.run(debug=True, port=6000)