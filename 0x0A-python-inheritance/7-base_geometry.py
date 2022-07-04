#!/usr/bin/python3
"""
Geometry Base Class module doc
"""


class BaseGeometry:

    """
    Blue print for BaseGeometry Objects
    """
    def area(self):

        """
        Calculate Area

        Raises:
            Exception: if not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Validate input parameters

        Args:
            name(str): name of param to be validated
            value(int): param to be validated
        Raises:
            TypeError: if value is not integer
            ValueError: if value <= 0
        """

        if not (type(value) == int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
