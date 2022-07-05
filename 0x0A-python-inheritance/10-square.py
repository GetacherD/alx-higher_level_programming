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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
