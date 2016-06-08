import unittest
from pruebas.modulos.modulo_de_prueba import *

class ClaseDePruebaTest(unittest.TestCase):
    
    def test_saluda(self):
        #arrange
            self.obj = ClaseDePrueba()
        #act
            self.res = self.obj.saluda()
        #assert
            self.assertEqual(self.res, "hola SQRUM")