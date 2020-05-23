#!/usr/bin/python3
"""[this module test the max_integer function]
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test1_int_list(self):
        data = [10, 20, 3, 666, 5]
        self.assertEqual(max_integer(data), 666)

    def test2_int_list(self):
        data = [99.3, -20, 3, 666.0, 5]
        self.assertEqual(max_integer(data), 666)

    def test3_int_list(self):
        data = [1]
        self.assertEqual(max_integer(data), 1)

    def test4_empty_list(self):
        data = []
        self.assertIsNone(max_integer(data))

    def test5_empty_function(self):
        self.assertIsNone(max_integer())

    def test6_error_int(self):
        self.assertRaises(TypeError, max_integer, 2)

    def test8_str(self):
        self.assertEqual(max_integer("hola"), "o")

    def test9_empty_dict(self):
        self.assertIsNone(max_integer({}))

    def test10_error_dict(self):
        self.assertRaises(KeyError, max_integer, {2: "sdsd"})

    def test11_error_list(self):
        self.assertRaises(TypeError, max_integer, ["sdsdds", 3, 4])
