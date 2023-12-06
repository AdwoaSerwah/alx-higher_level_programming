#!/usr/bin/python3
"""This module defines a function called append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename (str): File to write to
        text (str): Text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
