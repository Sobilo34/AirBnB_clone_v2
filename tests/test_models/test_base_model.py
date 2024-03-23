#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class Test_basemodel(unittest.TestCase):
    """This is to test the base model"""

    def __init__(self, *args, **kwargs):
        """A test fot __init__ method"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Test fot setup"""
        pass

    def tearDown(self):
        """Test fot Teardown"""
        try:
            os.remove('file.json')
        except Execption:
            pass

    def test_default(self):
        """Test for default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test for kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test for kwargs is integer"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)

    def test_str(self):
        """This is to test string """
        string_repr = str(self.model)
        self.assertIsInstance(string_repr, str)
        self.assertTrue('[BaseModel]' in string_repr)
        self.assertTrue('id' in string_repr)
        self.assertTrue(self.model.id in string_repr)

    def test_todict(self):
        """Test for to_dict method """
        dict_representation = self.model.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertTrue('__class__' in dict_representation)
        self.assertEqual(dict_representation['__class__'], 'BaseModel')
        self.assertTrue('created_at' in dict_representation)
        self.assertTrue('updated_at' in dict_representation)

    def test_kwargs_none(self):
        """Test for if kwargs is none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test for if kwarg is one"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test fot is """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test for created at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test for updated at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_delete(self):
        """ This is to test the delete method"""
        self.model.delete()
        mock_delete.assert_called_once_with(self.model)


if __name__ == '__main__':
    unittest.main()
