#!/usr/bin/python3
"""UnitTest for base_model file"""
import unittest
from models.state import State
import models


class TestState_init(unittest.TestCase):
    """unittest for user class init"""
    def setUp(self):
        self.obj = State()

    def test_correct_type(self):
        self.assertEqual(str, type(self.obj.name))

    def test_correct_values(self):
        self.assertEqual("", self.obj.name)


if __name__ == "__main__":
    unittest.main()
