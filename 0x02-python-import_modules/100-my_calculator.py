#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, sub, div

if __name__ == "__main__":
    l = len(argv)
    e2 = "Unknown operator. Available operators: +, -, * and /"

    if l != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    o = argv[2]

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
    print("{:d} {} {:d} = {:d}".format(a, o, b, res))
