#!/usr/bin/python3
"""square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """constructor.

        arg:
            size: length of a side.
            position: postion of # in square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """return current pos."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square
        Return: the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for k in range(0, self.__position[1])]
        for k in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for h in range(0, self.__size)]
            print("")
