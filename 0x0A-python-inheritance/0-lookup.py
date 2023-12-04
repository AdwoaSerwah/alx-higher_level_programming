#!/usr/bin/python3
"""This module defines the function lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: Object

    Returns:
        list: List
    """
    return dir(obj)
