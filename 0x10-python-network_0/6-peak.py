#!/usr/bin/python3
"""
Find peak module
"""


def find_peak(list_of_integers):
    """ find peak """
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 0:
        return None
    else:
        le = len(list_of_integers)//2
        left = list_of_integers[0:le]
        right = list_of_integers[le:]
        return max(find_peak(left), find_peak(right))
