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
