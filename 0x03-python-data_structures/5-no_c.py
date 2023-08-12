#!/usr/bin/python3
def no_c(my_string):
    removed = [char for char in my_string if char not in "cC"]
    return "".join(removed)
