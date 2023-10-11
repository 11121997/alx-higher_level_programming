#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda k: list(map(lambda n: n**2, k)), matrix))
