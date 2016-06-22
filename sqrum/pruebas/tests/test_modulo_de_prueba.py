import unittest
from pruebas.modulos.modulo_de_prueba import *

@unittest.skip("")
class ClaseDePruebaTest(unittest.TestCase):
    def test_saludo(self):
        ''' pruebas - ClaseDePruebaTest | Devuelve "hola SQRUM" '''
        #arrange
        self.obj = ClaseDePrueba()
        #act
        self.res = self.obj.saluda()
        #assert
        self.assertEqual(self.res, "hola SQRUM")