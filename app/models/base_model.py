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
    manager = storage.Storage()

    def __init__(self, **kwargs):
        """Initialize the base model with unique ID and timestamps."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        else:
            self.id = kwargs.get("id")
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))
            self.__dict__.update(kwargs)
            
    
    def save(self):
        """Update the updated_at timestamp
        """
        BaseModel.manager.new(self)       
        self.updated_at = datetime.now()
    
    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["class"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def save_to_json(self):
        
        BaseModel.manager.save()

    def delete(self):
        
        BaseModel.manager.delete(self.id)

    def update(self, *args, **kwargs):
        if args: 
            for i in args:
                self.__dict__[str(i)] = i
        elif kwargs:
             self.__dict__.update(kwargs)
        else
            print("Nothing to update.")

