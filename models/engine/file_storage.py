#!/usr/bin/python3
"""
FileStorage module for storing and updating data
"""

import json
from datetime import datetime
from models.base_model import BaseModel
import os


class FileStorage:
    """This module serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    """This method returns dictionary of objects"""
    def all(self):
        return self.__objects

    """This method adds a new object to the __objects dictionary"""
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes stored objects to the JSON file.
        """
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialized, f)

    """deserialize the JSON file to __objects (if the file exists)"""
    def reload(self):
        if os.path.exists(self.__file_path):
            definclass = {'BaseModel': BaseModel}
            try:
                with open(self.__file_path, mode='r') as f:
                    data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj_class = definclass[class_name]
                    obj = obj_class(**value)
                    self.__objects[key] = obj
                    # obj = self.class_list[value['__class__']](**value)
                    # self.__objects[key] = obj

            except FileNotFoundError:
                pass
