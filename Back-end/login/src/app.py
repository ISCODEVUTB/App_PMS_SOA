from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required


# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

server = Flask(__name__)

server.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
server.config['MYSQL_USER'] = 'bee0e9755133d2'
server.config['MYSQL_PASSWORD'] = 'f3e9360a'
server.config['MYSQL_DB'] = 'heroku_23edc9681868d22'
db = MySQL(server)
login_manager_server = LoginManager(server)


@login_manager_server.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@server.route('/')
def index():
    return redirect(url_for('login'))


@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@server.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@server.route('/home')
@login_required
def home():
    return render_template('home.html')


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    server.register_error_handler(401, status_401)
    server.secret_key = '5saf151d5f16adf'
    server.register_error_handler(404, status_404)
    server.run(debug=True, port= 3000)
