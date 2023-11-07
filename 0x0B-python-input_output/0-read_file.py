#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """function that reads a text file (UTF8)"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
