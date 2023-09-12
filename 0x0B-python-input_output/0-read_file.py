#!/usr/bin/python3
"""module to read a file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
