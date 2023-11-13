#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, k=True):
        """validation of all setter methods"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if k and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if not k and value <= 0:
            raise ValueError("{} must be > 0".format(name))
