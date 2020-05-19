#!/usr/bin/python3
"""square class module
"""


class Square:
    """class square
    """
    def __init__(self, size=0):
        """__init__

        Arguments:
            size {int} -- is the size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
