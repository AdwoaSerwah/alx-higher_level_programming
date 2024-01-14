#!/usr/bin/python3
"""This module represents Base class"""
import json


class Base:
    """This defines a Base instance"""
    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
