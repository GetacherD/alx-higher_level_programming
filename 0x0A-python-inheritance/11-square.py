#!/usr/bin/python3
"""
Geometry Base Class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Square class
    """
    def __init__(self, size):

        """
        Initialize new Square object
        Args:
            size(int): size of square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):

        """
        calculate area
        """
        return self.__size * self.__size

    def __str__(self):

        """
        str representation
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
