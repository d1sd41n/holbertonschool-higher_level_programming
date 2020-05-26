#!/usr/bin/python3
"""[summary]"""


class Rectangle:
    """[summary]
    """
    def __init__(self, width=0, height=0):
        """[summary]

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]

        Arguments:
            value {[type]} -- [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
