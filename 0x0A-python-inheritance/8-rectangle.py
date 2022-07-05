#!/usr/bin/python3
"""
Geometry Base Class Repr doc
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
