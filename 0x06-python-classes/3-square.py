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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of a square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
