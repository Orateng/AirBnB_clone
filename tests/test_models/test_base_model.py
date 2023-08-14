#!/usr/bin/python3
"""
Tests for scrpt base_model
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBase(unittest.TestCase):
    """Perform unittests for class TestBase"""

    def setUp(self):
        """The unittest setUp method"""
        self.my_model = BaseModel()

    def tearDown(self):
        """The unittest teardown method"""
        del self.my_model

    def test_id_type(self):
        """ The test method for id object"""
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_updated_created(self):
        """Tests time and date"""
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_to_dict(self):
        """Tests dict{} method"""
        self.assertEqual("<class 'dict'>",
                         str(type(self.my_model.to_dict())))

    def test_to_dict_class(self):
        """Tests the dict{} class"""
        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_updated(self):
        """Tests format for updated_at method"""
        self.assertEqual("<class 'str'>",
                         str(type((self.my_model.to_dict())["updated_at"])))

    def test_to_dict_created(self):
        """Tests format for create_at method"""
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs(self):
        """Tests key value object instances"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)
