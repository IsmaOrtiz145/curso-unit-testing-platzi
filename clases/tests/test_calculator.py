"""Clase 03"""
from clases.src.calculator import suma, resta
import unittest

class CalculatorTest(unittest.TestCase):

    def test_suma(self):
        # assert suma(2, 3) == 5
        assert suma(2, 3) == 6

    def test_resta(self):
        assert resta(10, 5) == 5

