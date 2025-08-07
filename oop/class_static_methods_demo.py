#!/usr/bin/env python3

"""
A module that demonstrates the use and difference between static methods
and class methods in Python.
"""

class Calculator:
    """
    A simple calculator class that contains a static method for addition
    and a class method for multiplication.
    """
    # A class attribute that is shared by all instances of the class.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method to perform addition.
        It does not have access to the class or instance state (no 'self' or 'cls').
        It is a simple utility function logically grouped with the class.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method to perform multiplication.
        It receives the class itself as the first argument (cls).
        This allows it to access class attributes like 'calculation_type'.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    