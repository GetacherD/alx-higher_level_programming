#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = map(lambda row: [i * i for i in row], matrix)
