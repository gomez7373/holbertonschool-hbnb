"""
This module defines the Place class.
"""

import json
import os
from datetime import datetime
from .base_model import BaseModel
from app.storage import Storage

class Place(BaseModel):
    """
    Place model class.
    """
    storage = Storage()

    def __init__(self, name, city_id, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests):
        """Initialize the place with specific attributes."""
        super().__init__()
        self.name = name
        self.city_id = city_id
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []
        self.reviews = []

    def save_to_file(self):
        """Save the place to a file."""
        self.storage.save(self)

    @classmethod
    def get_by_id(cls, place_id):
        """Retrieve a place by its ID."""
        place_data = cls.storage.get(place_id)
        if place_data:
            return cls.from_dict(place_data)
        return None

    @classmethod
    def update(cls, place_id, **kwargs):
        """Update a place's attributes."""
        place = cls.get_by_id(place_id)
        if not place:
            return None
        for key, value in kwargs.items():
            if hasattr(place, key):
                setattr(place, key, value)
        place.save_to_file()
        return place

    @classmethod
    def delete(cls, place_id):
        """Delete a place by its ID."""
        return cls.storage.delete(place_id)

    def to_dict(self):
        """Convert the place to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name,
            'city_id': self.city_id,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenities': self.amenities,
            'reviews': self.reviews
        }

    @classmethod
    def from_dict(cls, data):
        """Create a place from a dictionary."""
        place = cls(
            name=data['name'],
            city_id=data['city_id'],
            host_id=data['host_id'],
            number_of_rooms=data['number_of_rooms'],
            number_of_bathrooms=data['number_of_bathrooms'],
            price_per_night=data['price_per_night'],
            max_guests=data['max_guests']
        )
        place.id = data['id']
        place.created_at = datetime.fromisoformat(data['created_at'])
        place.updated_at = datetime.fromisoformat(data['updated_at'])
        place.amenities = data.get('amenities', [])
        place.reviews = data.get('reviews', [])
        return place
