#!/usr/bin/python3
# The script for FileStorage class
import json
"""The class FileStorage is created"""


class FileStorage:
    """The class FileStorage objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        The function all returns
        the dictionary object __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the
        JSON file (path: __file_path)
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as f:
                FileStorage.__objects = json.load(f)
            for key, value in FileStorage.__objects.items():
                class_name = value["class"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass
