#!/usr/bin/python3
"""
save json dump file
"""


def save_to_json_file(my_obj, filename):

    """
    save to file
    Args:
        my_obj: object to be serialized
        filename: file name to save serialized data
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
