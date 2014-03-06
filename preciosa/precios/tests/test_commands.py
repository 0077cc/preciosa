# from django.core.management import call_command
from django.test import TestCase
from mock import patch
from preciosa.precios.models import Producto
from preciosa.precios.management.commands.annalisa import Annalisa


class AnnalisaTestCase(TestCase):

    def setUp(self):
        self.patcher = patch('preciosa.precios.management.commands.annalisa.requests')
        self.api = Annalisa()

    def tearDown(self):
        self.patcher.stop()

    def config(self, json_response):
        """json_response es el Mock de la respuesta json de Annalisa"""
        mock = self.patcher.start()
        mock.get.return_value.json.return_value = json_response

    def test_unidad_volumen_litro_es_normalizada(self):
        " Test my custom command."
        self.config({'unidad_volumen': 'litro'})
        r = self.api.analyze('')
        self.assertEqual(r['unidad_medida'], Producto.UM_L)

    def test_unidad_volumen_ml_es_normalizada(self):
        " Test my custom command."
        self.config({'unidad_volumen': 'mililitro'})
        r = self.api.analyze('')
        self.assertEqual(r['unidad_medida'], Producto.UM_ML)

    def test_unidad_volumen_cc_es_normalizada(self):
        " Test my custom command."
        self.config({'unidad_volumen': 'centimetro cubico'})
        r = self.api.analyze('')
        self.assertEqual(r['unidad_medida'], Producto.UM_ML)


