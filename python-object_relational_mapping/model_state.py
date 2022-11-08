#!/usr/bin/python3
"""
  File that contains the class definition of a State
  and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# declare new mapping
Base = declarative_base()


# map class to inherit from Base
class State(Base):
    """
      Class state the definition
    """

    # table
    __tablename__ = 'states'

    # Describe table, with column objects,
    # and use methods imported from sqlalchemy
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
