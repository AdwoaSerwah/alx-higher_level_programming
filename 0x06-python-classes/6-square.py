#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square and has a private
instance attributes, size and position. It includes getter
and setter methods for these attributes. It also includes
public instance methods for calculating the area and printing
the square.
"""


class Square:
    """
    This class represents a square.

    It has a private instance attributes, size and position,
    and includes getter and setter methods. It also includes
    public instance methods for calculating the area and
    printing the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object

        Args:
            size (int): Square size (default is 0)
            position (tuple): Square coordinate (default is (0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving size attribute

        Returns:
            int: The size of the square
        """
        return self.__size

    @property
    def position(self):
        """
        Retrieves position attribute

        Returns:
            tuple: The square position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Sets the position attribute

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or \
            len(value) != 2 or \
            not all(isinstance(i, int) for i in value) or \
                any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of a square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout"""
        if self.__size == 0:
            print()
        else:
            [print() for _ in range(self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
