from unittest import TestCase
import stock_controller
import mysql.connector
from dotenv import load_dotenv
from os import getenv
import json

load_dotenv()


def connection():
    try:
        connec = mysql.connector.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('PASSWORD'),
                                         database=getenv('DB'))
        return connec
    except ValueError:
        print("Connection error")


class TestStock(TestCase):
    info = {
        'name': 'T-Cross',
        'motor': '1.0 TSI 115 CV',
        'gearbox': 'Manual',
        'security': 'ABS, ESP, ASR, EDS, Airbag',
        'type': 4,
        'url': 'https://awscdn.volkswagen.co/media/Abstract_Image_B1280_Component.Box_Stage_Fullscreen_Item_Media_Image_Image_Component/51614-stage-428138-media-child-image-b1280/dh-1435-6b7102/389b850c/1657115433/t-cross-volkswagen-colombia.jpg',
        'description': 'El T-Cross es un SUV compacto que combina la versatilidad de un SUV con la comodidad de un sedán. '
                       'Con un diseño moderno y deportivo, el T-Cross es el SUV ideal para disfrutar de la ciudad.',
        'data_sheet': 'https://www.chevrolet.com.co/content/dam/chevrolet/south-america/colombia/espanol/index/technical-sheets/17-pdfs/ficha-tecnica-onix-turbo-hb.pdf'
    }

    def test_all_stock(self):
        r = stock_controller.stock(connection())
        result = json.loads(r)
        self.assertEqual(len(result['vehicles']), 7)

    def test_vehicle(self):
        r = stock_controller.vehicle(connection(), 1)
        result = json.loads(r)
        self.assertEqual(result['vehicle']['name'], 'Voyage')

    """def test_create_vehicle(self):
        r = create_vehicle(connection(), self.info)
        result = json.loads(r)
        self.assertEqual(result, 'Vehicle created')"""