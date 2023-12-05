#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" This module defines Square class"""


class Square(Rectangle):
    """This class represents Square instances"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
