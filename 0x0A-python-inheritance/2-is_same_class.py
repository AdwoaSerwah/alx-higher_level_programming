#!/usr/bin/python3
"""This module defines is_same_class function"""


def is_same_class(obj, a_class):
    """
    Checks if object is exactly an instance of the specified class

    Args:
        obj: Object
        a_class: Specified class

    Returns:
        bool: True or False
    """
    return type(obj) is a_class
