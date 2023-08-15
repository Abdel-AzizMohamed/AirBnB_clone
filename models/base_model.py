#!/usr/bin/python3
"""Define a basemodel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Define a base object"""
    def __init__(self, *args, **kwargs):
        """Initalize a new object"""
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    convert = datetime.strptime(value, time_form)
                    self.__dict__[key] = convert
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.today()
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
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)

        return new_dict
