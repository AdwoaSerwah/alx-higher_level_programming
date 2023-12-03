#!/usr/bin/python3
""" This module defines  function say_my_name"""


def say_my_name(first_name="default", last_name=""):
    """
    Says your name

    Args:
        first_name (str): First Name
        last_name (str): Last Name

    Raises:
        TypeError: If first or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    first_name = first_name.strip()
    last_name = last_name.strip()
    print("My name is {} {}".format(first_name, last_name))
