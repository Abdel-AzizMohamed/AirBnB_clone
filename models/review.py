#!/usr/bin/python3
"""Define a review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define a review object"""
    place_id = ""
    user_id = ""
    text = ""
