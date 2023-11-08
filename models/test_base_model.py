#!/usr/bin/python3
import unittest
from datetime import datetime
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        base_model = BaseModel()
        prev_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(prev_updated_at, base_model.updated_at)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_to_dict(self):
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(base_model.id, obj_dict['id'])

    def test_str(self):
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

if __name__ == '__main__':
    unittest.main()
