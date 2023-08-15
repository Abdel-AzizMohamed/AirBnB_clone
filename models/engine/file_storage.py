#!/usr/bin/python3
"""Define a FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Define a FileStorage object"""
    __file_path = "main.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects class attribute"""
        return FileStorage.__objects

    def new(self, obj):
        """add object to __objects dict"""
        obj_class = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class, obj.id)] = obj

    def save(self):
        """
            serializes __objects to the json file
            stored in __file_path
        """
        obj_dict = FileStorage.__objects
        con_dict = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as w:
            json.dump(con_dict, w)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as r:
                json_data = json.load(r)
                for obj in json_data.values():
                    obj_class = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(obj_class)(**obj))
