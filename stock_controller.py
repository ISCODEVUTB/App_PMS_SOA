import json


# the function that allows to list all vehicles in stock is created
def stock(mysql):
    try:
        cursor = mysql.cursor()
        sql = "select s.idstock, v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security, t.name, v.url " \
            "from stock s inner join vehicle v on (s.name = v.id) inner join supplier su on (s.supplier = su.idsupplier)"\
            " inner join type t on (v.type = t.idtype)"
        cursor.execute(sql)
        data = cursor.fetchall()
        vehicles = []
        for fila in data:
            vehicle = {'id': fila[0], 'name': fila[1], 'supplier': fila[2], 'price': fila[3], 'motor': fila[4],
                    'gearbox': fila[5], 'security': fila[6], 'type': fila[7], 'image': fila[8]}
            vehicles.append(vehicle)
        info = {'vehicles': vehicles}
        return json.dumps(info)
    except ValueError:
        return 'Error'


# the function allowing to list the information of a particular vehicle is created
def vehicle(mysql, id):
    cursor = mysql.cursor()
    sql = "select s.idstock, v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security, t.name, v.url, v.description, v.data_sheet from stock s inner join vehicle v on (s.name = v.id) inner join supplier su on (s.supplier = su.idsupplier) inner join type t on (v.type = t.idtype) where s.idstock = '{0}'".format(id)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is not None:
        vehicle = {'id': data[0], 'name': data[1], 'supplier': data[2], 'price': data[3], 'motor': data[4], 'gearbox': data[5],
                   'security': data[6], 'type': data[7], 'image': data[8], 'description': data[9], 'data_sheet': data[10]}
        info = {'vehicle': vehicle}
        return json.dumps(info)
    else:
        return jsonify({'message': 'Vehicle not found'})


# the function allowing the creation of a new vehicle is created
def create_vehicle(mysql, info: dict):
   cursor = mysql.cursor()
   sql = "insert into vehicle (name, motor, gearbox, security, type, url, description, data_sheet) values " \
         "(%s, %s, %s, %s, %s, %s, %s, %s)"
   val = (info['name'], info['motor'], info['gearbox'], info['security'], info['type'], info['url'], info['description'], info['data_sheet'])
   cursor.execute(sql, val)
   mysql.commit()
   message = {"message": "Vehicle created"}
   return json.dumps(message)


# the function is created that allows a vehicle to be removed from stock
# the function that allows you to create a new stock is created
def create_stock(mysql, info: dict):
    cursor = mysql.cursor()
    sql = "insert into stock (name, supplier, selling_price, quantity) values (%s, %s, %s, %s)"
    val = (info['name'], info['supplier'], info['selling_price'], info['quantity'])
    cursor.execute(sql, val)
    mysql.commit()
    message = {"message": "Stock created"}
    return json.dumps(message)


# the function is created that allows a vehicle to be removed from stock
def delete_stock(mysql, id):
    sql = "delete from stock where idstock = '{0}'".format(id)
    cursor = mysql.cursor()
    cursor.execute(sql)
    mysql.commit()
    message = {"message": "Stock deleted"}
    return json.dumps(message)