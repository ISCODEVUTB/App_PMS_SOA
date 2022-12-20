# we invoke the necessary libraries
from flask import Flask
from app import connection
from flask_wtf.csrf import CSRFProtect
import shopcar_controller


server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


@server.get('/')
def index():
    return shopcar_controller.clear()


# The route to enter the service is created
@server.route('/show')
def show():
    return shopcar_controller.show_car()


@server.route('/shopcar')
def car():
    return shopcar_controller.show_list()


@server.get('/shopcar/<id>')
def car_product(id):
    return shopcar_controller.into_shop_car(connection(), id)


# the application is executed
if __name__ == '__main__':
    server.run(debug=True)
