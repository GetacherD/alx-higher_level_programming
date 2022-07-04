#!/usr/bin/python3
"""
inheritance example
"""


def inherits_from(obj, a_class):

    """
    Check is obj is inherits from a_class
    Args:
        obj: object to be checked
        a_class: class to be checked
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
