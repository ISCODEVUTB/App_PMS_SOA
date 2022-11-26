import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = "https://servicio-stock.onrender.com/"
    vehicles = "{}/vehicles".format(API_URL)
    vehicle = "{}/vehicle".format(API_URL)
    stock = "{}/stock".format(API_URL)
    stock_delete = "{}/stock/4".format(API_URL)
    vehicle_object = {
            "name": "Onix Turbo RS 2023",
            "motor": "MOTOR TURBO 115 HP TORQUE 160 NM",
            "gearbox": "HP 115 Torque 160 Nm",
            "security": "6 AIRBAGS",
            "type": 4
    }
    stock_object = {
        "name": 14,
        "supplier": 1,
        "selling_price": 1000000000,
        "quantity": 2
    }

    def test_1_get_all_vehicles(self):
        r = requests.get(ApiTest.vehicles)
        self.assertEqual(r.status_code, 200)

    def test_2_create_vehicle(self):
        r = requests.post(ApiTest.vehicle, json=ApiTest.vehicle_object)
        self.assertEqual(r.status_code, 200)

    def test_3_create_stock(self):
        r = requests.post(ApiTest.stock, json=ApiTest.stock_object)
        self.assertEqual(r.status_code, 200)

    def test_4_delete_stock(self):
        r = requests.delete(ApiTest.stock)
        self.assertEqual(r.status_code, 200)
