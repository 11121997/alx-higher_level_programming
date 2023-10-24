#!/usr/bin/python3
"""square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """constructor.

        arg:
            size: length of a side.
        raise:
            TypeError: if size is not int
            ValueError: if size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
