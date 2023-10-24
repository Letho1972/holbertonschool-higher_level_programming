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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            list: An empty list if `list_objs` is None or empty;
            otherwise, None.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        converted_objs = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(converted_objs)

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string into a Python object.

        Args:
            json_string (str): A string containing valid JSON data.

        Returns:
            object: The Python object represented by the JSON
            string. If the input
            string is empty or None, an empty list will be returned.
            if json_string is None or len(json_string) == 0:
            return []
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
