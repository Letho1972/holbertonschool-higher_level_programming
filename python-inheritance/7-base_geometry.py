#!/usr/bin/python3

""" 7-base_geometry """


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class currently doesn't have any specific functionality
    and is intended to be used as a base for more specialized geometry classes.

    Methods:
        (None)
    """

    def area(self):
        """
        Calculate the area of géometry (not implemented).

        Raises:
            Exception: Indicates that the method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.

        Raises:
            Type Error: If `name` is not a string or `value` is not an integer.
            ValueError: If `value` is not greater than 0.

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
