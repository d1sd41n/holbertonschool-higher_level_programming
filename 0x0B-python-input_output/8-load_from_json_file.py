#!/usr/bin/python3
"""[summary]"""
import json


def load_from_json_file(filename):
    """[summary]

    Arguments:
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    with open(filename) as file:
        return json.loads(file.read())
