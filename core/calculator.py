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
        b (int | float) and b > 0 : The second number

        Return:
        (int | float): The multiply of a and b
        """
        if b == 0:
            raise ValueError("It cannot be divided by 0.")
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
        return a ** b