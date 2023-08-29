#!/usr/bin/python3
"""this is a square class module"""


class Square:
    """This is the square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        error = 0
        if not isinstance(value, tuple):
            error = 1
        elif len(value) != 2:
            error = 1
        elif not isinstance(value[0], int) or not isinstance(value[0], int):
            error = 1
        elif value[0] < 0 or value[1] < 0:
            error = 1
        if error:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return pow(self.__size, 2)

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
