#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size * self.__size

    def __str__(self):
        """string representation"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
