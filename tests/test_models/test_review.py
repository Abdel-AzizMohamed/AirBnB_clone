#!/usr/bin/python3
"""UnitTest for review file"""
import unittest
from models.review import Review
import models


class TestCity_init(unittest.TestCase):
    """unittest for review class init"""
    def setUp(self):
        self.obj = Review()

    def test_correct_type(self):
        self.assertEqual(str, type(self.obj.place_id))
        self.assertEqual(str, type(self.obj.user_id))
        self.assertEqual(str, type(self.obj.text))

    def test_correct_values(self):
        self.assertEqual("", self.obj.place_id)
        self.assertEqual("", self.obj.user_id)
        self.assertEqual("", self.obj.text)


if __name__ == "__main__":
    unittest.main()
