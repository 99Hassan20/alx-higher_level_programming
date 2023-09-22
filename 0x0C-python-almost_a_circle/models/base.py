#!/usr/bin/python3

""" Base class for all models"""
import json


class Base:
    """ Base class for all models"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(lis_dictionaries):
        """ Return JSON string representation of list of dictionaries"""
        if lis_dictionaries is None or lis_dictionaries == []:
            return "[]"
        return json.dumps(lis_dictionaries)
