#!/usr/bin/python3
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_rectangle_instance_id(self):
        rec = Rectangle(1, 1, id=666)
        self.assertIsInstance(rec, Rectangle)
        self.assertEqual(rec.id, 666)
        rec = Rectangle(1, 1, id="666")
        self.assertEqual(rec.id, "666") 