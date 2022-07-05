#!/usr/bin/python3
"""
create object from json file
"""
import json


def load_from_json_file(filename):

    """
    create object from json file
    Args:
        filename: file name
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
