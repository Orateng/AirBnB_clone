#!/usr/bin/python3
# The class BaseModel is imported
from models.base_model import BaseModel
"""The User class"""


class User(BaseModel):
    # The class User inherits BaseModel class
    email = ""
    password = ""
    first_name = ""
    last_name = ""
