#!/usr/bin/python3
"""Base class module"""


class Base:
    """class named base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects
