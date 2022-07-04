#!/usr/bin/python3
"""
Geometry Base Class Repr doc
"""


class BaseGeometry:

    """
    BaseGeometry class Blueprint
    """
    def area(self):

        """
        not implemented , must be imeplemented in sub classes
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
