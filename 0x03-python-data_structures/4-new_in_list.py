#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list
    cpy = my_list[::1]
    if idx >= len(my_list):
        return cpy
    cpy[idx] = element

    return cpy
