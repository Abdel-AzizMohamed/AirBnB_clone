#!/usr/bin/python3
"""UnitTest for base_model file"""
import unittest
import os
from json import dump, load
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage_all(unittest.TestCase):
    """unittest for baseModel class init"""
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, "temp")

        self.file = FileStorage()
        self.data = self.file.all()
        self.obj = BaseModel()

    def test_correct_type(self):
        self.assertEqual(dict, type(self.data))


    def test_extra_arguments(self):
        with self.assertRaises(TypeError):
            self.file.all(None)


class TestFileStorage_new(unittest.TestCase):
    """unittest for baseModel class init"""
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, "temp")

        self.file = FileStorage()
        self.data = self.file.all()
        self.obj = BaseModel()
    
    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            os.rename("temp", self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_correct_key(self):
        base_id = self.obj.id
        self.assertIn("BaseModel.{}".format(base_id), self.data)

    def test_correct_value(self):
        base_id = self.obj.id
        base_obj = self.data["BaseModel.{}".format(base_id)]
        self.assertEqual(self.obj, base_obj)

    def test_bad_arguments(self):
        with self.assertRaises(AttributeError):
            self.file.new(None)

    def test_extra_arguments(self):
        with self.assertRaises(TypeError):
            self.file.new(BaseModel(), 1)


class TestFileStorage_save(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, "temp")

        self.file = FileStorage()
        self.data = self.file.all()

        self.base_obj = BaseModel()

        self.file.save()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            os.rename("temp", self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_extra_arguments(self):
        with self.assertRaises(TypeError):
            self.file.save(None)

    def test_correct_save(self):
        base_id = self.base_obj.id

        with open(self.file_path, "r") as r:
            file_data = r.read()
            self.assertIn("BaseModel.".format(base_id), file_data)


class TestFileStorage_reload(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, "temp")

        self.file = FileStorage()
        self.data = self.file.all()

        self.base_obj = BaseModel()

        self.file.save()
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            os.rename("temp", self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_extra_arguments(self):
        with self.assertRaises(TypeError):
            self.file.reload(None)

    def test_correct_reload(self):
        self.file.reload()
        obj_data = FileStorage._FileStorage__objects
        base_id = self.base_obj.id

        self.assertIn("BaseModel.{}".format(base_id), obj_data)
