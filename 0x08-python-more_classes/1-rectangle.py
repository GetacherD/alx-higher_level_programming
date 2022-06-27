#!/usr/bin/python3
"""
Class Representing Rectangle
"""


class Rectangle:
    """
    Rectangle Objects Blueprint
    """
    def __init__(self, width=0, height=0):

        """
        initialize new objects

        Args:
            width(int): width of new Rectangle
            height(int): height of new Rectangle
        Raises:
            TypeError: if height or width is not type of int
            ValueError: if height ir width < 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):

        """ Get width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):

        """ set width of rectangle
        Args:
            value(int): new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ Get height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):

        """ set height of rectangle objects
        Args:
            value(int): new height to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
