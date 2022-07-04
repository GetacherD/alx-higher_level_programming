#!/usr/bin/python3
"""
dir built in module example
"""


def lookup(obj):

    """
    list all attributes of any object
    Args:
        obj(object): any object Type
    Returns:
        list of all attributes
    """
    return list(dir(obj))
