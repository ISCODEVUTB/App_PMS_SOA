# we invoke the necessary libraries
from flask import Flask, render_template
from flask_mysqldb import MySQL
import shop

# The access point is created
server = Flask(__name__)

# The connection point to the base is created
server.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
server.config['MYSQL_USER'] = 'bee0e9755133d2'
server.config['MYSQL_PASSWORD'] = 'f3e9360a'
server.config['MYSQL_DB'] = 'heroku_23edc9681868d22'
mysql = MySQL(server)


shop_car = []


# The route to enter the service is created
@server.get('/')
def index():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("select u.name, r.name from users u join rool r on u.rool = r.idrool")
        data = cursor.fetchall()
        print(data)
        return {'data': data}
    except Exception as ex:
        return "Error"

# Function that returns items from the shopping cart.
@server.get('/shop')
def car():
    return shop.show_shopping_car(shop_car)


# Function that adds items to shopping cart.
@server.post('/shop')
def shopping_car():
    return shop.add_shopping_car(mysql, shop_car)


# Function that performs the shopping cart purchase and updates the database.
@server.put('/buy')
def buy():
    return shop.complete_buy(mysql, shop_car)


# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.register_error_handler(404, page_not_found)
    server.run(debug=True)
