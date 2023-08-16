#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = []
    for number in my_list:
        if number not in seen:
            seen.append(number)
    return sum(seen)
