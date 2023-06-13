#!/usr/bin/python3
"""
    A module that returns a list of available attributes
    and methods of an object
"""


def lookup(obj):
    """A function that returns all attributes and methods"""
    return dir(obj)
