#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    ls = [0, 0]
    if len(tuple_a) >= 2:
        ls[0] = ls[0] + tuple_a[0]
        ls[1] = ls[1] + tuple_a[1]
    elif len(tuple_a) == 1:
        ls[0] = ls[0] + tuple_a[0]
    if len(tuple_b) >= 2:
        ls[0] = ls[0] + tuple_b[0]
        ls[1] = ls[1] + tuple_b[1]
    elif len(tuple_b) == 1:
        ls[0] = ls[0] + tuple_b[0]
    return tuple(ls)
