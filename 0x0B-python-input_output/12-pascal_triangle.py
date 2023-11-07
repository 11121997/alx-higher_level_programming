#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """function that returns a list of lists of integers representing
    the Pascal’s triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        i = triangle[-1]
        k = [1]
        for h in range(len(i) - 1):
            k.append(i[h] + i[h + 1])
        k.append(1)
        triangle.append(k)
    return triangle
