#!/usr/bin/python3

""" Module that contains a class BaseGeometry """


class BaseGeometry:
    """ Class that contains methods area and integer_validator """
    def area(self):
        """ Method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if int(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))
