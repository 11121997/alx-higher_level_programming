#!/usr/bin/python3
""" My list module """


class MyList(list):
    """
    class inherits from list
    """
    def print_sorted(self):
        """instance method prints the list"""
        print(sorted(self))
