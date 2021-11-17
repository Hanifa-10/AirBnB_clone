#!/usr/bin/python3
"""
Module that inherits from BaseModel
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    contains public attributes
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        super().__init__(*args, **kwargs)
