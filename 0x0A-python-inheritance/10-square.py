#!/usr/bin/python3
"""Square #1 module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size * self.__size
