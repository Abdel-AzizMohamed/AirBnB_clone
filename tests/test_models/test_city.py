#!/usr/bin/python3
"""UnitTest for city file"""
import unittest
from models.city import City
import models


class TestCity_init(unittest.TestCase):
    """unittest for city class init"""
    def setUp(self):
        self.obj = City()

    def test_correct_type(self):
        self.assertEqual(str, type(self.obj.name))
        self.assertEqual(str, type(self.obj.state_id))

    def test_correct_values(self):
        self.assertEqual("", self.obj.name)
        self.assertEqual("", self.obj.state_id)


if __name__ == "__main__":
    unittest.main()
