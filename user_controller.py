from flask import jsonify, request
import json


def all_user(mysql):
    cursor = mysql.connection.cursor()
    sql = "select u.name, u.last_name, u.email, u.address, r.name from users u inner join rool r on (u.rool = r.idrool)"
    cursor.execute(sql)
    data = cursor.fetchall()
    users = []
    for fila in data:
        user_pro = {'name': fila[0], 'last name': fila[1], 'email': fila[2], 'rool': fila[3]}
        users.append(user_pro)
    return jsonify({"users": users})


def user(mysql, id):
    cursor = mysql.connection.cursor()
    sql = "select u.name, u.last_name, u.user, u.email, r.name from users u inner join rool r on (u.rool = r.idrool)" \
          "where u.user = '{0}'".format(id)
    cursor.execute(sql)
    data = cursor.fetchone()
    user_info = []
    if data is not None:
        user_pro = {'name': data[0], 'last name': data[1], 'username': data[2], 'email': data[3], 'rool': data[4]}
        user_info.append(user_pro)
        return jsonify({"user_info": user_info})
    else:
        return jsonify(user_info)


def update_user(mysql):
    try:
        cursor = mysql.connection.cursor()
        sql = "update users set name = '{0}', last_name = '{1}', user = '{2}', email = '{3}', password = '{4}'," \
              "rool = '{5}', address = '{6}' where id = '{7}'".format(request.json['name'], request.json['last_name'],
                                                                      request.json['user'], request.json['email'],
                                                                      request.json['password'],
                                                                      request.json['rool'],
                                                                      request.json['address'], request.json['id'])
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"Message": "User successfully updated"})
    except ValueError:
        return jsonify({"Message": "It was not possible to update the user's data"})


def create_user(mysql):
    name = request.json['name']
    last_name = request.json['last_name']
    user = request.json['user']
    email = request.json['email']
    password = request.json['password']
    rool = request.json['rool']
    address = request.args['address']
    cursor = mysql.connection.cursor()
    sql = "insert into users (name, last_name, user, email, password, rool, address) " \
          "values {0}', '{1}', '{2}', '{3}','{4}','{5}', '{6}')".format(name, last_name, user, email, password,
                                                                          rool, address)
    cursor.execute(sql)
    mysql.connection.commit()
    if mysql.connection.commit():
        return {"Message": "The user was successfully created"}