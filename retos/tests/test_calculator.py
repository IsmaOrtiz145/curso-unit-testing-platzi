"""Reto de la clase 03"""
from retos.src.calculator import suma, resta, multiplicacion, division, potencia_num
import unittest

class CalculatorTest(unittest.TestCase):

    def test_suma(self):
        assert suma(2, 3) == 5

    def test_resta(self):
        assert resta(10, 5) == 5

    def test_multiplicacion(self):
        assert multiplicacion(5, 3) == 15

    def test_division(self):
        assert division(10, 2) == 5

    def test_potencia(self):
        assert potencia_num(5, 6) == 15625

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(6, 0)
