#!/usr/bin/python3
"""This modules defines a Student class"""


class Student:
    """This represents an instance of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        obj = self.__dict__
        if type(attrs) is list and all((type(i) is str) for i in attrs):
            for k, v in obj.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict

        for key, value in obj.items():
            if isinstance(value, (list, dict, str, int, bool)):
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
