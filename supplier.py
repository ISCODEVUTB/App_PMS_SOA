# we invoke the necessary libraries
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from os import getenv
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
import supplier_contraller


# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


# The connection point to the base is created
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('DB')
mysql = MySQL(server)


# The route to enter the service is created
@server.get('/supplier')
def index():
    try:
        return supplier_contraller.show_supplier(mysql)
    except Exception as error:
        return jsonify({"Message": error})


# this route is created to remove data from this service
@server.delete('/supplier/<id>')
def supplier_delete(id):
    try:
        return supplier_contraller.delete_supplier(mysql, id)
    except ValueError:
        return jsonify({"Message": "Error"})


# this route is created to update data of this service
@server.put('/supplier/<id>')
def supplier_update(id):
    try:
        return supplier_contraller.update_supplier(mysql, id)
    except ValueError:
        return jsonify({"message": "Error"})


# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True)