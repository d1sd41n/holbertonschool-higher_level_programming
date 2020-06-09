#!/usr/bin/python3
"""[summary]"""
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """[summary]"""

    def test_sqaure_instance_id(self):
        """[summary]"""
        sq = Square(1, 1, id=666)
        self.assertIsInstance(sq, Square)
        self.assertEqual(sq.id, 666)
        sq = Square(1, 1, id="666")
        self.assertEqual(sq.id, "666")

    def test_pep8(self):
        """[summary]"""
        pep = pep8.StyleGuide()
        pep = pep.check_files(['./models/square.py'])
        self.assertEqual(pep.total_errors, 0)

    def test_update(self, *args, **kwargs):
        """[summary]"""
        pass

    def test_to_dictionary(self):
        """[summary]"""
        pass

    def test_error(self):
        """[summary]"""
        pass
