#!/usr/bin/python3
"""Define a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define a user object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
