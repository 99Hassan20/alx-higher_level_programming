#!/usr/bin/python3
""" Module that contains a function that returns the list of available  attributes and methods of an object """ 


class MyList(list):
    """ Class that inherits from list """
    def print_sorted(self):
        """ Function that prints the list, but sorted (ascending sort) """
        print(sorted(self))