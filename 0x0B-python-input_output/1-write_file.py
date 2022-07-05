#!/usr/bin/python3
"""
write to file
"""


def write_file(filename="", text=""):

    """
    write to file
    Args:
        filename(str): file name to write to
        text(str): text to be written
    """
    count = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        count = f.write(text)
    return count
