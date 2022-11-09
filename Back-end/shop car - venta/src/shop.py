from flask import jsonify, request
from secrets import token_hex


def show_shopping_car(shopping_car):
    """
    Function that returns in json form the content of the shopping cart.

    :param shopping_car:
    :return: Json
    """
    try:
        total_price = 0
        quantity_items = 0
        data = []
        for row in shopping_car:
            total_price += row['price_unitary'] * row['quantity']
            quantity_items += row['quantity']
            data.append(row)

        return jsonify({'shopping_cart': data, 'quantity_items': quantity_items, 'total_price': total_price})
    except TypeError:
        return jsonify({'Error': 'TypeError'})


def is_in_shopping_car(id_product, quantity, shopping_car):
    """
    Function that verifies if an item has already been added to the cart, if it exists, it only increases the number of
    units in the cart so as not to have duplications.

    :param id_product:
    :param quantity:
    :param shopping_car:
    :return: Bool
    """
    for row in shopping_car:
        if id_product == row['idProduct']:
            row['quantity'] = quantity + row['quantity']
            return True
    return False


def add_shopping_car(mysql, shopping_car):
    """
    Function that adds selected items to the shopping cart.

    :param mysql:
    :param shopping_car:
    :return: JSON
    """

    id_product = request.json['idProduct']
    quantity = request.json['quantity']

    cursor = mysql.connection.cursor()
    cursor.cursor = mysql.connection.cursor()
    db_query = 'select s.idstock, ss.name, sup.name, ss.description, s.selling_price, s.quantity ' \
               'from (stock s, supplier sup) join stocksupl ss ' \
               'on s.name = ss.idstocksupl and sup.idsupplier = s.supplier and s.idstock = {0}'.format(id_product)
    cursor.execute(db_query)
    data = cursor.fetchall()

    # If "data" is empty after making the request to the database server, it means that the id of the selected product
    # was not found, in other words, it does not exist.
    if data == ():
        return jsonify({'error': 'don\'t exist this id: {0}'.format(id_product)})


    # We verify that there are enough items in the inventory to add to the database.
    quantity_in_stock = data[0][5]
    for row in shopping_car:
        print(row)
        if id_product == row['idProduct']:
            if (quantity_in_stock - (row['quantity'] + quantity)) < 0:
                return jsonify({'Error': 'Not enough items in stock, choose a smaller quantity.'})

    # We checked if the item already existed in the shopping cart.
    if is_in_shopping_car(id_product, quantity, shopping_car):
        pass
    else:
        aux_shopping_car = {'idProduct': data[0][0],
                            'nameProduct': data[0][1],
                            'supplier': data[0][2],
                            'description': data[0][3],
                            'quantity': quantity,
                            'price_unitary': data[0][4]}
        shopping_car.append(aux_shopping_car)
        print(shopping_car)
    return show_shopping_car(shopping_car)


def complete_buy(mysql, shopping_car):
    """
    Función que genera el código de transacción de compra de los artículos del carrito, además, actualizar la base de
    datos con la nueva cantidad de articulos en el inventario, y vacía el carrito de compras.

    :param mysql:
    :param shopping_car:
    :return: JSON
    """

    if not shopping_car:
        return jsonify({'Error': 'Don\'t have any in the shopping car'})

    cursor = mysql.connection.cursor()
    cursor.cursor = mysql.connection.cursor()
    db_query = 'SELECT idstock, quantity FROM stock'
    cursor.execute(db_query)
    stocks = cursor.fetchall()

    # Updating the database with the new quantity of items in stock.
    for item_car in shopping_car:
        for stock in stocks:
            if item_car['idProduct'] == stock[0]:
                new_quantity = stock[1] - item_car['quantity']
                db_update = 'UPDATE stock SET quantity = {0} WHERE idstock = {1};'.format(new_quantity, stock[0])
                cursor.execute(db_update)
                cursor.connection.commit()

    # It generates the unique transaction code and the json that we will return.
    security_key = token_hex()
    facture = jsonify({'hash_transaction': security_key,
                       'bought_items': shopping_car,
                       'transaction_state': 'Finally'})

    # Emptying the shopping cart.
    shopping_car.clear()
    return facture
