#!/usr/bin/python3
"""
add attributes
"""


def add_attribute(obj, name, value):

    """
    add attributes
    Args:
        obj: to add attributes
        name: name of attr
        value: value of attr
    Raises:
        TypeError: if not able to add attr
    """
    if obj is None or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if name is None or value is None:
        raise TypeError("can't add new attribute")
    setattr(obj, name, name)
