#!/usr/bin/python3
"""
Json Class inherited
"""
import json


def class_to_json(obj):

    """
    return dictionary description of obj
    Args:
        obj: any object
    """
    if hasattr(obj, "__dict__"):
        return json.dumps(obj.__dict__)
