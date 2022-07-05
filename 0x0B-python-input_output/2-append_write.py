#!/usr/bin/python3
"""
append to file
"""


def append_write(filename="", text=""):

    """
    append text to end of file
    Args:
        filename(str): file name
        text(str): text to be appended
    """
    count = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        count = f.write(text)
    return count
