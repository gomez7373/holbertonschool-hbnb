"""
This module defines the Review class.
"""

import json
import os
from datetime import datetime
from base_model import BaseModel
#from app.models.Persistance.storage import Storage

class Review(BaseModel):
    """
    Review model class.
    """
    rating = 0
    text = ""
    user_id = ""
    place_id = ""
    #storage = Storage()

    # def __init__(self, rating, text, user, place):
    #     """Initialize the review with specific attributes."""
    #     super().__init__()
    #     self.rating = rating
    #     self.text = text
    #     self.user_id = user.id
    #     self.place_id = place.id

    # def save_to_file(self):
    #     """Save the review to a file."""
    #     self.storage.save(self)

    # @classmethod
    # def get_by_id(cls, review_id):
    #     """Retrieve a review by its ID."""
    #     review_data = cls.storage.get(review_id)
    #     if review_data:
    #         return cls.from_dict(review_data)
    #     return None

    # @classmethod
    # def update(cls, review_id, **kwargs):
    #     """Update a review's attributes."""
    #     review = cls.get_by_id(review_id)
    #     if not review:
    #         return None
    #     for key, value in kwargs.items():
    #         if hasattr(review, key):
    #             setattr(review, key, value)
    #     review.save_to_file()
    #     return review

    # @classmethod
    # def delete(cls, review_id):
    #     """Delete a review by its ID."""
    #     return cls.storage.delete(review_id)

    # def to_dict(self):
    #     """Convert the review to a dictionary."""
    #     return {
    #         'id': self.id,
    #         'created_at': self.created_at.isoformat(),
    #         'updated_at': self.updated_at.isoformat(),
    #         'rating': self.rating,
    #         'text': self.text,
    #         'user_id': self.user_id,
    #         'place_id': self.place_id
    #     }

    # @classmethod
    # def from_dict(cls, data):
    #     """Create a review from a dictionary."""
    #     review = cls(
    #         rating=data['rating'],
    #         text=data['text'],
    #         user_id=data['user_id'],
    #         place_id=data['place_id']
    #     )
    #     review.id = data['id']
    #     review.created_at = datetime.fromisoformat(data['created_at'])
    #     review.updated_at = datetime.fromisoformat(data['updated_at'])
    #     return review
