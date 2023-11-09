#!/usr/bin/python3
"""
Unittest for BaseModel
"""

import unittest
from datetime import datetime
from models import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_object_creation(self):
        """Instantiating from BaseModel class"""
        obj = BaseModel()
        """Check if the object is an instance of BaseModel"""
        self.assertIsInstance(obj, BaseModel)
        """Check if 'id' is not None"""
        self.assertIsNotNone(obj.id)
        """Check if 'created_at' is a datetime object"""
        self.assertIsInstance(obj.created_at, datetime)
        """Check if 'updated_at' is a datetime object"""
        self.assertIsInstance(obj.updated_at, datetime)

    def test_attribute_setting(self):
        obj = BaseModel()
        obj.my_attribute = "test_value"
        """Check if attribute setting works"""
        self.assertEqual(obj.my_attribute, "test_value")

    def test_update_method(self):
        obj = BaseModel()
        previous_updated_at = obj.updated_at
        obj.update()
        """Check if 'update' method updates 'updated_at'"""
        self.assertNotEqual(previous_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        """Check if 'to_dict' returns a dictionary"""
        self.assertIsInstance(obj_dict, dict)
        """Check if '__class__' is in the dictionary"""
        self.assertIn('__class__', obj_dict)
        """Check if '__class__' value is 'BaseModel'"""
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        """Check if 'created_at' is in the dictionary"""
        self.assertIn('created_at', obj_dict)
        """Check if 'updated_at' is in the dictionary"""
        self.assertIn('updated_at', obj_dict)


if __name__ == '__main':
    unittest.main()
