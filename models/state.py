#!/usr/bin/python3
"""
The module inherits from BaseModel
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    class has public attribute- name
    """
    name = ""

    def __init__(self, *args, **kwargs):
    """
    State constructor
    """
    super().__init__(*args, **kwargs)
