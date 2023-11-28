#!/usr/bin/python3
"""
This module represents Magic Class

It has a private instance attribute, radius, and two public
instance methods, area and circumference.
"""
import math


class MagicClass:
    """
    Python class MagicClass.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (int or float): The radius of the circle (default is 0).

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
