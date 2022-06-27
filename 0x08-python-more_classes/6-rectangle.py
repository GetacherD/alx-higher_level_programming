#!/usr/bin/python3
"""
Class Representing Rectangle
"""


class Rectangle:
    """
    Rectangle Objects Blueprint
    """
    number_of_instances = 0

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
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):

        """ Get area of rectangle objects """
        return self.__height * self.__width

    def perimeter(self):

        """ Get perimeter of rectangle objects """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):

        """  str representation of rectangle objects"""
        if self.__height == 0 or self.__width == 0:
            return ""
        st = [("#" * self.__width + "\n") for i in range(self.__height)]
        return "".join(st)

    def __repr__(self):

        """ str representation with eval(obj.__repr__()) """
        return "Rectangle(" + str(self.__width)\
            + ", " + str(self.__height) + ")"

    def __del__(self):

        """ print info when rectangle obj deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
