#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    bast = 0
    maqam = 0
    for item in my_list:
        bast += item[0] * item[1]
        maqam += item[1]
    return bast / maqam
