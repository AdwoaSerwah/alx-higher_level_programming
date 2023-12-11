#!/usr/bin/python3
"""This module appends a new string after a specific string is found"""


def append_after(filename="", search_string="", new_string=""):
    """
     Inserts a line to a file, after each line containing a specific string

     Args:
         search_string (str): String to search
         new_string (str): String to append
    """
    new = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new = new + line
            if search_string in line:
                new = new + (new_string * 2)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new)
