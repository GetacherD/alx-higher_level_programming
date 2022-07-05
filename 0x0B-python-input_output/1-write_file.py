#!/usr/bin/python3
"""
write to file in python
"""


def write_file(filename="", text=""):

    """
    write text to file with filename
    Args:
        filename(str): file name
        text(str): text to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
