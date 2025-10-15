import math
from typing import Union

class Calculator:

    """Basic calculator class for arithmetic operations."""

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Adds two numbers.

        Parameters:
        a (int | float): The first number
        b (int | float): The second number

        Return:
        (int | float): The sum of a and b
        """
        return a + b

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract two numbers.

        Parameters:
        a (int | float): The first number
        b (int | float): The second number

        Return:
        (int | float): The subtract of a and b
        """
        return a - b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        multiply two numbers.

        Parameters:
        a (int | float): The first number
        b (int | float): The second number

        Return:
        (int | float): The multiply of a and b
        """
        return a * b

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divide two numbers.

        Parameters:
        a (int | float): The first number
        b (int | float): The second number; b != 0

        Return:
        (int | float): The multiply of a and b
        """
        if b == 0:
            raise ValueError("It cannot be divided by zero.")
        else:
            return a / b

    def power(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Increases the base according to the given exponent.

        Parameters:
        a (int | float): It is the base
        b (int | float): It is the exponent

        Return:
        (int | float): base ** exponent.
        """
        if a < 0 and b != round(b):
            raise ValueError("Cannot calculate real power of a negative base with a fractional exponent.")
        return a ** b

    def root(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Calculates the n-th root of a number, returning only real results.

        Parameters:
        a (int | float): The number to extract the root from.
        b (int | float): The root index. Can be negative for reciprocal roots, must not be zero.

        Return:
        (int | float): The n-th root of a (real number only).

        Raises:
        ValueError: If b is zero or if trying to calculate an even root of a negative number.
        """
        if b == 0:
            raise ValueError("The root index cannot be zero.")
        if b < 0:
            if a == 0:
                raise ValueError("Root index is negative, and the base (a) is zero, resulting in division by zero.")
            a = 1 / a
            b = abs(b)
        if a < 0 and round(b) == b and int(round(b)) % 2 == 0:
            raise ValueError("Cannot calculate the real root of a negative number with an even index.")

        return a ** (1 / b) 

    def square_root(self, a: Union[int, float]) -> float:
        """
        Calculate the square root of a number.

        Parameters:
        a (int | float): Number from which the square root is going to be taken; a > 0

        Return:
        (float): square root of a
        """
        if a < 0:
            raise ValueError("The number must be greater than or equal to zero.")
        
        return self.root(a, 2)

    def logarithm(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Calculates the logarithm of a value with the given base.

        Parameters:
        a (int | float): It is a argument; a > 0
        b (int | float): It is a base, b > 1

        Return:
        (int | float): logarithm
        """
        if a <= 0:
            raise ValueError("The arguement (a) must be positive (a > 0).")
        if b <= 0 or b == 1:
            raise ValueError("The base (b) must be positive (b > 0) and cannot be 1.")
        return math.log(a, b)

    def factorial(self, n: int) -> int:
        """
        Calculates the factorial of a non-negative integer.

        Parameters:
        n (int): positive number

        Return:
        (int): Factorial of n
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers (0, 1, 2, ..).")
        return math.factorial(n)

    def absolute(self, a: Union[int, float]) -> Union[int, float]:
        """
        Calcule the absolute value of the number.

        Parameters:
        a (int | float): positive or negative number

        Return:
        (int | float): absolute value of a
        """
        return abs(a)

    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Calculates the remainder of a divided by b.

        Parameters:
        a (int | float): dividend
        b (int | float): divider; b != 0

        Return:
        (int | float): remainder of a divided by b
        """
        if b == 0:
            raise ValueError("Modulus operation cannot divide by zero.")
        return a % b

    def percentage(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Calculate what percentage is 'part' of 'whole'.

        Parameters:
        a (int | float): Percentage value, 
        b (int | float): Total

        Return:
        (int | float): Quantity that represents the percentage.
        """
        return b * (a / 100)