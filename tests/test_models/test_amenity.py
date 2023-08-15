#!/usr/bin/python3
"""UnitTest for amenity file"""
import unittest
from models.amenity import Amenity
import models


class TestCity_init(unittest.TestCase):
    """unittest for amenity class init"""
    def setUp(self):
        self.obj = Amenity()

    def test_correct_type(self):
        self.assertEqual(str, type(self.obj.name))

    def test_correct_values(self):
        self.assertEqual("", self.obj.name)


if __name__ == "__main__":
    unittest.main()
