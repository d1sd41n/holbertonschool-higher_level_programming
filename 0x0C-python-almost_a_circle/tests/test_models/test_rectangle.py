#!/usr/bin/python3
"""[summary]"""
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """[summary]"""

    def test_rectangle_instance_id(self):
        """[summary]"""
        rec = Rectangle(1, 1, id=666)
        self.assertIsInstance(rec, Rectangle)
        self.assertEqual(rec.id, 666)
        rec = Rectangle(1, 1, id="666")
        self.assertEqual(rec.id, "666")

    def test_pep8(self):
        """[summary]"""
        pep = pep8.StyleGuide()
        pep = pep.check_files(['./models/rectangle.py'])
        self.assertEqual(pep.total_errors, 0)

    def test_width(self):
        """[summary]"""
        pass

    def test_width(self):
        """[summary]"""
        pass

    def test_height(self):
        """[summary]"""
        pass

    def test_height(self):
        """[summary]"""
        pass

    def test_area(self):
        """[summary]"""
        pass

    def test_display(self):
        """[summary]
        """
        pass

    def test_update(self):
        """[summary]"""
        pass

    def test_to_dictionary(self):
        """[summary]"""
        pass
