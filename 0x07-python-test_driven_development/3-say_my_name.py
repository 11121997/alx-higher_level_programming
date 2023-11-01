#!/usr/bin/python3
"""Say my name module"""


def say_my_name(first_name, last_name=""):
    """ function that prints My name:

    Args:
        first_name: string
        last_name: string

    Raise:
        TypeError:
            1- first_name must be a string
            2- last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
