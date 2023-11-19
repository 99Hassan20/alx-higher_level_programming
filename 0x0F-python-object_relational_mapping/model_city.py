#!/usr/bin/python3
"""this is model for the the state table"""

from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """ the state model inherits from the base class"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True,
                primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
