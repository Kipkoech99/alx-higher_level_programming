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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """set height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """print the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

