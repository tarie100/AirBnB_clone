#!/usr/bin/python3
"""import modules"""
from models.base_model import BaseModel

<<<<<<< HEAD
=======
class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
>>>>>>> cac35d3f9b5443870432f5dbe43d2bedfc867b11

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
