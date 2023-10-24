#!/usr/bin/python3
"""square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """constructor.

        arg:
            size: length of a side.
        """
        self.__size = size

    @property
    def size(self):
        """
        get the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square
        Reurn: the current square area
        """
        return self.__size ** 2

    def my_print(self):
        for k in range(self.size):
            for h in range(self.size):
                print("#", end='\n' if h == self.size - 1 and k != i else "")
        print()
