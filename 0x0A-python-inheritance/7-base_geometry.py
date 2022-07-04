#!/usr/bin/python3
"""
Geometry Base Class
"""


class BaseGeometry:

    """
    BaseGeometry class
    """

    def __init__(self):

        """ empty init"""
        pass

    def area(self):

        """
        Calculate Area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        validate input param
        Args:
            name(str): name of param to be validated
            value(int): param to be validated
        """
        if not (type(value) == int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
