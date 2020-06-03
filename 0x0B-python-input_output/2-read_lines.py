#!/usr/bin/python3
"""[summary]"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        nb_lines {int} -- [description] (default: {0})
    """
    with open(filename, 'r') as file:
        n = number_of_lines(filename)
        if nb_lines <= 0 or n < nb_lines:
            print(file.read(), end="")
        else:
            for i in range(nb_lines):
                print(file.readline(), end="")
