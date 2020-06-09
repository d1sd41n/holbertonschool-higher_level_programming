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
        """dict 2 string
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
        """string 2 dict
        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns:
            [type]: [description]
        """
        if cls.__name__ == "Square":
            obj = cls(1)

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            [type]: [description]
        """
        try:
            with open(cls.__name__ + ".json", mode="r") as file:
                data = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in data]
        except FileNotFoundError:
            return []
