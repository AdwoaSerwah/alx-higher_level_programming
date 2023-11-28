#!/usr/bin/python3
"""This module represents class LockedClass"""


class LockedClass:
    """This defines a LockedClass"""
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        """
        Sets first name attribute

        Args:
            name (str): The name
            value: The value

        Raises:
            AttributeError: If attribute is not first_name
        """
        if name != 'first_name':
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
