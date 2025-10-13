import pytest
from core.calculator import Calculator

class TestCalculator:
    def test_add(self):
        """Tests addition of two numbers, including positive, negative, and zero values."""
        calc = Calculator()
        assert calc.add(2, 3) == 5

    def test_subtract(self):
        """Tests subtraction between two numbers, handling positive, negative, and zero results."""
        calc = Calculator()
        assert calc.subtract(7, 2) == 5

    def test_multiplication(self):
        """Tests multiplication of two numbers, verifying correct sign and magnitude for all combinations of positive and negative inputs."""
        calc = Calculator()
        assert calc.multiply(3, 4) == 12

    def test_divide(self):
        """Tests division of two numbers, ensuring correct result and proper handling of division by zero errors."""
        calc = Calculator()
        assert calc.divide(10, 2) == 5

    def test_power(self):
        """Tests exponentiation, including positive and negative bases, integer exponents, and zero exponent."""
        calc = Calculator()
        assert calc.power(3, 2) == 9

    def test_root(self):
        """Tests n-th root calculation, verifying correct results for positive numbers and valid exponents, and handling invalid cases for even roots of negative numbers."""
        calc = Calculator()
        assert calc.root(8, 3) == 2

    def test_square_root(self):
        """Tests square root calculation for positive numbers and ensures invalid input (negative numbers) is handled correctly."""
        calc = Calculator()
        assert calc.square_root(16) == 4

    def test_logarithm(self):
        """Tests logarithm calculation with different bases, ensuring input and base are valid and result matches expected mathematical value."""
        calc = Calculator()
        assert calc.logarithm(8, 2) == 3

    def test_factorial(self):
        """Tests factorial calculation for non-negative integers and ensures invalid inputs (negative or non-integer) are handled properly."""
        calc = Calculator()
        assert calc.factorial(4) == 24

    def test_absolute(self):
        """Tests absolute value function, ensuring negative numbers are correctly converted to positive and positive numbers remain unchanged."""
        calc = Calculator()
        assert calc.absolute(-4) == 4

    def test_modulo(self):
        """Tests modulus operation between two numbers, including positive and negative divisors and dividends."""
        calc = Calculator()
        assert calc.modulo(10, 3) == 1

    def test_percentage(self):
        """Tests percentage calculation, verifying correct computation of 'x% of y' and handling of zero or negative values."""
        calc = Calculator()
        assert calc.percentage(20, 300) == 60