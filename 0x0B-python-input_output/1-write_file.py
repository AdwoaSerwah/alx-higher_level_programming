#!/usr/bin/python3
"""This module defines the function called write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (str): File to write to
        text (str): Text to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
