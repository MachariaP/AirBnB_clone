#!/usr/bin/python3
""""Module for FileStorage class."""
import os
import datetime
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """This is the class for storing and retrieving data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """This sets in __objects the obj with key <obj class name>.id"""

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """function that serializes __objects to the JSON file"""

        with open(self.__file_path, "w") as f:
            j_dict = {}
            for y, z in self.__objects.items():
                j_dict[y] = z.to_dict()
            json.dumps(j_dict, f)

    def reload(self):
        """returns the valid attributes and their types for classname"""

        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
