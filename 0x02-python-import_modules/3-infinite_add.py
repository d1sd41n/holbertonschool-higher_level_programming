#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    l = len(arg)
    sum = 0

    for i in range(1, l):
        sum += int(arg[i])
    print("{}".format(sum))
