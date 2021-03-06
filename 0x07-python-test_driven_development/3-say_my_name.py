#!/usr/bin/python3
"""
Module for say_my_name
"""


def say_my_name(first_name, last_name=""):

    """
    print full name speaking way
    Args:
        first_name(str): First Name
        last_name(str): Last Name
    Raises:
        TypeError: if first_name or last_name is not str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
