#!/usr/bin/python3
"""This modules defines a Student class"""


class Student:
    """This represents an instance of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        new_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                new_dict[key] = value
        return new_dict
