#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square and has a private
instance attribute, size. It includes getter and setter
methods for the size attribute.
"""


class Square:
    """
    This class represents a square.

    It has a private instance attribute, size and includes
    getter and setter methods.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object

        Args:
            size (int): Square size (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving size attribute

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of a square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
