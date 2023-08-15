#!/usr/bin/python3
"""Tests the script file_storage"""

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime

class Test_FileStorage(unittest.TestCase):
    """Testcases for the class FileStorage"""

    def setUp(self):
        """Test setUp method for class models"""
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """Test tearDown method for class Filetorage"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all function attributes"""
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        """Tests object values for new method"""
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects(self):
        """Tests class objects"""
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        """Tests input files created"""
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        """Tests conctents of saved file"""
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as f:
            content = json.load(f)

        self.assertTrue(type(content) is dict)

    def test_files_saved(self):
        """Tests the contnts inside the file"""
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as f:
            content = f.read()

        self.assertIsInstance(content, str)

    def test_reload_save(self):
        """Tests saved files when created"""
        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

