#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    n = dict(a_dictionary)
    for i in n:
        n[i] *= 2
    return n
