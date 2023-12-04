#!/usr/bin/python3
"""This module defines the class MyList
"""


class MyList(list):
    """
    Represents the class MyList
    
    This is a subclass of the list object
    """
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
