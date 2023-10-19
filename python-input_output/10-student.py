#!/usr/bin/python3

"""10-student module"""


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
        Initializes a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Returns:
            None
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name
                
    def to_json(self, attrs=None):
        """If no specific attributes are provided, 
        return a dictionary with all attributes   """
        
        if attrs is None:

             return self.__dict__
        
        else:
         
            return {key: value for key, value in self.__dict__.items() if key in attrs}
