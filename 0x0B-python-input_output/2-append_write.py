#!/usr/bin/python3
"""This module appends to a file"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file(UTF8) and
    returns the number of characters
    Args:
        filename: path name to file
        text: content to be written to file
    Return:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
