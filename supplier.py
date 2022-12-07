# we invoke the necessary libraries
from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from os import getenv
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


@cross_origin
# The route to enter the service is created
@server.get('/supplier')
def index():
    try:
        return contraller.show_supplier(mysql)
    except Exception as error:
        return jsonify({"Message": error})


@cross_origin
# this route is created to remove data from this service
@server.delete('/supplier/<id>')
def supplier_delete(id):
    try:
        return contraller.delete_supplier(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


@cross_origin
# this route is created to update data of this service
@server.put('/supplier/<id>')
def supplier_update(id):
    try:
        return contraller.update_supplier(mysql, id)
    except Exception as ex:
        return page_not_found(ex)


@cross_origin
# A function is created to show when a page is not found.
def page_not_found(error):
    return render_template('404.html')


# the application is executed
if __name__ == '__main__':
    server.run(debug=True)