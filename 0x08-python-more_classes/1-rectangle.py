#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """ Initializing rectangle class
        Args:
            width: The width of rectangle
            height: The height of rectangle

        Raises:
            TypeError: if not integer
            ValueError: if less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
