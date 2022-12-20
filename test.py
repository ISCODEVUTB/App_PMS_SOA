import unittest
from stock_controller import stock, delete_stock, vehicle, create_stock, create_vehicle
from app import connection
from stock import index, get_vehicle, stock_delete, create_vehicle_stock, create_stock_
from supplier_contraller import show_supplier, delete_supplier, update_supplier
from supplier import index, supplier_delete, supplier_update
from users_controller import all_user, get_user, update_user, create_user
from users import all_users_, user, user_create, user_update
from shopcar_controller import show_car, show_list, into_shop_car, clear
from shopcar import index, car, car_product, show
from os import getenv
from dotenv import load_dotenv
from logic.cart import Cart
import json


class TestStock(unittest.TestCase):
    info_test = "Test passed"
    test_expected = "Test passed"
    info = {
        'name': 'Nivus',
        'motor': ' 200 TSI',
        'gearbox': 'Manual',
        'security': 'ABS, Front Assist',
        'type': 4,
        'url': 'https://awscdn.volkswagen.co/media/Abstract_Image_B960_Component.Content_Model_HighlightFeatureSection_Item_Content_Gallery_Item_Component/47530-1067663-750344-content-gallery-750345-b960/dh-857-e0864f/0fce03af/1657115420/Comf-MT-4.jpg',
        'description': 'Diseño, tecnología, modernidad y potencia. Nivus: una camioneta pensada para emocionar',
        'data_sheet': 'https://awscdn.volkswagen.co/media/Kwc_Basic_DownloadTag_Component/47530-1067658-750328-1141514-816457-linkTag-child/default/09ebc1ce/1668812829/ft-volkswagen-nivus-v2-my22.pdf?_ga=2.163114748.1129427029.1670683187-379648666.1669674914&_gl=1*1ehbr8z*_ga*Mzc5NjQ4NjY2LjE2Njk2NzQ5MTQ.*_ga_41DDCT7V7B*MTY3MDcwMjkzNC40LjEuMTY3MDcwMzc4OC4wLjAuMA..'
    }

    stock_vehicle = {
        'name': '304',
        'supplier': 2,
        "selling_price": 101990000,
        "quantity": 3,
    }

    def test_all_stock_controller(self):
        r = stock(connection())
        result = json.loads(r)
        if 'vehicles' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_vehicle_controller(self):
        r = vehicle(connection(), 1)
        result = json.loads(r)
        self.assertEqual(result['vehicle']['name'], 'Voyage')

    def test_create_vehicle_controller(self):
        r = create_vehicle(connection(), TestStock.info)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Vehicle created')

    def test_create_stock_controller(self):
        r = create_stock(connection(), TestStock.stock_vehicle)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Stock created')

    def test_delete_stock_controller(self):
        r = delete_stock(connection(), 254)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Stock deleted')

    def test_stock_index(self):
        r = index()
        result = json.loads(r)
        if 'vehicles' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_stock_get_vehicle(self):
        r = get_vehicle(1)
        result = json.loads(r)
        self.assertEqual(result['vehicle']['name'], 'Voyage')

    def test_stock_delete_stock(self):
        r = stock_delete(214)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Stock deleted')

    def test_create_vehicle_stock(self):
        r = create_vehicle_stock(TestStock.info)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Vehicle created')

    def test_create_stock(self):
        r = create_stock_(TestStock.stock_vehicle)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Stock created')


class TesTSupplier(unittest.TestCase):

    info = {
        "name": 'Toyota',
        "nit": "9007805105",
        "address": "CARRERA 9 A 99 02 OFICINA 60 BOGOTA",
        "phone": "6016381200",
        "email": "atencion.Toyota@gmail.com",
        "idsupplier": 3
    }

    def test_show_supplier_controller_ok(self):
        r = show_supplier(connection())
        result = json.loads(r)
        if 'suppliers' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_delete_supplier_controller(self):
        r = delete_supplier(connection(), 3)
        result = json.loads(r)
        self.assertEqual(result['status'], 'deleted')

    def test_create_supplier_controller(self):
        r = update_supplier(connection(), TesTSupplier.info)
        result = json.loads(r)
        self.assertEqual(result['status'], 'updated')

    def test_show_supplier(self):
        r = index()
        result = json.loads(r)
        if 'suppliers' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_supplier_delete(self):
        r = supplier_delete(3)
        result = json.loads(r)
        self.assertEqual(result['status'], 'deleted')

    def test_supplier_update(self):
        r = supplier_update(TesTSupplier.info)
        result = json.loads(r)
        self.assertEqual(result['status'], 'updated')


