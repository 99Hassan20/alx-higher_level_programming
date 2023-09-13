#!/usr/bin/python3
""" Module that contains a class Saquare that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(BaseGeometry):
    """ Class that defines a square """
    def __init__(self, size):
        """ Method that initializes the instance """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Method that returns the area of the square """
        return self.__size ** 2
