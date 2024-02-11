#!/usr/bin/python3
"""module for the Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
