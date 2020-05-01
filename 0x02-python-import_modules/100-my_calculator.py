#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div

if __name__ == "__main__":
    arg = sys.argv
    l = len(arg)
    e1 = "Usage: " + arg[0] + " <a> <operator> <b>"
    e2 = "Unknown operator. Available operators: +, -, * and /"

    if l < 4:
        print("{}".format(e1))
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
        print("{}".format(e2))
        exit(1)
    print("{} {} {} = {}".format(a, o, b, res))
