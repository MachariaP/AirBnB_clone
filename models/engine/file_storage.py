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
        """Serializes __objects to the JSON file (path: __file_path)"""

        j_dict = {}
        for key, value in self.__objects.items():
            j_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(j_dict, f)

    def reload(self):

        """Load JSON data from the file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = f.read()
            if data:
                json_data = json.loads(data)

                for obj in json_data.values():
                    cls_name = obj['__class__']
                    cls = models.classes.get(cls_name)
                    if cls:
                        instance = cls(**obj)
                        key = "{}.{}".format(cls_name, instance.id)
                        self.__object[key] = instance

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
