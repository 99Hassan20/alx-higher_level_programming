#!/usr/bin/python3

def is_roman_string(str):
    for letter in str:
        if letter not in "IVXLCDM":
            return 0
    return 1


def roman_to_int(roman_string):
    if not roman_string\
            or not is_roman_string(roman_string)\
            or type(roman_string) is not str:
        return 0
    roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    sum_numbers = 0
    for i in range(len(roman_string) - 1):
        if roman_numbers[roman_string[i]] < roman_numbers[roman_string[i + 1]]:
            sum_numbers -= roman_numbers[roman_string[i]]
        else:
            sum_numbers += roman_numbers[roman_string[i]]
    sum_numbers += roman_numbers[roman_string[len(roman_string) - 1]]
    return sum_numbers
