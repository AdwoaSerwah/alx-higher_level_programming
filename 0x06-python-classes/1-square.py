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
    def __init__(self, size):
        """
        Initializes a square object

        Args:
            size (int): Square size
        """
        self.__size = size
