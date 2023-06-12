#!/usr/bin/python3

"""
    A module that creates a class with methods
"""

class BaseGeometry:
    """
        A class with methods

        Raises:
        Message: area() is not implemented

    """
    def area(self):
        """Calculates the area and raises exception message"""
        raise Exception("area() is not implemented")
