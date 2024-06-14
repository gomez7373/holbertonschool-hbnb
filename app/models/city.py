"""
This module defines the City class.
"""

import json
import os
from datetime import datetime
from .base_model import BaseModel
from app.models.Persistance.storage import Storage

class City(BaseModel):
    """
    City model class.
    """
    storage = Storage()

    def __init__(self, name, country_code):
        """Initialize the city with specific attributes."""
        super().__init__()
        self.name = name
        self.country_code = country_code

    def save_to_file(self):
        """Save the city to a file."""
        self.storage.save(self)

    @classmethod
    def get_by_id(cls, city_id):
        """Retrieve a city by its ID."""
        city_data = cls.storage.get(city_id)
        if city_data:
            return cls.from_dict(city_data)
        return None

    @classmethod
    def update(cls, city_id, **kwargs):
        """Update a city's attributes."""
        city = cls.get_by_id(city_id)
        if not city:
            return None
        for key, value in kwargs.items():
            if hasattr(city, key):
                setattr(city, key, value)
        city.save_to_file()
        return city

    @classmethod
    def delete(cls, city_id):
        """Delete a city by its ID."""
        return cls.storage.delete(city_id)

    def to_dict(self):
        """Convert the city to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name,
            'country_code': self.country_code
        }

    @classmethod
    def from_dict(cls, data):
        """Create a city from a dictionary."""
        city = cls(
            name=data['name'],
            country_code=data['country_code']
        )
        city.id = data['id']
        city.created_at = datetime.fromisoformat(data['created_at'])
        city.updated_at = datetime.fromisoformat(data['updated_at'])
        return city
