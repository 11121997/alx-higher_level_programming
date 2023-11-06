#!/usr/bin/python3
"""add attribute module"""


def add_attribute(obj, attr, value):
    """
    function that adds a new attribute
    to an object if it’s possible
    Args:
        obj: object to add to attribute
        attr: name of attribute
        value: the value of attribute
    Raise:
        TypeError: "can't add new attribute"
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
