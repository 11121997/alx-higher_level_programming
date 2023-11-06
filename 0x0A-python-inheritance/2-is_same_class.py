#!/usr/bin/python3
""" is same class mpdule"""


def is_same_class(obj, a_class):
    """function check if bject is exactly an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
