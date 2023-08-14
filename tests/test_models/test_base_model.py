#!/usr/bin/python3
"""
Tests for scrpt base_model
"""
import unittest
from models.base_model import BaseModel
import sys
from io import StringIO
import datetime


class TestBase(unittest.TestCase):
    """Perform unittests for class TestBase"""

    def setUp(self):
        """The unittest setUp method"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"

    def tearDown(self):
        """The unittest teardown method"""
        del self.my_model

    def test_id_type(self):
        """ The test method for id object"""
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_name(self):
        """Tests for class attribute"""
        self.assertEqual("My First Model", self.my_model.name)

    def test_updated_created(self):
        """Tests time and date"""
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_to_dict(self):
        """Tests dict{} method"""
        self.assertEqual("<class 'dict'>",
                         str(type(self.my_model.to_dict())))

    def test_save(self):
        """Tests updates created"""
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def tests_str_override(self):
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

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

    def test_type_create(self):
        """Tests instances of class attribute"""
        my_model_dict = self.my_model.to_dict()
        new_model= BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_update(self):
        """Tests dict values instantiated"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)

    def test_instance(self):
        """Tests values of class instances"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)
