"""
This module defines the BaseModel class.
"""

import uuid
from datetime import datetime
import Persistance.storage as storage

class BaseModel:
    """
    Base model class that includes common attributes and methods.
    """

    def __init__(self, **kwargs):
        """Initialize the base model with unique ID and timestamps."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        else:
            self.id = kwargs.get("id")
            self.created_at = kwargs.get("created_at")
            self.updated_at = kwargs.get("updated_at")
            self.__dict__.update(kwargs)
            
    
    def save(self):
        """Update the updated_at timestamp
        """
        manager = storage.Storage()
        manager.save(self)       
        self.updated_at = datetime.now()
    def to_dict(self):
        new_dict = self.__dict__.copy()
        return new_dict     
temp= BaseModel()
temp.save()
#print(temp.to_dict())
