#!/usr/bin/python3


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: path to the file
    Returns:
        None.
    """
    with open("filename", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
