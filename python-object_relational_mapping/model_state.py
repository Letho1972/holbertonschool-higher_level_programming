#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (int): an auto-generated, unique integer
                  representing the state's ID.
        name (str): a string with a maximum of
                    128 characters representing the state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
