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

    @classmethod
    def load_from_file(cls):
        """loads object from file"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**k) for k in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save object to csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[k.id, k.width, k.height, k.x, k.y]
                             for k in list_objs]
            else:
                list_objs = [[k.id, k.size, k.x, k.y]
                             for k in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        H = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(k) for k in row]
                if cls is Rectangle:
                    n = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    n = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                H.append(cls.create(**n))
        return H
