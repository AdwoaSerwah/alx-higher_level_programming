#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square and has a private
instance attribute, size.
"""


class Square:
    """
    This class represents a square.

    It has a private instance attribute, self.
    """
    def __init__(self, size=0):
        """
        Initializes a square object

        Args:
            size (int): Square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
