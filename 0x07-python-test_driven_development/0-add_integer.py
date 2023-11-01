#!/usr/bin/python3
"""Module for add numbers"""


def add_integer(a, b=98):
    """function that adds 2 integers
    ARGS:
        a: first number
        b: second number

    Raise:
        if a and b not int or float
    Return: addition of a + b"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
