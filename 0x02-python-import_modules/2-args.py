#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument{'s' if argc > 1 else ''}:")
        for index, value in enumerate(argv[1:]):
            print(f"{index + 1}: {value}")
