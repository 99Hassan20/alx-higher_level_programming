#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    res = 0
    for number in argv[1:]:
        res += int(number)
    print(res)