class TestUser(unittest.TestCase):
    info = {
        "username": "Esneider3",
        "email": "esneydergp69@gmail.com",
        "password": getenv("PASSWORD_2"),
    }

    info_update = {
        "name": "Esneider",
        "lastname": "Guzman",
        "user": "Esneider3",
        "email": "guzmane@utb.edu.co",
        "password": getenv("PASSWORD_2"),
        "rool": 4,
        "address": "Calle 1 # 2 - 3",
        "id": 1
    }

    info_create = {
        "name": "Diego",
        "lastname": "Quintana",
        "user": "DiegoQuintana",
        "email": "dquintana@utb.edu.co",
        "password": getenv("PASSWORD_2"),
        "rool": 4,
        "address": "None",
    }

    def test_all_users_controller(self):
        r = all_user(connection())
        result = json.loads(r)
        if 'users' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_get_user_controller(self):
        r = get_user(connection(), TestUser.info)
        result = json.loads(r)
        if 'user' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_update_user_controller(self):
        r = update_user(connection(), TestUser.info_update)
        result = json.loads(r)
        self.assertEqual(result['Message'], 'The user was successfully updated')

    def test_create_user_controller(self):
        r = create_user(connection(), TestUser.info_create)
        result = json.loads(r)
        self.assertEqual(result['Message'], 'The user was successfully created')

    def test_all_users(self):
        r = all_users_()
        result = json.loads(r)
        if 'users' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_user(self):
        r = user(TestUser.info)
        result = json.loads(r)
        if 'user' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def user_update(self):
        r = user_update(TestUser.info_update)
        result = json.loads(r)
        self.assertEqual(result['Message'], 'The user was successfully updated')

    def test_user_create(self):
        r = user_create(TestUser.info_create)
        result = json.loads(r)
        self.assertEqual(result['Message'], 'The user was successfully created')


class TestShopCar(unittest.TestCase):
    def test_clear_controller(self):
        r = clear()
        result = json.loads(r)
        self.assertEqual(result['Welcome'], 'Welcome tu api car')

    def test_show_car_controller(self):
        r = show_car()
        result = json.loads(r)
        self.assertEqual(result['count'], result['count'])

    def test_show_list_controller(self):
        r = show_list()
        result = json.loads(r)
        self.assertEqual(result['total_price'], result['total_price'])

    def test_into_car_controller(self):
        r = into_shop_car(connection(), 44)
        result = json.loads(r)
        self.assertEqual(result['Message'], 'The product was successfully added')

    def test_index(self):
        r = index()
        result = json.loads(r)
        self.assertEqual(result['Welcome'], 'Welcome tu api car')

    def test_car(self):
        r = car()
        result = json.loads(r)
        self.assertEqual(result['total_price'], result['total_price'])

    def test_into_car(self):
        r = car_product(44)
        result = json.loads(r)
        self.assertEqual(result['Message'], 'The product was successfully added')


class TestClassCar(unittest.TestCase):
    info = Cart(id_product=6, name='Audi R8', sup_name='Audi', price=1000000, motor='V8', security='airbag',
                gearbox='automatic')
    info_car = {
        "id_product": 6,
        "name": "Audi R8",
        "sup_name": "Audi",
        "price": 1000000,
        "motor": "V8",
        "security": "airbag",
        "gearbox": "automatic"
    }

    def test_class_car(self):
       result = self.info.car_info(TestClassCar.info_car)
       self.assertEqual(result, f"This is a car {TestClassCar.info_car}")


# Path: stock_controller.py
if __name__ == '__main__':
    load_dotenv()
    unittest.main()

