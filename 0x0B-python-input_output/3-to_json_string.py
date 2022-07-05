#!/usr/bin/python3
"""
convert to json
"""


def to_json_string(my_obj):

    """
    convert to json
    Args:
        my_obj: any object
    """
    import json
    return json.dumps(my_obj)
