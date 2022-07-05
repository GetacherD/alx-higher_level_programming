#!/usr/bin/python3
"""
Json Class inherited
"""


def class_to_json(obj):

    """
    return dictionary description of obj
    Args:
        obj: any object
    """
    return obj.__dict__
