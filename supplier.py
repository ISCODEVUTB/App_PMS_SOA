# we invoke the necessary libraries
from flask import Flask
from app import connection
from flask_wtf.csrf import CSRFProtect
import supplier_contraller


# The access point is created
server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)


# The route to enter the service is created
@server.get('/supplier')
def index():
    return supplier_contraller.show_supplier(connection())


# this route is created to remove data from this service
@server.delete('/supplier/<id>')
def supplier_delete(id):
    return supplier_contraller.delete_supplier(connection(), id)


# this route is created to update data of this service
@server.put('/supplier/<id>')
def supplier_update(info: dict):
    return supplier_contraller.update_supplier(connection(), info)


# the application is executed
if __name__ == '__main__':
    server.run(debug=True)
