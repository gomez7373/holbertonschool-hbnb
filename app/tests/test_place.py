"""
This module contains unit tests for the Place model.
"""

import unittest
from app.models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place model."""

    def test_create_place(self):
        """Test place creation."""
        place = Place(name="Test Place", city_id="1", host_id="1", number_of_rooms=3, number_of_bathrooms=2, price_per_night=100, max_guests=4)
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, "Test Place")

if __name__ == '__main__':
    unittest.main()
