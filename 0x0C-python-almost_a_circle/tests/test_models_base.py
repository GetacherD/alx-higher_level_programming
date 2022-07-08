#!/usr/bin/python3
"""
Test for base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    """ Base class test """
    def test_id_None(self):

        """ test for case id = None """
        self.b = Base()
        self.assertTrue(self.b.id == 1)

    def test_id(self):

        """ test if id provided """
        self.b2 = Base(100)
        self.assertEqual(self.b2.id, 100)

    def test_id_increment(self):

        """ test if id incremented """
        self.b3 = Base()
        self.assertEqual(self.b3.id, 2)
        self.b4 = Base(4)
        self.assertEqual(self.b4.id, 4)
        self.b5 = Base()
        self.assertEqual(self.b5.id, 3)
