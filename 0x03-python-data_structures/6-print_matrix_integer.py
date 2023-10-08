#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in matrix:
        if len(k) == 0:
            print()
        for n in range(len(k)):
            print("{:d}".format(k[n]), end="\n" if n == len(k) - 1 else " ")
