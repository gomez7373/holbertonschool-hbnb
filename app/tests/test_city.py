"""
This module contains unit tests for the City model.
"""

import unittest
from app.models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City model."""

    def test_create_city(self):
        """Test city creation."""
        city = City(name="Test City", country_code="US")
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Test City")

if __name__ == '__main__':
    unittest.main()
