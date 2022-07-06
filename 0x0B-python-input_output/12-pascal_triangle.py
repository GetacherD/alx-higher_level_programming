#!/usr/bin/python3
"""
Print python triangle
"""


def pascal_triangle(n):

    """
    return pascal_triangle
    Args:
        n(int): number of row
    Returns:
        list: pascal_triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    ret = [[1]]
    res = [[1]]
    i = 1
    prev_row = [1, 1]
    while i < n:
        for i in range(len(prev_row) - 1):
            res[0].append(prev_row[i] + prev_row[i + 1])
        res[0].append(1)
        ret += res
        prev_row = res[0][::1]
        res = [[1]]
        i += 1
    return ret
