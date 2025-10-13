import pytest
from core.calculator import Calculator

class TestCalculator:
    def test_suma(self):
        calc = Calculator()
        assert calc.sumar(2, 3) == 5

    def test_restar(self):
        calc = Calculator()
        assert calc.restar(7, 2) == 5

    def test_multiplicacion(self):
        calc = Calculator()
        assert calc.multiplicar(3, 4) == 12

    def test_dividir(self):
        calc = Calculator()
        assert calc.dividir(10, 2) == 5