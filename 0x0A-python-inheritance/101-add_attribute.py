#!/usr/bin/python3
"""[summary]"""


def add_attribute(o, a, v):
    """[summary]

    Arguments:
        o {[type]} -- [description]
        a {[type]} -- [description]
        v {[type]} -- [description]

    Raises:
        TypeError: [description]
    """
    if not hasattr(o, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(o, a, v)
