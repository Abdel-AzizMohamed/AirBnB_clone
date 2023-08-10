#!/usr/bin/python3
"""UnitTest for base_model file"""
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    def setUp(self):
        self.obj = BaseModel()

    def test_attributes_type(self):
        self.assertEqual(str, type(self.obj.id))
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_unique_id(self):
        self.assertNotEqual(BaseModel().id, self.obj.id)

    def test_different_time(self):
        sleep(1)
        self.assertLess(self.obj.created_at, BaseModel().created_at)
        self.assertLess(self.obj.updated_at, BaseModel().updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    def setUp(self):
        self.obj = BaseModel()

    def test_return_type(self):
        self.assertEqual(dict, type(self.obj.to_dict()))

    def test_date_type(self):
        self.assertEqual(str, type(self.obj.to_dict()["created_at"]))
        self.assertEqual(str, type(self.obj.to_dict()["updated_at"]))

    def test_correct_keys(self):
        self.assertIn("id", self.obj.to_dict())
        self.assertIn("created_at", self.obj.to_dict())
        self.assertIn("updated_at", self.obj.to_dict())
        self.assertIn("__class__", self.obj.to_dict())

    def test_correct_values(self):
        time_convert = self.obj.created_at.isoformat()

        self.assertEqual("BaseModel", self.obj.to_dict()["__class__"])
        self.assertEqual(self.obj.id, self.obj.to_dict()["id"])
        self.assertEqual(time_convert, self.obj.to_dict()["created_at"])

    def test_added_attributes(self):
        self.obj.name = "test"
        self.assertIn("name", self.obj.to_dict())

    def test_output(self):
        current_time = datetime.now()
        time_convert = current_time.isoformat()
        
        self.obj.id = "1"
        self.obj.created_at = self.obj.updated_at = current_time
        
        check_dict = {"__class__": "BaseModel", "id": "1",
                     "created_at": time_convert, "updated_at": time_convert}

        self.assertDictEqual(self.obj.to_dict(), check_dict)

