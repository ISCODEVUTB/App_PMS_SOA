import os
import unittest
import urllib.parse
import requests


class ApiTestStock(unittest.TestCase):
    API_URL = "https://servicio-stock.onrender.com"
    vehicles = "{}/vehicles".format(API_URL)
    vehicle = "{}/vehicle".format(API_URL)
    stock = "{}/stock".format(API_URL)
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
        r = requests.get(ApiTestStock.vehicles)
        self.assertEqual(r.status_code, 200)

    def test_2_create_vehicle(self):
        r = requests.post(ApiTestStock.vehicle, json=ApiTestStock.vehicle_object)
        self.assertEqual(r.status_code, 200)

    def test_3_create_stock(self):
        r = requests.post(ApiTestStock.stock, json=ApiTestStock.stock_object)
        self.assertEqual(r.status_code, 200)

    def test_4_delete_stock(self):
        r = requests.delete(ApiTestStock.stock + '/4')
        self.assertEqual(r.status_code, 200)


class TestAppiSupplier(unittest.TestCase):
    API_URL = 'https://servicio-suplier.onrender.com'
    supplier = "{}/supplier".format(API_URL)
    update_object = {
        "name": "Toyota",
        "nit": "9007805105",
        "address": "CARRERA 9 A 99 02 OFFICE 602, Bogota, Colombia",
        "phone": "01 8000 123 691",
        "email": "clientes@toyota.com.co"
    }

    def test_5_get_all_supplier(self):
        r = requests.get(TestAppiSupplier.supplier)
        self.assertEqual(r.status_code, 200)

    def test_6_delete_supplier(self):
        r = requests.delete(TestAppiSupplier.supplier + '/4')
        self.assertEqual(r.status_code, 200)

    def test_7_put_supplier(self):
        r = requests.put(TestAppiSupplier.supplier + '/4', json=TestAppiSupplier.update_object)
        self.assertEqual(r.status_code, 200)


class TestApiLogin(unittest.TestCase):
    URL = 'https://login-norma.herokuapp.com/api'
    user = '{}/user'.format(URL)
    params = {
        'email': f'{os.getenv("EMAIL", "esneydergp69@gmail.com")}',
        'password': os.getenv("PASSWORD", "123456")
    }
    info = '{}/login?' + urllib.parse.urlencode(params)
    login = info.format(URL)
    Token = {
        'token': os.getenv('TOKEN', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6IkVzbmV'
                 'pZGVyIEVucmlxdWUiLCJsYXN0X25hbWUiOiJHdXptYW4iLCJ1c2VyIjoiRXNuZWlkZXIyIiwiZW1haWwiOiJlc2'
                 '5leWRlcmdwNjlAZ21haWwuY29tIiwidHlwZSI6IlN1cGVyIEFkbWluaXN0cmFkb3IiLCJleHAiOjE2NjkyMTA4NDZ9.W3NAkyW5'
                 'WGDDwhuJ6v1xLkvBcvSVAHn0aJ3QIG8YAm0')
    }
    index = '{}/index?Esneider'.format(URL)

    def test_8_post_create_token(self):
        r = requests.post(TestApiLogin.login)
        self.assertEqual(r.status_code, 200)

    def test_9_verify_token(self):
        r = requests.get(TestApiLogin.user, headers={'Authorization': 'Bearer {}'.format(TestApiLogin.Token)})
        self.assertEqual(r.status_code, 200)

    def test_10_verify_index(self):
        r = requests.get(TestApiLogin.index, headers={'Authorization': 'Bearer {}'.format(TestApiLogin.Token)})
        self.assertEqual(r.status_code, 200)



