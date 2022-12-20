import unittest
from stock_controller import stock, delete_stock, vehicle, create_stock, create_vehicle
from app import connection
from stock import index, get_vehicle, stock_delete, create_vehicle_stock, create_stock_
from supplier_contraller import show_supplier, delete_supplier
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

    def test_show_supplier_controller_ok(self):
        r = show_supplier(connection())
        result = json.loads(r)
        if 'suppliers' in result:
            self.assertEqual(TestStock.info_test, TestStock.test_expected)

    def test_delete_supplier_controller(self):
        r = delete_supplier(connection(), 3)
        result = json.loads(r)
        self.assertEqual(result['status'], 'deleted')


# Path: stock_controller.py
if __name__ == '__main__':
    unittest.main()