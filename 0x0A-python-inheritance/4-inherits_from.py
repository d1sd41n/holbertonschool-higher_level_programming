#!/usr/bin/python3
"""[summary]"""


def inherits_from(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if (issubclass(type(obj), a_class) and
       type(obj) is not a_class):
        return True
    else:
        return False
