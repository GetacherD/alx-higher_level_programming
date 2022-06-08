#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [i * i for i in row], matrix))
