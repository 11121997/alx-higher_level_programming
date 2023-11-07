#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """function that returns the dictionary description"""
    return obj.__dict__
