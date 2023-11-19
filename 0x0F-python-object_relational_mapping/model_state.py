#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""this is model for the the state table"""

Base = declarative_base()


class State(Base):
    """ the state model inherits from the base class"""
    __tablename__ = "states"
    id = Column(Integer,
                primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
