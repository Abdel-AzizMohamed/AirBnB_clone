#!/usr/bin/python3
"""UnitTest for base_model file"""
import unittest
from models.user import User
import models


class TestUser_init(unittest.TestCase):
    """unittest for user class init"""
    def setUp(self):
        self.user_obj = User()

    def test_correct_type(self):
        self.assertEqual(str, type(self.user_obj.email))
        self.assertEqual(str, type(self.user_obj.password))
        self.assertEqual(str, type(self.user_obj.first_name))
        self.assertEqual(str, type(self.user_obj.last_name))

    def test_correct_values(self):
        self.assertEqual("", self.user_obj.email)
        self.assertEqual("", self.user_obj.password)
        self.assertEqual("", self.user_obj.first_name)
        self.assertEqual("", self.user_obj.last_name)


if __name__ == "__main__":
    unittest.main()
