"""
This module defines the BaseModel class.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Base model class that includes common attributes and methods.
    """

    def __init__(self):
        """Initialize the base model with unique ID and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now()
