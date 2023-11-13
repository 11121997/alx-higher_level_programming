#!/usr/bin/python3
"""Base class module"""
from json import dumps, loads


class Base:
    """class named base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """static method"""
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [k.to_dictionary() for k in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fi:
            fi.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            copy = Rectangle(1, 1)
        elif cls is Square:
            copy = Square(1)
        else:
            copy = None
        copy.update(**dictionary)
        return copy
