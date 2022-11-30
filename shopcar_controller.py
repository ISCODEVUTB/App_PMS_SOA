# we invoke the necessary libraries
from flask import jsonify, request
from logic.cart import Cart

model = []
aux = []


def clear():
    model.clear()
    return jsonify({"Welcome": 'Welcome tu api car'})


def show_car():
    data = [(i.idProduct, i.name, i.supName, i.price, i.motor, i.gearbox, i.security) for i in model]
    if data != 0:
        return jsonify({'count': len(data), 'total_price': price_total()})
    else:
        return jsonify({'messeger: "There are no data'})


def show_list():
    data = [(i.idProduct, i.name, i.supName, i.price, i.motor, i.gearbox, i.security) for i in model]
    print(data)
    return jsonify({'shopping_cart': data, 'total_price': price_total()})


def into_shopcar(mysql, idProduct):
    cursor = mysql.connection.cursor()
    cursor.execute("select v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security "
                   "from stock s inner join vehicle v on (s.name = v.id)"
                   "inner join supplier su on (s.supplier = su.idsupplier) where s.idstock = '{0}'".format(idProduct))
    data = cursor.fetchall()
    if data is not None:
        for fila in data:
            c = Cart(idProduct=idProduct, name=fila[0], supName=fila[1], price=fila[2], motor=fila[3], gearbox=fila[4],
                     security=fila[5])
            model.append(c)
            print(data)
        data = [(i.idProduct, i.name, i.supName, i.price, i.motor, i.gearbox, i.security) for i in model]
        return jsonify({'listProduct': data, 'messeger': "save to shopping cart"})
    else:
        return jsonify({'messeger: "There are no data'})


def price_total():
    p = 0
    for i in model:
        p = p + i.price
    return p
