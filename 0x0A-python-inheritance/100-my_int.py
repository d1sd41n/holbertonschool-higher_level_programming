#!/usr/bin/python3
"""[summary]

    Returns:
        [type] -- [description]
"""


class MyInt(int):
    """[summary]

    Arguments:
        int {[type]} -- [description]
    """
    def __init__(self, n):
        self.__n = n

    def __eq__(self, i):
        """[summary]

        Arguments:
            i {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        return self.__n != i

    def __ne__(self, i):
        """[summary]

        Arguments:
            i {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        return self.__n == i
