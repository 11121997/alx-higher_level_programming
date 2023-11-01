#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """function that prints a square:
        Args:
            size: the size length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    print((("#" * size + '\n') * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
