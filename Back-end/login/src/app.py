from flask import Flask, jsonify
from database import mysql
from routes.auth import routes_auth
from routes.protect import protect

server = Flask(__name__)
server.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
server.config['MYSQL_USER'] = 'bee0e9755133d2'
server.config['MYSQL_PASSWORD'] = 'f3e9360a'
server.config['MYSQL_DB'] = 'heroku_23edc9681868d22'
mysql.init_app(server)
server.register_blueprint(routes_auth, url_prefix="/api")
server.register_blueprint(protect, url_prefix="/api")


if __name__ == '__main__':
    server.secret_key= "KQSFKGNIJSOPDGBIOMOP"
    server.run(debug=True, port=3000, host="0.0.0.0")
