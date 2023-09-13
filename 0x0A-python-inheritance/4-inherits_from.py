#!/usr/bin/python3
""" Module that contains a function that checks if an object is an instance """


def inherits_from(obj, a_class):
    """ checks if obj is an instance of a class that inherited from a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
