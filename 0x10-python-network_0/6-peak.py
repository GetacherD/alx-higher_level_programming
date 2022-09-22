#!/usr/bin/python3
"""
Find peak module
"""


def find_peak(list_of_integers):
    """ find peak """
    ls = list_of_integers
    if not ls:
        return None
    max = ls[0]
    i = 0
    while i < len(ls):
        if ls[i] > max:
            max = ls[i]
        i += 1
    return max
