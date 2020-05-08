#!/usr/bin/python3


def search_replace(my_list, search, replace):
    n = []
    for i in my_list:
        n.append(replace if i == search else i)
    return n
