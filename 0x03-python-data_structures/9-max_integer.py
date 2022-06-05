#!/usr/bin/python3


def max_integer(my_list=[]):

    maximum = 0
    if my_list is None or len(my_list) == 0:
        return None
    for i in my_list:
        if i > maximum:
            maximum = i

    return maximum
