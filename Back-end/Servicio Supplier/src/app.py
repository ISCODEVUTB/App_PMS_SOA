# we invoke the necessary libraries
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import contraller
from dotenv import load_dotenv
from os import getenv

# The access point is created
server = Flask(__name__)

# The connection point to the base is created
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('BD')
mysql = MySQL(server)


# The route to enter the service is created
@server.get('/supplier')
def index():
    try:
        return contraller.show_supplier(mysql)
    except Exception as error:
        return jsonify({"Message": error})


# this route is created to remove data from this service
@server.delete('/supplier/<id>')
def supplier_delete(id):
    try:
        return contraller.delete_supplier(mysql, id)
    except Exception as ex:
        return jsonify({"Message": ex})


# this route is created to update data of this service
@server.put('/supplier/<id>')
def supplier_update(id):
    try:
        return contraller.update_supplier(mysql, id)
    except Exception as ex:
        return jsonify({"message": ex})


# the application is executed
if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True)
