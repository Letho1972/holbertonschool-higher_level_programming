#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (int): an auto-generated, unique integer
                  representing the state's ID.
        name (str): a string with a maximum of
                    128 characters representing the state's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id',
                                          ondelete='CASCADE'), nullable=False)
