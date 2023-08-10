#!/usr/bin/python3
"""Define a basemodel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Define a base object"""
    def __init__(self, *args, **kwargs):
        """Initalize a new object"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            json_model = dict(kwargs)
            convert_create = datetime.fromisoformat(json_model["created_at"])
            convert_update = datetime.fromisoformat(json_model["updated_at"])

            json_model["created_at"] = convert_create
            json_model["updated_at"] = convert_update
            del json_model["__class__"]

            for key, value in json_model.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the string representation of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            attributes of the instance

            the created_at, updated_at attributes converted to isoformat
            also the class name is added with the key __class__
        """

        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.created_at)

        return new_dict
