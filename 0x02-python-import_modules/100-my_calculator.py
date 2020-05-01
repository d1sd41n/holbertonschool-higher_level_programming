#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div

if __name__ == "__main__":
    arg = sys.argv
    l = len(arg)

    if l - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(arg[1])
    b = int(arg[3])
    o = arg[2]

    if o == "+":
        res = add(a, b)
    elif o == "-":
        res = sub(a, b)
    elif o == "*":
        res = mul(a, b)
    elif o == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, o, b, res))
