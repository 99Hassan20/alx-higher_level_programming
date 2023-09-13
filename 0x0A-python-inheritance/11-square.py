#!/usr/bin/python3
""" Module that contains a class Saquare that inherits from BaseGeometry """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a square """
    def __init__(self, size):
        """ Method that initializes the instance """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Method that returns the string representation of the square """
        return "[Square] {}/{}".format(self.__size, self.__size)
