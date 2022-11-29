# we invoke the necessary libraries
from flask import jsonify, request


# This function returns the supplier information
def show_supplier(mysql):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("select idsupplier, name, nit, address, phone, email from supplier")
        data = cursor.fetchall()
        if data is not None:
            list_supplier = []
            for fila in data:
                list_supplier_get = {'id_supplier': fila[0], 'name': fila[1], 'nit': fila[2], 'address': fila[3],
                                     'phone': fila[4], 'email': fila[5]}
                list_supplier.append(list_supplier_get)
            return jsonify({'listSupplier': list_supplier, 'message': "List of suppliers"})
        else:
            return jsonify({'message': "There are no data"})
    except Exception as ex:
        return jsonify({'message': ex})


# This function deletes a data from a supplier
def delete_supplier(mysql, id_supplier):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("delete from supplier where idsupplier = (%s)", id_supplier)
        data = cursor.fetchall()
        print("Provider to be deleted: ", data)
        cursor.execute("select idsupplier, name, nit, address, phone, email from supplier where idsupplier = (%s)",
                       id_supplier)
        mysql.connection.commit()
        return show_supplier(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


# This function updates a data of a supplier
def update_supplier(mysql, id_supplier):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("update supplier set name = '{0}', nit = '{1}', address = '{2}', phone = '{3}',"
                       "email = '{4}' where idsupplier = '{5}'".format(request.json['name'], request.json['nit'],
                                                                       request.json['address'], request.json['phone'],
                                                                       request.json['email'], id_supplier))
        mysql.connection.commit()
        return show_supplier(mysql)
    except Exception as ex:
        return jsonify({'message': ex})
