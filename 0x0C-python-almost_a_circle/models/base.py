#!/usr/bin/python3
import json
"""[summary]"""


class Base:
    """[summary]"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Args:
            list_objs ([type]): [description]
        """
        l = []
        f_name = cls.__name__ + ".json"
        with open(f_name, mode="w") as file:
            if not list_objs or list_objs is None:
                file.write("[]")
                return
            for i in list_objs:
                l.append(i.to_dictionary())
            file.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
