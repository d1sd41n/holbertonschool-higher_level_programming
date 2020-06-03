#!/usr/bin/python3
"""[summary]"""


def read_file(filename=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
