#!/usr/bin/python3
"""[summary]"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """[summary]"""

    def test_instance_id(self):
        """[summary]"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
        base = Base()
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base(666)
        self.assertEqual(base.id, 666)
        base = Base("666")
        self.assertEqual(base.id, "666")
        base = Base()
        self.assertEqual(base.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_to_json_string(self):
        """[summary]"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{"width": 10}]
        o = Base.to_json_string(d)
        self.assertCountEqual(o, '[{"width": 10}]')

    def test_from_json_string(self):
        """[summary]"""
        dic1 = {"id": 9, "x": 4, "y": 6}
        dics = '[{"id": 9, "x": 4, "y": 6}]'
        dic = Base.from_json_string(dics)
        self.assertEqual(dic[0]["id"], dic1["id"])
        self.assertEqual(dic[0]["x"], dic1["x"])
        self.assertEqual(dic[0]["y"], dic1["y"])

    def test_create(self):
        """[summary]"""
        dic = {"id": 1, "x": 1, "y":
               2, "width": 2, "height": 2}
        rec = Rectangle.create(**dic)
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 1/2 - 2/2")
        dic = {"id": 1, "x": 1, "y":
               2, "size": 2}
        rec = Square.create(**dic)
        self.assertEqual(rec.__str__(), "[Square] (1) 1/2 - 2")

    def test_load_from_file(self):
        """[summary]"""
        pass

    def test_pep8(self):
        """[summary]"""
        pep = pep8.StyleGuide()
        pep = pep.check_files(["models/base.py"])
        self.assertEqual(pep.total_errors, 0)
