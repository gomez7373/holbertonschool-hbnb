"""
This module defines the Country class.
"""

from app.storage import Storage

class Country:
    """
    Country model class.
    """
    storage = Storage()

    def __init__(self, code, name):
        """Initialize the country with specific attributes."""
        self.code = code
        self.name = name

    @classmethod
    def get_all(cls):
        """Retrieve all countries."""
        return [
            cls(code="US", name="United States"),
            cls(code="CA", name="Canada"),
            # Add more countries as needed
        ]

    @classmethod
    def get_by_code(cls, code):
        """Retrieve a country by its code."""
        countries = cls.get_all()
        for country in countries:
            if country.code == code:
                return country
        return None

    def update(self, **kwargs):
        """Update a country's attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def delete(cls, code):
        """Delete a country by its code."""
        countries = cls.get_all()
        for country in countries:
            if country.code == code:
                countries.remove(country)
                return True
        return False

    def to_dict(self):
        """Convert the country to a dictionary."""
        return {
            'code': self.code,
            'name': self.name
        }
