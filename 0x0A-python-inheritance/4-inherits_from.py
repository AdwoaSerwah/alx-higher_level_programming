#!/usr/bin/python3
"""This module defines the function inherits_from"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj: Object
        a_class: Specified class

    Returns:
        bool: True or False
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
