#!/usr/bin/python3
"""This module defines a function called read_file"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename (str): File to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
