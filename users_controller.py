import json


def all_user(mysql):
    cursor = mysql.cursor()
    sql = "select u.name, u.last_name, u.email, u.address, r.name from users u inner join rool r on (u.rool = r.idrool)"
    cursor.execute(sql)
    data = cursor.fetchall()
    users = []
    for fila in data:
        user_pro = {'name': fila[0], 'last name': fila[1],
                    'email': fila[2], 'address': fila[3],  'rool': fila[4]}
        users.append(user_pro)
    info = {'users': users}
    return json.dumps(info)


def get_user(mysql, info: dict):
    user_name = info['username']
    email = info['email']
    password = info['password']
    cursor = mysql.cursor()
    sql = "select u.id, u.name, u.last_name, u.user, u.email, r.name from users u inner join rool r on (u.rool = r.idrool)" \
          "where (u.user = '{0}' or u.email = '{1}') and u.password = '{2}'".format(
              user_name, email, password)
    cursor.execute(sql)
    data = cursor.fetchone()
    user_info = {'id': data[0], 'name': data[1], 'last name': data[2], 'username': data[3], 'email': data[4],
                 'rool': data[5]}
    info = {'user': user_info}
    return json.dumps(info)


def update_user(mysql, info: dict):
    cursor = mysql.cursor()
    cursor.execute("update users set name = '{0}', last_name = '{1}', user = '{2}', email = '{3}', "
                   "password = '{4}', rool = '{5}', address = '{6}' where id = '{7}'".format(info['name'],
                                                                                             info['lastname'],
                                                                                             info['user'], info['email']
                                                                                             , info['password'],
                                                                                             info['rool'],
                                                                                             info['address'],
                                                                                             info['id']))

    mysql.commit()
    info = {'Message': 'The user was successfully updated'}
    return json.dumps(info)


def create_user(mysql, info: dict):
    name = info['name']
    last_name = info['lastname']
    user = info['user']
    email = info['email']
    password = info['password']
    rool = info['rool']
    address = info['address']
    cursor = mysql.cursor()
    sql = "insert into users (name, last_name, user, email, password, rool, address) " \
          "values ('{0}', '{1}', '{2}', '{3}','{4}','{5}', '{6}')".format(name, last_name, user, email, password,
                                                                          rool, address)
    cursor.execute(sql)
    mysql.commit()
    info = {'Message': 'The user was successfully created'}
    return json.dumps(info)
