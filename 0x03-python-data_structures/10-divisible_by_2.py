#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mask = []
    for number in my_list:
        if number % 2 == 0:
            mask.append(True)
        else:
            mask.append(False)
    return mask
