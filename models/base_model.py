#!/usr/bin/python3
"""BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class that defines the base attributes for other classes"""

    def _init_(self, *args, **kwargs):
        """
        constructor of a class
        initializes BaseModel with provided arguments"""

        from models import storage
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self._dict_["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self._dict_["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self._dict_[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def _str_(self):
        """Define string representation of BaseModel object
        """

        return "[{}] ({}) {}".format(type(self)._name, self.id, self.dict_)

    def save(self):
        """updates the public instance attribute updated_at"""

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of _dict_"""
        my_dict = self._dict_.copy()
        my_dict["_class"] = type(self).name_
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
