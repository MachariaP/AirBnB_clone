#!/usr/bin/python3
"""BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class that defines the base attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """
        constructor of a class
        initializes BaseModel with provided arguments"""

        from models import storage
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Define string representation of BaseModel object
        """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of __dict__"""

        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for i, j in self.__dict__.items():
            if i in ("created_at", "updated_at"):
                j = self.__dict__[i].isoformat()
                dict_1[i] = j
        return dict_1
