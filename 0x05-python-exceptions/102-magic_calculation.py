#!/usr/bin/python3


def magic_calculation(a, b):

    result = 0
    for i in range(1, 3):
        if not (i > a):
            raise Exception("Too far")
        try:
            result += (a ** b) / i
        except:
            result = a + b
            continue
    return result
