from flask import Blueprint, request, jsonify
from function_jwt import validate_token
from database import mysql

protect = Blueprint("protect", __name__)


def token_info():
    token = request.headers['Authorization'].split(" ")[1]
    return token


@protect.before_request
def verify_token_middleware():
    validate_token(token_info(), output=False)


@protect.route("/index")
def index():
    try:
        return jsonify({"Message": request.args.get('username')})
    except ValueError:
        return jsonify({"Message": "Error"})


@protect.route('/update')
def update():
    try:
        return jsonify({"Message": "Welcome tu update"})
    except ValueError:
        return jsonify({"Message": "Error"})


@protect.route("/user")
def verify():
    try:
        return jsonify({"User": validate_token(token_info(), output=True)})
    except ValueError:
        return jsonify({"Message": "error"})
