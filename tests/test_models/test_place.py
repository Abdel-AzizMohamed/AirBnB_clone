#!/usr/bin/python3
"""UnitTest for place file"""
import unittest
from models.place import Place
import models


class TestCity_init(unittest.TestCase):
    """unittest for place class init"""
    def setUp(self):
        self.obj = Place()

    def test_correct_type(self):
        self.assertEqual(str, type(self.obj.city_id))
        self.assertEqual(str, type(self.obj.user_id))
        self.assertEqual(str, type(self.obj.description))
        self.assertEqual(int, type(self.obj.number_rooms))
        self.assertEqual(int, type(self.obj.number_bathrooms))
        self.assertEqual(int, type(self.obj.max_guest))
        self.assertEqual(int, type(self.obj.price_by_night))
        self.assertEqual(float, type(self.obj.latitude))
        self.assertEqual(float, type(self.obj.longitude))
        self.assertEqual(list, type(self.obj.amenity_ids))

    def test_correct_values(self):
        self.assertEqual("", self.obj.city_id)
        self.assertEqual("", self.obj.user_id)
        self.assertEqual("", self.obj.name)
        self.assertEqual("", self.obj.description)
        self.assertEqual(0, self.obj.number_rooms)
        self.assertEqual(0, self.obj.number_bathrooms)
        self.assertEqual(0, self.obj.max_guest)
        self.assertEqual(0, self.obj.price_by_night)
        self.assertEqual(0.0, self.obj.latitude)
        self.assertEqual(0.0, self.obj.longitude)
        self.assertEqual([], self.obj.amenity_ids)


if __name__ == "__main__":
    unittest.main()
