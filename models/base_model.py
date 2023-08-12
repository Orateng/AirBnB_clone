#!/usr/bin/python3
# The BaseModel script
import uuid
from datetime import datetime
import models
"""The BaseModel class is created"""


class BaseModel:
    """The class BaseModel is made functional"""
    def __init__(self, *args, **kwargs):
        # The __init__ function instantiates objects for BaseModel
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            tstrf = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], tstrf)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        # Function that formats string attributes for BaseModel
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        # Function that updates BaseModel from storage
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Function that creates and  updates dictionay
        values for BaseModel
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
