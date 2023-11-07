#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

        if kwargs and '__class__' in kwargs:
            del kwargs['__class__']

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.updated_at = datetime.now().isoformat()

    def save(self):
        self.update()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at
        obj_dict['updated_at'] = self.updated_at
        return obj_dict

    def dict_saver(self):
        dict_format = {}
        dict_format["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_format[key] = value.isoformat()
            else:
                dict_format[key] = value
                return dict_format
    
    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"
