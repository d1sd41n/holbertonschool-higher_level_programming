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

    def area(self):
        """[area]

        Returns:
            int -- square of size
        """
        return self.__size ** 2

    def size(self):
        """[size]

        Returns:
            int -- size
        """
        return self.__size

    def size(self, value):
        """[summary]

        Arguments:
            value {[value]} -- [description]

        Raises:
            TypeError: [size must be an integer]
            TypeError: [size must be >= 0]
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value
