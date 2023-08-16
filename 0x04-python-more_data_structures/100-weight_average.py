#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    avg = 0
    bast = 0
    maqam = 0
    for item in my_list:
        bast += item[0] * item[1]
        maqam += item[1]
    return bast / maqam
