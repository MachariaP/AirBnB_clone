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

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    setattr(self, "created_at", datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    setattr(self, "updated_at", datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Define string representation of BaseModel object"""

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of _dict_"""
        my_dict = self.__dict__.copy()
        my_dict["_class"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
