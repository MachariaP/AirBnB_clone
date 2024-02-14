#!/usr/bin/python3
"""
FileStorage class model
"""
import json
import os.path

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to JSON file
    also
    deserializes JSON file to an instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary set of __objects
        """
        return self.__objects

    def new(self, obj):
        """
        function that sets in __objects
        the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        function that serializes set of
        __objects to JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for x, y in self.__objects.items():
                dict_storage[x] = y.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if it exists.
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
                for obj_data in data.values():
                    class_name = obj_data.get("__class__")
                    if class_name:
                        cls = getattr(models, class_name, None)
                        if cls:
                            obj_instance = cls(**obj_data)
                            self.new(obj_instance)
                        else:
                            logging.warning(f"Class {class_name} not found.")
                    else:
                        logging.warning("Class name not found in JSON data.")
        except FileNotFoundError:
            logging.warning("JSON file not found.")
