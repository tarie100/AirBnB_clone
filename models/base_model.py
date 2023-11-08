#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']

            if 'created_at' in kwargs:
                if isinstance(kwargs['created_at'], str):
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                if isinstance(kwargs['updated_at'], str):
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

        self.updated_at = self.created_at

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
