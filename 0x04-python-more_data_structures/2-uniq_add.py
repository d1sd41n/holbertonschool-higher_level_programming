#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) > 0:
        n = sum(set(my_list))
        return n
