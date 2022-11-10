#!/usr/bin/python3
"""
  The efinition of the State of class with relationship to the City
"""

from sqlalchemy.orm import relationship
from relationship_city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class State(Base):
    """
      The class of the State
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
