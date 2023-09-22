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

    @staticmethod
    def to_json_string(lis_dictionaries):
        """ Return JSON string representation of list of dictionaries"""
        if lis_dictionaries is None or lis_dictionaries == []:
            return "[]"
        return json.dumps(lis_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))
