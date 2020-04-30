#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    l = len(arg)
    if l == 1:
        print("{} arguments.".format(l - 1))
    else:
        if l == 2:
            print("{} argument:".format(l - 1))
        else:
            print("{} arguments:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, arg[i]))
