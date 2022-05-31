#!/usr/bin/python3
def pow(a, b):
    tmp = 1/a
    tmp2 = a
    if b == 0:
        return 1
    elif b < 0:
        for i in range(1, -b):
            tmp = tmp * (1/a)
        a = tmp
    else:
        for i in range(1, b):
            a = tmp2*a
    return a
