#!/usr/bin/python3
"""prints a sqare
"""


def print_square(size):
    """prints a sqare

    Arguments:
        size {[int]} -- [size of square]
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    else:
        for i in range(size):
            print("#" * size)
