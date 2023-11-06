#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method must be implemented"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
