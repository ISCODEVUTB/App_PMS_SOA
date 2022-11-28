from flask import jsonify, request


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


def user(mysql):
    user_name = request.args.get('user_name')
    email = request.args.get('email')
    cursor = mysql.connection.cursor()
    sql = "select u.name, u.last_name, u.user, u.email, r.name from users u inner join rool r on (u.rool = r.idrool)" \
          "where u.user = '{0}' or u.email = '{1}'".format(user_name, email)
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
              "rool = '{5}', address = '{6}' where id = '{7}'".format(request.args.get('name'),
                                                                      request.args.get('last_name'),
                                                                      request.args.get('user'),
                                                                      request.args.get('email'),
                                                                      request.args.get('password'),
                                                                      request.args.get('rool'),
                                                                      request.args.get('address'), request.args.get('id'))
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({"Message": "User successfully updated"})
    except Exception as error:
        return jsonify({"Message": "It was not possible to update the user's data"})


def create_user(mysql):
    name = request.args.get('name')
    last_name = request.args.get('last_name')
    user = request.args.get('user')
    email = request.args.get('email')
    password = request.args.get('password')
    rool = request.args.get('rool')
    address = request.args('address')
    cursor = mysql.connection.cursor()
    sql = "insert into users (name, last_name, user, email, password, rool, address) " \
          "values ('{0}', '{1}', '{2}', '{3}','{4}','{5}', '{6}')".format(name, last_name, user, email, password,
                                                                          rool, address)
    cursor.execute(sql)
    mysql.connection.commit()
    if mysql.connection.commit():
        return {"Message": "The user was successfully created"}