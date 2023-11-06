#!/usr/bin/python3
"""My integer module"""


class MyInt(int):
    """MyInt class"""
    def __new__(cls, args, **kwargs):
        """new instance of class"""
        return super(MyInt, cls).__new__(cls, args, **kwargs)

    def __eq__(self, other):
        """equal is not equal"""
        return int(self) != other

    def __ne__(self, other):
        """not equal is equal"""
        return int(self) == other
