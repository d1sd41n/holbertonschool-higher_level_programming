#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        val = max(a_dictionary.values())
        for i, j in a_dictionary.items():
            if j == val:
                return i
    else:
        return None
