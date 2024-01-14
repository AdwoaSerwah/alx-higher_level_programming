#!/usr/bin/python3
"""This module defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This defines an instance of this class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
