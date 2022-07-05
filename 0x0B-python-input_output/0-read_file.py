#!/usr/bin/python3
"""
read file doc
"""


def read_file(filename=""):

    """
    read file
    Args:
        filename(str): file name to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
