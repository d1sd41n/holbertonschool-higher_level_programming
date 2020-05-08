#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        num = 0
        denom = 0
        for i, j in my_list:
            num += i * j
            denom += j
        div = num / denom
        return div
    else:
        return 0
