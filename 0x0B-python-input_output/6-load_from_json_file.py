#!/usr/bin/python3
"""
create object from json file
"""


def load_from_json_file(filename):

    """
    create object from json file
    Args:
        filename: file name
    """
    import json
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not Found")
        return []
