#!/usr/bin/python3

"""9-student module """


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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object to a dictionary.

        Returns:
            dict: A dictionary containing the student's information.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
