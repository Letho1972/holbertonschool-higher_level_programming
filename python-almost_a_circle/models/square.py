#!/usr/bin/python3
'''A module that contains the Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A class that creates a square.

    instances:
        size: the int value of the width and height of Square.
        x: axe position for Square.
        y: second axe Position for square.
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''A public method that assigns an argument to each attribute.'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''A method that return a dictionnary
        of all instances of the class.
        '''
        new_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return new_dict
