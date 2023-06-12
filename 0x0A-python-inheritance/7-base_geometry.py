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

    def integer_validator(self, name, value):
        """ method that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".formar(name))
