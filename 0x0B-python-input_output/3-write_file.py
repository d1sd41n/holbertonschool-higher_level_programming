#!/usr/bin/python3
"""[summary]"""


def write_file(filename="", text=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, 'w') as file:
        chars = file.write(text)
    return chars
