#!/usr/bin/python3
from calculator_1 import add, sub, div, mul


def print_opr(num1, num2, opr):
    if opr == "+":
        res = num1 + num2
    elif opr == "-":
        res = num1 - num2
    elif opr == "*":
        res = num1 * num2
    elif opr == "/":
        res = num1 / num2
    print("{:d} {} {:d} = {:d}".format(num1, opr, num2, int(res)))


if __name__ == "__main__":
    a = 10
    b = 5
    print_opr(a, b, "+")
    print_opr(a, b, "-")
    print_opr(a, b, "*")
    print_opr(a, b, "/")
