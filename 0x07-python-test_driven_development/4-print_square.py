#!/usr/bin/python3
"""Tis module defines the function print_square"""


def print_square(size=0):
    """
    Prints a square with the character #

    Args:
        size (int): Size length of the square

    Raises:
        TypeError: if size is not an integer or size is float and < 0
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    [print("#" * size) for i in range(size)]
