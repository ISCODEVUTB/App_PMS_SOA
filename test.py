from unittest import TestCase
import users
import user_controller
import stock
from os import getenv


class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(app.suma(2, 2), 4)


class TestUsers(TestCase):
    update = {
        "name": "Esneider",
        "last_name": "Guzman",
        "user": "esneider23",
        "email": "esneydergp69@gmail.com",
        "password": getenv("PASSWORD", "1234567"),
        "rool": "2",
        "address": "Calle 12 # 12 - 12",
        "id": "1"
    }
    create = {
        "name": "Diego Andres",
        "last_name": "Quintana",
        "user": "Qdiego25",
        "email": "dquintana@utb.edu.co",
        "password": getenv("PASSWORD", "1234567"),
        "rool": "1",
        "address": "Calle 12 # 12 - 12",
        "id": "4"
    }

    def test_all_users(self):
        r = users.all_users_1()
        self.assertEqual(len(r.json()), 2)

    def test_get_user(self):
        r = users.user()
        self.assertEqual(len(r.json()), 2)

    def test_update_user(self):
        r = users.update_user(json=self.update)
        self.assertEqual(len(r.json()), 2)

    def test_create_user(self):
        r = users.create_user(json=self.create)
        self.assertEqual(len(r.json()), 2)
    
    def test_all_users_controller(self):
        r = user_controller.all_user(users.mysql)
        self.assertAlmostEqual(len(r.json()), 2)

    def test_get_user_controller(self):
        r = user_controller.user(users.mysql, 1)
        self.assertEqual(len(r.json()), 2)
    
    def test_update_user_controller(self):
        r = user_controller.update_user(users.mysql, self.update)
        self.assertEqual(len(r.json()), 2)
    
    def test_create_user_controller(self):
        r = user_controller.create_user(users.mysql, self.create)
        self.assertEqual(len(r.json()), 2)
    


class TestStock(TestCase):

    create_vehicle = {
        'id': 7,
        'name': 'gol', 
        'motor': 1.6 ,
        'gearbox': 'manual',
        'security': 'Antiblock of brakes',
        'type': 4,
        'url': 'https://awscdn.volkswagen.co/media/Abstract_Image_B1280_Component.Box_Stage_Fullscreen_Item_Media_Image_Image_Component/46890-stage-382004-media-child-image-b1280/dh-1435-6b7102/f1b0c4bf/1657115417/Gol-banner-1.jpg',
        "description": "Funcional y seguro al mismo tiempo, un ejemplo perfecto de cómo un auto simple puede sobresalir",
        'data_sheet': 'https://awscdn.volkswagen.co/media/Kwc_Basic_DownloadTag_Component/46890-699855-474948-1140714-815706-linkTag-child/default/1181892f/1668615641/gol-last-edition-my23-v20.pdf?_ga=2.121926539.1614351708.1669781517-379648666.1669674914&_gl=1*1alpjz4*_ga*Mzc5NjQ4NjY2LjE2Njk2NzQ5MTQ.*_ga_41DDCT7V7B*MTY2OTc4MTUxNy4yLjEuMTY2OTc4MTYzMS4wLjAuMA..'
    }
    create_stock = {
        'name': 7,
        'supplier': 2,
        'selling_price': 10000000,
        'quantity': 2,
    }
    
    def test_all_vehicles(self):
        r = stock.index()
        self.assertEqual(len(r.json()), 2)
    
    def test_get_vehicle(self):
        r = stock.get_vehicle(1)
        self.assertEqual(len(r.json()), 2)
    
    def test_create_vehicle(self):
        r = stock.create_vehicle(json=self.create_vehicle)
        self.assertEqual(len(r.json()), 2)

    def test_create_stock(self):
        r = stock.create_stock(json=self.create_stock)
        self.assertEqual(len(r.json()), 2)

    
