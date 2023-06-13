#!/usr/bin/python3
"""
    A module that creates a square
"""
Rectangle = __import__ ('9-rectangle').Rectangle

class Square(Rectangle):
    """A class that inherits from Rectangle"""
    def __init__(self, size):
        """initialize a Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area():
        """Finds the area of the Square"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns print() and str() representation"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
