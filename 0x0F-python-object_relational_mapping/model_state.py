#!/usr/bin/python3
"""this is model for the the state table"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata_ = MetaData()
Base = declarative_base(metadata=metadata_)


class State(Base):
    """ the state model inherits from the base class"""
    __tablename__ = "states"
    id = Column(Integer, unique=True,
                primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
