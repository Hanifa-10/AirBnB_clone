#!/usr/bin/python3
"""
The module inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    The class has public attributes and uses FileStorage in engine folder for serialization and deserialization of user
    """
    email = ""
    password = ""
    first_name = ""
    las_name = ""

    def __init__(self, *args, **kwargs):
        """
        User constructor
        """
        super().__init__(*args, **kwargs)
