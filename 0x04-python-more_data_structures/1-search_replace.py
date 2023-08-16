#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for element in my_list:
        if element == search:
            new.append(replace)
        else:
            new.append(element)
    return new
