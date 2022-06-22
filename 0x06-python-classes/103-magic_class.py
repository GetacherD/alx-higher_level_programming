#!/usr/bin/python3
import math
""" Define Magic Class"""


class MagicClass:

    """ The Magic Class"""
    def __init__(self, radius=0):

        """ initialize
        Args:
            radius(int): radius
        """
        self.__radius = 0
        if (type(radius) is not int):
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):

        """ return area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):

        """ return perimeter"""
        return (2 * math.pi) * self.__radius
