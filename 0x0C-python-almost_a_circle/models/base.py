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

    @staticmethod
    def from_json_string(json_string):
        """ Return list of JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Return list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dicts = cls.from_json_string(f.read())
                list_instances = []
                for dictionary in list_dicts:
                    list_instances.append(cls.create(**dictionary))
                return list_instances
        except FileNotFoundError:
            return []
