#!/usr/bin/python3
"""[summary]"""
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Arguments:
        my_obj {[type]} -- [description]
        filename {[type]} -- [description]
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
