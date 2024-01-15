#!/usr/bin/python3
"""This module represents Base class"""
import json


class Base:
    """This defines a Base instance"""
    __nb_objects = 0

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            str_j = cls.to_json_string([o.to_dictionary() for o in list_objs])
            f.write(str_j)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
