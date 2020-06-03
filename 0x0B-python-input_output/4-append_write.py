#!/usr/bin/python3
"""[summary]"""


def append_write(filename="", text=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, 'a') as file:
        chars = file.write(text)
    return chars
