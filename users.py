# we invoke the necessary libraries
from flask import Flask
import json
from flask_wtf.csrf import CSRFProtect
import users_controller
from app import connection
from dotenv import load_dotenv

# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


@server.get("/users")
def all_users_():
    data = users_controller.all_user(connection())
    return data


@server.get("/user")
def user(info: dict):
    data = users_controller.get_user(connection(), info)
    return data


@server.post('/user')
def user_create(info: dict):
    data = users_controller.create_user(connection(), info)
    return data


@server.put('/update')
def user_update(info: dict):
    update = users_controller.update_user(connection(), info)
    return update


# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True, port=6000)