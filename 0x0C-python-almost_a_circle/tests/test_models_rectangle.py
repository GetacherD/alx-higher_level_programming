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

    def test_rect_two_args(self):

        """ test for 2 args """
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rect_three_args(self):

        """ Test for three args """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_rect_four_args(self):

        """ test for 4 args """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_for_invalid_width(self):

        """ test for invalid input """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_for_invalid_height(self):

        """ test for invalid height """
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x(self):

        """ test for invalid x"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y(self):

        """ Test for invalid y """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_for_all_args(self):

        """ test for all args supplied """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_for_value_width(self):

        """ test for Valueof Width """
        with self.assertRaises(ValueError):
            Rectangle(-1, 3)

    def test_Value_height(self):

        """ Test for Value of height"""
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_for_value_x(self):

        """ test for proper value of x """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_for_value_y(self):

        """ test for value of y"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)
