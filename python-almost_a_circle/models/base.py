#!/usr/bin/python3
"""The first class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """A method that that returns the JSON
        string representation of a dictionary"""

        if not list_dictionaries or\
                len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
