#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    n = {}
    for i in a_dictionary.items():
        n[i[0]] = a_dictionary[i[0]] * 2
    return n
