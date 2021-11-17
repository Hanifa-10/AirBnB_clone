#!/usr/bin/python3
"""
module to inherit from Basemodel
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
"""
class inherits from BaseModel
"""
name = ""

def __init__(self, *args, **kwargs):
"""
constructor for Amenity
"""
super().__init__(*args, **kwargs)
