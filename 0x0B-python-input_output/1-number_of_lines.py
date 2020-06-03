#!/usr/bin/python3
"""[summary]"""


def number_of_lines(filename=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, 'r') as file:
        return len(file.readlines())
