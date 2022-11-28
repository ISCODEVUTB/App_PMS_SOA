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
    URL = 'https://login-normal.onrender.com/api'
    params = {
        "email": os.getenv("EMAIL", "esneydergp69@gmail.com"),
        "password": os.getenv("PASSWORD", "123456")
    }
    info = '{}/login?' + urllib.parse.urlencode(params)
    login = info.format(URL)
    token = {
    "token": os.getenv("TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6IkVzbmVpZGVyIEVucmlxdWUiLCJsYXN0X25hbWUiOiJHdXptYW4iLCJ1c2VyIjoiRXNuZWlkZXIyIiwiZW1haWwiOiJlc25leWRlcmdwNjlAZ21haWwuY29tIiwidHlwZSI6IlN1cGVyIEFkbWluaXN0cmFkb3IiLCJleHAiOjE2Njk4MjU4MDN9.LqgN7jlhV9Hf5JQ35buZozxBmkYG-35uRMe-9nrCEx0")
    }
    user = '{}/user'.format(URL)
    update = '{}/update'.format(URL)
    info_update = {
    "name": "Kevin", 
    "last_name": "Martinez",
    "user": "Kmapax", 
    "email": "guzmane@utb.edu.co", 
    "password": os.getenv("PASSWORD2", "KevinLea"),
    "rool": 3, 
    "address": "Manzana G lote 1", 
    "id": 2  
    }
    users = '{}/users'.format(URL)
    headers={'Authorization': 'Bearer {}'.format(token['token'])}
    index = '{}/index?username=Esneider'.format(URL)


    def test_8_create_token(self):
        r = requests.post(TestApiLogin.login)
        self.assertAlmostEqual(r.status_code, 200)
    
    def test_9_veriify_user(self):
        r = requests.get(TestApiLogin.user, headers=TestApiLogin.headers )
        self.assertAlmostEqual(r.status_code, 200)

    def test_10_update_user(self):
        r = requests.get(TestApiLogin.update, json=TestApiLogin.info_update, headers=TestApiLogin.headers)
        self.assertAlmostEqual(r.status_code, 200)
    
    def test_11_users(self):
        r = requests.get(TestApiLogin.users, headers=TestApiLogin.headers)
        self.assertAlmostEqual(r.status_code, 200)

    def test_12_index(self):
        r = requests.get(TestApiLogin.index, headers=TestApiLogin.headers)
        self.assertAlmostEqual(r.status_code, 200)

    

class TestApiUsers(unittest.TestCase):
    URL = 'https://users-gt8n.onrender.com'
    users = '{}/users'.format(URL)
    user = '{}/user?username=Esneider2&email=esneydergp69@gmail.com'.format(URL)
    params = {
        "name": "Esneider E",
        "last_name": "Guzman P",
        "user": "Esneide2",
        "email": "esneydergp69@gmail.com",
        "password": os.getenv("PASSWORD", "123456"),
        "rool": 2,
        "id": 2
    }
    
    info = '{}/user?' + urllib.parse.urlencode(params)
    user_update = info.format(URL)

    def test_13_all_users(self):
        r = requests.get(TestApiUsers.users)
        self.assertAlmostEqual(r.status_code, 200)
    
    def test_14_user(self):
        r = requests.get(TestApiUsers.user)
        self.assertAlmostEqual(r.status_code, 200)

    def test_15_create_user(self):
        r = requests.post(TestApiUsers.user_update)
        self.assertAlmostEqual(r. status_code, 200)

