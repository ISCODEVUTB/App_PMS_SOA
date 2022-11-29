from flask import Blueprint, request, jsonify
from function_jwt import write_token, validate_token
from database import mysql

routes_auth = Blueprint("routes_aut", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    cursor = mysql.connection.cursor()
    sql = "select u.id, u.name, u.last_name, u.user, u.email, r.name from users u inner join rool r on " \
          "(u.rool = r.idrool) where u.email = '{0}' and u.password = '{1}'"\
        .format(email, password)
    cursor.execute(sql)
    info = cursor.fetchone()
    if info is not None:
        key = ('id', 'name', 'last_name', 'user', 'email', 'type')
        res = dict(zip(key, info))
        return jsonify({'token': write_token(data=res)})
    else:
        response = jsonify({"Message": "User not found"})
        response.status_code = 404
        return response


