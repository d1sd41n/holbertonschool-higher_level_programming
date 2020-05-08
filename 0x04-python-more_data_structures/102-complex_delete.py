#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    l = list(a_dictionary)
    for i in l:
        if value == a_dictionary[i]:
            del a_dictionary[i]
    return a_dictionary
