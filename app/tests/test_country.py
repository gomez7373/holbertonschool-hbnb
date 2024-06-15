"""
This module contains unit tests for the Country model.
"""

import unittest
from app.models.country import Country

class TestCountry(unittest.TestCase):
    """Test cases for the Country model."""

    def test_create_country(self):
        """Test country creation."""
        country = Country(code="US", name="United States")
        self.assertEqual(country.code, "US")
        self.assertEqual(country.name, "United States")

if __name__ == '__main__':
    unittest.main()
