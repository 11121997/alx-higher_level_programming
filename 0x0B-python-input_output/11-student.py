#!/usr/bin/python3
"""Student to JSON module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        diction = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                diction[key] = value
        return diction

    def reload_from_json(self, json):
        """replaces all attributes"""
        for key, value in json.items:
            if key in self.__dict__:
                self.__dict__[key] = value
