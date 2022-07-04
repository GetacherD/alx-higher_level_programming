#!/usr/bin/python3
"""
Geometry Base Class
"""


class BaseGeometry:

    """
    BaseGeometry class
    """
    def area(self):

        """
        Calculate Area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Validate inputs
        Args:
            name(str): name of Geometry
            value(int): integer value to be validated
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """
    Rectangle class inheriting from Base Geometry
    """
    def __init__(self, width, height):

        """
        Initialize new object
        Args:
            width(int): width
            height(int): height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigh = height
