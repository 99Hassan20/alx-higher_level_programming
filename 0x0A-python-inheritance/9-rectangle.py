#!/usr/bin/python3
""" Rectangle Module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle """
    def __init__(self, width, height):
        """ Method that initializes the instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Method that returns the string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
