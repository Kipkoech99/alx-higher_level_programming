#!/usr/bin/python3
"""This module writes content to a file"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and returns
    the number of characters written
    Args:
        filename: path to file
        text: content to write to file
    Return:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
