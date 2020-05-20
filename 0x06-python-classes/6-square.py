#!/usr/bin/python3
"""square class module
"""


class Square:
    """class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """[summary]

        Keyword Arguments:
            size {int} -- [description] (default: {0})
            position {tuple} -- [description] (default: {(0, 0)})

        Raises:
            TypeError: [size must be an integer]
            TypeError: [size must be >= 0]
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

    def area(self):
        """[area]

        Returns:
            int -- square of size
        """
        return self.__size ** 2

    @property
    def size(self):
        """[size]

        Returns:
            int -- size
        """
        return self.__size

    @size.setter
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

    def my_print(self):
        """[prints square]
        """
        s = self.__size
        pos0 = self.__position[0]
        pos1 = self.__position[1]
        if s == 0:
            print()
        else:
            for i in range(pos1):
                print()
            for i in range(s):
                print(" " * pos0, end="")
                print("#" * s)

    @property
    def position(self):
        """[position]

        Returns:
            [int] -- [pos]
        """
        return self.__position

    @position.setter
    def position(self, value):
        """[position]

        Arguments:
            value {[tuple]} -- [description]

        Raises:
            TypeError: [position must be a tuple of 2 positive integers]
        """
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
