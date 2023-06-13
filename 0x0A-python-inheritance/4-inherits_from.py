#!/usr/bin/python3
"""
    A module that checks if the object is an instance of
    a class that inherited
"""


def inherits_from(obj, a_class):
    """return True or False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
