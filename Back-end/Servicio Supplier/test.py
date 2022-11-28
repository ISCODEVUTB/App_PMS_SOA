import unittest
import requests

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