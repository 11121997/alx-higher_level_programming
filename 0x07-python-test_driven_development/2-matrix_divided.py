#!/usr/bin/python3
"""divide a matrix module"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix:
    Args:
        matrix
        div
    raise:
        TypeError:
                1- matrix must be a matrix
                (list of lists) of integers/floats
                2- Each row of the matrix must have the same size
                3- div must be a number
        ZeroDivisionError: division by zero
    Return: new matrix"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for k in row:
            if not isinstance(k, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(k / div, 2) for k in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
