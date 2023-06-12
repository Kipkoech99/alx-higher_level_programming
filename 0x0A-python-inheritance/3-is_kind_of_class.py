#!/usr/bin/python3

"""
    A module that checks whether object is instance of class 
    or one it was inherited from
"""
def is_kind_of_class(obj, a_class):
    """
    returns true if the object is an instance of the class or if its
    an instance of the super class
    """
    return (isinstance(obj, a_class))
