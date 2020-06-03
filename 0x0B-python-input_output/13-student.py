#!/usr/bin/python3
"""[summary]

Returns:
    [type] -- [description]
"""


class Student:
    """[summary]
    """
    def __init__(self, first_name, last_name, age):
        """[summary]

        Arguments:
            first_name {[type]} -- [description]
            last_name {[type]} -- [description]
            age {[type]} -- [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """[summary]

        Keyword Arguments:
            attrs {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        if attrs is None or type(attrs) != list:
            return self.__dict__

        d = {}
        for i in attrs:
            if i in self.__dict__:
                d[i] = self.__dict__.get(i)
        return d

    def reload_from_json(self, json):
        """[summary]

        Arguments:
            json {[type]} -- [description]
        """
        for i in json:
            self.__dict__[i] = json[i]

