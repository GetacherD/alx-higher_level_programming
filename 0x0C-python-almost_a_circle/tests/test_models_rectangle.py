#!/usr/bin/python3
"""
Test Rectangle Class
"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    """ Test Rectangle """
    def setUp(self):

        """ initialize test fixture """
        self.rec = Rectangle(2, 2)

    def test_width(self):

        self.rec.width = 40
        self.assertEqual(self.rec.width, 40)
        with self.assertRaises(TypeError):
            self.rec.width = "hello"
        with self.assertRaises(ValueError):
            self.rec.width = -1

    def test_height(self):
        self.rec.height = 4
        self.assertEqual(self.rec.height, 4)
        with self.assertRaises(TypeError):
            self.rec.height = "Hello"
        with self.assertRaises(ValueError):
            self.rec.height = -1

    def test_x(self):
        self.rec.x = 4
        self.assertEqual(self.rec.x, 4)
        with self.assertRaises(TypeError):
            self.rec.x = "Hello"
        with self.assertRaises(ValueError):
            self.rec.x = -1

    def test_y(self):
        self.rec.y = 4
        self.assertEqual(self.rec.y, 4)
        with self.assertRaises(TypeError):
            self.rec.y = "hello"
        with self.assertRaises(ValueError):
            self.rec.y = -1

    def test_area(self):

        """ Test for Area output """
        self.rec.height = 20
        self.rec.width = 10
        self.assertEqual(self.rec.area(), 200)
