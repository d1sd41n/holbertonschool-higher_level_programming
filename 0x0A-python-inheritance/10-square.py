#!/usr/bin/python3
"""[summary]"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """[summary]

    Arguments:
        Rectangle {[type]} -- [description]
    """
    def __init__(self, size):
        """[summary]

        Arguments:
            size {[type]} -- [description]
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
