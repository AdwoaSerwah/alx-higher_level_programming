#!/usr/bin/python3
""" This module defines Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents Square instances"""
    def __init__(self, size):
        """
        Initializes an instance of Square

        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
