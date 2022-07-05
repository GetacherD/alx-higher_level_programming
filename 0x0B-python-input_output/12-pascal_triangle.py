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
    res = [[]]
    res[0].append(1)
    prev_row = pascal_triangle(n - 1)[-1]
    for i in range(len(prev_row) - 1):
        res[0].append(prev_row[i] + prev_row[i + 1])
    res[0].append(1)
    return pascal_triangle(n - 1) + res
