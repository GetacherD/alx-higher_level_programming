#!/usr/bin/python3
"""
Get object from json
"""


def from_json_string(my_str):

    """
    Get object from json string
    Args:
        my_str: json parsed string
    """
    import json
    return json.loads(my_str)
