#!/usr/bin/python3
"""This module defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename: Filename
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
