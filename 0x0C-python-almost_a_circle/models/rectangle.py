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
    def widthy(self, value):
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value, k=True):
        """validation of all setter methods"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if k and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if not k and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance"""
        ch = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(ch, end="")

    def __str__(self):
        '''Returns info about the rectangle in string'''
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)
