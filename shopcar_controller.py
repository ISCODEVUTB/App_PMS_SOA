# we invoke the necessary libraries
import json
from logic.cart import Cart

model = []
aux = []


def clear():
    model.clear()
    info = {"Welcome": 'Welcome tu api car'}
    return json.dumps(info)


def show_car():
    data = [(i.id_product, i.name, i.sup_name, i.price, i.motor, i.gearbox, i.security) for i in model]
    info = {'count': len(data), 'total_price': price_total()}
    return json.dumps(info)


def show_list():
    data = [(i.id_product, i.name, i.sup_name, i.price, i.motor, i.gearbox, i.security) for i in model]
    info = {'shopping_cart': data, 'total_price': price_total()}
    return json.dumps(info)


def into_shop_car(mysql, id_product):
    cursor = mysql.cursor()
    cursor.execute("select v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security "
                   "from stock s inner join vehicle v on (s.name = v.id)"
                   "inner join supplier su on (s.supplier = su.idsupplier) where s.idstock = '{0}'".format(id_product))
    data = cursor.fetchall()
    for fila in data:
        c = Cart(id_product=id_product, name=fila[0], sup_name=fila[1], price=fila[2], motor=fila[3],
                 security=fila[5], gearbox=fila[4])
        model.append(c)
    data = [(i.id_product, i.name, i.sup_name, i.price, i.motor, i.gearbox, i.security) for i in model]
    info = {'listProduct': data, 'total_price': price_total(), 'Message': 'The product was successfully added',
            'count': len(data)}
    return json.dumps(info)



def price_total():
    p = 0
    for i in model:
        p = p + i.price
    return p
