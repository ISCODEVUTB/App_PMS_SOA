from flask import Flask
from database import mysql
from routes.auth import routes_auth
from routes.protect import protect
from dotenv import load_dotenv
from os import getenv
from flask_wtf.csrf import CSRFProtect


server = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(server)
server.config['MYSQL_HOST'] = getenv('HOST')
server.config['MYSQL_USER'] = getenv('USER')
server.config['MYSQL_PASSWORD'] = getenv('PASSWORD')
server.config['MYSQL_DB'] = getenv('BD')
server.config['WTF_CSRF_ENABLED'] = getenv('PROTECT')
mysql.init_app(server)
server.register_blueprint(routes_auth, url_prefix="/api")
server.register_blueprint(protect, url_prefix="/api")


if __name__ == '__main__':
    load_dotenv()
    server.run(debug=True, port=3000, host="0.0.0.0")
