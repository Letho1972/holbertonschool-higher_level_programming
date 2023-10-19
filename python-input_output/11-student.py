#!/usr/bin/python3

"""11-student module """


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Convert the Student object to a dictionary.

        Args:
            attrs (list, optional): A list of attributes
            to include in the dictionary.
            If None, all attributes will be included. Default is None.

        Returns:
            dict: A dictionary containing the student's information.
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):

        """
        Convert the Student object to a dictionary.

        Returns:
            dict: A dictionary containing the student's information.
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    my_dict[key] = getattr(self, key)
        return my_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
