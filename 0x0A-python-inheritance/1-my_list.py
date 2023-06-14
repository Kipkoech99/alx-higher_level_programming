#!/usr/bin/python3

"""
    A module that inherits from a list class
"""

class MyList(list):
    """A class that is a child to list"""
    def print_sorted(self):
        """Method to sort list"""
        print(sorted(self))
