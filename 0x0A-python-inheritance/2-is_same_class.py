#!/usr/bin/python3
"""
module for inheritance
"""


def is_same_class(obj, a_class):

    """
    Check if obj is instance of a_class
    Args:
        obj: object to be checked
        a_class: class
    """
    return type(obj) is a_class
