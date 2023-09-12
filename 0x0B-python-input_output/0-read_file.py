#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

if __name__ == "__main__":
    read_file("my_file_0.txt")      